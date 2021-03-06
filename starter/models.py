class NearEarthObject(object):
    """
    Object containing data describing a Near Earth Object and it's orbits.

    # TODO: You may be adding instance methods to NearEarthObject to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given Near Earth Object, only a subset of attributes used
        """
        self.neo_id=kwargs["id"]
        self.name=kwargs["name"]
        self.height=float(kwargs["absolute_magnitude_h"])
        self.diameter_min_km=float(kwargs["estimated_diameter_min_kilometers"])
        self.diameter_max_km=float(kwargs["estimated_diameter_max_kilometers"])
        self.is_potentially_hazardous_asteroid=kwargs["is_potentially_hazardous_asteroid"]
        self.orbits=[]
        # TODO: What instance variables will be useful for storing on the Near Earth Object?

    def __repr__(self):

        return {"neo_id":self.neo_id,"name":self.name,"height":self.height,"min_diameter":self.diameter_min_km,"max_diameter":self.diameter_max_km,"hazardous":self.is_potentially_hazardous_asteroid,"No. of orbits":len(self.orbits)}

    def __str__(self):
        return "neo_id={} | name={} | height(km)={} | min_diameter(km)={} | max_diameter(km)={} | hazardous={} | No. of orbits={}".format(self.neo_id,self.name,self.height,self.diameter_min_km,self.diameter_max_km,self.is_potentially_hazardous_asteroid,len(self.orbits))

    def update_orbits(self, orbit):
        """
        Adds an orbit path information to a Near Earth Object list of orbits

        :param orbit: OrbitPath
        :return: None
        """
        # TODO: How do we connect orbits back to the Near Earth Object?
        if(orbit.neo_reference_id==self.neo_id):
            self.orbits.append(orbit)



class OrbitPath(object):
    """
    Object containing data describing a Near Earth Object orbit.

    # TODO: You may be adding instance methods to OrbitPath to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given orbit, only a subset of attributes used
        """
        # TODO: What instance variables will be useful for storing on the Near Earth Object?
        self.neo_name=kwargs["name"]
        self.neo_reference_id=kwargs["neo_reference_id"]
        self.speed=float(kwargs["kilometers_per_hour"])
        self.close_approach_date=kwargs["close_approach_date"]
        self.miss_distance_kilometers=float(kwargs["miss_distance_kilometers"])
        self.orbiting_body=kwargs["orbiting_body"]

    def __str__(self):
        return "neo_reference_id={} | neo_name={} | speed(km/h)={} | approach_date={} | miss_distance(km)={} | orbiting_body={}".format(self.neo_reference_id,self.neo_name,self.speed,self.close_approach_date,self.miss_distance_kilometers,self.orbiting_body)
    def __repr__(self):
        return {"neo_reference_id":self.neo_reference_id,"neo_name":self.neo_name,"speed":self.speed,"approach_date":self.close_approach_date, "miss_distance":self.miss_distance_kilometers,"orbiting_body":self.orbiting_body}
