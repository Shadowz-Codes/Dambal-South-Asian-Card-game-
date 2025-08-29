import pygame
import sys
import random
from collections import Counter

# Game settings
pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
font = pygame.font.Font('fonts/comic.ttf', 40)
pile_font = pygame.font.Font('fonts/comic.ttf', 22)
win_font = pygame.font.Font('fonts/comic.ttf', 55)
pygame.display.set_caption('Dambal')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps = 60
timer = pygame.time.Clock()



class Button():
    def __init__(self, image, x, y, text_input, color):
        self.image = image
        self.x = x
        self.y = y
        self.is_enabled = True
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_input = text_input
        self.text = font.render(self.text_input, True, color)
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def draw(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)


    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) and self.is_enabled:
            return True
        else:
            return False

class Card():
    def __init__(self, id, card_x, card_y, card_size, num):
        self.card_value = id
        self.is_selected = False
        self.player_card_num = f"{num}"
        self.img = f"Images/Playing Cards/{self.card_value}.png"
        self.card_img = pygame.image.load(self.img)
        self.card_img = pygame.transform.scale(self.card_img, (card_size))
        self.card_button = Button(self.card_img, card_x, card_y, None, 'black')


    def selectCard(self):
       pass

    def draw(self):
        screen.blit(self.card_img, self.card_button)

    def __repr__(self):
        return str(f"player_card{self.player_card_num}")
    
def deal_cards(hand, current_deck):
    card = random.randint(0, len(current_deck))
    hand.append(current_deck[card-1])
    current_deck.pop(card-1)
    return hand, current_deck


def showCard():
    pass

def confirmCard():
    pass
    
    
        

def gameRunning():

    initial_deal = True
    deck = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']
    royal_card_conversion = {
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10
    }
    random.shuffle(deck)
    player_hand = []
    inital_hand = []
    AI_hand = []
    pile_deck = []
    game_running = True
    player_card1_selected = False
    player_card2_selected = False
    player_card3_selected = False
    player_card4_selected = False
    player_card5_selected = False
    selected_card1_confirm = False
    selected_card2_confirm = False
    selected_card3_confirm = False
    selected_card4_confirm = False
    selected_card5_confirm = False
    remove_card1 = False
    remove_card2 = False
    remove_card3 = False
    remove_card4 = False
    remove_card5 = False
    player_card1_removed = False
    player_card2_removed = False
    player_card3_removed = False
    player_card4_removed = False
    player_card5_removed = False
    selected_cards = []
    card1_button_enabled = True
    player_new_card = False
    deal_new_card = False
    AI_turn = False
    player_turn = False
    AI_turn_done = False
    AI_function_called = False
    remove_AI_cards = False
    counter = 0
    draw_AI_pile = False
    draw_player_pile = False
    deal_AI_card = False
    get_pile_card = False
    pile_card1_selected = False
    pile_card2_selected = False
    pile_card3_selected = False
    pile_card4_selected = False
    pile_card5_selected = False
    pile_card_confirmed = False
    player_cardnum_val = []
    AI_cardnum_val = []
    get_player_cardnum = False
    get_AI_cardnum = False
    player_show_card = False
    player_wins = False
    AI_wins = False
    show_AI_card1 = None
    show_AI_card2 = None
    show_AI_card3 = None
    show_AI_card4 = None
    show_AI_card5 = None
    AI_show_card = False
    AI_card_dealed = False
    get_pile_cardnum = False
    pile_cardnum_val = []
    player_one_pair = False
    player_two_pair = False
    player_three_of_a_kind = False
    player_cardnum_value = []
    get_player_cardnumV2 = True
    player_total_countS = 0    
    player_total_countD = 0    
    player_total_countC = 0    
    player_total_countH = 0    
    count_suit_num = True

    def AI_card_sort(cardval):
        value = cardval[:-1]

        if value == 'A':
            value = 1
        elif value == 'J':
            value = 11
        elif value == 'Q':
            value = 12
        elif value == 'K':
            value = 13
        else:
            value = int(value)

        return value

    if initial_deal:
        for i in range(5):
            player_hand, deck = deal_cards(player_hand, deck)
            AI_hand, deck = deal_cards(AI_hand, deck)
            inital_hand.append(player_hand[i])
        print(player_hand, AI_hand, inital_hand)  
    initial_deal = False


    while game_running:

        game_mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        nc_button_surface = pygame.image.load("Images/Button images/GameButton.png")
        sc_button_surface = pygame.image.load("Images/Button images/GameButton.png")
        cc_button_surface = pygame.image.load("Images/Button images/GameButton.png")

        nc_button_surface = pygame.transform.scale(nc_button_surface, (450, 150))
        sc_button_surface = pygame.transform.scale(sc_button_surface, (450, 150))
        cc_button_surface = pygame.transform.scale(cc_button_surface, (450, 150))

        new_card_button = Button(nc_button_surface, 200, 70, 'NEW CARD', 'black')
        show_card_button = Button(sc_button_surface, 1300, 730, 'SHOW CARD', 'black')
        confirm_card_button = Button(cc_button_surface, 1300, 830, 'CONFIRM', 'black')
        confirm_card_button.is_enabled = False

        new_card_button.draw()
        show_card_button.draw()
        confirm_card_button.draw()

        new_card_button.is_enabled = False
        show_card_button.is_enabled = False

        inital_hand.sort(reverse=True, key=AI_card_sort)
        player_hand.sort(reverse=True, key=AI_card_sort)

        player_card1 = Card(inital_hand[0], 130, 770, (200, 300), "1")
        player_card2 = Card(inital_hand[1], 350, 770, (200, 300), "2")
        player_card3 = Card(inital_hand[2], 570, 770, (200, 300), "3")
        player_card4 = Card(inital_hand[3], 790, 770, (200, 300), "4")
        player_card5 = Card(inital_hand[4], 1010, 770, (200, 300), "5")

        player_cards = [player_card1, player_card2, player_card3, player_card4, player_card5]

        for cards in player_cards:
            cards.draw()

        AI_hand.sort(reverse=True, key=AI_card_sort)
        print(AI_hand)

        AI_card1 = Card(("card back red"), 1000, 200, (200, 300), "1")
        AI_card2 = Card(("card back red"), 1080, 203, (200, 300), "2")
        AI_card3 = Card(("card back red"), 1160, 206, (200, 300), "3")
        AI_card4 = Card(("card back red"), 1240, 209, (200, 300), "4")
        AI_card5 = Card(("card back red"), 1320, 212, (200, 300), "5")


        screen.blit(AI_card1.card_img, AI_card1.card_button)
        screen.blit(AI_card2.card_img, AI_card2.card_button)
        screen.blit(AI_card3.card_img, AI_card3.card_button)
        screen.blit(AI_card4.card_img, AI_card4.card_button)
        screen.blit(AI_card5.card_img, AI_card5.card_button)

        pile_card1 = Card(player_card1.card_value, 710, 350, (135, 190), "1")
        pile_card2 = Card(player_card2.card_value, 570, 350, (135, 190), "2")
        pile_card3 = Card(player_card3.card_value, 430, 350, (135, 190), "3")
        pile_card4 = Card(player_card4.card_value, 290, 350, (135, 190), "4")
        pile_card5 = Card(player_card5.card_value, 150, 350, (135, 190), "5")

        pile_card1.card_button.is_enabled = False
        pile_card2.card_button.is_enabled = False
        pile_card3.card_button.is_enabled = False
        pile_card4.card_button.is_enabled = False
        pile_card5.card_button.is_enabled = False


        card_text1 = font.render(f"SELECTED", True, 'white')
        card_text_rect1 = card_text1.get_rect(center=(130, 955))

        card_text2 = font.render(f"SELECTED", True, 'white')
        card_text_rect2 = card_text2.get_rect(center=(350, 955))

        card_text3 = font.render(f"SELECTED", True, 'white')
        card_text_rect3 = card_text3.get_rect(center=(570, 955))

        card_text4 = font.render(f"SELECTED", True, 'white')
        card_text_rect4 = card_text4.get_rect(center=(790, 955))

        card_text5 = font.render(f"SELECTED", True, 'white')
        card_text_rect5 = card_text5.get_rect(center=(1010, 955))


        pile_text1 = pile_font.render(f"SELECETED", True, 'white')
        pile_text_rect1 = pile_text1.get_rect(center=(710, 470))

        pile_text2 = pile_font.render(f"SELECETED", True, 'white')
        pile_text_rect2 = pile_text2.get_rect(center=(570, 470))

        pile_text3 = pile_font.render(f"SELECETED", True, 'white')
        pile_text_rect3 = pile_text3.get_rect(center=(430, 470))

        pile_text4 = pile_font.render(f"SELECETED", True, 'white')
        pile_text_rect4 = pile_text4.get_rect(center=(290, 470))

        pile_text5 = pile_font.render(f"SELECETED", True, 'white')
        pile_text_rect5 = pile_text5.get_rect(center=(150, 470))

        if len(deck) == 0:
            deck.extend('2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS')
            random.shuffle(deck)
            print(deck)



        if player_card1_selected:
            confirm_card_button.is_enabled = True
            screen.blit(card_text1, card_text_rect1)
        else:
            screen.fill('black', card_text_rect1) 

        if player_card2_selected:
            confirm_card_button.is_enabled = True
            screen.blit(card_text2, card_text_rect2)
        else:
            screen.fill('black', card_text_rect2) 

        if player_card3_selected:
            confirm_card_button.is_enabled = True
            screen.blit(card_text3, card_text_rect3) 
        else:
            screen.fill('black', card_text_rect3)

        if player_card4_selected:
            confirm_card_button.is_enabled = True
            screen.blit(card_text4, card_text_rect4) 
        else:
            screen.fill('black', card_text_rect4)

        if player_card5_selected:
            confirm_card_button.is_enabled = True
            screen.blit(card_text5, card_text_rect5)  
        else:
            screen.fill('black', card_text_rect5)  


        print(selected_cards)


        if confirm_card_button.is_enabled  == False:
            selected_card_confirm = False      
        
        if selected_card_confirm:

            if get_player_cardnumV2:
                player_cardnum_value.clear()
                for cardval in player_hand:
                    if cardval[0] in royal_card_conversion:
                        player_cardnum_value.append(royal_card_conversion[cardval[0]])
                    else:
                        player_cardnum_value.append(int(cardval[:-1]))
                    player_cardnum_value.sort(reverse = True)
            get_player_cardnumV2 = False 


            def PlayerCheckForConsecutive(n):      

                for cardnum in range(len(player_cardnum_value) - n + 1):
                    player_consecutive_list = player_cardnum_value[cardnum : cardnum + n]
                    print(player_consecutive_list)
                    print("happy")
                    if len(set(player_consecutive_list)) == n: 
                        if max(player_consecutive_list) - min(player_consecutive_list) == n - 1:
                            return True
                        else:
                            return False
                        

            if count_suit_num:            
                player_total_countS = 0
                player_total_countD = 0
                player_total_countC = 0
                player_total_countH = 0

                for cardval in player_hand:
                    player_total_countS += cardval.count("S")
                    player_total_countD += cardval.count("D")
                    player_total_countC += cardval.count("C")
                    player_total_countH += cardval.count("H")   
            count_suit_num = False
            
            match (player_card1_selected, player_card2_selected, player_card3_selected, player_card4_selected, player_card5_selected):

                case (True, False, False, False, False):
                    selected_card1_confirm = True
                    player_card2.card_button.is_enabled = False
                    player_card3.card_button.is_enabled = False
                    player_card4.card_button.is_enabled = False
                    player_card5.card_button.is_enabled = False
                    new_card_button.is_enabled = True             
                case (False, True, False, False, False):
                    selected_card2_confirm = True
                    player_card1.card_button.is_enabled = False
                    player_card3.card_button.is_enabled = False
                    player_card4.card_button.is_enabled = False
                    player_card5.card_button.is_enabled = False
                    new_card_button.is_enabled = True
                case (False, False, True, False, False):
                    selected_card3_confirm = True
                    player_card1.card_button.is_enabled = False
                    player_card2.card_button.is_enabled = False
                    player_card4.card_button.is_enabled = False
                    player_card5.card_button.is_enabled = False
                    new_card_button.is_enabled = True
                case (False, False, False, True, False):
                    selected_card4_confirm = True
                    player_card1.card_button.is_enabled = False
                    player_card2.card_button.is_enabled = False
                    player_card3.card_button.is_enabled = False
                    player_card5.card_button.is_enabled = False
                    new_card_button.is_enabled = True

                case (False, False, False, False, True):
                    selected_card5_confirm = True
                    player_card1.card_button.is_enabled = False
                    player_card2.card_button.is_enabled = False
                    player_card3.card_button.is_enabled = False
                    player_card4.card_button.is_enabled = False
                    new_card_button.is_enabled = True


                case (True, True, False, False, False):
                    if player_cardnum_value[0] - player_cardnum_value[1] == 0:
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        player_card3.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card2_selected = False
                        draw_player_pile = False
                case (True, False, True, False, False):
                    if player_cardnum_value[0] - player_cardnum_value[2] == 0:
                        selected_card1_confirm = True
                        selected_card3_confirm = True
                        player_card2.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card3_selected = False
                        draw_player_pile = False
                case (True, False, False, True, False):
                    if player_cardnum_value[0] - player_cardnum_value[3] == 0:
                        selected_card1_confirm = True
                        selected_card4_confirm = True
                        player_card2.card_button.is_enabled = False
                        player_card3.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card4_selected = False
                        draw_player_pile = False
                case (True, False, False, False, True):
                    if player_cardnum_value[0] - player_cardnum_value[4] == 0:
                        selected_card1_confirm = True
                        selected_card5_confirm = True
                        player_card2.card_button.is_enabled = False
                        player_card3.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card4_selected = False
                        draw_player_pile = False
                case (False, True, True, False, False):
                    if player_cardnum_value[1] - player_cardnum_value[2] == 0:
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card2_selected = False
                        player_card3_selected = False
                        draw_player_pile = False
                case (False, True, False, True, False):
                    if player_cardnum_value[1] - player_cardnum_value[3] == 0:
                        selected_card2_confirm = True
                        selected_card4_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card3.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card2_selected = False
                        player_card4_selected = False    
                        draw_player_pile = False                    
                case (False, True, False, False, True):
                    if player_cardnum_value[1] - player_cardnum_value[4] == 0:
                        selected_card2_confirm = True
                        selected_card5_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card3.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card2_selected = False
                        player_card5_selected = False  
                        draw_player_pile = False                         
                case (False, False, True, True, False):
                    if player_cardnum_value[2] - player_cardnum_value[3] == 0:
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card2.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card3_selected = False
                        player_card4_selected = False    
                        draw_player_pile = False                     
                case (False, False, True, False, True):
                    if player_cardnum_value[2] - player_cardnum_value[4] == 0:
                        selected_card3_confirm = True
                        selected_card5_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card2.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card3_selected = False
                        player_card5_selected = False 
                        draw_player_pile = False                        
                case (False, False, False, True, True):
                    if player_cardnum_value[3] - player_cardnum_value[4] == 0:
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card2.card_button.is_enabled = False
                        player_card3.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card4_selected = False
                        player_card5_selected = False        
                        draw_player_pile = False                  


                case (True, True, True, False, False):
                    if player_cardnum_value[0] - player_cardnum_value[1] == player_cardnum_value[1] - player_cardnum_value[2] and (player_total_countS >= 3 or player_total_countD >= 3 or player_total_countC >= 3 or player_total_countH >= 3):
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        player_card3.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[0] + player_cardnum_value[1]) - player_cardnum_value[2] == player_cardnum_value[0]:
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        player_card3.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card2_selected = False
                        player_card3_selected = False   
                        draw_player_pile = False                                                
                case (True, False, True, True, False):
                    if player_cardnum_value[0] - player_cardnum_value[2] == player_cardnum_value[2] - player_cardnum_value[3] and (player_total_countS >= 3 or player_total_countD >= 3 or player_total_countC >= 3 or player_total_countH >= 3):
                        selected_card1_confirm = True
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        player_card2.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[0] + player_cardnum_value[2]) - player_cardnum_value[3] == player_cardnum_value[0]:
                        selected_card1_confirm = True
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        player_card2.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card3_selected = False
                        player_card4_selected = False 
                        draw_player_pile = False
                case (True, False, True, False, True):
                    if player_cardnum_value[0] - player_cardnum_value[2] == player_cardnum_value[2] - player_cardnum_value[4] and (player_total_countS >= 3 or player_total_countD >= 3 or player_total_countC >= 3 or player_total_countH >= 3):
                        selected_card1_confirm = True
                        selected_card3_confirm = True
                        selected_card5_confirm = True
                        player_card2.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[0] + player_cardnum_value[2]) - player_cardnum_value[4] == player_cardnum_value[0]:
                        selected_card1_confirm = True
                        selected_card3_confirm = True
                        selected_card5_confirm = True
                        player_card2.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card3_selected = False
                        player_card5_selected = False
                        draw_player_pile = False
                case (True, False, False, True, True):
                    if player_cardnum_value[0] - player_cardnum_value[3] == player_cardnum_value[3] - player_cardnum_value[4] and (player_total_countS >= 3 or player_total_countD >= 3 or player_total_countC >= 3 or player_total_countH >= 3):
                        selected_card1_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card2.card_button.is_enabled = False
                        player_card3.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[0] + player_cardnum_value[3]) - player_cardnum_value[4] == player_cardnum_value[0]:
                        selected_card1_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card2.card_button.is_enabled = False
                        player_card3.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card4_selected = False
                        player_card5_selected = False
                        draw_player_pile = False
                case (True, True, False, True, False):
                    if player_cardnum_value[0] - player_cardnum_value[1] == player_cardnum_value[1] - player_cardnum_value[3] and (player_total_countS >= 3 or player_total_countD >= 3 or player_total_countC >= 3 or player_total_countH >= 3):
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card4_confirm = True
                        player_card3.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[0] + player_cardnum_value[1]) - player_cardnum_value[3] == player_cardnum_value[0]:
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card4_confirm = True
                        player_card3.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card2_selected = False
                        player_card4_selected = False
                        draw_player_pile = False
                case (True, True, False, False, True):
                    if player_cardnum_value[0] - player_cardnum_value[1] == player_cardnum_value[1] - player_cardnum_value[4] and (player_total_countS >= 3 or player_total_countD >= 3 or player_total_countC >= 3 or player_total_countH >= 3):
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card5_confirm = True
                        player_card3.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[0] + player_cardnum_value[1]) - player_cardnum_value[4] == player_cardnum_value[0]:
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card5_confirm = True
                        player_card3.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card2_selected = False
                        player_card5_selected = False
                        draw_player_pile = False
                case (False, True, True, True, False):
                    if player_cardnum_value[1] - player_cardnum_value[2] == player_cardnum_value[2] - player_cardnum_value[3] and (player_total_countS >= 3 or player_total_countD >= 3 or player_total_countC >= 3 or player_total_countH >= 3):
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[1] + player_cardnum_value[2]) - player_cardnum_value[3] == player_cardnum_value[1]:
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card2_selected = False
                        player_card3_selected = False
                        player_card4_selected = False
                        draw_player_pile = False
                case (False, True, True, False, True):
                    if player_cardnum_value[1] - player_cardnum_value[2] == player_cardnum_value[2] - player_cardnum_value[4] and (player_total_countS >= 3 or player_total_countD >= 3 or player_total_countC >= 3 or player_total_countH >= 3):
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        selected_card5_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[1] + player_cardnum_value[2]) - player_cardnum_value[4] == player_cardnum_value[1]:
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        selected_card5_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card2_selected = False
                        player_card3_selected = False
                        player_card5_selected = False
                        draw_player_pile = False
                case (False, True, False, True, True):
                    if player_cardnum_value[1] - player_cardnum_value[3] == player_cardnum_value[3] - player_cardnum_value[4] and (player_total_countS >= 3 or player_total_countD >= 3 or player_total_countC >= 3 or player_total_countH >= 3):
                        selected_card2_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card3.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[1] + player_cardnum_value[3]) - player_cardnum_value[4] == player_cardnum_value[1]:
                        selected_card2_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card3.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card2_selected = False
                        player_card4_selected = False
                        player_card5_selected = False
                        draw_player_pile = False
                case (False, False, True, True, True):
                    if player_cardnum_value[2] - player_cardnum_value[3] == player_cardnum_value[3] - player_cardnum_value[4] and (player_total_countS >= 3 or player_total_countD >= 3 or player_total_countC >= 3 or player_total_countH >= 3):
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card2.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[2] + player_cardnum_value[3]) - player_cardnum_value[4] == player_cardnum_value[2]:
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card1.card_button.is_enabled = False
                        player_card2.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card2_selected = False
                        player_card3_selected = False
                        draw_player_pile = False


                case (True, True, True, True, False):
                    if player_cardnum_value[0] - player_cardnum_value[1] == player_cardnum_value[2] - player_cardnum_value[3] and (player_total_countS >= 4 or player_total_countD >= 4 or player_total_countC >= 4 or player_total_countH >= 4):
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[0] - player_cardnum_value[1]) + (player_cardnum_value[2] - player_cardnum_value[3]) == 0:
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        player_card5.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card2_selected = False
                        player_card3_selected = False
                        player_card4_selected = False
                        draw_player_pile = False
                case (True, True, True, False, True):
                    if player_cardnum_value[0] - player_cardnum_value[1] == player_cardnum_value[2] - player_cardnum_value[4] and (player_total_countS >= 4 or player_total_countD >= 4 or player_total_countC >= 4 or player_total_countH >= 4):
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        selected_card5_confirm = True
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[0] - player_cardnum_value[1]) + (player_cardnum_value[2] - player_cardnum_value[4]) == 0:
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        selected_card5_confirm = True
                        player_card4.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        player_card1_selected = False
                        player_card2_selected = False
                        player_card3_selected = False
                        player_card5_selected = False
                        draw_player_pile = False
                case (True, True, False, True, True):
                    if player_cardnum_value[0] - player_cardnum_value[1] == player_cardnum_value[3] - player_cardnum_value[4] and (player_total_countS >= 4 or player_total_countD >= 4 or player_total_countC >= 4 or player_total_countH >= 4):
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card3.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[0] - player_cardnum_value[1]) + (player_cardnum_value[3] - player_cardnum_value[4]) == 0:
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card3.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        selected_card1_confirm = False
                        selected_card2_confirm = False
                        selected_card4_confirm = False
                        selected_card5_confirm = False
                        draw_player_pile = False
                case (True, False, True, True, True):
                    if player_cardnum_value[0] - player_cardnum_value[2] == player_cardnum_value[3] - player_cardnum_value[4] and (player_total_countS >= 4 or player_total_countD >= 4 or player_total_countC >= 4 or player_total_countH >= 4):
                        selected_card1_confirm = True
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card2.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[0] - player_cardnum_value[2]) + (player_cardnum_value[3] - player_cardnum_value[4]) == 0:
                        selected_card1_confirm = True
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card2.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        selected_card1_confirm = False
                        selected_card3_confirm = False
                        selected_card4_confirm = False
                        selected_card5_confirm = False
                        draw_player_pile = False
                case (False, True, True, True, True):
                    if player_cardnum_value[1] - player_cardnum_value[2] == player_cardnum_value[3] - player_cardnum_value[4] and (player_total_countS >= 4 or player_total_countD >= 4 or player_total_countC >= 4 or player_total_countH >= 4):
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card1.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    elif (player_cardnum_value[1] - player_cardnum_value[2]) + (player_cardnum_value[3] - player_cardnum_value[4]) == 0:
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        player_card1.card_button.is_enabled = False
                        new_card_button.is_enabled = True
                    else:
                        selected_card2_confirm = False
                        selected_card3_confirm = False
                        selected_card4_confirm = False
                        selected_card5_confirm = False
                        draw_player_pile = False

                case (True, True, True, True, True):
                    if player_cardnum_value[0] - player_cardnum_value[1] == player_cardnum_value[1] - player_cardnum_value[2] and player_cardnum_value[2] - player_cardnum_value[3] == player_cardnum_value[3] - player_cardnum_value[4] and (player_total_countS >= 5 or player_total_countD >= 5 or player_total_countC >= 5 or player_total_countH >= 5):
                        selected_card1_confirm = True
                        selected_card2_confirm = True
                        selected_card3_confirm = True
                        selected_card4_confirm = True
                        selected_card5_confirm = True
                        new_card_button.is_enabled = True
                    else:
                        selected_card1_confirm = False
                        selected_card2_confirm = False
                        selected_card3_confirm = False
                        selected_card4_confirm = False
                        selected_card5_confirm = False
                        draw_player_pile = False
        else:
            player_card1.card_button.is_enabled = False
            player_card2.card_button.is_enabled = False
            player_card3.card_button.is_enabled = False
            player_card4.card_button.is_enabled = False
            player_card5.card_button.is_enabled = False    


        if selected_card1_confirm:
            screen.blit(pile_card1.card_img, pile_card1.card_button)
            screen.fill('black', player_card1.card_button)
            screen.fill('black', card_text_rect1)
            if remove_card1:
                pile_card1_index = player_hand.pop(0)
                print(player_hand)
                pile_deck.append(pile_card1_index)
                player_card1_removed = True
            if pile_card1_selected:
                player_hand.insert(0, AI_pile[0])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card2_selected:
                player_hand.insert(1, AI_pile[1])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card3_selected:
                player_hand.insert(2, AI_pile[2])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card4_selected:
                player_hand.insert(3, AI_pile[3])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card5_selected:
                player_hand.insert(4, AI_pile[4])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            player_cards.remove(player_card1)
            print(player_cards)
            print(pile_deck)
            remove_card1 = False
            player_card1.card_button.is_enabled = False
            confirm_card_button.is_enabled = False
            pile_card1_selected = False      
            pile_card2_selected = False                  
            pile_card3_selected = False                  
            pile_card4_selected = False                  
            pile_card5_selected = False                              
        selected_card1_confirm = False
            
        if selected_card2_confirm:
            screen.blit(pile_card2.card_img, pile_card2.card_button)
            screen.fill('black', player_card2.card_button)
            screen.fill('black', card_text_rect2)
            if player_card1_removed and remove_card2:
                pile_card2_index = player_hand.pop(0)
                pile_deck.append(pile_card2_index)
                print(player_hand)
                player_card2_removed = True
                remove_card2 = False             
            elif remove_card2:
                pile_card2_index = player_hand.pop(1)
                pile_deck.append(pile_card2_index)  
                print(player_hand)
                player_card2_removed = True        
                remove_card2 = False  
            if pile_card1_selected:
                player_hand.insert(0, AI_pile[0])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card2_selected:
                player_hand.insert(1, AI_pile[1])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card3_selected:
                player_hand.insert(2, AI_pile[2])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card4_selected:
                player_hand.insert(3, AI_pile[3])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card5_selected:
                player_hand.insert(4, AI_pile[4])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            player_cards.remove(player_card2)
            print(player_cards)   
            print(pile_deck)
            remove_card2 = False
            player_card2.card_button.is_enabled = False
            confirm_card_button.is_enabled = False
            pile_card1_selected = False      
            pile_card2_selected = False                  
            pile_card3_selected = False                  
            pile_card4_selected = False                  
            pile_card5_selected = False
        selected_card2_confirm = False
                
        if selected_card3_confirm:
            screen.blit(pile_card3.card_img, pile_card3.card_button)
            screen.fill('black', player_card3.card_button)
            screen.fill('black', card_text_rect3)
            if (player_card1_removed and remove_card3) and (player_card2_removed and remove_card3):
                pile_card3_index = player_hand.pop(0)
                pile_deck.append(pile_card3_index)  
                print(player_hand) 
                player_card3_removed = True  
                remove_card3 = False 
            elif ((player_card1_removed and remove_card3) or (player_card2_removed and remove_card3)) or ((player_card1_removed and remove_card3) or (player_card2_removed and remove_card3)):
                pile_card3_index = player_hand.pop(1)
                pile_deck.append(pile_card3_index)
                print(player_hand)
                player_card3_removed = True       
                remove_card3 = False  
            elif remove_card3:
                pile_card3_index = player_hand.pop(2)
                pile_deck.append(pile_card3_index)
                print(player_hand)
                player_card3_removed = True       
                remove_card3 = False     
            if pile_card1_selected:
                player_hand.insert(0, AI_pile[0])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card2_selected:
                player_hand.insert(1, AI_pile[1])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card3_selected:
                player_hand.insert(2, AI_pile[2])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card4_selected:
                player_hand.insert(3, AI_pile[3])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card5_selected:
                player_hand.insert(4, AI_pile[4])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            player_cards.remove(player_card3)
            print(player_cards)
            print(pile_deck)
            remove_card3 = False
            player_card3.card_button.is_enabled = False
            confirm_card_button.is_enabled = False
            pile_card1_selected = False      
            pile_card2_selected = False                  
            pile_card3_selected = False                  
            pile_card4_selected = False                  
            pile_card5_selected = False
        selected_card3_confirm = False

        if selected_card4_confirm:
            screen.blit(pile_card4.card_img, pile_card4.card_button)
            screen.fill('black', player_card4.card_button)
            screen.fill('black', card_text_rect4)
            if (player_card1_removed and remove_card4) and (player_card2_removed and remove_card4) and (player_card3_removed and remove_card4):
                pile_card4_index = player_hand.pop(0)
                pile_deck.append(pile_card4_index) 
                print(player_hand) 
                player_card4_removed = True  
                remove_card4 = False                 
            elif ((player_card1_removed and remove_card4) and (player_card2_removed and remove_card4)) or ((player_card1_removed and remove_card4) and (player_card3_removed and remove_card4)) or ((player_card2_removed and remove_card4) and (player_card3_removed and remove_card4)):
                pile_card4_index = player_hand.pop(1)
                pile_deck.append(pile_card4_index)  
                print(player_hand) 
                player_card4_removed = True  
                remove_card4 = False 
            elif (player_card1_removed and remove_card4) or (player_card2_removed and remove_card4) or (player_card3_removed and remove_card4):
                pile_card4_index = player_hand.pop(2)
                pile_deck.append(pile_card4_index)
                print(player_hand)
                player_card4_removed = True       
                remove_card4 = False  
            elif remove_card4:
                pile_card4_index = player_hand.pop(3)
                pile_deck.append(pile_card4_index)
                print(player_hand)
                player_card4_removed = True       
                remove_card4 = False    
            if pile_card1_selected:
                player_hand.insert(0, AI_pile[0])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card2_selected:
                player_hand.insert(1, AI_pile[1])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card3_selected:
                player_hand.insert(2, AI_pile[2])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card4_selected:
                player_hand.insert(3, AI_pile[3])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card5_selected:
                player_hand.insert(4, AI_pile[4])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            player_cards.remove(player_card4)
            print(player_cards) 
            print(pile_deck)
            remove_card4 = False
            player_card4.card_button.is_enabled = False
            confirm_card_button.is_enabled = False
            pile_card1_selected = False      
            pile_card2_selected = False                  
            pile_card3_selected = False                  
            pile_card4_selected = False                  
            pile_card5_selected = False
        selected_card4_confirm = False
            
        if selected_card5_confirm:
            screen.blit(pile_card5.card_img, pile_card5.card_button)
            screen.fill('black', player_card5.card_button)
            screen.fill('black', card_text_rect5)  
            if (player_card1_removed and remove_card5) and (player_card2_removed and remove_card5) and (player_card3_removed and remove_card5) and (player_card4_removed and remove_card5):
                pile_card5_index = player_hand.pop(0)
                pile_deck.append(pile_card5_index)  
                print(player_hand) 
                player_card5_removed = True  
                remove_card5 = False                
            elif ((player_card1_removed and remove_card5) and (player_card2_removed and remove_card5) and (player_card3_removed and remove_card5)) or ((player_card1_removed and remove_card5) and (player_card3_removed and remove_card5) and (player_card4_removed and remove_card5)) or ((player_card1_removed and remove_card5) and (player_card2_removed and remove_card5) and (player_card4_removed and remove_card5)) or ((player_card2_removed and remove_card5) and (player_card3_removed and remove_card5) and (player_card4_removed and remove_card5)):
                pile_card5_index = player_hand.pop(1)
                pile_deck.append(pile_card5_index)  
                print(player_hand) 
                player_card5_removed = True  
                remove_card5 = False                 
            elif ((player_card1_removed and remove_card5) and (player_card2_removed and remove_card5)) or ((player_card1_removed and remove_card5) and (player_card3_removed and remove_card5)) or ((player_card1_removed and remove_card5) and (player_card4_removed and remove_card5) or ((player_card2_removed and remove_card5) and (player_card3_removed and remove_card5)) or ((player_card2_removed and remove_card5) and (player_card4_removed and remove_card5)) or ((player_card3_removed and remove_card5) and (player_card4_removed and remove_card5))):
                pile_card5_index = player_hand.pop(2)
                pile_deck.append(pile_card5_index)  
                print(player_hand) 
                player_card5_removed = True  
                remove_card5 = False 
            elif (player_card1_removed and remove_card5) or (player_card2_removed and remove_card5) or (player_card3_removed and remove_card5) or (player_card4_removed and remove_card5):
                pile_card5_index = player_hand.pop(3)
                pile_deck.append(pile_card5_index)
                print(player_hand)
                player_card5_removed = True       
                remove_card5 = False  
            elif remove_card5:
                pile_card5_index = player_hand.pop(4)
                pile_deck.append(pile_card5_index)
                print(player_hand)
                player_card5_removed = True       
                remove_card5 = False     
            if pile_card1_selected:
                player_hand.insert(0, AI_pile[0])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card2_selected:
                player_hand.insert(1, AI_pile[1])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card3_selected:
                player_hand.insert(2, AI_pile[2])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card4_selected:
                player_hand.insert(3, AI_pile[3])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            elif pile_card5_selected:
                player_hand.insert(4, AI_pile[4])
                print(player_hand)
                print(AI_hand) 
                pile_card_confirmed = True
            player_cards.remove(player_card5)
            print(player_cards)
            print(pile_deck)
            remove_card5 = False
            player_card5.card_button.is_enabled = False
            confirm_card_button.is_enabled = False 
            pile_card1_selected = False      
            pile_card2_selected = False                  
            pile_card3_selected = False                  
            pile_card4_selected = False                  
            pile_card5_selected = False          
        selected_card5_confirm = False


            
        if get_pile_cardnum:
            pile_cardnum_val.clear()
            for cardval in pile_deck:
                if cardval[0] in royal_card_conversion:
                    pile_cardnum_val.append(royal_card_conversion[cardval[0]])
                else:
                    pile_cardnum_val.append(int(cardval[:-1]))

                pile_cardnum_val.sort()
        get_pile_cardnum = False

        print(pile_cardnum_val)
        print(player_cards)


        if deal_new_card:
            new_card = random.choice(deck)
            player_hand.append(new_card)
            deck.remove(new_card)

        if deal_AI_card:
            get_AI_cardnum = True
            new_AI_card = random.choice(deck)
            AI_hand.append(new_AI_card)
            deck.remove(new_AI_card)
            AI_card_dealed = True
        deal_AI_card = False

        if player_new_card:
            print(player_hand)

            if player_card1 not in player_cards:
                player_card1 = Card(new_card, 130, 770, (200, 300), "1")
                player_card1.draw()
                player_cards.insert(0, player_card1)
            elif player_card2 not in player_cards:
                player_card2 = Card(new_card, 350, 770, (200, 300), "2")
                player_card2.draw()
                player_cards.insert(1, player_card2)                
            elif player_card3 not in player_cards:
                player_card3 = Card(new_card, 570, 770, (200, 300), "3")
                player_card3.draw()
                player_cards.insert(2, player_card3)              
            elif player_card4 not in player_cards:
                player_card4 = Card(new_card, 790, 770, (200, 300), "4")
                player_card4.draw()
                player_cards.insert(3, player_card4)  
            elif player_card5 not in player_cards:
                player_card5 = Card(new_card, 1010, 770, (200, 300), "5")
                player_card5.draw()
                player_cards.insert(4, player_card5)
            new_card_button.is_enabled = False

        if get_player_cardnum:
            player_cardnum_val.clear()
            for cardval in player_hand:
                if cardval[0] in royal_card_conversion:
                    player_cardnum_val.append(royal_card_conversion[cardval[0]])
                else:
                    player_cardnum_val.append(int(cardval[:-1]))

                player_cardnum_val.sort()
        get_player_cardnum = False

        if get_AI_cardnum:
            AI_cardnum_val.clear()
            for cardval in AI_hand:
                if cardval[0] in royal_card_conversion:
                    AI_cardnum_val.append(royal_card_conversion[cardval[0]])
                else:
                    AI_cardnum_val.append(int(cardval[:-1]))

                AI_cardnum_val.sort()
        get_AI_cardnum = False
        
        print(player_cardnum_val)




        print(player_total_countS)
        print(player_total_countD)
        print(player_total_countC)
        print(player_total_countH) 

        print(player_cardnum_value)

        if len(player_hand) == 5:    
            player_card1 = Card(player_hand[0], 130, 770, (200, 300), "1")
            player_card2 = Card(player_hand[1], 350, 770, (200, 300), "2")
            player_card3 = Card(player_hand[2], 570, 770, (200, 300), "3")
            player_card4 = Card(player_hand[3], 790, 770, (200, 300), "4")
            player_card5 = Card(player_hand[4], 1010, 770, (200, 300), "5")
            player_card1.draw()
            player_card2.draw()
            player_card3.draw()
            player_card4.draw()
            player_card5.draw() 
            if confirm_card_button.is_enabled == False and new_card_button.is_enabled == True:
                player_card1.card_button.is_enabled = False
                player_card2.card_button.is_enabled = False
                player_card3.card_button.is_enabled = False
                player_card4.card_button.is_enabled = False
                player_card5.card_button.is_enabled = False

        elif len(player_hand) == 4:
            player_card1 = Card(player_hand[0], 130, 770, (200, 300), "1")
            player_card2 = Card(player_hand[1], 350, 770, (200, 300), "2")
            player_card3 = Card(player_hand[2], 570, 770, (200, 300), "3")
            player_card4 = Card(player_hand[3], 790, 770, (200, 300), "4")
            player_card1.draw()
            player_card2.draw()
            player_card3.draw()
            player_card4.draw()
            screen.fill('black', player_card5.card_button)
            player_card5.card_button.is_enabled = False
            if confirm_card_button.is_enabled == False and new_card_button.is_enabled == True:
                player_card1.card_button.is_enabled = False
                player_card2.card_button.is_enabled = False
                player_card3.card_button.is_enabled = False
                player_card4.card_button.is_enabled = False



            
        elif len(player_hand) == 3:
            player_card1 = Card(player_hand[0], 130, 770, (200, 300), "1")
            player_card2 = Card(player_hand[1], 350, 770, (200, 300), "2")
            player_card3 = Card(player_hand[2], 570, 770, (200, 300), "3")
            player_card1.draw()
            player_card2.draw()
            player_card3.draw()
            screen.fill('black', player_card4.card_button)
            screen.fill('black', player_card5.card_button)
            player_card4.card_button.is_enabled = False
            player_card5.card_button.is_enabled = False
            if confirm_card_button.is_enabled == False and new_card_button.is_enabled == True:
                player_card1.card_button.is_enabled = False
                player_card2.card_button.is_enabled = False
                player_card3.card_button.is_enabled = False


        elif len(player_hand) == 2:
            player_card1 = Card(player_hand[0], 130, 770, (200, 300), "1")
            player_card2 = Card(player_hand[1], 350, 770, (200, 300), "2")
            player_card1.draw()
            player_card2.draw()
            screen.fill('black', player_card3.card_button)
            screen.fill('black', player_card4.card_button)
            screen.fill('black', player_card5.card_button)
            player_card3.card_button.is_enabled = False
            player_card4.card_button.is_enabled = False
            player_card5.card_button.is_enabled = False
            if confirm_card_button.is_enabled == False and new_card_button.is_enabled == True:
                player_card1.card_button.is_enabled = False
                player_card2.card_button.is_enabled = False


        elif len(player_hand) == 1:
            player_card1 = Card(player_hand[0], 130, 770, (200, 300), "1")
            player_card1.draw()
            screen.fill('black', player_card2.card_button)
            screen.fill('black', player_card3.card_button)
            screen.fill('black', player_card4.card_button)
            screen.fill('black', player_card5.card_button)
            player_card2.card_button.is_enabled = False
            player_card3.card_button.is_enabled = False
            player_card4.card_button.is_enabled = False
            player_card5.card_button.is_enabled = False
            if confirm_card_button.is_enabled == False and new_card_button.is_enabled == True:
                player_card1.card_button.is_enabled = False
        
        elif len(player_hand) == 0:
            screen.fill('black', player_card1.card_button)
            screen.fill('black', player_card2.card_button)
            screen.fill('black', player_card3.card_button)
            screen.fill('black', player_card4.card_button)
            screen.fill('black', player_card5.card_button)


        deal_new_card = False

        print(player_cards)

        if pile_card_confirmed == True:
            player_card1_selected = False
            player_card2_selected = False
            player_card3_selected = False
            player_card4_selected = False
            player_card5_selected = False
            get_player_cardnum = True
            get_player_cardnumV2 = True
            count_suit_num = False
            draw_player_pile = False
            AI_turn = True
            remove_AI_cards = True
            draw_AI_pile = True
            deal_AI_card = True
            get_pile_card = True
        pile_card_confirmed = False

        if AI_turn:
            pile_card1.card_button.is_enabled = True
            pile_card2.card_button.is_enabled = True
            pile_card3.card_button.is_enabled = True
            pile_card4.card_button.is_enabled = True
            pile_card5.card_button.is_enabled = True
            pile_deck.clear()
            player_turn = False
            AI_pile = []
            AI_pile_obj = []
            AI_cardnum_value = []
            remaining_cards = []
            consecutiveV2 = []
            three_consecutive_numbers = False
            four_consecutive_numbers = False
            five_consecutive_numbers = False
            one_pair = False
            one_pair_in_making = False
            three_of_a_kind = False
            four_of_a_kind = False
            high_card_down = False
            total_countS = 0
            total_countD = 0
            total_countC = 0
            total_countH = 0
            
            AI_cardnum_value.clear()
            for cardval in AI_hand:
                if cardval[0] in royal_card_conversion:
                    AI_cardnum_value.append(royal_card_conversion[cardval[0]])
                else:
                    AI_cardnum_value.append(int(cardval[:-1]))

                AI_cardnum_value.sort()

            def CheckForConsecutive(n):      

                for cardnum in range(len(AI_cardnum_value) - n + 1):
                    consecutive_list = AI_cardnum_value[cardnum : cardnum + n]
                    print(consecutive_list)
                    print("happy")
                    if len(set(consecutive_list)) == n: 
                        if max(consecutive_list) - min(consecutive_list) == n - 1:
                            return True
                        else:
                            return False

            def CheckForConsecutiveV2(n):

                for cardnum in range(len(consecutiveV2) - n + 1):
                    consecutive_listV2 = consecutiveV2[cardnum : cardnum + n]
                    print(consecutive_listV2)
                    print("nigger")
                    if len(set(consecutive_listV2)) == n:
                        if max(consecutive_listV2) - min(consecutive_listV2) == n - 1:
                            return True
                        else:
                            return False

            for cardval in AI_hand:
                total_countS += cardval.count("S")
                total_countD += cardval.count("D")
                total_countC += cardval.count("C")
                total_countH += cardval.count("H")

            for cardval in AI_hand:

                if CheckForConsecutive(5) and total_countS == 5 and CheckForConsecutiveV2(5):
                    if "S" == cardval[-1]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        five_consecutive_numbers = True

                elif CheckForConsecutive(5) and total_countD == 5 and CheckForConsecutiveV2(5):     
                    if "D" == cardval[-1]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        five_consecutive_numbers = True

                elif CheckForConsecutive(5) and total_countC == 5 and CheckForConsecutiveV2(5):
                    if "C" == cardval[-1]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        five_consecutive_numbers = True

                elif CheckForConsecutive(5) and total_countH == 5 and CheckForConsecutiveV2(5):
                    if "H" == cardval[-1]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        five_consecutive_numbers = True


                elif "K" == cardval[0] and AI_cardnum_value.count(13) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)        
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 13, AI_cardnum_value))

                elif "Q" == cardval[0] and AI_cardnum_value.count(12) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)     
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 12, AI_cardnum_value))

                elif "J" == cardval[0] and AI_cardnum_value.count(11) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)  
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 11, AI_cardnum_value))

                elif "1" == cardval[0] and "0" == cardval[1] and AI_cardnum_value.count(10) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile) 
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 10, AI_cardnum_value))

                elif "9" == cardval[0] and AI_cardnum_value.count(9) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)  
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 9, AI_cardnum_value))

                elif "8" == cardval[0] and AI_cardnum_value.count(8) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)  
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 8, AI_cardnum_value))

                elif "7" == cardval[0] and AI_cardnum_value.count(7) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)    
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 7, AI_cardnum_value))

                elif "6" == cardval[0] and AI_cardnum_value.count(6) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)   
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 6, AI_cardnum_value))

                elif "5" == cardval[0] and AI_cardnum_value.count(5) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)     
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 5, AI_cardnum_value))

                elif "4" == cardval[0] and AI_cardnum_value.count(4) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)        
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 4, AI_cardnum_value))

                elif "3" == cardval[0] and AI_cardnum_value.count(3) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)        
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 3, AI_cardnum_value))

                elif "2" == cardval[0] and AI_cardnum_value.count(2) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)        
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 2, AI_cardnum_value))

                elif "A" == cardval[0] and AI_cardnum_value.count(1) == 4:
                    AI_pile.append(f"{cardval}")                
                    print(AI_pile)
                    four_of_a_kind = True
                    if len(AI_pile) == 4:
                        AI_cardnum_value = list(filter(lambda item: item != 1, AI_cardnum_value))


                elif CheckForConsecutive(4) and total_countS == 4 and CheckForConsecutiveV2(4):
                    if "S" == cardval[-1]:
                        AI_pile.append(f"{cardval}")
                        consecutiveV2.append(royal_card_conversion[cardval[0]]) 
                        consecutiveV2.sort()  
                        print(consecutiveV2)                 
                        print(AI_pile)
                        four_consecutive_numbers = True
                        if len(AI_pile) == 4 and CheckForConsecutiveV2(4) == False:
                            AI_pile.clear()
                            consecutiveV2.clear()
                            four_consecutive_numbers = False
                            continue

                elif CheckForConsecutive(4) and total_countD == 4 and CheckForConsecutiveV2(4):
                    if "D" == cardval[-1]:
                        AI_pile.append(f"{cardval}")
                        consecutiveV2.append(royal_card_conversion[cardval[0]]) 
                        consecutiveV2.sort()  
                        print(consecutiveV2)                 
                        print(AI_pile)
                        four_consecutive_numbers = True
                        if len(AI_pile) == 4 and CheckForConsecutiveV2(4) == False:
                            AI_pile.clear()
                            consecutiveV2.clear()
                            four_consecutive_numbers = False
                            continue

                elif CheckForConsecutive(4) and total_countC == 4 and CheckForConsecutiveV2(4):
                    if "C" == cardval[-1]:
                        AI_pile.append(f"{cardval}")
                        consecutiveV2.append(royal_card_conversion[cardval[0]]) 
                        consecutiveV2.sort()  
                        print(consecutiveV2)                 
                        print(AI_pile)
                        four_consecutive_numbers = True
                        if len(AI_pile) == 4 and CheckForConsecutiveV2(4) == False:
                            AI_pile.clear()
                            consecutiveV2.clear()
                            four_consecutive_numbers = False
                            continue

                elif CheckForConsecutive(4) and total_countH == 4 and CheckForConsecutiveV2(4):
                    if "H" == cardval[-1]:
                        AI_pile.append(f"{cardval}")
                        consecutiveV2.append(royal_card_conversion[cardval[0]]) 
                        consecutiveV2.sort()  
                        print(consecutiveV2)                 
                        print(AI_pile)
                        four_consecutive_numbers = True
                        if len(AI_pile) == 4 and CheckForConsecutiveV2(4) == False:
                            AI_pile.clear()
                            consecutiveV2.clear()
                            four_consecutive_numbers = False
                            continue


                elif AI_cardnum_value.count(13) == 3:
                    if "K" == cardval[0]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 13, AI_cardnum_value))

                elif AI_cardnum_value.count(12) == 3:
                    if "Q" == cardval[0]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 12, AI_cardnum_value))

                elif AI_cardnum_value.count(11) == 3:
                    if "J" == cardval[0]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 11, AI_cardnum_value))

                elif AI_cardnum_value.count(10) == 3:
                    if "1" == cardval[0] and "0" == cardval[1]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 10, AI_cardnum_value))

                elif AI_cardnum_value.count(9) == 3:
                    if "9" == cardval[0]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 9, AI_cardnum_value))
                        
                elif AI_cardnum_value.count(8) == 3:
                    if "8" == cardval[0]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 8, AI_cardnum_value))

                elif AI_cardnum_value.count(7) == 3:
                    if "7" == cardval[0]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 7, AI_cardnum_value))

                elif AI_cardnum_value.count(6) == 3:
                    if "6" == cardval[0]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 6, AI_cardnum_value))

                elif AI_cardnum_value.count(5) == 3:
                    if "5" == cardval[0]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 5, AI_cardnum_value))

                elif AI_cardnum_value.count(4) == 3:
                    if "4" == cardval[0]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 4, AI_cardnum_value))

                elif AI_cardnum_value.count(3) == 3:
                    if "3" == cardval[0]: 
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 3, AI_cardnum_value))

                elif AI_cardnum_value.count(2) == 3:
                    if "2" == cardval[0]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 2, AI_cardnum_value))

                elif AI_cardnum_value.count(1) == 3:
                    if "A" == cardval[0]:
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)        
                        three_of_a_kind = True
                        if len(AI_pile) == 3:
                            AI_cardnum_value = list(filter(lambda item: item != 1, AI_cardnum_value))


                elif CheckForConsecutive(3) and total_countS == 3 and CheckForConsecutiveV2(3):
                    if "S" == cardval[-1]:
                        AI_pile.append(f"{cardval}")
                        consecutiveV2.append(royal_card_conversion[cardval[0]]) 
                        consecutiveV2.sort()  
                        print(consecutiveV2)                 
                        print(AI_pile)
                        three_consecutive_numbers = True
                        if len(AI_pile) == 3 and CheckForConsecutiveV2(3) == False:
                            AI_pile.clear()
                            consecutiveV2.clear()
                            three_consecutive_numbers = False
                            continue

                elif CheckForConsecutive(3) and total_countD == 3 and CheckForConsecutiveV2(3):
                    if "D" == cardval[-1]:
                        AI_pile.append(f"{cardval}")
                        consecutiveV2.append(royal_card_conversion[cardval[0]]) 
                        consecutiveV2.sort()  
                        print(consecutiveV2)                 
                        print(AI_pile)
                        three_consecutive_numbers = True
                        if len(AI_pile) == 3 and CheckForConsecutiveV2(3) == False:
                            AI_pile.clear()
                            consecutiveV2.clear()
                            three_consecutive_numbers = False
                            continue

                elif CheckForConsecutive(3) and total_countC == 3 and CheckForConsecutiveV2(3):
                    if "C" == cardval[-1]:
                        AI_pile.append(f"{cardval}")
                        consecutiveV2.append(royal_card_conversion[cardval[0]]) 
                        consecutiveV2.sort()  
                        print(consecutiveV2)                 
                        print(AI_pile)
                        three_consecutive_numbers = True
                        if len(AI_pile) == 3 and CheckForConsecutiveV2(3) == False:
                            AI_pile.clear()
                            consecutiveV2.clear()
                            three_consecutive_numbers = False
                            continue

                elif CheckForConsecutive(3) and total_countH == 3 and CheckForConsecutiveV2(3):
                    if "H" == cardval[-1]:
                        AI_pile.append(f"{cardval}")
                        consecutiveV2.append(royal_card_conversion[cardval[0]]) 
                        consecutiveV2.sort()  
                        print(consecutiveV2)                 
                        print(AI_pile)
                        three_consecutive_numbers = True
                        if len(AI_pile) == 3 and CheckForConsecutiveV2(3) == False:
                            AI_pile.clear()
                            consecutiveV2.clear()
                            three_consecutive_numbers = False
                            continue


                elif AI_cardnum_value.count(13) == 2:
                    if "K" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True    
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 13, AI_cardnum_value))

                elif AI_cardnum_value.count(12) == 2:
                    if "Q" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True    
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 12, AI_cardnum_value))

                elif AI_cardnum_value.count(11) == 2:
                    if "J" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True    
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 11, AI_cardnum_value))

                elif AI_cardnum_value.count(10) == 2:
                    if "1" == cardval[0] and "0" == cardval[1]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True    
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 10, AI_cardnum_value))

                elif AI_cardnum_value.count(9) == 2:
                    if "9" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True    
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 9, AI_cardnum_value))
                        
                elif AI_cardnum_value.count(8) == 2:
                    if "8" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True    
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 8, AI_cardnum_value))

                elif AI_cardnum_value.count(7) == 2:
                    if "7" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True    
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 7, AI_cardnum_value))

                elif AI_cardnum_value.count(6) == 2:
                    if "6" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True    
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 6, AI_cardnum_value))

                elif AI_cardnum_value.count(5) == 2:
                    if "5" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True    
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 5, AI_cardnum_value))

                elif AI_cardnum_value.count(4) == 2:
                    if "4" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True    
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 4, AI_cardnum_value))

                elif AI_cardnum_value.count(3) == 2:
                    if "3" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True    
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 3, AI_cardnum_value))

                elif AI_cardnum_value.count(2) == 2:
                    if "2" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True   
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 2, AI_cardnum_value))

                elif AI_cardnum_value.count(1) == 2:
                    if "A" == cardval[0]:
                        if three_consecutive_numbers or one_pair or three_of_a_kind:
                            continue
                        else:
                            AI_pile.append(f"{cardval}")                
                            print(AI_pile)
                            one_pair = True  
                            if len(AI_pile) != 2:
                                one_pair = False
                                one_pair_in_making = True   
                            else:
                                AI_cardnum_value = list(filter(lambda item: item != 1, AI_cardnum_value))
                                

                elif five_consecutive_numbers == False and four_consecutive_numbers == False and three_consecutive_numbers == False and four_of_a_kind == False and three_of_a_kind == False and one_pair == False:
                    if one_pair_in_making == True or high_card_down == True:
                        continue
                    elif cardval[0] == "K":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True
                        AI_cardnum_value = list(filter(lambda item: item != 13, AI_cardnum_value))
                    elif cardval[0] == "Q":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True
                        AI_cardnum_value = list(filter(lambda item: item != 12, AI_cardnum_value))
                    elif cardval[0] == "J":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True
                        AI_cardnum_value = list(filter(lambda item: item != 11, AI_cardnum_value))
                    elif cardval[0] == "1" and cardval[1] == "0":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True
                        AI_cardnum_value = list(filter(lambda item: item != 10, AI_cardnum_value))
                    elif cardval[0] == "9":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True
                        AI_cardnum_value = list(filter(lambda item: item != 9, AI_cardnum_value))
                    elif cardval[0] == "8":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True
                        AI_cardnum_value = list(filter(lambda item: item != 8, AI_cardnum_value))
                    elif cardval[0] == "7":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True
                        AI_cardnum_value = list(filter(lambda item: item != 7, AI_cardnum_value))
                    elif cardval[0] == "6":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True
                        AI_cardnum_value = list(filter(lambda item: item != 6, AI_cardnum_value))
                    elif cardval[0] == "5":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True
                        AI_cardnum_value = list(filter(lambda item: item != 5, AI_cardnum_value))
                    elif cardval[0] == "4":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True
                        AI_cardnum_value = list(filter(lambda item: item != 4, AI_cardnum_value))
                    elif cardval[0] == "3":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True
                        AI_cardnum_value = list(filter(lambda item: item != 3, AI_cardnum_value))
                    elif cardval[0] == "2":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True      
                        AI_cardnum_value = list(filter(lambda item: item != 2, AI_cardnum_value)) 
                    elif cardval[0] == "A":
                        AI_pile.append(f"{cardval}")                
                        print(AI_pile)
                        high_card_down = True     
                        AI_cardnum_value = list(filter(lambda item: item != 1, AI_cardnum_value))
                else:
                    remaining_cards.append(f"{cardval}")

                AI_pile.sort(key=AI_card_sort)

            print(AI_pile)
            print(AI_hand)
            print(remaining_cards)
            print(AI_hand)
            AI_turn_done = True
        
        if draw_AI_pile:
            print(AI_pile)
            screen.fill('black', pile_card1.card_button)
            screen.fill('black', pile_card2.card_button)
            screen.fill('black', pile_card3.card_button)
            screen.fill('black', pile_card4.card_button)
            screen.fill('black', pile_card5.card_button)

            screen.fill('black', AI_card1.card_button)
            screen.fill('black', AI_card2.card_button)
            screen.fill('black', AI_card3.card_button)
            screen.fill('black', AI_card4.card_button)
            screen.fill('black', AI_card5.card_button)

            if len(AI_hand) == 5:
                AI_card5.draw()
                AI_card4.draw()
                AI_card3.draw()
                AI_card2.draw()
                AI_card1.draw()

                if len(AI_pile) == 1:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    AI_pile_obj = [pile_card1]
    
            elif len(AI_hand) == 4:
                AI_card5.draw()
                AI_card4.draw()
                AI_card3.draw()
                AI_card2.draw()
                
                if len(AI_pile) == 2:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    AI_pile_obj = [pile_card1, pile_card2] 
                elif len(AI_pile) == 1:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    AI_pile_obj = [pile_card1]

            elif len(AI_hand) == 3:
                AI_card5.draw()
                AI_card4.draw()
                AI_card3.draw()

                if len(AI_pile) == 3:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(AI_pile[2], 430, 350, (135, 190), "3")
                    AI_pile_obj = [pile_card1, pile_card2, pile_card3]  
                elif len(AI_pile) == 2:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    AI_pile_obj = [pile_card1, pile_card2] 
                elif len(AI_pile) == 1:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    AI_pile_obj = [pile_card1]

            elif len(AI_hand) == 2:
                AI_card5.draw()
                AI_card4.draw()

                if len(AI_pile) == 4:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(AI_pile[2], 430, 350, (135, 190), "3")
                    pile_card4 = Card(AI_pile[3], 290, 350, (135, 190), "4")
                    AI_pile_obj = [pile_card1, pile_card2, pile_card3, pile_card4]       
                elif len(AI_pile) == 3:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(AI_pile[2], 430, 350, (135, 190), "3")
                    AI_pile_obj = [pile_card1, pile_card2, pile_card3]  
                elif len(AI_pile) == 2:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    AI_pile_obj = [pile_card1, pile_card2] 
                elif len(AI_pile) == 1:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    AI_pile_obj = [pile_card1]  

            elif len(AI_hand) == 1:
                AI_card5.draw()

                if len(AI_pile) == 5:  
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(AI_pile[2], 430, 350, (135, 190), "3")
                    pile_card4 = Card(AI_pile[3], 290, 350, (135, 190), "4")
                    pile_card5 = Card(AI_pile[4], 150, 350, (135, 190), "5")
                    AI_pile_obj = [pile_card1, pile_card2, pile_card3, pile_card4, pile_card5]
                if len(AI_pile) == 4:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(AI_pile[2], 430, 350, (135, 190), "3")
                    pile_card4 = Card(AI_pile[3], 290, 350, (135, 190), "4")
                    AI_pile_obj = [pile_card1, pile_card2, pile_card3, pile_card4]       
                elif len(AI_pile) == 3:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(AI_pile[2], 430, 350, (135, 190), "3")
                    AI_pile_obj = [pile_card1, pile_card2, pile_card3]  
                elif len(AI_pile) == 2:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    AI_pile_obj = [pile_card1, pile_card2] 
                elif len(AI_pile) == 1:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    AI_pile_obj = [pile_card1]

            else:    
                if len(AI_pile) == 5:  
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(AI_pile[2], 430, 350, (135, 190), "3")
                    pile_card4 = Card(AI_pile[3], 290, 350, (135, 190), "4")
                    pile_card5 = Card(AI_pile[4], 150, 350, (135, 190), "5")
                    AI_pile_obj = [pile_card1, pile_card2, pile_card3, pile_card4, pile_card5]
                if len(AI_pile) == 4:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(AI_pile[2], 430, 350, (135, 190), "3")
                    pile_card4 = Card(AI_pile[3], 290, 350, (135, 190), "4")
                    AI_pile_obj = [pile_card1, pile_card2, pile_card3, pile_card4]       
                elif len(AI_pile) == 3:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(AI_pile[2], 430, 350, (135, 190), "3")
                    AI_pile_obj = [pile_card1, pile_card2, pile_card3]  
                elif len(AI_pile) == 2:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(AI_pile[1], 570, 350, (135, 190), "2")
                    AI_pile_obj = [pile_card1, pile_card2] 
                elif len(AI_pile) == 1:
                    pile_card1 = Card(AI_pile[0], 710, 350, (135, 190), "1")
                    AI_pile_obj = [pile_card1]

            for cards in AI_pile_obj:
                cards.draw()

        if remove_AI_cards:
            for card in AI_pile:
                if card in AI_hand:
                    AI_hand.remove(card)

        remove_AI_cards = False

        if AI_turn_done:
            remove_AI_cards = False
            player_turn = True
            deal_AI_card = True
        AI_turn_done = False

        if player_turn:
            AI_turn = False
            player_new_card = False
            remove_card1 = False
            remove_card2 = False
            remove_card3 = False
            remove_card4 = False
            remove_card5 = False
            player_card1_removed = False
            player_card2_removed = False
            player_card3_removed = False
            player_card4_removed = False
            player_card5_removed = False
            

            if player_card1_selected:
                confirm_card_button.is_enabled = True
                screen.blit(card_text1, card_text_rect1)
            else:
                screen.fill('black', card_text_rect1) 

            if player_card2_selected:
                confirm_card_button.is_enabled = True
                screen.blit(card_text2, card_text_rect2)
            else:
                screen.fill('black', card_text_rect2) 

            if player_card3_selected:
                confirm_card_button.is_enabled = True
                screen.blit(card_text3, card_text_rect3) 
            else:
                screen.fill('black', card_text_rect3)

            if player_card4_selected:
                confirm_card_button.is_enabled = True
                screen.blit(card_text4, card_text_rect4) 
            else:
                screen.fill('black', card_text_rect4)

            if player_card5_selected:
                confirm_card_button.is_enabled = True
                screen.blit(card_text5, card_text_rect5)  
            else:
                screen.fill('black', card_text_rect5)

            if get_pile_card == True:
                if len(AI_pile) == 5:
                    pile_card1.card_button.is_enabled = True
                    pile_card2.card_button.is_enabled = True
                    pile_card3.card_button.is_enabled = True
                    pile_card4.card_button.is_enabled = True
                    pile_card5.card_button.is_enabled = True
                if len(AI_pile) == 4:
                    pile_card1.card_button.is_enabled = True
                    pile_card2.card_button.is_enabled = True
                    pile_card3.card_button.is_enabled = True
                    pile_card4.card_button.is_enabled = True
                if len(AI_pile) == 3:
                    pile_card1.card_button.is_enabled = True
                    pile_card2.card_button.is_enabled = True
                    pile_card3.card_button.is_enabled = True
                if len(AI_pile) == 2:
                    pile_card1.card_button.is_enabled = True
                    pile_card2.card_button.is_enabled = True
                if len(AI_pile) == 1:
                    pile_card1.card_button.is_enabled = True

                if pile_card1_selected:
                    screen.blit(pile_text1, pile_text_rect1)
                else:
                    screen.fill('black', pile_text_rect1)

                if pile_card2_selected:
                    screen.blit(pile_text2, pile_text_rect2)
                else:
                    screen.fill('black', pile_text_rect2)

                if pile_card3_selected:
                    screen.blit(pile_text3, pile_text_rect3)
                else:
                    screen.fill('black', pile_text_rect3)

                if pile_card4_selected:
                    screen.blit(pile_text4, pile_text_rect4)
                else:
                    screen.fill('black', pile_text_rect4)

                if pile_card5_selected:
                    screen.blit(pile_text5, pile_text_rect5)
                else:
                    screen.fill('black', pile_text_rect5)                                        

            if new_card_button.is_enabled == True:
                confirm_card_button.is_enabled = False  
                screen.fill('black', card_text_rect1)
                screen.fill('black', card_text_rect2)
                screen.fill('black', card_text_rect3)
                screen.fill('black', card_text_rect4)
                screen.fill('black', card_text_rect5)

            if draw_player_pile:
                screen.fill('black', pile_card1.card_button)
                screen.fill('black', pile_card2.card_button)
                screen.fill('black', pile_card3.card_button)
                screen.fill('black', pile_card4.card_button)
                screen.fill('black', pile_card5.card_button)  

                if len(pile_deck) == 5:

                    pile_card1 = Card(pile_deck[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(pile_deck[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(pile_deck[2], 430, 350, (135, 190), "3")
                    pile_card4 = Card(pile_deck[3], 290, 350, (135, 190), "4")
                    pile_card5 = Card(pile_deck[4], 150, 350, (135, 190), "5")       
                    pile_card1.draw() 
                    pile_card2.draw()
                    pile_card3.draw()
                    pile_card4.draw()
                    pile_card5.draw()
                elif len(pile_deck) == 4:

                    pile_card1 = Card(pile_deck[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(pile_deck[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(pile_deck[2], 430, 350, (135, 190), "3")
                    pile_card4 = Card(pile_deck[3], 290, 350, (135, 190), "4")    
                    pile_card1.draw() 
                    pile_card2.draw()
                    pile_card3.draw()
                    pile_card4.draw()
                elif len(pile_deck) == 3:

                    pile_card1 = Card(pile_deck[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(pile_deck[1], 570, 350, (135, 190), "2")
                    pile_card3 = Card(pile_deck[2], 430, 350, (135, 190), "3")       
                    pile_card1.draw() 
                    pile_card2.draw()
                    pile_card3.draw()                      
                elif len(pile_deck) == 2:

                    pile_card1 = Card(pile_deck[0], 710, 350, (135, 190), "1")
                    pile_card2 = Card(pile_deck[1], 570, 350, (135, 190), "2")   
                    pile_card1.draw() 
                    pile_card2.draw()
                elif len(pile_deck) == 1:

                    pile_card1 = Card(pile_deck[0], 710, 350, (135, 190), "1")    
                    pile_card1.draw()   

            player_cardnum_sum = sum(player_cardnum_val)
            AI_cardnum_sum = sum(AI_cardnum_val)
            print(AI_cardnum_val)
            print(player_cardnum_sum)
            print(AI_cardnum_sum)
            print(player_hand)
            print(AI_hand)

            if player_cardnum_sum <= 5:
                show_card_button.is_enabled = True

            if AI_cardnum_sum <= 5 and AI_card_dealed == True:
                AI_turn = False
                print("Ai did it")
                AI_show_card = True

            if AI_show_card == True:
                player_show_card = True

            if player_show_card == True:
                screen.fill('black', AI_card1.card_button)
                screen.fill('black', AI_card2.card_button)
                screen.fill('black', AI_card3.card_button)
                screen.fill('black', AI_card4.card_button)
                screen.fill('black', AI_card5.card_button)
                screen.fill('black', pile_card1.card_button)
                screen.fill('black', pile_card2.card_button)
                screen.fill('black', pile_card3.card_button)
                screen.fill('black', pile_card4.card_button)
                screen.fill('black', pile_card5.card_button)
                player_card1.card_button.is_enabled = False
                player_card2.card_button.is_enabled = False
                player_card3.card_button.is_enabled = False
                player_card4.card_button.is_enabled = False
                player_card5.is_enabled = False
                pile_card1.card_button.is_enabled = False
                pile_card2.card_button.is_enabled = False
                pile_card3.card_button.is_enabled = False
                pile_card4.card_button.is_enabled = False
                pile_card5.card_button.is_enabled = False

                if len(AI_hand) == 5:
                    show_AI_card1 = Card(AI_hand[0], 490, 200, (200, 300), "1")
                    show_AI_card2 = Card(AI_hand[1], 710, 200, (200, 300), "2")
                    show_AI_card3 = Card(AI_hand[2], 930, 200, (200, 300), "3")
                    show_AI_card4 = Card(AI_hand[3], 1150, 200, (200, 300), "4")
                    show_AI_card5 = Card(AI_hand[4], 1370, 200, (200, 300), "5")  
                    show_AI_card1.draw()
                    show_AI_card2.draw()
                    show_AI_card3.draw()
                    show_AI_card4.draw()
                    show_AI_card5.draw()

                    AI_final_score = font.render(f"AI SCORE: {AI_cardnum_sum}", True, 'white')
                    AI_score_rect = AI_final_score.get_rect(center=(930, 410))
                elif len(AI_hand) == 4:
                    show_AI_card2 = Card(AI_hand[0], 710, 200, (200, 300), "2")
                    show_AI_card3 = Card(AI_hand[1], 930, 200, (200, 300), "3")
                    show_AI_card4 = Card(AI_hand[2], 1150, 200, (200, 300), "4")
                    show_AI_card5 = Card(AI_hand[3], 1370, 200, (200, 300), "5")  
                    show_AI_card2.draw()
                    show_AI_card3.draw()
                    show_AI_card4.draw()
                    show_AI_card5.draw()

                    AI_final_score = font.render(f"AI SCORE: {AI_cardnum_sum}", True, 'white')
                    AI_score_rect = AI_final_score.get_rect(center=(1040, 410))
                elif len(AI_hand) == 3:
                    show_AI_card3 = Card(AI_hand[0], 930, 200, (200, 300), "3")
                    show_AI_card4 = Card(AI_hand[1], 1150, 200, (200, 300), "4")
                    show_AI_card5 = Card(AI_hand[2], 1370, 200, (200, 300), "5")  
                    show_AI_card3.draw()
                    show_AI_card4.draw()
                    show_AI_card5.draw()      

                    AI_final_score = font.render(f"AI SCORE: {AI_cardnum_sum}", True, 'white')
                    AI_score_rect = AI_final_score.get_rect(center=(1150, 410))
                elif len(AI_hand) == 2:
                    show_AI_card4 = Card(AI_hand[0], 1150, 200, (200, 300), "4")
                    show_AI_card5 = Card(AI_hand[1], 1370, 200, (200, 300), "5")   
                    show_AI_card4.draw()
                    show_AI_card5.draw()

                    AI_final_score = font.render(f"AI SCORE: {AI_cardnum_sum}", True, 'white')
                    AI_score_rect = AI_final_score.get_rect(center=(1260, 410))
                elif len(AI_hand) == 1:
                    show_AI_card5 = Card(AI_hand[0], 1370, 200, (200, 300), "5")   
                    show_AI_card5.draw()

                    AI_final_score = font.render(f"AI SCORE: {AI_cardnum_sum}", True, 'white')
                    AI_score_rect = AI_final_score.get_rect(center=(1350, 410))

                if len(player_hand) == 5:
                    player_final_score = font.render(f"PLAYER SCORE: {player_cardnum_sum}", True, 'white')
                    player_score_rect = player_final_score.get_rect(center=(570, 550))  
                elif len(player_hand) == 4:
                    player_final_score = font.render(f"PLAYER SCORE: {player_cardnum_sum}", True, 'white')
                    player_score_rect = player_final_score.get_rect(center=(470, 550))    
                elif len(player_hand) == 3:
                    player_final_score = font.render(f"PLAYER SCORE: {player_cardnum_sum}", True, 'white')
                    player_score_rect = player_final_score.get_rect(center=(350, 550))    
                elif len(player_hand) == 2:
                    player_final_score = font.render(f"PLAYER SCORE: {player_cardnum_sum}", True, 'white')
                    player_score_rect = player_final_score.get_rect(center=(230, 550))                                            
                elif len(player_hand) == 1:
                    player_final_score = font.render(f"PLAYER SCORE: {player_cardnum_sum}", True, 'white')
                    player_score_rect = player_final_score.get_rect(center=(180, 550))

                screen.blit(player_final_score, player_score_rect)      
                screen.blit(AI_final_score, AI_score_rect)


                if AI_cardnum_sum >= 6:
                    player_wins = True
                    player_wins_reason = True
                elif player_cardnum_sum < AI_cardnum_sum:
                    player_wins = True
                    player_lower_score = True
                elif AI_cardnum_sum < player_cardnum_sum:
                    AI_wins = True
                    AI_lower_score = True
                elif player_cardnum_sum == AI_cardnum_sum and AI_show_card:
                    player_wins = True
                    player_match = True
                elif player_cardnum_sum == AI_cardnum_sum:
                    AI_wins = True
                    AI_match = True
            
            if player_wins:
                win_text = win_font.render("Player Wins!", True, 'white') 
                win_text_rect = win_text.get_rect(center=(1130, 550))

                screen.blit(win_text, win_text_rect)     

            if AI_wins:
                win_text = win_font.render("AI Wins!", True, 'white') 
                win_text_rect = win_text.get_rect(center=(1130, 550))

                screen.blit(win_text, win_text_rect)                      

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:            

                if player_card1.card_button.checkForInput(game_mouse_pos) and player_card1.card_button.is_enabled:
                    player_card1_selected = not player_card1_selected         

                if player_card2.card_button.checkForInput(game_mouse_pos) and player_card1.card_button.is_enabled:
                    player_card2_selected = not player_card2_selected

                if player_card3.card_button.checkForInput(game_mouse_pos) and player_card1.card_button.is_enabled:
                    player_card3_selected = not player_card3_selected 

                if player_card4.card_button.checkForInput(game_mouse_pos) and player_card1.card_button.is_enabled:
                    player_card4_selected = not player_card4_selected

                if player_card5.card_button.checkForInput(game_mouse_pos) and player_card1.card_button.is_enabled:
                    player_card5_selected = not player_card5_selected

                if pile_card1.card_button.checkForInput(game_mouse_pos) and pile_card1.card_button.is_enabled:
                    pile_card1_selected = not pile_card1_selected

                if pile_card2.card_button.checkForInput(game_mouse_pos) and pile_card2.card_button.is_enabled:
                    pile_card2_selected = not pile_card2_selected

                if pile_card3.card_button.checkForInput(game_mouse_pos) and pile_card3.card_button.is_enabled:
                    pile_card3_selected = not pile_card3_selected

                if pile_card4.card_button.checkForInput(game_mouse_pos) and pile_card4.card_button.is_enabled:
                    pile_card4_selected = not pile_card4_selected

                if pile_card5.card_button.checkForInput(game_mouse_pos) and pile_card5.card_button.is_enabled:
                    pile_card5_selected = not pile_card5_selected

                if confirm_card_button.checkForInput(game_mouse_pos):
                    get_pile_cardnum = True
                    get_pile_card = False
                    selected_card_confirm = True
                    draw_player_pile = True
                    get_player_cardnum = True
                    get_player_cardnumV2 = True
                    get_AI_cardnum = True
                    count_suit_num = True
                    remove_card1 = True
                    remove_card2 = True
                    remove_card3 = True
                    remove_card4 = True
                    remove_card5 = True               
                    
                if new_card_button.checkForInput(game_mouse_pos):
                    player_card1_selected = False
                    player_card2_selected = False
                    player_card3_selected = False
                    player_card4_selected = False
                    player_card5_selected = False
                    draw_player_pile = False
                    deal_new_card = True
                    player_new_card = True
                    get_player_cardnum = True
                    get_player_cardnumV2 = True
                    get_AI_cardnum = True
                    count_suit_num = True
                    AI_turn = True
                    remove_AI_cards = True
                    draw_AI_pile = True
                    get_pile_card = True
                if show_card_button.checkForInput(game_mouse_pos):
                    player_show_card = True

                

        pygame.display.update()




def Menu():
    is_running = True

    while is_running:
        
        menu_mouse_pos = pygame.mouse.get_pos()

        timer.tick(fps)

        ng_btn_surface = pygame.image.load("Images/Button images/GameButton.png")
        ng_btn_surface = pygame.transform.scale(ng_btn_surface, (500, 200))

        new_game_button = Button(ng_btn_surface, 760, 500, 'NEW GAME', 'black')

        new_game_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_button.checkForInput(menu_mouse_pos):
                    gameRunning()

        pygame.display.update()

            
Menu()