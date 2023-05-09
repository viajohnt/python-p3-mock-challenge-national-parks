class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str) and not hasattr (self, 'name'):
            self._name = new_name
        else:
            raise Exception
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor) and new_visitor not in self._visitors:
            self._visitors.append(new_visitor)
        return self._visitors
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        if self._visitors:
            return max(self._visitors, key=lambda visitor: len(visitor._trips))
        else:
            return None
        
        # max_visitor = None
        # max_visits = 0
        # for v in self._visitors:
        #     v_visits = len([t for t in self._trips if t.visitor == v])
        #     if v_visits > max_visits:
        #         max_visits = v_visits
        #         max_visitor = v
        # return max_visitor