from models import OrbitPath, NearEarthObject
import csv

class NEODatabase(object):
    """
    Object to hold Near Earth Objects and their orbits.

    To support optimized date searching, a dict mapping of all orbit date paths to the Near Earth Objects
    recorded on a given day is maintained. Additionally, all unique instances of a Near Earth Object
    are contained in a dict mapping the Near Earth Object name to the NearEarthObject instance.
    """

    def __init__(self, filename):
        """
        :param filename: str representing the pathway of the filename containing the Near Earth Object data
        """
        # TODO: What data structures will be needed to store the NearEarthObjects and OrbitPaths?
        # TODO: Add relevant instance variables for this.
        self.filename=filename
        self.neo_date_dict=dict()
        self.orbit_date_dict=dict()
        self.neo_name_dict=dict()

    def load_data(self, filename=None):
        """
        Loads data from a .csv file, instantiating Near Earth Objects and their OrbitPaths by:
           - Storing a dict of orbit date to list of NearEarthObject instances
           - Storing a dict of the Near Earth Object name to the single instance of NearEarthObject

        :param filename:
        :return:
        """
        if not (filename or self.filename):
            raise Exception('Cannot load data, no filename provided')

        filename = filename or self.filename
        self.neo_date_dict.clear()
        self.neo_name_dict.clear()
        self.orbit_date_dict.clear()
        # TODO: Load data from csv file.
        # TODO: Where will the data be stored?

        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            c=-1
            for row in csvreader:
                c=c+1
                if(c!=0):
                    neo=self.neo_name_dict.get(row[2])
                    if(neo is None):
                        neo=NearEarthObject(id=row[0],name=row[2],absolute_magnitude_h=row[4],estimated_diameter_min_kilometers=row[5],estimated_diameter_max_kilometers=row[6],is_potentially_hazardous_asteroid=row[13])
                        self.neo_name_dict[row[2]]=neo
                    orbit=OrbitPath(name=row[2],neo_reference_id=row[1],kilometers_per_hour=row[15],close_approach_date=row[17],miss_distance_kilometers=row[21],orbiting_body=row[23])
                    neo.update_orbits(orbit)
                    if(self.orbit_date_dict.get(row[17]) is None):
                        self.orbit_date_dict[row[17]]=list()
                    self.orbit_date_dict[row[17]].append(orbit)
                    if(self.neo_date_dict.get(row[17]) is None):
                        self.neo_date_dict[row[17]]=list()
                    if(neo not in self.neo_date_dict.values()):
                        self.neo_date_dict[row[17]].append(neo)
        return None

    def retrieve(self):
        return (self.neo_date_dict,self.orbit_date_dict,self.neo_name_dict)

