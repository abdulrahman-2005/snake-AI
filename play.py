import pygame
from helpers.snakeGame import *

def main():
	"""Function to play the Snake Game."""

	fps = 8
	game = SnakeGame(fps)
	pygame.font.init()

	while game.play:
		#Lock the game at a set fps
		game.clock.tick(game.fps)
		
		game.move_snake()
		game.check_collisions()

		if game.restart == True:
			game.restart = False
			continue
		
		game.redraw_window()
		game.event_handler()

		
if __name__ == "__main__":
	main()