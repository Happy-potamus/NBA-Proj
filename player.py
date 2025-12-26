class game_stats:
    def __init__(self, height, weight, age, def_rating, minutes):
        self.opponent_height = height
        self.opponent_weight = weight
        self.opponent_age = age
        self.opponent_def_rating = def_rating
        self.minutes_played = minutes
        self.shot_stats = {
            "free_throw_attempt": 0,
            "short_attempt": 0,
            "medium_attempt": 0,
            "long_attempt": 0,
            "short_make": 0,
            "medium_make": 0,
            "long_make": 0
        
        }