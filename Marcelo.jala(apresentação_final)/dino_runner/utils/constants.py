import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

ALTURA = 680
LARGURA = 500
tela = pygame.display.set_mode((ALTURA, LARGURA))

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioWallpaper.png"))

pygame.mixer.init()

SOUNDTRACK = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/theme.mp3"))

JUMP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/jump.wav"))

POWER_UP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/power-up.wav"))

DEATH_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/lost_a_life.wav"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioWalk1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioWalk2.png")).convert_alpha(),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioStarWalk1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioStarWalk2.png")).convert_alpha(),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")).convert_alpha(),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioStarJump.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioDuck.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioDuck.png")).convert_alpha(),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioStarDuck.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioStarDuck.png")).convert_alpha(),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")).convert_alpha(),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/Dragon.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/gumba.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/gumba.png")).convert_alpha(),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/GreenTube.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/GreenTube.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/GreenTube.png")).convert_alpha(),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/Canon.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/Canon.png")).convert_alpha(),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Mario/others/Flower.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))


RAGE_BAR= pygame.image.load(os.path.join(IMG_DIR, 'Other/Rage.png')).convert_alpha()

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
