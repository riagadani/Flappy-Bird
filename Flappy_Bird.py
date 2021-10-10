import pygame
import time
import random

class Bird:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.g = .98
        self.velocity = 0
        self.t0 = time.time()
    def jump(self):
        self.velocity = -5
        self.t0 = time.time()
        self.move()
    def move(self):
        current_time = time.time()
        if self.velocity < 5:
            self.velocity += (current_time-self.t0)*self.g
        elif self.velocity > 5:
            self.velocty = 5
        if self.y + self.velocity < 600:
            self.y += self.velocity

class Pipe:
    def __init__(self):
      self.x = 800
      self.y = random.randint(100, 500)
    def move(self):
        self.x -= 1
        


class App():
    window = width, height = 800, 6000
    player = 0
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.image_surf = None
        self.bird = Bird()
        self.pipes = [Pipe()]

    def on_init(self):
        pygame.init()
        pygame.font.init()
        self.display_surf = pygame.display.set_mode(self.window)
        pygame.display.set_caption("Flappy Bird")
        self.image_surf = pygame.image.load("bird.png").convert()

        self.running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.on_cleanup()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.bird.jump()
        

    
    def on_loop(self):
        self.bird.move()
        for pipe in self.pipes:
            pipe.move()
        if self.pipes[0].x%200 == 0:
            self.pipes.append(Pipe())
        if self.pipes[0].x == 0:
            self.pipes.pop(0)
        print(len(self.pipes))
        

    def on_render(self):
        self.display_surf.fill((0,0,0))
        self.display_surf.blit(self.image_surf, (self.bird.x, self.bird.y))
        green = (0,255,0)
        for pipe in self.pipes:
            pygame.draw.rect(self.display_surf, green, (pipe.x, 0, 10, pipe.y))
            pygame.draw.rect(self.display_surf, green, (pipe.x, pipe.y + 200, 10, 600 - pipe.y + 200))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
    
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
        while self.running:
            pygame.event.pump()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        pygame.display.update()

        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()