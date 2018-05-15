import pygame
import random

FPS = 50

window_width = 400
window_height = 400

paddle_width = 20
paddle_height = 60

ball_width = 10
ball_height = 10


paddle_speed = 2
ball_x_speed = 3
ball_y_speed = 2

white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode(window_width,window_height)

def drawBall(ballXpos, ballYpos):
	ball = pygame.rect(ballXpos,ballYpos,ball_width,ball_height)
	pygame.draw.rect(screen,white,ball)


def drawPaddle(PaddleYpos):
	paddle = pygame.rect(paddle_buffer,paddleYpos,paddle_wid)