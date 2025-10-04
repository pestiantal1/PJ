class GameState:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100
        self.total_kills = 0
        self.game_over = False
        
    def add_xp(self, amount):
        self.xp += amount
        leveled_up = False
        
        while self.xp >= self.xp_to_next_level and self.level < 100:
            self.xp -= self.xp_to_next_level
            self.level += 1
            self.xp_to_next_level = self._calculate_xp_for_level(self.level)
            leveled_up = True
            
        return leveled_up
    
    def _calculate_xp_for_level(self, level):
        base = 100
        growth_rate = 0.08
        return int(base * ((1 + growth_rate) ** (level - 1)))
    
    def add_score(self, points):
        self.score += points
        return self.add_xp(points)
    
    def increment_kills(self):
        self.total_kills += 1
    
    def reset(self):
        self.score = 0
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100
        self.total_kills = 0
        self.game_over = False
        