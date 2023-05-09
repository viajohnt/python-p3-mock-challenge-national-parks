
class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        visitor.trips(self)
        visitor.national_parks(national_park)
        national_park.trips(self)
        national_park.visitors(visitor)
        

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, new_visitor):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor):
            self._visitor = new_visitor
        else:
            raise Exception
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, new_national_park):
        from classes.national_park import NationalPark
        if isinstance(new_national_park, NationalPark):
            self._national_park = new_national_park
        else:
            raise Exception 
