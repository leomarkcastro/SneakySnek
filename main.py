from variable import *
from game_over import *

pygame.init()

game_folder = os.path.dirname(__file__)
#para makuha yung mga graphics na nasa ibang folder
img_folder = os.path.join(game_folder, 'img')

#para ma play yung music----
music = pygame.mixer.music.load('ost.mp3')
#--- eto para naka loop yung music 
pygame.mixer.music.play(-1)

snake = pygame.image.load(os.path.join(img_folder, "snake.png")).convert_alpha()
#nasa isang picture yung head/body/tail / corners ng snake, kinukuha bawat part gamit yung subsurface + x and y component, check nyo yung image sa img folder
snk_hed = snake.subsurface(pygame.Rect((16,0),(16,16)))
snk_hed = pygame.transform.scale(snk_hed, (blocksize,blocksize))

snk_tel = snake.subsurface(pygame.Rect((16,16),(16,16)))
snk_tel = pygame.transform.scale(snk_tel, (blocksize,blocksize))

snk_cor = snake.subsurface(pygame.Rect((32,32),(16,16)))
snk_cor = pygame.transform.scale(snk_cor, (blocksize,blocksize))

snk_bod = snake.subsurface(pygame.Rect((16,48),(16,16)))
snk_bod = pygame.transform.scale(snk_bod, (blocksize,blocksize))

grass = pygame.image.load(os.path.join(img_folder, "grass.jpg")).convert()
grass = pygame.transform.scale(grass, (650,500))

startup = pygame.image.load(os.path.join(img_folder, "startup.jpg")).convert()
startup = pygame.transform.scale(startup, (800,600))

food = pygame.image.load(os.path.join(img_folder, "food.png")).convert_alpha()
food = pygame.transform.scale(food, (blocksize,blocksize))

#rotation of head ng snake
snake_head = {
    up : pygame.transform.rotate(snk_hed, 90),
    left : pygame.transform.rotate(snk_hed, 180),
    down : pygame.transform.rotate(snk_hed, 270),
    right : pygame.transform.rotate(snk_hed, 0),
    }

snake_body = {
    up : pygame.transform.rotate(snk_bod, 90),
    left : pygame.transform.rotate(snk_bod, 180),
    down : pygame.transform.rotate(snk_bod, 270),
    right : pygame.transform.rotate(snk_bod, 0),
    
    downleft : pygame.transform.rotate(snk_cor, 0),
    downright : pygame.transform.rotate(snk_cor, 90),
    upright : pygame.transform.rotate(snk_cor, 180),
    upleft : pygame.transform.rotate(snk_cor, 270),
    }

snake_tail = {
    up : pygame.transform.rotate(snk_tel, 90),
    left : pygame.transform.rotate(snk_tel, 180),
    down : pygame.transform.rotate(snk_tel, 270),
    right : pygame.transform.rotate(snk_tel, 0),
    }



class mainGame():
    def __init__(self):
        
        self.gameDisplay = pygame.display.set_mode((screenWidth,screenHeight),flags)
        pygame.display.set_caption('Sneaky Snek')
        self.run = 'A'
        self.clock = pygame.time.Clock()

        self.game_over = Gameover()
        self.SceneLooper()

    def SceneLooper(self):
        while len(self.run) != 0:

            if self.run == 'A':
                self.SceneA()
            elif self.run == 'B':
                self.SceneB()
            elif self.run == 'C':
                self.game_over.SceneGameOver()
                if self.game_over.choice == 'A':
                    self.run = 'A'
                elif self.game_over.choice == 'B':
                    self.run = 'B'
    
    def SceneA(self):
        def start():
            self.delay = 50
            self.snake_tick = pygame.time.get_ticks()
            self.snake_head_x = -1
            self.snake_head_y = 0
            self.snake_dir = left
            self.snake_length = 4
            
            self.food = (random.randint(1,25),random.randint(1,19))
            
            self.snake = [
                [left,(11,8),left],
                [left,(12,8),left],
                [left,(13,8),left],
                [left,(14,8),left]
                ]
            self.do_it = False
            
            loop()
        
        def loop_control():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = ''
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_SPACE:
                        self.run = 'B'
                        beep_array['beep02'].play()
                    elif event.key == pygame.K_ESCAPE:
                        self.run = ''
        
        def loop_logic():
            pass
        
        def loop_display():
            # main menu display,tapos x and y component lang ulit para malaman kung saan mag iistart yung picture.
            self.gameDisplay.blit(startup, (0,0))

                    
            pygame.display.flip()
        
        def loop():
            while self.run == 'A':
                loop_control()
                loop_logic()
                loop_display()
                
                self.clock.tick(fps)
        
        start()
    
    def SceneB(self):
        def start():
            self.delay = 85
            self.snake_tick = pygame.time.get_ticks()
            self.snake_head_x = -1
            self.snake_head_y = 0
            self.snake_dir = left
            self.snake_length = 2
            self.score = 0
            
            self.food = (random.randint(1,25),random.randint(1,19))
            
            self.snake = [
                [left,(11,8),left],
                [left,(12,8),left],
                [left,(13,8),left],
                [left,(14,8),left]
                ]
            self.do_it = False
            
            loop()
        
        def loop_control():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = 'C'
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.snake_head_y == 0:
                        self.snake_head_x = 0
                        self.snake_head_y = -1
                        self.snake_dir = up
                        self.do_it = True
                        
                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.snake_head_y == 0:
                        self.snake_head_x = 0
                        self.snake_head_y = 1
                        self.snake_dir = down
                        self.do_it = True
                    if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.snake_head_x == 0:
                        self.snake_head_y = 0
                        self.snake_head_x = -1
                        self.snake_dir = left
                        self.do_it = True
                    if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.snake_head_x == 0:
                        self.snake_head_y = 0
                        self.snake_head_x = 1
                        self.snake_dir = right
                        self.do_it = True
                    if event.key == pygame.K_SPACE:
                        self.do_it = True
                        self.snake_length += 1
        
        def loop_logic():
            if self.snake_tick + self.delay < pygame.time.get_ticks() or self.do_it:
                snake_dir = snake_spr = self.snake_dir
                snake_headx = self.snake[0][1][0] + self.snake_head_x
                snake_heady = self.snake[0][1][1] + self.snake_head_y
                
                if self.score > 0:
                    self.score -= 0.1
                
                ol_snake_dir = ol_snake_spr = self.snake_dir
                
                if self.snake[0][0] != snake_dir:
                    if (self.snake[0][0] == left and snake_dir == down):
                        ol_snake_spr = downright
                        
                    elif (self.snake[0][0] == up and snake_dir == right):
                        ol_snake_spr = downright
                        
                    
                    elif (self.snake[0][0] == right and snake_dir == down):
                        ol_snake_spr = downleft
                        
                    elif (self.snake[0][0] == up and snake_dir == left):
                        ol_snake_spr = downleft
                        
                        
                    elif (self.snake[0][0] == left and snake_dir == up):
                        ol_snake_spr = upright
                        
                    elif (self.snake[0][0] == down and snake_dir == right):
                        ol_snake_spr = upright
                        
                        
                    elif (self.snake[0][0] == right and snake_dir == up):
                        ol_snake_spr = upleft
                        
                    elif (self.snake[0][0] == down and snake_dir == left):
                        ol_snake_spr = upleft
                        
                    
                    
                        
                self.snake[0] = [ol_snake_dir,self.snake[0][1],ol_snake_spr]
                self.snake.insert(0, (snake_dir,(snake_headx,snake_heady),snake_spr))
                
                if (snake_headx,snake_heady) == self.food:
                    self.snake_length += 1
                    self.score += 25
                    beep_array['beep03'].play()
                    self.food = (random.randint(1,25),random.randint(1,19))
                
                for i in range(1,len(self.snake)-1):
                    if (snake_headx,snake_heady) in self.snake[i]:
                        self.run = 'C'
                        beep_array['beep04'].play()
                
                if not(0 < snake_headx < 26) or not(0 < snake_heady < 20):
                    self.run = 'C'
                    beep_array['beep04'].play()
                
                while len(self.snake) > self.snake_length:
                    self.snake.pop()
                
                self.snake_tick = pygame.time.get_ticks()
                self.do_it = False
        
        def loop_display():
            self.gameDisplay.blit(startup, (0,0))
            # eto yung arena ng snake
            self.gameDisplay.blit(grass,(75,50,650,500))
            
            for i in range(len(self.snake)):
                if i == 0:
                    self.gameDisplay.blit(snake_head[self.snake[i][0]],(75+blocksize*self.snake[i][1][0], 50+blocksize*self.snake[i][1][1],blocksize,blocksize))
                elif i == len(self.snake)-1:
                    self.gameDisplay.blit(snake_tail[self.snake[i][0]],(75+blocksize*self.snake[i][1][0], 50+blocksize*self.snake[i][1][1],blocksize,blocksize))
                else:
                    self.gameDisplay.blit(snake_body[self.snake[i][2]],(75+blocksize*self.snake[i][1][0], 50+blocksize*self.snake[i][1][1],blocksize,blocksize))
                    
            self.gameDisplay.blit(food, (75+blocksize*self.food[0], 50+blocksize*self.food[1],blocksize,blocksize))
            
            text,textRect = textdisplay("Sneaky Snek",font_color[6],font_typo[0])
            textRect.center = (800//2,600//2)
            textRect.top = 0
            self.gameDisplay.blit(text, textRect)
            
            text,textRect = textdisplay("Score:{}".format(int(self.score)),font_color[6],font_typo[1])
            textRect.center = (800//2,600//2)
            textRect.top = 555
            self.gameDisplay.blit(text, textRect)
                    
            pygame.display.flip()
        
        def loop():
            while self.run == 'B':
                loop_control()
                loop_logic()
                loop_display()
                
                self.clock.tick(fps)
        
        start()


mainGame()

pygame.quit()
            
