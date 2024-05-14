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
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def collision_with_screen(self):
        if self.x <= -1:
            self.x = 0
            return True
        if self.y <= -1:
            self.y = 0
            return True
        if self.x + self.width > width_screen:
            self.x = width_screen - self.width
            return True
        if self.y + self.height > height_screen:
            self.y = height_screen - self.height
            return True
        else:
            return False

    def move_by_keyboard(self, step, direction):
        if not self.collision_with_screen():
            match direction:
                case 'left':
                    self.x -= step
                case 'right':
                    self.x += step
                case 'up':
                    self.y -= step
                case 'down':
                    self.y += step
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_by_joystick(self, step_x, step_y):
        if not self.collision_with_screen():
            self.x += step_x
            self.y += step_y
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)


def main():
    square = Solid(0, 0, 'test_sprite.png')
    alisa = Solid(width_screen - pygame.image.load('Alisa.png').get_width(),
                  height_screen - pygame.image.load('Alisa.png').get_height(), 'Alisa.png')
    step = 10
    joysticks = {}
    for joystick_index in range(pygame.joystick.get_count()):
        joysticks[pygame.joystick.Joystick(joystick_index).get_instance_id()] \
            = pygame.joystick.Joystick(joystick_index)
    screen = pygame.display.set_mode((width_screen, height_screen))
    pygame.display.set_caption('Some kind of game')
    clock = pygame.time.Clock()
    test = True
    while test:
        screen.fill(white)
        screen.blit(square.image, (square.x, square.y, square.width, square.height))
        screen.blit(alisa.image, (alisa.x, alisa.y, alisa.width, alisa.height))
        if not square.collision_with_screen() or not alisa.collision_with_screen:
            for joystick in joysticks.values():
                axis_x_square = float(joystick.get_axis(0))
                axis_y_square = float(joystick.get_axis(1))
                axis_x_alisa = float(joystick.get_axis(2))
                axis_y_alisa = float(joystick.get_axis(3))
                if abs(axis_x_square) >= 0.01 and abs(axis_y_square) >= 0.01:
                    square.move_by_joystick(axis_x_square, axis_y_square)
                if abs(axis_x_alisa) >= 0.01 and abs(axis_y_alisa) >= 0.01:
                    alisa.move_by_joystick(axis_x_alisa, axis_y_alisa)
                if joystick.get_button(5):
                    pygame.quit()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        alisa.move_by_keyboard(step, 'down')
                    if event.key == pygame.K_UP:
                        alisa.move_by_keyboard(step, 'up')
                    if event.key == pygame.K_LEFT:
                        alisa.move_by_keyboard(step, 'left')
                    if event.key == pygame.K_RIGHT:
                        alisa.move_by_keyboard(step, 'right')

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        alisa.move_by_keyboard(step, 'down')
                    if event.key == pygame.K_UP:
                        alisa.move_by_keyboard(step, 'up')
                    if event.key == pygame.K_LEFT:
                        alisa.move_by_keyboard(step, 'left')
                    if event.key == pygame.K_RIGHT:
                        alisa.move_by_keyboard(step, 'right')

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        square.move_by_keyboard(step, 'down')
                    if event.key == pygame.K_w:
                        square.move_by_keyboard(step, 'up')
                    if event.key == pygame.K_a:
                        square.move_by_keyboard(step, 'left')
                    if event.key == pygame.K_d:
                        square.move_by_keyboard(step, 'right')

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        square.move_by_keyboard(step, 'down')
                    if event.key == pygame.K_w:
                        square.move_by_keyboard(step, 'up')
                    if event.key == pygame.K_a:
                        square.move_by_keyboard(step, 'left')
                    if event.key == pygame.K_d:
                        square.move_by_keyboard(step, 'right')
                if event.type == pygame.JOYDEVICEADDED:
                    for joystick_index in range(pygame.joystick.get_count()):
                        joysticks[pygame.joystick.Joystick(joystick_index).get_instance_id()] \
                            = pygame.joystick.Joystick(joystick_index)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.QUIT:
                    test = False
        pygame.display.flip()
    clock.tick(60)


if __name__ == '__main__':
    main()
    pygame.quit()
