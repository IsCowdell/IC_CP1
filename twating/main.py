import pygame
import sys
import csv
import os
from datetime import datetime
 
pygame.init()
 
# ─────────────────────────────────────────────
# DISPLAY
# ─────────────────────────────────────────────
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("THE FINAL BLIGHT")
 
# ─────────────────────────────────────────────
# COLORS
# ─────────────────────────────────────────────
WHITE     = (255, 255, 255)
GRAY      = (180, 180, 180)
DARK      = (50,  50,  50)
GREEN     = (100, 200, 100)
RED       = (139, 0,   0)       # Deep crimson for the kingdom backdrop
BLACK     = (0,   0,   0)
GOLD      = (212, 175, 55)
 
# ─────────────────────────────────────────────
# FONT  ← your Darkbyte font, one function for everything
# ─────────────────────────────────────────────
FONT_PATH       = r'assets\Darkbyte-4nly6.ttf'
FONT_SIZE       = 36
FONT_SIZE_LARGE = 52
FONT_SIZE_SMALL = 24
 
def draw_text(text, size, color, surface, x, y):
    font = pygame.font.Font(FONT_PATH, size)
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
 
# ─────────────────────────────────────────────
# IMAGES  ← drop your asset paths here
# ─────────────────────────────────────────────
# bg_image  = pygame.image.load("assets/images/intro_bg.png").convert()
# bg_image  = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
bg_image  = None   # Replace with the lines above when ready
 
# king_portrait = pygame.image.load("assets/images/king.png").convert_alpha()
king_portrait = None
 
# ─────────────────────────────────────────────
# MUSIC  ← drop your asset path here
# ─────────────────────────────────────────────
# pygame.mixer.music.load("assets/music/intro_theme.ogg")
# pygame.mixer.music.set_volume(0.6)
# pygame.mixer.music.play(-1)          # -1 = loop forever
print("Dramatic Music Playing...")     # placeholder until real file is set
 
# ─────────────────────────────────────────────
# SAVE-GAME CSV HELPER
# ─────────────────────────────────────────────
SAVE_FILE = "save_data.csv"
 
def create_new_save():
    """Write a fresh save record and return the save dict."""
    save = {
        "player_name":  "Zan",
        "level":        1,
        "health":       100,
        "gold":         0,
        "created_at":   datetime.now().isoformat(timespec="seconds"),
        "last_played":  datetime.now().isoformat(timespec="seconds"),
    }
    fieldnames = list(save.keys())
    file_exists = os.path.isfile(SAVE_FILE)
    with open(SAVE_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(save)
    print(f"New game saved to '{SAVE_FILE}'.")
    return save
 
def load_level(level_number):
    """
    Transition point — swap in your real level loader here.
    For now it just prints and returns a placeholder dict.
    """
    print(f"Loading Level {level_number}...")
    # TODO: return Level(level_number) once you have a Level class
    return {"level": level_number, "name": f"Level {level_number}"}
 
# ─────────────────────────────────────────────
# SKIP BUTTON
# ─────────────────────────────────────────────
class SkipButton:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
 
    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect, border_radius=8)
        # Measure first so we can centre, then draw with draw_text
        tmp = pygame.font.Font(FONT_PATH, FONT_SIZE_SMALL).render(self.text, True, DARK)
        tx  = self.rect.x + (self.rect.w - tmp.get_width())  // 2
        ty  = self.rect.y + (self.rect.h - tmp.get_height()) // 2
        draw_text(self.text, FONT_SIZE_SMALL, DARK, screen, tx, ty)
 
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
 
skip_button = SkipButton("Skip Intro", 620, 520, 150, 50)
 
# ─────────────────────────────────────────────
# INTRO LINES
# ─────────────────────────────────────────────
intro_lines = [
    "Prelude: A kingdom called ArisKatsia",
    "The last king lays slaughtered in front of the prince's eyes.",
    "This is a trial about tragedy.",
    "Now it's only up to you, our last prince, Zan.",
    "THE FINAL BLIGHT",
]
 
line_index     = 0
last_update    = pygame.time.get_ticks()
delay          = 2500          # ms between lines
intro_skipped  = False
intro_done     = False         # True once all lines have shown
clock          = pygame.time.Clock()
 
# ─────────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────────
running = True
while running:
    # ── Events ──────────────────────────────
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save = create_new_save()
            level_data = load_level(save["level"])
            print(f"Starting: {level_data['name']}")
            running = False
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if skip_button.is_clicked(event.pos):
                intro_skipped = True
                line_index = len(intro_lines) - 1
 
    # ── Advance lines ────────────────────────
    current_time = pygame.time.get_ticks()
    if not intro_skipped and not intro_done:
        if current_time - last_update > delay:
            if line_index < len(intro_lines) - 1:
                line_index += 1
                last_update = current_time
            else:
                intro_done = True
 
    # ── Draw ─────────────────────────────────
    # Background: image if loaded, else solid crimson
    if bg_image:
        screen.blit(bg_image, (0, 0))
    else:
        screen.fill(RED)
 
    # Optional portrait
    if king_portrait:
        screen.blit(king_portrait, (WIDTH - king_portrait.get_width() - 20, 20))
 
    # Last line gets the large title font and gold colour
    is_title = (line_index == len(intro_lines) - 1)
    size  = FONT_SIZE_LARGE if is_title else FONT_SIZE
    color = GOLD            if is_title else WHITE
    draw_text(intro_lines[line_index], size, color, screen, 50, HEIGHT // 2)
 
    # Skipped notice
    if intro_skipped:
        draw_text("Intro skipped — press any key to continue.",
                  FONT_SIZE_SMALL, GREEN, screen, 50, HEIGHT // 2 + 70)
 
    # Skip button (hide once fully done)
    if not intro_done:
        skip_button.draw()
 
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
sys.exit()