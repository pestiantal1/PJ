import random

class Upgrade:
    def __init__(self, name, description, effect_type, value, max_stacks = 5):
        self.name = name
        self.description = description
        self.effect_type = effect_type
        self.value = value
        self.max_stacks = max_stacks
        self.current_stacks = 0
        
    def apply(self, player, game_state):
        if self.current_stacks >= self.max_stacks:
            return False
        
        self.current_stacks += 1
        
        if self.effect_type == "player_speed":
            player.max_speed_multiplier = getattr(player, 'max_speed_multiplier', 1.0) + self.value
        elif self.effect_type == "player_turn_speed":
            player.turn_speed_bonus = getattr(player, 'turn_speed_bonus', 0) + self.value
        elif self.effect_type == "fire_rate":
            player.fire_rate_bonus = getattr(player, 'fire_rate_bonus', 0) + self.value
        elif self.effect_type == "bullet_damage":
            player.bullet_damage_multiplier = getattr(player, 'bullet_damage_multiplier', 1.0) + self.value
        
        return True
    
    def can_stack(self):
        return self.current_stacks < self.max_stacks
    
class UpgradeManager:
    
    def __init__(self):
        self.available_upgrades = self._create_upgrades()
        self.active_upgrades = {}
        
    def _create_upgrades(self):
        return [
            Upgrade("Speed", "+ SPEED", "player_speed", 0.15, max_stacks=5),
            Upgrade("Maneuverability", "+ TURN SPEED", "player_turn_speed", 1, max_stacks=5),
            Upgrade("Rapid fire", "+ FIRE RATE", "fire_rate", 2, max_stacks=15),
            Upgrade("Damage", "+ DAMAGE", "bullet_damage", 2, max_stacks=15),
            Upgrade("Afterburner", "+ SPEED", "player_speed", 0.2, max_stacks=5),
        ]
        
    def get_random_upgrades(self,count=3):
        available = [u for u in self.available_upgrades if u.name not in self.active_upgrades or self.active_upgrades[u.name].can_stack()]
        
        if len(available) == 0:
            return []
        
        count = min(count, len(available))
        return random.sample(available, count)
    
    def apply_upgrade(self,upgrade, player, game_state):
        if upgrade.name not in self.active_upgrades:
            self.active_upgrades[upgrade.name] = upgrade
        
        return self.active_upgrades[upgrade.name].apply(player, game_state)
    
    def reset(self):
        self.available_upgrades = self._create_upgrades()
        self.active_upgrades = {}

