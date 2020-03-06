from collections import namedtuple, defaultdict
from enum import Enum
from datetime import datetime,timedelta

from exceptions import UnsupportedFeature
from models import NearEarthObject, OrbitPath
import operator

class DateSearch(Enum):
    """
    Enum representing supported date search on Near Earth Objects.
    """
    between = 'between'
    equals = 'equals'

    @staticmethod
    def list():
        """
        :return: list of string representations of DateSearchType enums
        """
        return list(map(lambda output: output.value, DateSearch))


class Query(object):
    """
    Object representing the desired search query operation to build. The Query uses the Selectors
    to structure the query information into a format the NEOSearcher can use for date search.
    """

    Selectors = namedtuple('Selectors', ['date_search', 'number', 'filters', 'return_object'])
    DateSearch = namedtuple('DateSearch', ['type', 'values'])
    ReturnObjects = {'NEO': NearEarthObject, 'Path': OrbitPath}

    def __init__(self, **kwargs):
        """
        :param kwargs: dict of search query parameters to determine which SearchOperation query to use
        """
        # TODO: What instance variables will be useful for storing on the Query object?
        self.Selectors.number=kwargs.get("number")
        self.Selectors.filters=kwargs.get("filter")
        if(kwargs.get("return_object")=="Path"):
            self.Selectors.return_object=self.ReturnObjects["Path"]
        else:
            self.Selectors.return_object=self.ReturnObjects["NEO"]

        if(kwargs.get("date") is not None):
            self.DateSearch.type=DateSearch.equals
            self.DateSearch.values=kwargs.get("date")
        else:
            self.DateSearch.type=DateSearch.between
            self.DateSearch.values=dict()
            self.DateSearch.values["start"]=kwargs.get("start_date")
            self.DateSearch.values["end"]=kwargs.get("end_date")
        self.Selectors.date_search=self.DateSearch


    def build_query(self):
        """
        Transforms the provided query options, set upon initialization, into a set of Selectors that the NEOSearcher
        can use to perform the appropriate search functionality

        :return: QueryBuild.Selectors namedtuple that translates the dict of query options into a SearchOperation
        """

        # TODO: Translate the query parameters into a QueryBuild.Selectors object
        return self.Selectors


class Filter(object):
    """
    Object representing optional filter options to be used in the date search for Near Earth Objects.
    Each filter is one of Filter.Operators provided with a field to filter on a value.
    """
    Options = {
        # TODO: Create a dict of filter name to the NearEarthObject or OrbitalPath property
        "distance":"miss_distance_kilometers",
        "diameter":"diameter_min_km",
        "is_hazardous":"is_potentially_hazardous_asteroid"

    }

    Operators = {
        # TODO: Create a dict of operator symbol to an Operators method, see README Task 3 for hint
        "<":operator.lt,
        "<=":operator.le,
        ">":operator.gt,
        ">=":operator.ge,
        "=":operator.eq,
        "!=":operator.ne

    }

    def __init__(self, field, field_object, operation, value):
        """
        :param field:  str representing field to filter on
        :param field:  str representing object to filter on
        :param operation: str representing filter operation to perform
        :param value: str representing value to filter for
        """
        self.field = field
        self.object = field_object
        self.operation = operation
        self.value = value

    @staticmethod
    def create_filter_options(filter_options):
        """
        Class function that transforms filter options raw input into filters

        :param input: list in format ["filter_option:operation:value_of_option", ...]
        :return: defaultdict with key of NearEarthObject or OrbitPath and value of empty list or list of Filters
        """

        # TODO: return a defaultdict of filters with key of NearEarthObject or OrbitPath and value of empty list or list of Filters

        filters=defaultdict(list)
        if(filter_options is not None):
            for filter_option in filter_options:
                filter_option=filter_option.split(":")
                field=filter_option[0]
                operation=filter_option[1]
                value=filter_option[2]
                if(field!="distance"):
                    filters["NearEarthObject"].append((field,operation,value))
                else:
                    filters["OrbitPath"].append((field,operation,value))
            return filters
        else:
            return None

    def apply(self, results):
        """
        Function that applies the filter operation onto a set of results

        :param results: List of Near Earth Object results
        :return: filtered list of Near Earth Object results
        """
        # TODO: Takes a list of NearEarthObjects and applies the value of its filter operation to the results
        filtered_results=list()
        value=self.value
        if(self.field=="distance" or self.field=="diameter"):
            value=float(value)
        if(self.field=="diameter" or self.field=="is_hazardous"):
            for result in results:
                if(self.Operators[self.operation](getattr(result, self.Options[self.field]),value)):
                    filtered_results.append(result)
        elif(self.field=="distance"):    
            for result in results:
                orbits=result.orbits
                for orbit in orbits:
                    if(self.Operators[self.operation](getattr(orbit, self.Options[self.field]),value)):
                        filtered_results.append(result)
                        break

        return filtered_results



class NEOSearcher(object):
    """
    Object with date search functionality on Near Earth Objects exposed by a generic
    search interface get_objects, which, based on the query specifications, determines
    how to perform the search.
    """

    def __init__(self, db):
        """
        :param db: NEODatabase holding the NearEarthObject instances and their OrbitPath instances
        """
        self.db = db
        # TODO: What kind of an instance variable can we use to connect DateSearch to how we do search?
        self.db_data=db.retrieve()
        self.neo_date_dict=self.db_data[0]
        self.orbit_date_dict=self.db_data[1]
        self.neo_name_dict=self.db_data[2]


    def get_objects(self, query):
        """
        Generic search interface that, depending on the details in the QueryBuilder (query) calls the
        appropriate instance search function, then applys any filters, with distance as the last filter.

        Once any filters provided are applied, return the number of requested objects in the query.return_object
        specified.

        :param query: Query.Selectors object with query information
        :return: Dataset of NearEarthObjects or OrbitalPaths
        """
        # TODO: This is a generic method that will need to understand, using DateSearch, how to implement search
        # TODO: Write instance methods that get_objects can use to implement the two types of DateSearch your project
        # TODO: needs to support that then your filters can be applied to. Remember to return the number specified in
        # TODO: the Query.Selectors as well as in the return_type from Query.Selector
        if(query.date_search.type==DateSearch.between):
            results=self.date_between(query)
        elif(query.date_search.type==DateSearch.equals):
            results=self.date_equals(query)
        filters=Filter.create_filter_options(query.filters) or None
        numbers=int(query.number)
        final_results=results
        if(filters is not None):
            for key in filters:
                for filter_option in filters[key]:
                    Filters=Filter(filter_option[0],key,filter_option[1],filter_option[2])
                    final_results=Filters.apply(final_results)
                    if(len(final_results)>=numbers):
                        break
        return final_results[:numbers]
    

    def date_equals(self,query):
        date=query.date_search.values
        object_type=query.return_object
        if(object_type==NearEarthObject):
            return self.neo_date_dict[date]
        elif(object_type==OrbitPath):
            return self.orbit_date_dict[date]

    def date_between(self,query):
        start=query.date_search.values["start"]
        end=query.date_search.values["end"]
        start=datetime.strptime(start, '%Y-%m-%d')
        end=datetime.strptime(end, '%Y-%m-%d')
        end=end+timedelta(days=1)
        date_array =(start + timedelta(days=x) for x in range(0, (end-start).days))
        object_type=query.return_object
        if(object_type==NearEarthObject):
            neo_list=list()
            for date in date_array:
                date=date.strftime('%Y-%m-%d')
                neo_list=neo_list+self.neo_date_dict[date]
            return neo_list
        elif(object_type==OrbitPath):
            orbit_list=list()
            for date in date_array:
                date=date.strftime('%d-%m-%Y')
                orbit_list=orbit_list+self.orbit_date_dict[date]
            return neo_list