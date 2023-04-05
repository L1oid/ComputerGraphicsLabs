import pygame
import pygame as pg
import sys

W = 900
H = 900

sc = pg.display.set_mode((W, H))

surf = pg.image.load('image.jpg')
new_surf = pygame.Surface((900, 900))

pixels = [[0] * 900 for i in range(900)]
pixels_compress = [[0] * 300 for j in range(300)]

for i in range(W):
    for j in range(H):
        pixels[i][j] = (surf.get_at((i, j))[0], surf.get_at((i, j))[1], surf.get_at((i, j))[2])

for i in range(300):
    for j in range(300):
        pixels_compress[i][j] = ((pixels[i][j][0] + pixels[i][j + 1][0] + pixels[i][j + 2][0] + pixels[i + 1][j][0] + pixels[i + 1][j + 1][0] + pixels[i + 1][j + 2][0] + pixels[i + 2][j][0] + pixels[i + 2][j + 1][0] + pixels[i + 2][j + 2][0]) / 9, (pixels[i][j][1] + pixels[i][j + 1][1] + pixels[i][j + 2][1] + pixels[i + 1][j][1] + pixels[i + 1][j + 1][1] + pixels[i + 1][j + 2][1] + pixels[i + 2][j][1] + pixels[i + 2][j + 1][1] + pixels[i + 2][j + 2][1]) / 9, (pixels[i][j][2] + pixels[i][j + 1][2] + pixels[i][j + 2][2] + pixels[i + 1][j][2] + pixels[i + 1][j + 1][2] + pixels[i + 1][j + 2][2] + pixels[i + 2][j][2] + pixels[i + 2][j + 1][2] + pixels[i + 2][j + 2][2]) / 9)

print(pixels_compress)

for i in range(300):
    for j in range(300):
        new_surf.fill((pixels_compress[i][j][0], pixels_compress[i][j][1], pixels_compress[i][j][2]), (i, j, 1, 1))

rect = surf.get_rect(bottomright=(W, H))
sc.blit(new_surf, rect)

pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

pg.time.delay(20)
