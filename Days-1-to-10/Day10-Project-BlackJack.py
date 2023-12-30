import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
computer_hand = []
user_score = 0
final_uscore = 0
final_cpuscore = 0
computer_score = 0


def first_deal():
    global user_score
    global computer_score
    global user_hand
    global computer_hand

    user_hand = []
    computer_hand = []
    user_score = 0
    computer_score = 0

    user_deal = random.choices(cards, k=2)
    user_hand.extend(user_deal)

    user_score = sum(user_hand)
    print(f"Your cards: {user_hand}, current score: {user_score} ")

    computer_deal = random.choices(cards, k=2)
    computer_hand.extend(computer_deal)
    computer_string = computer_hand[0]
    computer_score = sum(computer_hand)
    print(f"Computer's first card {computer_string}")


def user_deal():
    global final_uscore
    global user_score
    global computer_string

    final_uscore = 0
    computer_string = computer_hand[0]

    more_card = True
    while more_card:
        if user_score < 21:
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                user_deal = random.choices(cards, k=1)
                user_hand.extend(user_deal)
                user_score = sum(user_hand)
                print(f"Your cards: {user_hand}, current score: {user_score} ")
            else:
                more_card = False
        else:
            print(f"Computer's first card {computer_string}")
            more_card = False
    final_uscore = sum(user_hand)
    print(f"Your final cards: {user_hand}, your final score: {final_uscore} ")


def cpu_deal():
    global final_cpuscore
    final_cpuscore = 0

    losing = True
    while losing:
        if computer_score < 13:
            computer_deal = random.choices(cards, k=1)
            computer_hand.extend(computer_deal)
            break
        elif computer_score < final_uscore:
            computer_deal = random.choices(cards, k=1)
            computer_hand.extend(computer_deal)
            break
        elif computer_score < 21:
            computer_deal = random.choices(cards, k=1)
            computer_hand.extend(computer_deal)
            break
        else:
            losing = False
    final_cpuscore = sum(computer_hand)
    print(
        f"Computer's final hand {computer_hand}, computer's final score: {final_cpuscore}"
    )


def check_blackjack():
    blackjack = [10, 11]
    check_user = all(item in blackjack for item in user_hand)
    check_cpu = all(item in blackjack for item in computer_hand)

    if check_user is True and check_cpu is False:
        print("Blackjack! You Wins")
        play_again()
    elif check_cpu is True:
        print("Computer wins! They have Blackjack")
        play_again()
    else:
        return 0


def compare_hands():
    if final_uscore > 21 and final_cpuscore < 21:
        print("You went over. You lose")
    elif final_uscore < final_cpuscore and final_cpuscore < 21:
        print("You lose")
    elif final_uscore < final_cpuscore and final_cpuscore > 21:
        print("Opponent went over. You win")
    elif final_uscore > final_cpuscore:
        print("You win")
    play_again()


def print_logo():
    from art import logo
    print(logo)


def start_play():
    wanna_play = input(
        "Do you want to play a game of Blackjack?: Type 'y' or 'n': ")
    if wanna_play == "y":
        playblackjack()
    else:
        return 0


def play_again():
    more_play = input(
        "Do you want to play a game of Blackjack?: Type 'y' or 'n': ")
    if more_play == "y":
        clear()
        print_logo()
        playblackjack()


def playblackjack():
    first_deal()
    check_blackjack()
    Continue_playing = True
    while Continue_playing:
        user_deal()
        cpu_deal()
        compare_hands()
        Continue_playing = False


print_logo()
start_play()
