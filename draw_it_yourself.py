import json
import pygame

def draw_it_yourself():
    pygame.init()
    screen = pygame.display.set_mode((512, 512))
    flag = True

    coords = []

    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif pygame.mouse.get_pressed()[0]:
                coord = pygame.mouse.get_pos()
                coords.append(coord)
                pygame.draw.circle(screen, (255, 145, 175), coord, 1)

            elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_r]:
                coords = []
                screen.fill(0)
                pygame.display.flip()

            elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_RETURN]:
                f =  open('input/coords', 'w')
                json.dump(coords, f)
                print(f"Save {len(coords)} coords successfully.")
                f.close()
                flag = False

        pygame.display.flip()

    pygame.quit()
