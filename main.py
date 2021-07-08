import pygame
from english_words import english_words_set

# Initializing PyGame
pygame.init()

# Creating game screen
width = 1000
height = 800
screen = pygame.display.set_mode((width, height))

# Setting caption
pygame.display.set_caption("Hangman")


# Asking player1 to enter a word
player1_answered = False
player1_ask_font = pygame.font.Font('freesansbold.ttf', 25)
player1_answer = ""

def player1(x, y):
    player1_ask_text = player1_ask_font.render(
        "Player 1, enter a word (max 8 letters) (lowercase): " + str(player1_answer), True,
        (0, 0, 0))
    screen.blit(player1_ask_text, (x, y))


# Validating the word entered by player1
def check_word(word):
    return (word in english_words_set)


# Display if invalid word
invalid_font = pygame.font.Font('freesansbold.ttf', 22)

def invalid_display(word, x, y):
    invalid_text = invalid_font.render(
        "'" + str(word) + "'" + " either isn't a word or has uppercase letters. TRY AGAIN!", True,
        (255, 0, 0))
    screen.blit(invalid_text, (x, y))
    pygame.display.update()


# Display if valid word
valid_font = pygame.font.Font('freesansbold.ttf', 22)

def valid_display(x, y):
    valid_text = valid_font.render("ACCEPTED!", True, (0, 255, 0))
    screen.blit(valid_text, (x, y))
    pygame.display.update()


# Drawing functions for creating the man being hung
def draw_base():
    pygame.draw.line(screen, (0, 0, 0), (700, 30), (975, 30), 4)

def draw1():
    pygame.draw.line(screen, (255, 0, 0), (837.5, 30), (837.5, 80), 4)

def draw2():
    pygame.draw.circle(screen, (255, 0, 0), (837.5, 110), 30, 4)

def draw3():
    pygame.draw.line(screen, (255, 0, 0), (837.5, 140), (837.5, 260), 4)

def draw4():
    pygame.draw.line(screen, (255, 0, 0), (837.5, 180), (775, 240), 4)

def draw5():
    pygame.draw.line(screen, (255, 0, 0), (837.5, 180), (900, 240), 4)

def draw6():
    pygame.draw.line(screen, (255, 0, 0), (837.5, 260), (740, 360), 4)

def draw7():
    pygame.draw.line(screen, (255, 0, 0), (837.5, 260), (935, 360), 4)
    pygame.display.update()


# Creating game outline for player2
word_status = ""
word_guessed = ""
word_status_font = pygame.font.Font('freesansbold.ttf', 30)
letters_done_font = pygame.font.Font('freesansbold.ttf', 25)
player2_prompt_font = pygame.font.Font('freesansbold.ttf', 25)
player2_answer = ""
correct_letters_list = []
wrong_letters_list = []
letters_font = pygame.font.Font('freesansbold.ttf', 22)

def player2(word_statusX, word_statusY, player2_promptX, player2_promptY):
    global word_status
    global correct_letters_list
    global wrong_letters_list
    global word_guessed

    # Updating the display of the word guessed so far by the user
    word_status = ""
    for letter in player1_answer:
        if letter in correct_letters_list:
            word_status += (letter + " ")
        else:
            word_status += "_ "

    word_guessed = ""
    for i in range(0, len(word_status), 2):
        word_guessed += word_status[i]

    word_status_text = word_status_font.render(word_status, True, (0, 0, 0))
    screen.blit(word_status_text, (word_statusX, word_statusY))

    player2_prompt_text = player2_prompt_font.render("Player 2, enter a letter: " + str(player2_answer), True, (0, 0, 0))
    screen.blit(player2_prompt_text, (player2_promptX, player2_promptY))

    # Drawing the hanging man based on number of wrong guesses
    draw_base()
    if len(wrong_letters_list) >= 1:
        draw1()
    if len(wrong_letters_list) >= 2:
        draw2()
    if len(wrong_letters_list) >= 3:
        draw3()
    if len(wrong_letters_list) >= 4:
        draw4()
    if len(wrong_letters_list) >= 5:
        draw5()
    if len(wrong_letters_list) >= 6:
        draw6()
    if len(wrong_letters_list) == 7:
        draw7()

    # Displaying the correct and wrong letters guessed so far; separating sections by a line
    pygame.draw.line(screen, (0, 0, 0), (width/2, 400), (width/2, 770))

    correct_letters_heading_text = letters_done_font.render("Accepted letters:", True, (0, 255, 0))
    screen.blit(correct_letters_heading_text, (50, 425))
    wrong_letters_heading_text = letters_done_font.render("Wrong letters:", True, (255, 0, 0))
    screen.blit(wrong_letters_heading_text, (550, 425))

    correct_letters_list = list(set(correct_letters_list))
    correct_letters = ""
    for corrlet in correct_letters_list:
        correct_letters += (str(corrlet) + " ")
    correct_letters_text = letters_font.render(correct_letters, True, (0, 200, 0))
    screen.blit(correct_letters_text, (50, 500))

    wrong_letters_list = list(set(wrong_letters_list))
    wrong_letters = ""
    for wronglet in wrong_letters_list:
        wrong_letters += (str(wronglet) + " ")
    wrong_letters_text = letters_font.render(wrong_letters, True, (200, 0, 0))
    screen.blit(wrong_letters_text, (550, 500))

    wrong_remaining(50, 260)


# Number of wrong guesses remaining
wrong_remaining_font = pygame.font.Font('freesansbold.ttf', 20)
def wrong_remaining(x, y):
    remaining = 7 - len(wrong_letters_list)
    wrong_remaining_text = wrong_remaining_font.render("You have " + str(remaining) + " wrong guesses left",
                                                       True, (0, 100, 100))
    screen.blit(wrong_remaining_text, (x, y))


# player2 Wins
win_font = pygame.font.Font('freesansbold.ttf', 25)
def player2_wins(x, y):
    win_text = win_font.render("Congratulations, Player 2. YOU WIN!", True, (0, 180, 0))
    screen.blit(win_text, (x, y))
    pygame.display.update()


# player2 Loses
lose_font = pygame.font.Font('freesansbold.ttf', 25)
def player2_loses(x, y):
    lose_text = lose_font.render("Player 2, YOU LOSE! CONGRATULATIONS Player 1!", True, (180, 0, 0))
    screen.blit(lose_text, (x, y))
    pygame.display.update()


# Creating the game loop:
running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if not player1_answered:  # if player 1 is still entering a word
                if event.key == pygame.K_RETURN:
                    # Validate the word
                    valid_word = check_word(player1_answer)
                    if valid_word:
                        player1_answered = True
                        # Display that it has been accepted for a few seconds
                        for i in range(200):
                            valid_display((width/2) - 50, height/2)
                    else:
                        # Estimating that the average width of a character of size 22 is 10px
                        invalid_x_shift = len("'" + str(
                            player1_answer) + "'" + " either isn't a word or has uppercase letters. TRY AGAIN!") * 10 / 2
                        print(invalid_x_shift)
                        # Display that it is an invalid word for a few seconds
                        for i in range(200):
                            invalid_display(player1_answer, (width / 2) - invalid_x_shift, height / 2)
                        player1_answer = ""

                elif event.key == pygame.K_BACKSPACE and len(player1_answer) > 0:
                    # No backspace unless something already entered (if nothing entered, [0:-1] will give error)
                    # Taking substring from 1st character to second last one
                    player1_answer = player1_answer[0:-1]  # (0-> inclusive, -1-> exclusive)

                elif event.key == pygame.K_SPACE:
                    pass

                elif len(player1_answer) <= 8:
                    player1_answer += event.unicode

            else:  # if player 1 has already entered a word (i.e. player 2 is playing now)
                if event.key == pygame.K_RETURN:
                    if player2_answer in player1_answer:
                        correct_letters_list.append(player2_answer)
                    else:
                        wrong_letters_list.append(player2_answer)
                    player2_answer = ""
                elif event.key == pygame.K_BACKSPACE and len(player2_answer) == 1:
                    player2_answer = ""
                elif event.key == pygame.K_SPACE:
                    pass
                elif len(player2_answer) == 0:
                    player2_answer += event.unicode

    # Prompting player1 to enter a word
    if not player1_answered:
        # Estimating that the average width of a character of size 25 is 15px
        player1_x_shift = (len("Player 1, enter a word (max 8 letters): " + str(player1_answer)) * 15) / 2
        player1((width / 2) - player1_x_shift, (height / 2))

    elif player1_answer == word_guessed:
        # Estimating that the average width of a character of size 25 is 15px
        win_shift = len("Congratulations, Player 2. YOU WIN!") * 15 / 2
        for i in range(200):
            player2_wins((width / 2) - win_shift, height / 2)
        pygame.quit()

    elif len(wrong_letters_list) == 7:
        for i in range(100):
            pass
        # Estimating that the average width of a character of size 25 is 15px
        lose_shift = len("Player 2, YOU LOSE! CONGRATULATIONS Player 1!") * 15 / 2
        for i in range(200):
            player2_loses((width/2) - lose_shift, height/2)
        pygame.quit()

    else:
        # Prompt player2 to guess a letter
        player2(50, 75, 50, 200)

    # Updating screen display
    pygame.display.update()