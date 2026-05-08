import pygame
 
class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 300, 50, 50)
        self.vel_x = 0
 
        # Dodge state
        self.is_dodging = False
        self.dodge_duration = 300        # How long the dodge lasts (ms)
        self.dodge_timer = 0
        self.dodge_cooldown = 800        # Time before you can dodge again (ms)
        self.last_dodge_time = 0
        self.dodge_speed = 8             # Pixels per frame during dodge
        self.dodge_direction = 1         # 1 = right, -1 = left
 
        # Invincibility window during dodge
        self.is_invincible = False
        self.invincible_window = 200     # Only invincible for first 200ms of dodge
 
    def dodge(self, direction):
        """
        Call this when the player presses the dodge key.
        direction: 1 for right, -1 for left
        """
        now = pygame.get_ticks()
 
        # Block dodge if already dodging or still on cooldown
        if self.is_dodging:
            print("Already dodging!")
            return
        if now - self.last_dodge_time < self.dodge_cooldown:
            remaining = self.dodge_cooldown - (now - self.last_dodge_time)
            print(f"Dodge on cooldown! {remaining}ms remaining.")
            return
 
        # Start the dodge
        self.is_dodging = True
        self.is_invincible = True
        self.dodge_timer = now
        self.last_dodge_time = now
        self.dodge_direction = direction
        print(f"Dodge! Direction: {'Right' if direction == 1 else 'Left'}")
 
    def update(self, screen_width):
        now = pygame.get_ticks()
 
        if self.is_dodging:
            elapsed = now - self.dodge_timer
 
            # Move the player in the dodge direction
            self.rect.x += self.dodge_speed * self.dodge_direction
 
            # Clamp to screen bounds
            self.rect.x = max(0, min(screen_width - self.rect.width, self.rect.x))
 
            # End invincibility window after invincible_window ms
            if elapsed > self.invincible_window and self.is_invincible:
                self.is_invincible = False
                print("Invincibility window ended.")
 
            # End dodge after dodge_duration ms
            if elapsed > self.dodge_duration:
                self.is_dodging = False
                self.is_invincible = False
                print("Dodge finished.")
 
    def take_hit(self, damage):
        if self.is_invincible:
            print(f"Attack dodged! ({damage} damage avoided)")
        else:
            print(f"Hit! Took {damage} damage.")
 
 
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dodge Demo")
 
player = Player()
clock = pygame.time.Clock()
 
# Simulated incoming attack (fires every 2 seconds)
last_attack_time = 0
attack_interval = 2000
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.dodge(direction=-1)
            if event.key == pygame.K_RIGHT:
                player.dodge(direction=1)
 
    # Simulate an enemy attack hitting the player every 2 seconds
    now = pygame.get_ticks()
    if now - last_attack_time > attack_interval:
        last_attack_time = now
        print("--- Incoming attack! ---")
        player.take_hit(damage=20)
 
    player.update(screen.get_width())
 
    # Draw
    screen.fill((30, 30, 30))
 
    # Player color: cyan when invincible, yellow when dodging, white normally
    if player.is_invincible:
        color = (0, 255, 255)
    elif player.is_dodging:
        color = (255, 255, 0)
    else:
        color = (255, 255, 255)
 
    pygame.draw.rect(screen, color, player.rect)
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit() 