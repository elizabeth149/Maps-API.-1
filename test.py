import sys
import requests
import pygame

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
address_ll = ",".join(sys.argv[1:3])
size = sys.argv[3]
sp = f"https://static-maps.yandex.ru/1.x/?ll={address_ll}&spn={size}," \
     f"{size}&l=sat"
response = requests.get(sp)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
