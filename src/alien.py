import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien."""

	def __init__(self, ai_settings, screen):
		"""Initialize the alien and set its starting position"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the alien image and set its image
		self.image = pygame.image.load('../images/GiosHead.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near the top of the left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alen's exact position.
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the alen at its current location."""
		self.screen.blit(self.image, self.rect)
