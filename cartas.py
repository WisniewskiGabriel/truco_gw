import copy
from math import floor
import random

# valores iniciais
initial_card = 1
naipe_range = [0, 1, 2, 3]
final_card = 12.3
forbidden_range = [8.0, 9.9]
max_hand_len = 3
card_count_threshold = 40


# instancia um 'baralho'
def make_cards():

    cards_list: list = []
    current_card = copy.copy(initial_card)

    while current_card < final_card:
        for naipe in naipe_range:
            card_str = (str(current_card)) + '.' +(str(naipe))
            if not (forbidden_range[0] <= current_card <= forbidden_range[1]):
                cards_list.append(float(card_str))
        current_card += 1
    return cards_list


# checagem para garantir que as cartas estejam em ordem crescente
def make_sure_cards_are_ordinal(cards:list):

    for card in cards:
        value = copy.copy(card)
        if card > value:
            continue
        else:
            raise "A ordem do baralho foi comprometida."


# a partir da info. da carta virada pegar list de manilhas
def get_jokers(starter_card: float, cards: list):

    index = cards.index(starter_card)
    index = index + len(naipe_range)

    if index >= len(cards):
        index -= len(cards)

    lower_joker = floor(cards[index])
    jokers = []

    for naipe in naipe_range:
        jokers.append(float(f'{str(lower_joker)}.{naipe}'))

    return jokers


# pegar 3 cartas aleatorias, importante passar a list de cartas na mesa
def get_hand_of_cards(cards: list, taken_cards: list):

    cards = [item for item in cards if item not in taken_cards]
    hand = []

    for idx in range(max_hand_len):

        random_idx = random.randint(a=0, b=len(cards))
        card = cards[random_idx]
        cards.remove(card)
        hand.append(card)

    return hand


def get_winner_card(cards_in_table: list, cards: list, jokers: list):

    table_has_jokers: bool = len([item for item in jokers if item not in cards_in_table]) > 0


print(get_winner_card(cards_in_table=[1.3, 3.1, 12.2, 10.2]))










