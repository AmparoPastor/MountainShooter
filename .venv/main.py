import pygame

print('Setup start')
pygame.init()
window = pygame.display.set_mode((800, 600))
print('Setup end')

print('Loop start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
