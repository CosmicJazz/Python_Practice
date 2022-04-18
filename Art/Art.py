import pygame.gfxdraw

# make sure pygame gets set up
pygame.init()


#set width and height of our screen we'll make next
screenWidth = 1280
screenHeight = 720

# create a screen to draw to with screenWidth and screenHeight
screen = pygame.display.set_mode((screenWidth, screenHeight))

#white is red, green, and blue light in equal amounts at maximum brightness (255)
white = (255,255,255)
black = (0,0,0)

# let's make something so we know when to stop
running = True

# let's run while true
while running:
    # fill the screen with black
    screen.fill(black)
    # our for loop, for the width of the screen
    for i in range(0, screenWidth):
        # draw a single white pixel in the middle of the screen
        pygame.gfxdraw.pixel(screen, i, int(i*(screenHeight/screenWidth)), white)
        pygame.gfxdraw.pixel(screen, screenWidth-i, int(i*screenHeight/screenWidth), white)
        pygame.gfxdraw.pixel(screen, int(screenWidth*(1/3)), i, white)
        pygame.gfxdraw.pixel(screen, int(screenWidth * (2 / 3)), i, white)
        pygame.gfxdraw.pixel(screen, i, int(screenHeight*(1/3)), white)
        pygame.gfxdraw.pixel(screen, i, int(screenHeight*(2/3)), white)


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.gfxdraw.pixel(screen, pos[0], pos[1], white)
        # if you try to quit, lets leave this loop
        if event.type == pygame.QUIT:
            running = False #finish the loop

    # this is how we update the screen we've been drawing on.
    pygame.display.flip()