import pygame

pygame.init()

width_screen = 1920
height_screen = 1080

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


class Solid(object):
    def __init__(self, x, y, filename):
        self.filename = filename
        self.image = pygame.image.load(filename)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y

    def collision_detection(self, border_x, border_y):
        if self.x <= -1:
            self.x = 0
        if self.y <= -1:
            self.y = 0
        if self.x + self.width >= border_x:
            self.x = border_x - self.width
        if self.y + self.height >= border_y:
            self.y = border_y - self.height
        return [self.x, self.y]


def main():
    joysticks = {}
    square = Solid(0, 0, 'test_sprite.png')
    alisa = Solid(width_screen, height_screen, 'Alisa.png')
    alisa.x = alisa.x - alisa.width
    alisa.y = alisa.y - alisa.height
    for joystick_index in range(pygame.joystick.get_count()):
        joysticks[pygame.joystick.Joystick(joystick_index).get_instance_id()] = pygame.joystick.Joystick(joystick_index)
    screen = pygame.display.set_mode((width_screen, height_screen))
    pygame.display.set_caption('Some kind of game')
    clock = pygame.time.Clock()
    test = True
    while test:
        screen.fill(white)
        screen.blit(square.image, (square.x, square.y, square.width, square.height))
        screen.blit(alisa.image, (alisa.x, alisa.y, alisa.width, alisa.height))
        for joystick in joysticks.values():
            axis_x_square = float(joystick.get_axis(0))
            axis_y_square = float(joystick.get_axis(1))
            if abs(axis_x_square) >= 0.01 and abs(axis_y_square) >= 0.01:
                square.x, square.y = (square.collision_detection(width_screen, height_screen)[0] + axis_x_square,
                                      square.collision_detection(width_screen, height_screen)[1] + axis_y_square)

            axis_x_alisa = float(joystick.get_axis(2))
            axis_y_alisa = float(joystick.get_axis(3))
            if abs(axis_x_alisa) >= 0.01 and abs(axis_y_alisa) >= 0.01:
                alisa.x, alisa.y = (alisa.collision_detection(width_screen, height_screen)[0] + axis_x_alisa,
                                    alisa.collision_detection(width_screen, height_screen)[1] + axis_y_alisa)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                test = False
        pygame.display.flip()
    clock.tick(60)


if __name__ == '__main__':
    main()
    pygame.quit()
