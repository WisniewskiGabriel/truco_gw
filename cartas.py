import copy
from math import floor
import random

# valores iniciais
initial_card = 1
naipe_range = [0, 1, 2, 3]
final_card = 12.3
forbidden_range = [8.0, 9.9]
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
    future_index = index + len(naipe_range)

    if future_index >= len(cards):
        future_index -= len(cards)

    lower_joker = floor(cards[future_index])
    jokers = []

    for naipe in naipe_range:
        jokers.append(float(f'{str(lower_joker)}.{naipe}'))

    return jokers


def get_hand_of_cards(cards: list, taken_cards: list):

    hand_len = 3









