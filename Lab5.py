import pygame
import pygame as pg
import sys
import math

DMC = [
    (255,255,255),
    (148,91,128),
    (206,148,186),
    (236,207,225),
    (243,218,228),
    (156,41,74),
    (219,128,115),
    (255,199,176),
    (255,240,228),
    (143,57,38),
    (209,102,84),
    (188,0,97),
    (255,231,109),
    (214,43,91),
    (0,0,0),
    (0,79,97),
    (58,84,103),
    (163,90,91),
    (220,141,141),
    (167,139,136),
    (197,198,190),
    (85,95,82),
    (138,153,120),
    (231,18,97),
    (81,109,135),
    (188,22,65),
    (61,0,103),
    (127,84,130),
    (115,140,170),
    (219,36,79),
    (36,73,103),
    (162,121,164),
    (145,180,197),
    (194,36,67),
    (220,61,91),
    (237,69,90),
    (255,128,135),
    (255,157,144),
    (255,196,184),
    (189,73,47),
    (226,114,91),
    (95,112,91),
    (181,206,162),
    (243,250,209),
    (184,138,87),
    (196,155,100),
    (203,162,107),
    (157,60,39),
    (255,190,164),
    (194,101,76),
    (109,95,95),
    (167,139,136),
    (221,221,218),
    (140,91,43),
    (237,172,123),
    (151,84,20),
    (178,103,70),
    (187,107,57),
    (231,152,115),
    (238,171,121),
    (255,176,0),
    (255,255,190),
    (179,151,143),
    (210,185,175),
    (235,207,185),
    (116,114,92),
    (133,143,108),
    (176,187,140),
    (238,255,182),
    (187,0,97),
    (43,57,41),
    (67,85,73),
    (134,158,134),
    (195,206,183),
    (206,221,193),
    (16,127,135),
    (102,148,154),
    (194,209,207),
    (55,73,18),
    (159,169,142),
    (172,183,142),
    (205,182,158),
    (85,85,89),
    (239,214,188),
    (109,18,97),
    (146,85,130),
    (160,100,146),
    (243,206,225),
    (59,96,76),
    (97,134,97),
    (182,212,180),
    (214,230,204),
    (0,103,0),
    (151,152,49),
    (128,151,132),
    (208,223,205),
    (208,57,106),
    (222,57,105),
    (231,84,122),
    (255,115,140),
    (255,189,202),
    (255,207,214),
    (255,0,0),
    (255,91,0),
    (151,104,84),
    (158,109,91),
    (203,152,103),
    (219,176,122),
    (162,77,52),
    (163,163,157),
    (174,176,170),
    (224,224,215),
    (113,113,113),
    (121,121,121),
    (190,190,185),
    (202,202,202),
    (213,39,86),
    (255,206,158),
    (255,231,182),
    (209,140,103),
    (0,91,6),
    (0,96,47),
    (79,108,69),
    (79,121,66),
    (121,144,76),
    (165,164,103),
    (245,240,219),
    (219,55,121),
    (200,36,43),
    (255,115,97),
    (255,146,109),
    (255,200,124),
    (255,224,128),
    (255,235,168),
    (243,176,128),
    (132,102,0),
    (140,103,0),
    (145,104,0),
    (206,155,97),
    (221,166,107),
    (244,195,139),
    (244,233,202),
    (255,131,19),
    (255,142,4),
    (255,183,85),
    (255,230,146),
    (255,239,170),
    (255,240,197),
    (246,234,219),
    (240,247,239),
    (251,227,209),
    (255,177,147),
    (249,160,146),
    (255,201,188),
    (232,232,229),
    (231,249,203),
    (247,246,248),
    (255,177,174),
    (255,199,184),
    (181,98,46),
    (181,107,56),
    (204,119,66),
    (225,146,85),
    (71,55,93),
    (97,97,128),
    (147,139,164),
    (187,208,218),
    (30,58,95),
    (30,66,99),
    (103,115,141),
    (132,156,182),
    (233,238,233),
    (123,71,20),
    (30,130,133),
    (128,167,160),
    (190,193,205),
    (175,195,205),
    (162,0,88),
    (166,0,91),
    (179,0,91),
    (219,24,85),
    (255,234,235),
    (248,247,221),
    (30,54,85),
    (242,234,219),
    (0,0,73),
    (71,97,116),
    (85,108,128),
    (115,138,153),
    (213,231,232),
    (237,247,238),
    (130,90,8),
    (136,95,18),
    (144,103,18),
    (178,119,55),
    (219,182,128),
    (242,209,142),
    (94,56,27),
    (109,66,39),
    (128,85,30),
    (188,134,107),
    (219,194,164),
    (107,103,102),
    (153,92,48),
    (153,92,48),
    (79,86,76),
    (241,49,84),
    (249,90,97),
    (243,149,157),
    (255,194,191),
    (89,92,78),
    (118,55,19),
    (233,109,115),
    (206,43,0),
    (138,24,77),
    (78,95,57),
    (98,119,57),
    (143,163,89),
    (185,200,102),
    (49,105,85),
    (48,116,91),
    (49,128,97),
    (115,158,115),
    (153,188,149),
    (170,24,91),
    (171,22,95),
    (168,68,76),
    (180,75,82),
    (197,94,88),
    (206,103,91),
    (237,134,115),
    (86,99,100),
    (96,116,115),
    (200,198,194),
    (225,224,216),
    (102,122,140),
    (124,135,145),
    (182,186,194),
    (62,59,40),
    (67,63,47),
    (69,69,49),
    (73,86,55),
    (99,39,16),
    (0,0,49),
    (0,162,117),
    (255,206,164),
    (244,73,0),
    (255,91,0),
    (255,243,231),
    (239,162,127),
    (255,229,188),
    (170,213,164),
    (214,230,204),
    (255,109,115),
    (255,204,208),
    (0,160,130),
    (171,206,177),
    (243,108,123),
    (253,134,141),
    (233,233,233),
    (208,224,210),
    (206,213,176),
    (255,117,24),
    (255,106,0),
    (255,146,0),
    (255,194,67),
    (158,67,18),
    (246,141,57),
    (255,164,73),
    (58,82,65),
    (83,97,73),
    (134,145,110),
    (134,153,110),
    (47,91,73),
    (146,183,165),
    (192,224,200),
    (0,123,134),
    (170,222,225),
    (123,91,64),
    (170,134,103),
    (208,195,164),
    (115,91,93),
    (172,172,170),
    (198,190,173),
    (210,208,205),
    (84,56,23),
    (188,156,120),
    (239,219,190),
    (190,155,167),
    (225,205,200),
    (216,151,105),
    (229,193,139),
    (255,236,211),
    (85,73,0),
    (137,141,114),
    (187,179,148),
    (194,101,76),
    (233,233,223),
    (255,255,220),
    (202,226,229),
    (255,157,150),
    (188,64,85),
    (255,123,103),
    (255,172,162),
    (97,100,82),
    (120,134,107),
    (128,152,115),
    (225,249,190),
    (201,79,91),
    (255,214,209),
    (96,95,84),
    (116,127,96),
    (161,167,135),
    (83,37,16),
    (231,79,134),
    (247,152,182),
    (255,214,229),
    (161,53,79),
    (203,78,97),
    (250,151,144),
    (255,213,216),
    (255,85,91),
    (255,128,109),
    (254,212,219),
    (230,101,107),
    (253,229,217),
    (255,211,212),
    (184,75,77),
    (184,89,88),
    (195,118,123),
    (255,199,196),
    (209,93,103),
    (255,154,148),
    (156,125,133),
    (235,235,231),
    (149,102,162),
    (230,236,232),
    (12,91,108),
    (194,209,206),
    (237,247,247),
    (158,176,206),
    (248,248,252),
    (102,142,152),
    (227,234,230),
    (24,128,134),
    (24,101,111),
    (92,110,108),
    (255,250,224),
    (173,83,62),
    (231,134,103),
    (255,220,193),
    (221,109,91),
    (191,64,36),
    (237,122,100),
    (255,177,152),
    (113,71,42),
    (206,175,144),
    (139,109,115),
    (140,117,109),
    (81,76,83)
]
size = len(DMC)

pygame.font.init()

surf = pg.image.load('image.jpg')
W = surf.get_width()
H = surf.get_height()
STEP = 10
sc = pg.display.set_mode((W, H))
number_font = pygame.font.Font(None, 1)

while W % STEP != 0:
    W -= 1

while H % STEP != 0:
    H -= 1

result = pygame.surface.Surface((W / STEP, H / STEP))
result2 = pygame.surface.Surface((W / STEP, H / STEP))

for x in range(0, W, STEP):
    for y in range(0, H, STEP):
        r, g, b = 0, 0, 0

        for _x in range(STEP):
            for _y in range(STEP):
                _r, _g, _b, a = surf.get_at((x + _x, y + _y))
                r += _r
                g += _g
                b += _b

        r //= STEP ** 2
        g //= STEP ** 2
        b //= STEP ** 2

        min_color = 999999999
        min_r = 0
        min_g = 0
        min_b = 0
        id_color = 0

        for i in range(0, size):
            current_dmc_color = math.sqrt(((r - DMC[i][0]) ** 2) + ((g - DMC[i][1]) ** 2) + ((b - DMC[i][2]) ** 2))
            if current_dmc_color < min_color:
                id_color = str(i)
                min_color = current_dmc_color
                min_r = DMC[i][0]
                min_g = DMC[i][1]
                min_b = DMC[i][2]

        result.set_at((x // STEP, y // STEP), (min_r, min_g, min_b))

# temp = number_font.render("TTTTTT", True, (255, 255, 255))
# result.blit(temp, (2, 2))

res = pygame.Surface((W * 10, H * 10))

for x in range(W):
    for y in range(H):
        res.fill(result.get_at((x, y)), (x * 10, y * 10, 10, 10))


pygame.image.save(res, "out.png")

rect = surf.get_rect(bottomright=(W, H))
sc.blit(surf, rect)

pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

pg.time.delay(20)
