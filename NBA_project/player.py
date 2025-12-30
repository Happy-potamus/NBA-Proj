class game_stats:
    def __init__(self, age, height, weight, guard_def_rating, cen_def_rating, guards):
        self.opponent_height = float(height)-75
        self.opponent_weight = float(weight)-213
        self.opponent_age = float(age)-23.5
        self.opponent_gdef_rating = 115-float(guard_def_rating)
        self.opponent_cdef_rating = 113-float(cen_def_rating)
        self.guards=int(guards)-3
       
        self.shot_stats = {
            "free_throw_attempt": 0,
            "short_attempt": 0,
            "medium_attempt": 0,
            "long_attempt": 0,
            "short_make": 0,
            "medium_make": 0,
            "long_make": 0
        
        }