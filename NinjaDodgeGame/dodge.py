import pygame
import random
import math

#Functions
def main_menu():
#Setup
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("images\The Final Battle.mp3")
    pygame.mixer.music.play()
    screen = pygame.display.set_mode((960, 540))
    running = True
    screen.fill("black")
    background = pygame.image.load("images\drew-some-grass-v0-2e5rtu0ss39c1.webp")

#Rectangles for Buttons
    playButton = pygame.Rect(((screen.get_width() - 400) // 2), 50, 400, 100)
    optionsButton = pygame.Rect(((screen.get_width() - 400) // 2), 200, 400, 100)
    quitButton = pygame.Rect(((screen.get_width() - 400) // 2), 350, 400, 100)

# Render the text
    font = pygame.font.Font(None, 48)
    surface_play = font.render("PLAY", True, (255, 255, 255))
    text_play = surface_play.get_rect()
    text_play.center = (playButton.x + playButton.width // 2, playButton.y + playButton.height // 2)
    surface_options = font.render("OPTIONS", True, (255, 255, 255))
    text_options = surface_options.get_rect()
    text_options.center = (optionsButton.x + optionsButton.width // 2, optionsButton.y + optionsButton.height // 2)
    surface_quit = font.render("QUIT", True, (255, 255, 255))
    text_quit = surface_quit.get_rect()
    text_quit.center = (quitButton.x + quitButton.width // 2, quitButton.y + quitButton.height // 2)
    mousePos = [0, 0]
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.x < mousePos[0] < playButton.x + playButton.width and playButton.y < mousePos[1] < playButton.y + playButton.height:
                    play()
                elif optionsButton.x < mousePos[0] < optionsButton.x + optionsButton.width and optionsButton.y < mousePos[1] < optionsButton.y + optionsButton.height:
                    print("Options")
                elif quitButton.x < mousePos[0] < quitButton.x + quitButton.width and quitButton.y < mousePos[1] < quitButton.y + quitButton.height:
                    running = False
        mousePos = pygame.mouse.get_pos()
    
        pygame.draw.rect(screen, (255, 0, 0), playButton)
        pygame.draw.rect(screen, (255, 0, 0), optionsButton)
        pygame.draw.rect(screen, (255, 0, 0), quitButton)
        screen.blit(surface_play, text_play)
        screen.blit(surface_options, text_options)
        screen.blit(surface_quit, text_quit)
        pygame.display.flip()
        # Render the text


def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
def play():
    pygame.init()
    screen = pygame.display.set_mode((960, 540))
    running = True
    screen.fill("black")
    ninjaIdle1 = pygame.image.load("images\Idle1.png")
    ninjaIdle2 = pygame.image.load("images\Idle2.png")
    ninjaRun1 = pygame.image.load("images\Run1.png")
    ninjaRun2 = pygame.image.load("images\Run2.png")
    ninjaRun3 = pygame.image.load("images\Run3.png")
    ninjaRun4 = pygame.image.load("images\Run4.png")
    ninjaIdle1F = pygame.transform.flip(ninjaIdle1, True, False)
    ninjaIdle2F = pygame.transform.flip(ninjaIdle2, True, False)
    ninjaRun1F = pygame.transform.flip(ninjaRun1, True, False)
    ninjaRun2F = pygame.transform.flip(ninjaRun2, True, False)
    ninjaRun3F = pygame.transform.flip(ninjaRun3, True, False)
    ninjaRun4F = pygame.transform.flip(ninjaRun4, True, False)
    background = pygame.image.load("images\drew-some-grass-v0-2e5rtu0ss39c1.webp")
    Gslime1 = pygame.image.load("images\Slime1.png").convert_alpha()
    Gslime1 = pygame.transform.scale(Gslime1, (30, 20))
    Gslime2 = pygame.image.load("images\Slime2.png").convert_alpha()
    Gslime2 = pygame.transform.scale(Gslime2, (30, 20))
    Rslime1 = pygame.image.load("images\RedSlime1.png").convert_alpha()
    Rslime1 = pygame.transform.scale(Rslime1, (30, 20))
    Rslime2 = pygame.image.load("images\RedSlime2.png").convert_alpha()
    Rslime2 = pygame.transform.scale(Rslime2, (30, 20))
    Bslime1 = pygame.image.load("images\BlueSlime1.png").convert_alpha()
    Bslime1 = pygame.transform.scale(Bslime1, (30, 20))
    Bslime2 = pygame.image.load("images\BlueSlime2.png").convert_alpha()
    Bslime2 = pygame.transform.scale(Bslime2, (30, 20))
    test = pygame.Rect(0, 0, 5, 5)
    blob_list = []
    current_ninja = ninjaIdle1
    current_slime = Bslime1
    ninja_state = 0
    speed = .06
    timer = 0
    timer2 = 0
    gameTimer = 0
    ninja_coordinates = [400, 400]
    pygame.mixer.init()
    pygame.mixer.music.load("images\Battle Grounds.mp3")
    pygame.mixer.music.play()


    #GameLoop
    while running:
    #Event For Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    #Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ninja_state = -1
            ninja_coordinates[0] -= speed
        if keys[pygame.K_RIGHT]:
            ninja_state = 1
            ninja_coordinates[0] += speed
        if keys[pygame.K_DOWN]:
            ninja_state = -1
            ninja_coordinates[1] += speed
        if keys[pygame.K_UP]:
            ninja_state = 1
            ninja_coordinates[1] -= speed
        if not any(keys):
            ninja_state = 0

    #Player Animation
        timer += 1
        if ninja_state == 0:
            if timer >= 400:
                timer = 0
                if current_ninja == ninjaIdle1:
                    current_ninja = ninjaIdle2
                elif current_ninja == ninjaIdle2:
                    current_ninja = ninjaIdle1
                else:
                    current_ninja = ninjaIdle1
        elif ninja_state == 1:
            if timer >= 200:
                timer = 0
                if current_ninja == ninjaIdle1 or current_ninja == ninjaIdle2:
                    current_ninja = ninjaRun1
                elif current_ninja == ninjaRun1:
                    current_ninja = ninjaRun2
                elif current_ninja == ninjaRun2:
                    current_ninja = ninjaRun3
                elif current_ninja == ninjaRun3:
                    current_ninja = ninjaRun4
                elif current_ninja == ninjaRun4:
                    current_ninja = ninjaRun1
        elif ninja_state == -1:
            if timer >= 200:
                timer = 0
                if current_ninja == ninjaIdle1 or current_ninja == ninjaIdle2:
                    current_ninja = ninjaRun1F
                elif current_ninja == ninjaRun1F:
                    current_ninja = ninjaRun2F
                elif current_ninja == ninjaRun2F:
                    current_ninja = ninjaRun3F
                elif current_ninja == ninjaRun3F:
                    current_ninja = ninjaRun4F
                elif current_ninja == ninjaRun4F:
                    current_ninja = ninjaRun1F

        screen.blit(background, (0, 0))

    #Slime Manager
    #[x-coordinate, y-coorindate, speed, angle]
        gameTimer += 1
        if len(blob_list) < 10 + (gameTimer // 3000):
            blob_list.append([-20, random.randint(30, 510), random.uniform(.02, .1), random.uniform(-.01, .01)])
        blobIndex = 0
        while blobIndex < len(blob_list):
            if blob_list[blobIndex][2] <= .03:
                screen.blit(Bslime1, (blob_list[blobIndex][0], blob_list[blobIndex][1]))
            elif blob_list[blobIndex][2] > .03 and blob_list[blobIndex][2] < .06:
                blob_list[blobIndex][1] += blob_list[blobIndex][3]
                screen.blit(Gslime1, (blob_list[blobIndex][0], blob_list[blobIndex][1]))
            elif blob_list[blobIndex][2] >= .06:
                blob_list[blobIndex][1] += blob_list[blobIndex][3]
                screen.blit(Rslime1, (blob_list[blobIndex][0], blob_list[blobIndex][1]))
            blob_list[blobIndex][0] += blob_list[blobIndex][2]
            if blob_list[blobIndex][0] > 970:
                blob_list.pop(blobIndex)
            if calculate_distance(blob_list[blobIndex][0], blob_list[blobIndex][1], ninja_coordinates[0] + 20, ninja_coordinates[1] + 20) < 19:
                running = False
            blobIndex += 1
    #Update Screen

        screen.blit(current_ninja, ninja_coordinates)
        # pygame.draw.rect(screen, (255, 0, 0), (ninja_coordinates[0] + 20, ninja_coordinates[1] + 20, test.width + 20, test.height + 20))
        pygame.display.flip()
    screen.fill("black")
    main_menu()

main_menu()


