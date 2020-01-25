import pygame
from button import Button
from colors import *
from font import *
from network import Network

pygame.font.init()

WIDTH = 700
HEIGHT = 500

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")


def half_width(text):
    return WIDTH / 2 - text.get_width() / 2


def redraw_window(window, game, p):
    window.fill(GREY_DR)

    if not (game.connected()):
        font = create_font(25, bold=True)
        text = font.render("Waiting for Player...", 1, YELLOW_DR, True)
        window.blit(text, (half_width(text), HEIGHT / 2 - text.get_height() / 2))
    else:
        font = create_font(20)
        text = yellow_font(font, "Your Move: ")
        window.blit(text, (20, 50))

        text = yellow_font(font, "Opponent's Move: ")
        window.blit(text, (330, 50))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)

        if game.both_went():
            text1 = white_font(font, move1)
            text2 = white_font(font, move2)
        else:
            if game.p1Went and p == 0:
                text1 = white_font(font, move1)
            elif game.p1Went:
                text1 = white_font(font, "Locked In")
            else:
                text1 = white_font(font, "Waiting...")
            if game.p2Went and p == 1:
                text2 = white_font(font, move2)
            elif game.p2Went:
                text2 = white_font(font, "Locked In")
            else:
                text2 = white_font(font, "Waiting...")

        if p == 1:
            window.blit(text2, (100, 50))
            window.blit(text1, (450, 50))
        else:
            window.blit(text1, (100, 50))
            window.blit(text2, (450, 50))

        for btn in buttons:
            btn.draw(window)

    pygame.display.update()


buttons = [
    Button("Rock", 50, 300, GREY),
    Button("Paper", 250, 300, PURPLE_DR),
    Button("Scissor", 450, 300, BLUE_DR),
    Button("Lizard", 350, 200, ORANGE_DR),
    Button("Spock", 150, 200, GREEN_DR),
]


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.get_p())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.both_went():
            redraw_window(window, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = create_font(25, bold=True)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = green_font(font, "You Won!")
            elif game.winner() == -1:
                text = green_font(font, "Tie Game!")
            else:
                text = green_font(font, "You Lost...")

            window.blit(text, (half_width(text), HEIGHT - 40))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in buttons:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(btn.text)

        redraw_window(window, game, player)


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        window.fill(GREY_DR)
        font = create_font(25, bold=True)
        text = yellow_font(font, "Click to Play!")
        window.blit(text, (half_width(text), HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


while True:
    menu_screen()
