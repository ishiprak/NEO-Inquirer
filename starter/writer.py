from enum import Enum
from database import NearEarthObject,OrbitPath
import csv
class OutputFormat(Enum):
    """
    Enum representing supported output formatting options for search results.
    """
    display = 'display'
    csv_file = 'csv_file'

    @staticmethod
    def list():
        """
        :return: list of string representations of OutputFormat enums
        """
        return list(map(lambda output: output.value, OutputFormat))


class NEOWriter(object):
    """
    Python object use to write the results from supported output formatting options.
    """

    def __init__(self):
        # TODO: How can we use the OutputFormat in the NEOWriter?
        pass

    def write(self, format, data, **kwargs):
        """
        Generic write interface that, depending on the OutputFormat selected calls the
        appropriate instance write function

        :param format: str representing the OutputFormat
        :param data: collection of NearEarthObject or OrbitPath results
        :param kwargs: Additional attributes used for formatting output e.g. filename
        :return: bool representing if write successful or not
        """
        # TODO: Using the OutputFormat, how can we organize our 'write' logic for output to stdout vs to csvfile
        # TODO: into instance methods for NEOWriter? Write instance methods that write() can call to do the necessary
        # TODO: output format.

        if(not isinstance(data, list)):
            return False

        writer=False
        if(format=="display"):
            writer=self.display_write(data)
        elif(format=="csv_file"):
            writer=self.csv_write(data)
        else:
            return False
        
        if(writer):
            return True
        else:
            return False
        return True

    def display_write(self,data):
        try:
            if(len(data)==0):
                print("\n")
                print("**************************************************************")
                print("Sorry no near earth objects could be found for the given parameters.")
            else:
                if(type(data[0])==NearEarthObject):
                    count=0
                    for neo in data:
                        count=count+1
                        print("\n\n")
                        print("***************************** Near Earth Object {} *********************************".format(count))
                        print(neo)
                        print()
                        print("***********Orbit Paths*************")
                        for orbit in neo.orbits:
                            print(orbit)
                elif(type(data[0])==OrbitPath):
                    count=0
                    for orbit in data:
                        count=count+1
                        print("\n\n")
                        print("***************************** Orbit Path {} *********************************".format(count))
                        print(orbit)
                else:
                    return False
            print()
            return True
        except:
            return False



    def csv_write(self,data):
        try:
            with open('neo_database_result.csv', 'w') as file:
                writer = csv.writer(file)
                if(len(data)==0):
                    writer.writerow(["No data found","No data found","No data found","No data found","No data found","No data found"])
                    return True
                if(type(data[0])==NearEarthObject):
                    writer.writerow(["NEO Id", "Name", "Near Earth Object No.", "Orbit Path No.", "Total Orbits", "Close Approach Date"])
                    if(len(data)==0):
                        writer.writerow(["No data found","No data found","No data found","No data found","No data found","No data found"])
                    else:
                        count=0
                        for neo in data:
                            count=count+1
                            count2=0
                            for orbit in neo.orbits:
                                count2=count2+1
                                row_list=[orbit.neo_reference_id,orbit.neo_name,count,count2,len(neo.orbits),orbit.close_approach_date]
                                writer.writerow(row_list)
                elif(type(data[0])==OrbitPath):  
                    writer.writerow(["Orbit-NEO Id", "NEO-Name", "Orbit No.", "Miss-Distance (in km)", "Close Approach Date"])
                    if(len(data)==0):
                        writer.writerow(["No data found","No data found","No data found","No data found","No data found"])
                    else:
                        count=0
                        for orbit in data:
                            count=count+1
                            row_list=[orbit.neo_reference_id,orbit.neo_name,count,orbit.miss_distance_kilometers,orbit.close_approach_date]
                            writer.writerow(row_list) 
                else:
                    return False
            return True
        except:
            return False 
        
