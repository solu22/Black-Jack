import random

user_cards = []
computer_cards = []
is_game_over = False

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def addCards():
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        print("You went over.You lose")
    if user_score == computer_score:
        print("Draw")
    elif computer_score == 0:
        print("Lost, opponent has a black jack")
    elif user_score == 0:
        print("Win with a blackjack")
    elif user_score > 21:
        print("Lost, score is higher than 21")
    elif computer_score > 21:
        print("You win, Opponent went over, score is higher than 21")
    elif user_score > computer_score:
        print("You win")
    else:
        print("You lose")

def gameStatus(is_game_over):
    while not is_game_over:
        user_score =  calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" usercard: {user_cards} : score: {user_score}")
        print(f" com first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_continue_game = input(
                "Type 'yes' to draw another card or 'no' to end the game: ")
            if user_continue_game == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f" You final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {
          computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)

def game_continue():
    while input("Do you want to play a game again with fresh start. Type y to play and n to not continue: ") == 'y':
        play_game()    

def play_game():
    addCards()
    gameStatus(is_game_over)
    
game_continue()

    

 

    