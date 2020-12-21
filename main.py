import pygame, random

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
        

pygame.init()

SCREENWIDTH=1000
SCREENHEIGHT=1000


size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")
 
carryOn = True
clock=pygame.time.Clock()



while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False
 
  #      keys = pygame.key.get_pressed()
  #      if keys[pygame.K_LEFT]:
  #          playerCar.moveLeft(5)
  #      if keys[pygame.K_RIGHT]:
  #          playerCar.moveRight(5)
        
        #Game Logic
  #      all_sprites_list.update()
 
        #Drawing on Screen
        screen.fill(GREY)
        #Draw The Road
        pygame.draw.rect(screen, GREY, [40,0, 200,300])
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [140,0],[140,300],5)
        
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
  #      all_sprites_list.draw(screen)
 
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit() 
