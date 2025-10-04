import time

class RunData:
    def __init__(self):
        self.start_time = time.time()
        self.asteroids_destroyed = {
            "large": 0,
            "medium": 0,
            "small": 0,
        }
        self.total_shots_fired = 0
        self.upgrades_take = []
        self.max_level_reached = 1
        
    def record_asteroid_kill(self,size):
        if size in self.asteroids_destroyed:
            self.asteroids_destroyed[size] += 1
            
    def record_shot(self):
        self.total_shots_fired += 1
        
    def record_upgrade(self, upgrade_name):
        self.upgrades_take.append(upgrade_name)
        
    def update_max_level(self, level):
        if level > self.max_level_reached:
            self.max_level_reached = level
            
    def get_elapsed_time(self):
        return time.time() - self.start_time
    
    def get_total_kills(self):
        return sum(self.asteroids_destroyed.values())
    
    def get_accuracy(self):
        if self.total_shots_fired == 0:
            return 0.0
        
        return (self.get_total_kills() / self.total_shots_fired) * 100
    
    def reset(self):
        self.start_time = time.time()
        self.asteroids_destroyed = {
            "large": 0,
            "medium": 0,
            "small": 0,
        }
        self.total_shots_fired = 0
        self.upgrades_take = []
        self.max_level_reached = 1