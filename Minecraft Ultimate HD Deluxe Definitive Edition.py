import pygame
import random
import os

pygame.init()
screen = pygame.display.set_mode((1024, 800))
pygame.display.set_caption('Minecraft Ultimate HD Deluxe Definitive Edition')

#Textures
textures = {}
for file in os.listdir(str(os.getcwd()) + "\Textures"):
    textures[file.replace(".png", "").lower()] = pygame.transform.scale(pygame.image.load(str(os.getcwd()) + "\Textures\\" + file).convert(), (32, 32))

#Map
class map:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.tiles = []

        self.generate()

    def generate(self):
        #Generate first two layers
        self.tiles = [["grass" for _ in range(self.width)], ["dirt" for _ in range(self.width)]]
            
        #Map generation
        for y in range(2, self.height):
            if y < 4:
                self.tiles.append([random.choice(["dirt", "stone"]) for _ in range(self.width)])
            elif y < 8:
                self.tiles.append(["stone" for _ in range(self.width)])
            else:
                self.tiles.append([random.choice(["coal", "stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone"]) for _ in range(self.width)])

    def render(self):
        #Display sky
        screen.fill((145, 226, 255))

        #Map render
        for y in range(0, len(self.tiles)):
            for tile in range(0, len(self.tiles[y])):
                screen.blit(textures[self.tiles[y][tile]], (tile * 32, y * 32 + 8 * 32))

        pygame.display.flip()

#Run the game
level = map(32, 32)
level.render()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False