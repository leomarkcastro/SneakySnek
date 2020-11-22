from variable import *


class Gameover:
    def __init__(self):
        self.img = pygame.image.load('img/game_over.png').convert_alpha()
        self.img_bounds = self.img.get_rect()
        self.img_bounds.center = (screenWidth/2, screenHeight/2)

    def SceneGameOver(self):
        self.isRun = True
        self.restart = False
        self.choice = ''
        while self.isRun:
            clock.tick(fps)
            self.loop_control()
            self.loop_display()
            self.loop_logic()

    def loop_control(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self.isRun = False
            if event == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.isRun = False
                if event.key == pygame.K_RETURN:
                    self.isRun = False
                    self.restart = True

    def loop_logic(self):
        self.isRun = self.wait_for_keypress()

    def loop_display(self):
        gameDisplay.blit(self.img, self.img_bounds)
        pygame.display.flip()

    def wait_for_keypress(self):
        while True:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.choice = 'A'
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.choice = 'A'
                        beep_array['beep02'].play()
                        return False
                    elif event.key == pygame.K_SPACE:
                        self.choice = 'B'
                        beep_array['beep02'].play()
                        return False
