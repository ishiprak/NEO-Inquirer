class NearEarthObject(object):
    """
    Object containing data describing a Near Earth Object and it's orbits.

    # TODO: You may be adding instance methods to NearEarthObject to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given Near Earth Object, only a subset of attributes used
        """
        neo_id=kwargs["id"]
        name=kwargs["name"]
        height=kwargs["absolute_magnitude_h"]
        diameter=kwargs["estimated_diameter_max_kilometers"]
        hazardous=kwargs["is_potentially_hazardous_asteroid"]
        orbits=[]
        # TODO: What instance variables will be useful for storing on the Near Earth Object?

    def __repr__(self):
        print("neo_id={} name={} height={} diameter={} hazardous={} orbits={}".format(self.neo_id,self.name,self.height,self.diameter,self.hazardous,self.orbits))

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
        neo_reference_id=kwargs["neo_reference_id"]
        speed=kwargs["kilometers_per_hour"]
        approach_date=kwargs["close_approach_date"]
        distance=kwargs["miss_distance_kilometers"]
        orbiting_body=kwargs["orbiting_body"]

    def __repr__(self):
        print("neo_reference_id={} speed={} approach_date={} distance=kwargs{} orbiting_body={}".format(self.neo_reference_id,self.speed,self.approach_date,self.distance,self.orbiting_body))
