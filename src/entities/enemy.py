import arcade
from src import constants

class Enemy(arcade.Sprite):
    def __init__(self, **kwargs):
        # Tiled passes properties via kwargs when using custom classes
        super().__init__("assets/images/enemy.png", scale=1.0)
        self.speed = 2
        self.patrol_timer = 0
        self.patrol_direction = 0
        
    def update_ia(self, player, walls, hazards):
        """Advanced AI: Follow player, but patrol away from walls and hazards"""
        old_x = self.center_x
        
        # If in patrol mode, continue patrolling until timer runs out
        if self.patrol_timer > 0:
            self.change_x = self.patrol_direction
            self.patrol_timer -= 1
        else:
            # Determine direction towards player
            if self.center_x < player.center_x:
                self.change_x = self.speed
            elif self.center_x > player.center_x:
                self.change_x = -self.speed
            else:
                self.change_x = 0
            
        # Move temporarily to check for collisions
        self.center_x += self.change_x
        
        # Check if we hit a wall or hazard
        hit_wall = arcade.check_for_collision_with_list(self, walls)
        hit_hazard = arcade.check_for_collision_with_list(self, hazards)
        
        if hit_wall or hit_hazard:
            # Revert movement
            self.center_x = old_x
            # Enter patrol mode: invert direction and set timer (e.g., 60 frames = 1 sec)
            self.patrol_direction = -self.change_x if self.change_x != 0 else -self.speed
            self.change_x = self.patrol_direction
            self.patrol_timer = 60 # Patrol for 1 second
        else:
            # Revert temporary move so game_view can apply it as standard
            self.center_x = old_x
            
    def update(self):
        # We don't call self.center_x += self.change_x here anymore 
        # as update_ia handles it or we do it in game_view
        pass
