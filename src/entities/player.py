import arcade
from src import constants

class Player(arcade.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__(scale=1.0)
        self.center_x = start_x
        self.center_y = start_y
        self.speed = constants.PLAYER_MOVEMENT_SPEED
        self.jump_speed = constants.PLAYER_JUMP_SPEED

        # Track state
        self.character_face_direction = 0 # 0 for right, 1 for left
        self.cur_texture = 0
        
        # Load textures
        main_path = "assets/images/player"
        
        def load_texture_pair(filename):
            """Helper to load a texture and its mirrored version"""
            texture = arcade.load_texture(filename)
            return [
                texture,
                texture.flip_left_right()
            ]

        # Idle texture
        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")
        
        # Jump and Fall textures
        self.jump_texture_pair = load_texture_pair(f"{main_path}_jump.png")
        self.fall_texture_pair = load_texture_pair(f"{main_path}_fall.png")
        
        # Walk textures
        self.walk_textures = []
        for i in range(1, 5):
            texture = load_texture_pair(f"{main_path}_walk_{i}.png")
            self.walk_textures.append(texture)
            
        # Set initial texture
        self.texture = self.idle_texture_pair[0]

    def update_animation(self, delta_time: float = 1/60):
        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == 0:
            self.character_face_direction = 1
        elif self.change_x > 0 and self.character_face_direction == 1:
            self.character_face_direction = 0

        # Jumping/Falling animation
        if self.change_y > 0:
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return
        elif self.change_y < 0:
            # Note: Physics engine might report small negative change_y when on ground
            # but Arcade's PhysicsEnginePlatformer usually handles this.
            # We check if we are actually in the air in a more robust way if needed,
            # but for now change_y is a good indicator.
            self.texture = self.fall_texture_pair[self.character_face_direction]
            return

        # Idle animation
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 3 * 5: # 5 frames per texture update
            self.cur_texture = 0
        frame = self.cur_texture // 5
        self.texture = self.walk_textures[frame][self.character_face_direction]
