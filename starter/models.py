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
        self.height=kwargs["absolute_magnitude_h"]
        self.diameter=kwargs["estimated_diameter_max_kilometers"]
        self.hazardous=kwargs["is_potentially_hazardous_asteroid"]
        self.orbits=[]
        # TODO: What instance variables will be useful for storing on the Near Earth Object?

    def __repr__(self):
        #print("neo_id={} name={} height={} diameter={} hazardous={}".format(self.neo_id,self.name,self.height,self.diameter,self.hazardous))
        return {"neo_id":self.neo_id,"name":self.name,"height":self.height,"diameter":self.diameter,"hazardous":self.hazardous}

    def __str__(self):
        return "neo_id={} name={} height={} diameter={} hazardous={}".format(self.neo_id,self.name,self.height,self.diameter,self.hazardous)

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
        self.neo_reference_id=kwargs["neo_reference_id"]
        self.speed=kwargs["kilometers_per_hour"]
        self.approach_date=kwargs["close_approach_date"]
        self.distance=kwargs["miss_distance_kilometers"]
        self.orbiting_body=kwargs["orbiting_body"]

    def __str__(self):
        return "neo_reference_id={} speed={} approach_date={} distance={} orbiting_body={}".format(self.neo_reference_id,self.speed,self.approach_date,self.distance,self.orbiting_body)
    def __repr__(self):
        return {"neo_reference_id":self.neo_reference_id,"speed":self.speed,"approach_date":self.approach_date, "distance":self.distance,"orbiting_body":self.orbiting_body}
