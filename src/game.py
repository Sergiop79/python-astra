import sys
import time
import pygame

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

ball = pygame.image.load("ball.png").convert()
ballrect = ball.get_rect()

speed_x, speed_y = 2, 2
acceleration_x, acceleration_y = 0, 0
black = 0, 0, 0
white = 255, 255, 255

font = pygame.font.Font(None, 36)
status_template = "Volume: %(volume)s (%(status)s)"
ball_template = "Speed: %s, %s   Accel: %s, %s"

music = 'audio.ogg'
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

pop_sound = pygame.mixer.Sound('pop.wav')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.dict['button'] == 4:
                print "volume+"
            elif event.dict['button'] == 5:
                print "volume-"
            elif event.dict['button'] == 6:
                print "mute"
            elif event.dict['button'] == 7:
                print "unmute"
        #elif event.type == pygame.JOYAXISMOTION:
        #    if event.dict['axis'] == 0 and event.dict['value'] > 0:
        #        acceleration_x = event.dict['value']
        #        print "derecha, "
        #    elif event.dict['axis'] == 0 and event.dict['value'] < 0:
        #        acceleration_x = -event.dict['value']
        #        print "izquierda"
        #    elif event.dict['axis'] == 1 and event.dict['value'] > 0:
        #        acceleration_y = event.dict['value']
        #        print "abajo"
        #    elif event.dict['axis'] == 1 and event.dict['value'] < 0:
        #        acceleration_y = -event.dict['value']
        #        print "arriba"
        elif event.type == pygame.JOYHATMOTION:
            acceleration_x, acceleration_y = event.dict['value']

    if speed_x >= 0:
        speed_x += acceleration_x
    else:
        speed_x -= acceleration_x
    if speed_y >= 0:
        speed_y += acceleration_y
    else:
        speed_y -= acceleration_y

    ballrect = ballrect.move((speed_x, speed_y))
    if ballrect.left < 0 or ballrect.right > width:
        speed_x = -speed_x
        pop_sound.play()
    if ballrect.top < 0 or ballrect.bottom > height:
        speed_y = -speed_y
        pop_sound.play()

    status_text = font.render(status_template, 1, white)
    ball_text = font.render(ball_template % (speed_x, speed_y, acceleration_x, acceleration_y),
                            1, white)

    screen.fill(black)
    screen.blit(status_text, status_text.get_rect())
    screen.blit(ball_text, ball_text.get_rect(bottom=height))
    screen.blit(ball, ballrect)

    pygame.display.flip()
    time.sleep(0.01)
