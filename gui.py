import pygame, sys
import game
import time

 
#This is to set-up the main menu itself.
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Egg Roll')

#This is to load the icon on the desktop taskbar.
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

#Screen resolution of the game
screen = pygame.display.set_mode((960, 768),0,32)


#These are the images (LIGHT mode)
main_menu_light = pygame.image.load('images/main_menu_light.png')

levels_light = pygame.image.load('images/levels_light.png')
loading_1_light = pygame.image.load('images/loading_1_light.png')
loading_2_light = pygame.image.load('images/loading_2_light.png')
loading_3_light = pygame.image.load('images/loading_3_light.png')
loading_4_light = pygame.image.load('images/loading_4_light.png')
loading_5_light = pygame.image.load('images/loading_5_light.png')

settings_light = pygame.image.load('images/settings_light.png')
tutorials_light = pygame.image.load('images/tutorials_light.png')
leaderboard_light = pygame.image.load('images/leaderboard_light.png')
control_keys_light = pygame.image.load('images/control_keys_light.png')
credits_light = pygame.image.load('images/credits_light.png')

sure_light = pygame.image.load('images/sure_light.png')


###Dark Mode
main_menu_dark = pygame.image.load('images/main_menu_dark.png')

levels_dark = pygame.image.load('images/levels_dark.png')
loading_1_dark = pygame.image.load('images/loading_1_dark.png')
loading_2_dark = pygame.image.load('images/loading_2_dark.png')
loading_3_dark = pygame.image.load('images/loading_3_dark.png')
loading_4_dark = pygame.image.load('images/loading_4_dark.png')
loading_5_dark = pygame.image.load('images/loading_5_dark.png')

settings_dark = pygame.image.load('images/settings_dark.png')
tutorials_dark = pygame.image.load('images/tutorials_dark.png')
leaderboard_dark = pygame.image.load('images/leaderboard_dark.png')
control_keys_dark = pygame.image.load('images/control_keys_dark.png')
credits_dark = pygame.image.load('images/credits_dark.png')

sure_dark = pygame.image.load('images/sure_dark.png')


#Main Menu Buttons
transparent_play_button = pygame.Surface((285,90), pygame.SRCALPHA)
#transparent_play_button.fill((255,0,0,128))
transparent_settings_button = pygame.Surface((285,90), pygame.SRCALPHA)
#transparent_settings_button.fill((255,0,0,128))
transparent_exit_game_button = pygame.Surface((310,90), pygame.SRCALPHA)
#transparent_exit_game_button.fill((255,0,0,128))

#Levels Button
transparent_level1_button = pygame.Surface((305,60), pygame.SRCALPHA)
#transparent_level1_button.fill((255,0,0,128))
transparent_level2_button = pygame.Surface((305,60), pygame.SRCALPHA)
#transparent_level2_button.fill((255,0,0,128))
transparent_level3_button = pygame.Surface((305,60), pygame.SRCALPHA)
#transparent_level3_button.fill((255,0,0,128))
transparent_level4_button = pygame.Surface((305,60), pygame.SRCALPHA)
#transparent_level4_button.fill((255,0,0,128))
transparent_level5_button = pygame.Surface((305,60), pygame.SRCALPHA)
#transparent_level5_button.fill((255,0,0,128))
transparent_main_menu_levels_button = pygame.Surface((305,60), pygame.SRCALPHA)
#transparent_main_menu_button.fill((255,0,0,128))

#Settings Button
transparent_tutorial_button = pygame.Surface((305,60), pygame.SRCALPHA)
transparent_tutorial_button.fill((255,0,0,128))

transparent_leaderboard_button = pygame.Surface((305,60), pygame.SRCALPHA)
transparent_leaderboard_button.fill((0,127,127,128))

transparent_control_keys_button = pygame.Surface((305,60), pygame.SRCALPHA)
transparent_control_keys_button.fill((255,127,0,128))

transparent_dark_mode_button = pygame.Surface((305,60), pygame.SRCALPHA)
transparent_dark_mode_button.fill((255,255,0,128))

transparent_credits_button = pygame.Surface((305,60), pygame.SRCALPHA)
transparent_credits_button.fill((0,127,127,128))

transparent_main_menu_settings_button = pygame.Surface((305,60), pygame.SRCALPHA)
transparent_main_menu_settings_button.fill((0,0,255,128))


transparent_back_to_settings_button = pygame.Surface((305,60), pygame.SRCALPHA)
#transparent_back_to_settings_button.fill((255,0,0,128))


#Exit_Game Buttons
transparent_yes_button = pygame.Surface((260,80), pygame.SRCALPHA)
#transparent_yes_button.fill((255,0,0,128))
transparent_no_button = pygame.Surface((260,80), pygame.SRCALPHA)
#transparent_no_button.fill((255,0,0,128))


def main_menu(mode='light'):
    click = False
    while True:
        if mode == "light":
            screen.blit(main_menu_light, (0, 0))
        else:
            screen.blit(main_menu_dark, (0, 0))
 
        position_x, position_y = pygame.mouse.get_pos()
 
        play_button = pygame.Rect(600, 330, 285, 90)
        settings_button = pygame.Rect(583, 450, 285, 90)
        exit_game_button = pygame.Rect(590, 570, 310, 90)

        if play_button.collidepoint((position_x, position_y)):
            if click:
                levels(mode)

        if settings_button.collidepoint((position_x, position_y)):
            if click:
                settings(mode)
        if exit_game_button.collidepoint((position_x, position_y)):
            if click:
                exit_game(mode)

        screen.blit(transparent_play_button, (600, 330))
        screen.blit(transparent_settings_button, (583, 450))
        screen.blit(transparent_exit_game_button, (590, 570))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
 
        pygame.display.update()
        mainClock.tick(60)


def levels(mode="light", tutorials="no"):
    click = False
    running = True
    while running:
        if mode == "light" and tutorials == "no":
            screen.blit(levels_light,(0,0))
        elif mode == "light" and tutorials == "yes":
            screen.blit(tutorials_light, (0,0))
        elif mode != "light" and tutorials == "no":
            screen.blit(levels_dark,(0,0))
        elif mode != "light" and tutorials == "yes":
            screen.blit(tutorials_dark,(0,0))

        position_x, position_y = pygame.mouse.get_pos()
 
        level1_button = pygame.Rect(575, 248, 305, 60)
        level2_button = pygame.Rect(575, 325, 305, 60)
        level3_button = pygame.Rect(580, 400, 305, 60)
        level4_button = pygame.Rect(575, 475, 305, 60)
        level5_button = pygame.Rect(580, 550, 305, 60)
        main_menu_levels_button = pygame.Rect(580, 625, 305, 60)

        if level1_button.collidepoint((position_x, position_y)):
            if click:
                loading(1, mode, tutorials)
        if level2_button.collidepoint((position_x, position_y)):
            if click:
                loading(2, mode, tutorials)
        if level3_button.collidepoint((position_x, position_y)):
            if click:
                loading(3, mode, tutorials)
        if level4_button.collidepoint((position_x, position_y)):
            if click:
                loading(4, mode, tutorials)
        if level5_button.collidepoint((position_x, position_y)):
            if click:
                loading(5, mode, tutorials)
        if main_menu_levels_button.collidepoint((position_x, position_y)):
            if click:
                #print("heyhey")
                if tutorials == "yes":
                    settings(mode)
                else:
                    main_menu(mode)

        screen.blit(transparent_level1_button, (575, 248))
        screen.blit(transparent_level2_button, (575, 325))
        screen.blit(transparent_level3_button, (580, 400))
        screen.blit(transparent_level4_button, (575, 475))
        screen.blit(transparent_level5_button, (580, 550))
        screen.blit(transparent_main_menu_levels_button, (580, 625))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if tutorials == "yes":
                        settings(mode)
                    else:
                        main_menu(mode)
 
        pygame.display.update()
        mainClock.tick(60)


def loading(file, mode="light", tutorials="no"):
    running = True
    while running:
        if file == 1:
            if mode == "light":
                screen.blit(loading_1_light,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no":
                    game.start_gui_with_level("tutorial1.in")
                else: 
                    game.start_gui_with_level("level1.in")
            else:
                screen.blit(loading_1_dark,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no":
                    game.start_gui_with_level("tutorial1.in", mode)
                else: 
                    game.start_gui_with_level("level1.in", mode)
        elif file == 2:
            if mode == "light":
                screen.blit(loading_2_light,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no":
                    game.start_gui_with_level("tutorial2.in")
                else: 
                    game.start_gui_with_level("level2.in")
            else:
                screen.blit(loading_2_dark,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no":
                    game.start_gui_with_level("tutorial2.in", mode)
                else: 
                    game.start_gui_with_level("level2.in", mode)
        elif file == 3:
            if mode == "light":
                screen.blit(loading_3_light,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no":
                    game.start_gui_with_level("tutorial3.in")
                else: 
                    game.start_gui_with_level("level3.in")
            else:
                screen.blit(loading_3_dark,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no":
                    game.start_gui_with_level("tutorial3.in", mode)
                else: 
                    game.start_gui_with_level("level3.in", mode)

        elif file == 4:
            if mode == "light":
                screen.blit(loading_4_light,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no":
                    game.start_gui_with_level("tutorial4.in")
                else: 
                    game.start_gui_with_level("level4.in")
            else:
                screen.blit(loading_4_dark,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no" :
                    game.start_gui_with_level("tutorial4.in", mode)
                else: 
                    game.start_gui_with_level("level4.in", mode)

        elif file == 5:
            if mode == "light":
                screen.blit(loading_5_light,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no":
                    game.start_gui_with_level("tutorial5.in")
                else: 
                    game.start_gui_with_level("level5.in")
            else:
                screen.blit(loading_5_dark,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no":
                    game.start_gui_with_level("tutorial5.in", mode)
                else: 
                    game.start_gui_with_level("level5.in", mode)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if tutorials == "yes":
                        levels(mode,"yes")
                    else:
                        levels(mode)                                                          
 
        pygame.display.update()
        mainClock.tick(60)

 
def settings(mode="light"):
    click = False
    running = True
    while running:
        if mode == "light":
            screen.blit(settings_light,(0,0))
        else:
            screen.blit(settings_dark,(0,0))

        position_x, position_y = pygame.mouse.get_pos()
 
        tutorial_button = pygame.Rect(590, 210, 305, 60)
        leaderboard_button = pygame.Rect(590, 285, 305, 60)
        control_keys_button = pygame.Rect(590, 375, 305, 60)
        dark_or_day_mode_button = pygame.Rect(595, 450, 305, 60)
        credits_button = pygame.Rect(590, 535, 305, 60)
        main_menu_settings_button = pygame.Rect(590, 615, 305, 60)
     
        if tutorial_button.collidepoint((position_x, position_y)):
            if click:
                levels(mode, "yes")
        if leaderboard_button.collidepoint((position_x, position_y)):
            if click:
                leaderboard(mode)
        if control_keys_button.collidepoint((position_x, position_y)):
            if click:
                control_keys_or_credits(mode)
        if dark_or_day_mode_button.collidepoint((position_x, position_y)):
            if click:
                if mode == "light":
                    settings("dark")
                else:
                    settings("light")
        if credits_button.collidepoint((position_x, position_y)):
            if click:
                control_keys_or_credits(mode, "credits")
        if main_menu_settings_button.collidepoint((position_x, position_y)):
            if click:
                main_menu(mode)

        screen.blit(transparent_tutorial_button, (590, 210))
        screen.blit(transparent_leaderboard_button, (590, 285))
        screen.blit(transparent_control_keys_button, (590, 375))
        screen.blit(transparent_dark_mode_button, (595, 450))
        screen.blit(transparent_control_keys_button, (590, 535))
        screen.blit(transparent_main_menu_settings_button, (590, 615))
     
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1: 
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu(mode)
 
        pygame.display.update()
        mainClock.tick(60)


def leaderboard(mode="light"):
    click = False
    running = True
    active_level = None  # Keeps track of the currently selected level
    scores = None        # Stores the scores of the active level

    while running:
        if mode == "light":
            screen.blit(leaderboard_light, (0, 0))
        else:
            screen.blit(leaderboard_dark, (0, 0))

        position_x, position_y = pygame.mouse.get_pos()

        leaderboard_level1_button = pygame.Rect(575, 248, 305, 60)
        leaderboard_level2_button = pygame.Rect(575, 325, 305, 60)
        leaderboard_level3_button = pygame.Rect(580, 400, 305, 60)
        leaderboard_level4_button = pygame.Rect(575, 475, 305, 60)
        leaderboard_level5_button = pygame.Rect(580, 550, 305, 60)
        leaderboard_back_to_settings_button = pygame.Rect(580, 625, 305, 60)

        # Check for button clicks and update active level and scores
        if leaderboard_level1_button.collidepoint((position_x, position_y)) and click:
            active_level = 'level1.in'
        if leaderboard_level2_button.collidepoint((position_x, position_y)) and click:
            active_level = 'level2.in'
        if leaderboard_level3_button.collidepoint((position_x, position_y)) and click:
            active_level = 'level3.in'
        if leaderboard_level4_button.collidepoint((position_x, position_y)) and click:
            active_level = 'level4.in'
        if leaderboard_level5_button.collidepoint((position_x, position_y)) and click:
            active_level = 'level5.in'
        if leaderboard_back_to_settings_button.collidepoint((position_x, position_y)) and click:
            settings(mode)

        # Load and display scores for the active level
        if active_level:
            first_score, second_score, third_score = game.get_leaderboard_scores(active_level)
            display_scores(first_score, second_score, third_score)

        # Display transparent buttons
        screen.blit(transparent_tutorial_button, (575, 248))
        screen.blit(transparent_leaderboard_button, (575, 325))
        screen.blit(transparent_control_keys_button, (580, 400))
        screen.blit(transparent_dark_mode_button, (575, 475))
        screen.blit(transparent_control_keys_button, (580, 550))
        screen.blit(transparent_main_menu_settings_button, (580, 625))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1: 
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu(mode)

        pygame.display.update()
        mainClock.tick(60)


def display_scores(first_score, second_score, third_score):
    font = pygame.font.Font(None, 36)

    first_score_text = font.render(f"{first_score}", True, (121, 78, 7))
    second_score_text = font.render(f"{second_score}", True, (121, 78, 7))
    third_score_text = font.render(f"{third_score}", True, (121, 78, 7))

    screen.blit(first_score_text, (275,355))
    screen.blit(second_score_text, (275,395))
    screen.blit(third_score_text, (275,437))


def control_keys_or_credits(mode="light", use="control_keys"): 
    running = True
    click = False
    while running:
        if mode == "light" and use == "control_keys":
            screen.blit(control_keys_light,(0,0))
        elif mode != "light" and use == "control_keys":
            screen.blit(control_keys_dark, (0,0))
        elif mode == "light" and use != "control_keys":
            screen.blit(credits_light,(0,0))
        else:
            screen.blit(credits_dark,(0,0))

        position_x, position_y = pygame.mouse.get_pos()

        back_to_settings_button = pygame.Rect(580, 645, 305, 60)

        if back_to_settings_button.collidepoint((position_x, position_y)):
            if click:
                settings(mode)

        screen.blit(transparent_back_to_settings_button, (580, 645))
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    settings(mode)

        pygame.display.update()
        mainClock.tick(60)


def exit_game(mode = "light"):
    running = True
    click = False
    while running:
        if mode == "light":
            screen.blit(sure_light,(0,0))
        else:
            screen.blit(sure_dark,(0,0))

        position_x, position_y = pygame.mouse.get_pos()
 
        yes_button = pygame.Rect(200, 450, 260, 80)
        no_button = pygame.Rect(530, 450, 260, 80)

        if yes_button.collidepoint((position_x, position_y)):
            if click:
                pygame.quit()
                sys.exit()
        if no_button.collidepoint((position_x, position_y)):
            if click:
                main_menu(mode)

        screen.blit(transparent_yes_button, (200, 450))
        screen.blit(transparent_no_button, (530, 450))
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu(mode)
 
        pygame.display.update()
        mainClock.tick(60)

main_menu()
