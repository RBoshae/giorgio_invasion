import pygame
from pygame.sprite import Group

from src.settings import Settings
from src.game_stats import GameStats
from src.scoreboard import Scoreboard
from src.button import Button
from src.ship import Ship
from src.alien import Alien
from src import game_functions as gf


def run_game():
	# Initialize pygame, settings and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Giorgio Invasion')

	# Make the Play button
	play_button = Button(ai_settings, screen, "Play")

	# Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	# Make an alien
	alien = Alien(ai_settings, screen)

	# Make ship, a group of bullets, and a group of aliens.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	# Create a fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Music
	music = pygame.mixer.music.load('./sound/tron-world-rame.wav')
	pygame.mixer.music.play(-1)

	# Start the main loop for the game
	while True:

		# Listen for keyboard and mouse events
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, 
		bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
			play_button)


run_game()

