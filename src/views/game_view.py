import arcade
from src import constants
from src.entities.player import Player

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player = None
        self.scene = None
        self.tile_map = None
        self.physics_engine = None
        self.camera = None
        self.ui_camera = None
        
        # Sounds
        self.jump_sound = None
        self.coin_sound = None
        self.hit_sound = None

    def setup(self):
        # Camera setup: Map screen pixels 1:1
        rect = arcade.LBWH(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.camera = arcade.camera.Camera2D(projection=rect)
        self.ui_camera = arcade.camera.Camera2D(projection=rect)
        
        # Center the UI camera so (0,0) is bottom-left and (Width, Height) is top-right
        self.ui_camera.position = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

        if self.window:
            self.window.background_color = arcade.color.AMAZON

        # Tilemap loading
        map_name = "maps/level_1.tmx"
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
                self.player, gravity_constant=0.5, walls=self.scene["Platforms"]
            )
            print("Physics engine initialized with walls.")
        else:
             print("Warning: Platforms layer missing in map.")
             self.physics_engine = arcade.PhysicsEnginePlatformer(
                self.player, gravity_constant=0.5, walls=arcade.SpriteList()
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
                
        # Check bounds (Falling off map)
        if self.player.center_y < -100:
            self.reset_player()
                
        self.center_camera_to_player()

    def on_key_press(self, key, modifiers):
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
