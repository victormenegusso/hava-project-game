import arcade
import os
from src import constants
from src.entities.player import Player
from src.entities.enemy import Enemy

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player = None
        self.scene = None
        self.tile_map = None
        self.physics_engine = None
        self.camera = None
        self.ui_camera = None
        
        # Game state
        self.level_complete = False
        self.game_complete = False
        
        # Level management
        self.levels = []
        self.current_level_index = 0
        self.find_levels()
        
        # Sounds
        self.jump_sound = None
        self.coin_sound = None
        self.hit_sound = None

    def find_levels(self):
        """Find all level_*.tmx files in maps/ and sort them numerically"""
        import os
        import re
        
        map_dir = "maps"
        if not os.path.exists(map_dir):
            return
            
        files = os.listdir(map_dir)
        level_files = [f for f in files if f.startswith("level_") and f.endswith(".tmx")]
        
        # Sort numerically by Extracting the number: level_1.tmx -> 1
        def get_level_num(filename):
            match = re.search(r"level_(\d+)", filename)
            return int(match.group(1)) if match else 0
            
        self.levels = sorted(level_files, key=get_level_num)
        print(f"Found levels: {self.levels}")

    def setup(self):
        # Reset level state
        self.level_complete = False
        self.game_complete = False
        
        # Camera setup: Map screen pixels 1:1
        rect = arcade.LBWH(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.camera = arcade.camera.Camera2D(projection=rect)
        self.ui_camera = arcade.camera.Camera2D(projection=rect)
        
        # Center the UI camera so (0,0) is bottom-left and (Width, Height) is top-right
        self.ui_camera.position = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

        if self.window:
            self.window.background_color = arcade.color.AMAZON

        # Tilemap loading
        if not self.levels:
            print("Error: No levels found in maps/ directory.")
            return

        map_name = os.path.join("maps", self.levels[self.current_level_index])
        layer_options = {
            "Platforms": {
                "use_spatial_hash": True,
            },
            "Coins": {
                "use_spatial_hash": True,
            },
            "Hazards": {
                "use_spatial_hash": True,
            },
            "enemy": {
                "use_spatial_hash": True,
                "custom_class": Enemy,
            },
            "goal": {
                "use_spatial_hash": True,
            },
        }
        
        # Read in the tiled map
        try:
            self.tile_map = arcade.load_tilemap(map_name, scaling=1.0, layer_options=layer_options)
            self.scene = arcade.Scene.from_tilemap(self.tile_map)
            # Arcade 3.x Scene keys can be accessed for debugging
            # Note: Scene acts like a dictionary of SpriteLists
            # print(f"Map loaded successfully. Layers: {list(str(k) for k in self.scene.keys() if hasattr(self.scene, 'keys'))}") # Safe print
        except FileNotFoundError:
             print(f"Error: Map file {map_name} not found.")
             return
        except Exception as e:
            print(f"Error loading map: {e}")
            import traceback
            traceback.print_exc()
            return

        # Player setup
        self.player = Player(100, 200) # Start slightly higher
        self.scene.add_sprite("Player", self.player)
        print(f"Player added at {self.player.position}")
        
        # Score setup
        self.score = 0
        
        # Physics setup with Platforms layer as walls
        if "Platforms" in self.scene:
            self.physics_engine = arcade.PhysicsEnginePlatformer(
                self.player, gravity_constant=constants.GRAVITY, walls=self.scene["Platforms"]
            )
            print("Physics engine initialized with walls.")
        else:
             print("Warning: Platforms layer missing in map.")
             self.physics_engine = arcade.PhysicsEnginePlatformer(
                self.player, gravity_constant=constants.GRAVITY, walls=arcade.SpriteList()
            )
            
        # Load sounds
        self.jump_sound = arcade.load_sound("assets/sounds/jump.wav")
        self.coin_sound = arcade.load_sound("assets/sounds/coin.wav")
        self.hit_sound = arcade.load_sound("assets/sounds/hit.wav")

    def on_show_view(self):
        if self.window:
            self.window.background_color = arcade.color.AMAZON
        self.setup()

    def on_draw(self):
        self.clear()
        
        # Draw World
        self.camera.use()
        if self.scene:
            self.scene.draw()
            
        # Draw GUI (Manually calculated world coordinates)
        # Camera position seems to be the bottom-left corner based on behavior
        cam_x, cam_y = self.camera.position
        
        # Draw relative to camera position (which is 0,0 or clamping upwards)
        score_x = cam_x + 20
        score_y = cam_y + constants.SCREEN_HEIGHT - 40
        
        arcade.draw_text(
            f"Score: {self.score}",
            score_x,
            score_y,
            arcade.color.WHITE,
            18
        )
        
        arcade.draw_text(
            "Controls: Arrows to Move, Space to Jump",
            score_x,
            score_y - 30, # Below score
            arcade.color.WHITE,
            14
        )
        
        level_name = self.levels[self.current_level_index].replace(".tmx", "").replace("_", " ").title()
        arcade.draw_text(
            f"Fase: {level_name}",
            score_x,
            score_y - 55, # Below controls
            arcade.color.WHITE,
            14
        )
        
        # Draw Congratulations Message
        if self.level_complete or self.game_complete:
            msg = constants.MSG_GAME_COMPLETE if self.game_complete else constants.MSG_LEVEL_COMPLETE
            
            # Draw semi-transparent background
            arcade.draw_rect_filled(
                arcade.XYWH(cam_x + constants.SCREEN_WIDTH / 2, cam_y + constants.SCREEN_HEIGHT / 2, 600, 200),
                (0, 0, 0, 150)
            )
            
            arcade.draw_text(
                msg,
                cam_x + constants.SCREEN_WIDTH / 2,
                cam_y + constants.SCREEN_HEIGHT / 2 + 20,
                arcade.color.GOLD,
                32,
                anchor_x="center"
            )
            
            arcade.draw_text(
                "Pressione ENTER para continuar",
                cam_x + constants.SCREEN_WIDTH / 2,
                cam_y + constants.SCREEN_HEIGHT / 2 - 40,
                arcade.color.WHITE,
                18,
                anchor_x="center"
            )
        
    def center_camera_to_player(self):
        if not self.player:
            return
            
        # Calculate the position to center the camera on the player
        # We assume .position sets the bottom-left corner of the viewport
        # based on user feedback (player appearing at bottom-left).
        
        screen_center_x = self.player.center_x - (constants.SCREEN_WIDTH / 2)
        screen_center_y = self.player.center_y - (constants.SCREEN_HEIGHT / 2)

        # Don't let camera travel past 0 (left/bottom map boundaries)
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
            
        self.camera.position = (screen_center_x, screen_center_y)
        
    def reset_player(self):
        """Teleport player back to start and reset movement"""
        self.player.center_x = 100
        self.player.center_y = 200
        self.player.change_x = 0
        self.player.change_y = 0
        
        # Play death sound
        arcade.play_sound(self.hit_sound)

    def on_update(self, delta_time):
        if not self.player or not self.physics_engine:
            return
            
        if self.physics_engine:
            self.physics_engine.update()
            
        # Debug print every 60 frames approx
        if int(1/delta_time) % 60 == 0: 
           print(f"Cam: {self.camera.position}, Player: {self.player.position}")
            
        # Coin Collision
        if self.player and "Coins" in self.scene:
            coins_hit = arcade.check_for_collision_with_list(self.player, self.scene["Coins"])
            for coin in coins_hit:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.coin_sound)
        
        # Hazard Collision
        if self.player and "Hazards" in self.scene:
            if arcade.check_for_collision_with_list(self.player, self.scene["Hazards"]):
                self.reset_player()
                
        # Enemy Collision and AI
        if self.player and "enemy" in self.scene:
            # Update Enemy AI
            for enemy in self.scene["enemy"]:
                if isinstance(enemy, Enemy):
                    enemy.follow_player(self.player)
                    enemy.update()

            enemies_hit = arcade.check_for_collision_with_list(self.player, self.scene["enemy"])
            for enemy in enemies_hit:
                # Check if player is falling onto the enemy
                if self.player.change_y < 0 and self.player.bottom > enemy.center_y:
                    enemy.remove_from_sprite_lists()
                    # Bounce player back up
                    self.player.change_y = constants.PLAYER_JUMP_SPEED / 2
                    arcade.play_sound(self.jump_sound)
                else:
                    self.reset_player()
                
        # Check bounds (Falling off map)
        if self.player.center_y < -100:
            self.reset_player()
            
        # Goal Collision
        if not (self.level_complete or self.game_complete) and self.player and "goal" in self.scene:
            if arcade.check_for_collision_with_list(self.player, self.scene["goal"]):
                if self.current_level_index < len(self.levels) - 1:
                    self.level_complete = True
                else:
                    self.game_complete = True
                self.player.change_x = 0
                self.player.change_y = 0
                
        self.center_camera_to_player()

    def on_key_press(self, key, modifiers):
        if self.level_complete or self.game_complete:
            if key == arcade.key.ENTER:
                if self.level_complete:
                    self.current_level_index += 1
                    self.level_complete = False
                    self.setup()
                elif self.game_complete:
                    from src.views.menu_view import MenuView
                    menu_view = MenuView()
                    self.window.show_view(menu_view)
                return

        if not self.player or not self.physics_engine:
            return
            
        if key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
             if self.physics_engine.can_jump():
                 self.player.change_y = self.player.jump_speed
                 arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = -self.player.speed
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = self.player.speed

    def on_key_release(self, key, modifiers):
        if not self.player:
            return
            
        if key == arcade.key.LEFT or key == arcade.key.A:
            if self.player.change_x < 0:
                self.player.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
             if self.player.change_x > 0:
                self.player.change_x = 0
