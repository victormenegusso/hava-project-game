import arcade
import math
from src import constants
from src.entities.enemy import Enemy

class Boss(Enemy):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.texture = arcade.load_texture("assets/images/boss.png")
        self.health = constants.BOSS_HEALTH
        self.speed = constants.BOSS_SPEED
        self.active = False
        self.activation_distance = 400
        
    def update_ia(self, player, walls, hazards):
        """Boss AI: Only starts following when player is nearby"""
        distance = math.sqrt((self.center_x - player.center_x)**2 + (self.center_y - player.center_y)**2)
        
        if not self.active and distance < self.activation_distance:
            self.active = True
            print("Boss activated!")
            
        if self.active:
            super().update_ia(player, walls, hazards)
        else:
            self.change_x = 0
