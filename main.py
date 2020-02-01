import pygame, sys, pygame.midi
from pygame.locals import *

# set up pygame
pygame.init()
pygame.midi.init()
print(pygame.midi.get_init())
print(pygame.midi.get_count())
print(pygame.midi.get_device_info(1))
print(pygame.midi.get_device_info(2))
print(pygame.midi.get_device_info(3))
print(pygame.midi.get_device_info(4))
print(pygame.midi.get_device_info(5))

midiInput = pygame.midi.Input(1)

while True:
    if midiInput.poll():
        print(midiInput.read(10))
# run the game loop
'''
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            '''

