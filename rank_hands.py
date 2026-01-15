from collections import Counter
from enum import Enum
from itertools import combinations
from typing import Sequence

from card import Card


class HandRanks(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9


def get_best_hand(hand: list[Card]):

    if len(hand) != 7:
        raise ValueError("Expected 7 cards")

    best_hand = HandRanks.HIGH_CARD

    for combo in combinations(hand, 5):
        rank = evaluate_hand(combo)
        if rank.value > best_hand.value:
            best_hand = rank

    return best_hand


def evaluate_hand(hand: Sequence[Card]):
    if len(hand) != 5:
        raise ValueError("Expected 5 cards")

    ranks = [card.rank.value for card in hand]
    suits = [card.suit for card in hand]

    rank_counts = Counter(ranks)
    counts = sorted(rank_counts.values(), reverse=True)

    is_flush = len(set(suits)) == 1
    is_straight = False

    sorted_ranks = sorted(ranks, reverse=True)

    if sorted_ranks == list(range(sorted_ranks[0], sorted_ranks[0] - 5, -1)):
        is_straight = True

    if sorted(ranks) == [2, 3, 4, 5, 14]:
        is_straight = True

    if is_straight and is_flush:
        return (
            HandRanks.ROYAL_FLUSH
            if sorted_ranks == [14, 13, 12, 11, 10]
            else HandRanks.STRAIGHT_FLUSH
        )

    if counts == [4, 1]:
        return HandRanks.FOUR_OF_A_KIND

    if counts == [3, 2]:
        return HandRanks.FULL_HOUSE

    if is_flush:
        return HandRanks.FLUSH

    if is_straight:
        return HandRanks.STRAIGHT

    if counts == [3, 1, 1]:
        return HandRanks.THREE_OF_A_KIND

    if counts == [2, 2, 1]:
        return HandRanks.TWO_PAIR

    if counts == [2, 1, 1, 1]:
        return HandRanks.ONE_PAIR

    return HandRanks.HIGH_CARD
