#imports
import pygame, sys, random, time 
pygame.init()

#
gameScreen = pygame.display.set_mode((700, 500))

# Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

#FPS controller
fpsController = pygame.time.Clock()

# Variables
startPos = [100, 50]
body = [[100,50], [90,50], [80,50]]
foodPos = [random.randrange(1, 70)*10, random.randrange(1, 50)*10]
food = True

direction = 'RIGHT'
onChange = direction

# Game over
def gameOver():
	myFont = pygame.font.SysFont('Monaco', 72)
	endMessage = myFont.render('Game Over', True, red)
	endRect = endMessage.get_rect()
	endRect.midtop = (350, 25)
	gameScreen.blit(endMessage, endRect)
	pygame.display.flip()
	time.sleep(2)
	pygame.quit()
	sys.exit()


# Game
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				onChange = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				onChange = 'LEFT'
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				onChange = 'DOWN'
			if event.key == pygame.K_UP or event.key == ord('w'):
				onChange = 'UP'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))

	#conditionals so snake doesn't move backwards
	if onChange == 'RIGHT' and not direction =='LEFT':
		direction = 'RIGHT'
	if onChange == 'LEFT' and not direction =='RIGHT':
		direction = 'LEFT'
	if onChange == 'UP' and not direction =='DOWN':
		direction = 'UP'
	if onChange == 'DOWN' and not direction =='UP':
		direction = 'DOWN'

	if direction == 'RIGHT':
		startPos[0] += 10
	if direction == 'LEFT':
		startPos[0] -=10
	if direction == 'UP':
		startPos[1] -= 10
	if direction == 'DOWN':
		startPos[1] += 10

	body.insert(0, list(startPos))
	if startPos[0] == foodPos[0] and startPos[1] == foodPos[1]:
		food = False
	else:
		body.pop()

	if food == False:
		foodPos = [random.randrange(1, 70)*10, random.randrange(1, 50)*10]
	food = True

	gameScreen.fill(white)

	for pos in body:
		pygame.draw.rect(gameScreen, green, pygame.Rect(pos[0], pos[1], 10, 10))

	pygame.draw.rect(gameScreen, blue, pygame.Rect(foodPos[0], foodPos[1], 10, 10))
	
	if startPos[0] > 690 or startPos[0] < 0:
		gameOver()
	if startPos[1] > 490 or startPos[1] < 0:
		gameOver()

	for block in body[1:]:
		if startPos[0] == block[0] and startPos[1] == block[1]:
			gameOver()

	pygame.display.flip()
	fpsController.tick(20)