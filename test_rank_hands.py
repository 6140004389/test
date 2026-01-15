import pytest

from card import Card, Rank, Suit
from rank_hands import HandRanks, evaluate_hand, get_best_hand


def c(rank: Rank, suit: Suit):
    return Card(rank=rank, suit=suit)


def test_royal_flush():
    hand = [
        c(Rank.TEN, Suit.HEARTS),
        c(Rank.JACK, Suit.HEARTS),
        c(Rank.QUEEN, Suit.HEARTS),
        c(Rank.KING, Suit.HEARTS),
        c(Rank.ACE, Suit.HEARTS),
    ]

    assert evaluate_hand(hand) == HandRanks.ROYAL_FLUSH


def test_straight_flush():
    hand = [
        c(Rank.NINE, Suit.SPADES),
        c(Rank.EIGHT, Suit.SPADES),
        c(Rank.SEVEN, Suit.SPADES),
        c(Rank.SIX, Suit.SPADES),
        c(Rank.FIVE, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.STRAIGHT_FLUSH


def test_four_of_a_kind():
    hand = [
        c(Rank.ACE, Suit.SPADES),
        c(Rank.ACE, Suit.HEARTS),
        c(Rank.ACE, Suit.DIAMONDS),
        c(Rank.ACE, Suit.CLUBS),
        c(Rank.KING, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.FOUR_OF_A_KIND


def test_full_house():
    hand = [
        c(Rank.QUEEN, Suit.SPADES),
        c(Rank.QUEEN, Suit.HEARTS),
        c(Rank.QUEEN, Suit.CLUBS),
        c(Rank.TEN, Suit.SPADES),
        c(Rank.TEN, Suit.HEARTS),
    ]

    assert evaluate_hand(hand) == HandRanks.FULL_HOUSE


def test_flush():
    hand = [
        c(Rank.ACE, Suit.CLUBS),
        c(Rank.JACK, Suit.CLUBS),
        c(Rank.NINE, Suit.CLUBS),
        c(Rank.FIVE, Suit.CLUBS),
        c(Rank.TWO, Suit.CLUBS),
    ]

    assert evaluate_hand(hand) == HandRanks.FLUSH


def test_straight_with_low_ace():
    hand = [
        c(Rank.ACE, Suit.SPADES),
        c(Rank.TWO, Suit.HEARTS),
        c(Rank.THREE, Suit.DIAMONDS),
        c(Rank.FOUR, Suit.CLUBS),
        c(Rank.FIVE, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.STRAIGHT


def test_three_of_a_kind():
    hand = [
        c(Rank.SEVEN, Suit.SPADES),
        c(Rank.SEVEN, Suit.HEARTS),
        c(Rank.SEVEN, Suit.DIAMONDS),
        c(Rank.KING, Suit.CLUBS),
        c(Rank.TWO, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.THREE_OF_A_KIND


def test_two_pair():
    hand = [
        c(Rank.JACK, Suit.SPADES),
        c(Rank.JACK, Suit.HEARTS),
        c(Rank.FOUR, Suit.DIAMONDS),
        c(Rank.FOUR, Suit.CLUBS),
        c(Rank.NINE, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.TWO_PAIR


def test_one_pair():
    hand = [
        c(Rank.KING, Suit.SPADES),
        c(Rank.KING, Suit.HEARTS),
        c(Rank.TEN, Suit.DIAMONDS),
        c(Rank.FIVE, Suit.CLUBS),
        c(Rank.TWO, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.ONE_PAIR


def test_high_card():
    hand = [
        c(Rank.ACE, Suit.SPADES),
        c(Rank.JACK, Suit.HEARTS),
        c(Rank.NINE, Suit.DIAMONDS),
        c(Rank.FIVE, Suit.CLUBS),
        c(Rank.THREE, Suit.SPADES),
    ]
    assert evaluate_hand(hand) == HandRanks.HIGH_CARD


def test_get_best_hand_best_of_seven():
    hand = [
        c(Rank.ACE, Suit.HEARTS),
        c(Rank.KING, Suit.HEARTS),
        c(Rank.QUEEN, Suit.HEARTS),
        c(Rank.JACK, Suit.HEARTS),
        c(Rank.TEN, Suit.HEARTS),
        c(Rank.TWO, Suit.CLUBS),
        c(Rank.THREE, Suit.DIAMONDS),
    ]

    assert get_best_hand(hand) == HandRanks.ROYAL_FLUSH
