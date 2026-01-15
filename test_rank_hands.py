from card import Card, Rank, Suit
from rank_hands import HandRanks, evaluate_hand, get_best_hand

def test_royal_flush():
    hand = [
        Card(Rank.TEN, Suit.HEARTS),
        Card(Rank.JACK, Suit.HEARTS),
        Card(Rank.QUEEN, Suit.HEARTS),
        Card(Rank.KING, Suit.HEARTS),
        Card(Rank.ACE, Suit.HEARTS),
    ]

    assert evaluate_hand(hand) == HandRanks.ROYAL_FLUSH


def test_straight_flush():
    hand = [
        Card(Rank.NINE, Suit.SPADES),
        Card(Rank.EIGHT, Suit.SPADES),
        Card(Rank.SEVEN, Suit.SPADES),
        Card(Rank.SIX, Suit.SPADES),
        Card(Rank.FIVE, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.STRAIGHT_FLUSH


def test_four_of_a_kind():
    hand = [
        Card(Rank.ACE, Suit.SPADES),
        Card(Rank.ACE, Suit.HEARTS),
        Card(Rank.ACE, Suit.DIAMONDS),
        Card(Rank.ACE, Suit.CLUBS),
        Card(Rank.KING, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.FOUR_OF_A_KIND


def test_full_house():
    hand = [
        Card(Rank.QUEEN, Suit.SPADES),
        Card(Rank.QUEEN, Suit.HEARTS),
        Card(Rank.QUEEN, Suit.CLUBS),
        Card(Rank.TEN, Suit.SPADES),
        Card(Rank.TEN, Suit.HEARTS),
    ]

    assert evaluate_hand(hand) == HandRanks.FULL_HOUSE


def test_flush():
    hand = [
        Card(Rank.ACE, Suit.CLUBS),
        Card(Rank.JACK, Suit.CLUBS),
        Card(Rank.NINE, Suit.CLUBS),
        Card(Rank.FIVE, Suit.CLUBS),
        Card(Rank.TWO, Suit.CLUBS),
    ]

    assert evaluate_hand(hand) == HandRanks.FLUSH


def test_straight_with_low_ace():
    hand = [
        Card(Rank.ACE, Suit.SPADES),
        Card(Rank.TWO, Suit.HEARTS),
        Card(Rank.THREE, Suit.DIAMONDS),
        Card(Rank.FOUR, Suit.CLUBS),
        Card(Rank.FIVE, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.STRAIGHT


def test_three_of_a_kind():
    hand = [
        Card(Rank.SEVEN, Suit.SPADES),
        Card(Rank.SEVEN, Suit.HEARTS),
        Card(Rank.SEVEN, Suit.DIAMONDS),
        Card(Rank.KING, Suit.CLUBS),
        Card(Rank.TWO, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.THREE_OF_A_KIND


def test_two_pair():
    hand = [
        Card(Rank.JACK, Suit.SPADES),
        Card(Rank.JACK, Suit.HEARTS),
        Card(Rank.FOUR, Suit.DIAMONDS),
        Card(Rank.FOUR, Suit.CLUBS),
        Card(Rank.NINE, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.TWO_PAIR


def test_one_pair():
    hand = [
        Card(Rank.KING, Suit.SPADES),
        Card(Rank.KING, Suit.HEARTS),
        Card(Rank.TEN, Suit.DIAMONDS),
        Card(Rank.FIVE, Suit.CLUBS),
        Card(Rank.TWO, Suit.SPADES),
    ]

    assert evaluate_hand(hand) == HandRanks.ONE_PAIR


def test_high_card():
    hand = [
        Card(Rank.ACE, Suit.SPADES),
        Card(Rank.JACK, Suit.HEARTS),
        Card(Rank.NINE, Suit.DIAMONDS),
        Card(Rank.FIVE, Suit.CLUBS),
        Card(Rank.THREE, Suit.SPADES),
    ]
    assert evaluate_hand(hand) == HandRanks.HIGH_CARD


def test_get_best_hand_best_of_seven():
    hand = [
        Card(Rank.ACE, Suit.HEARTS),
        Card(Rank.KING, Suit.HEARTS),
        Card(Rank.QUEEN, Suit.HEARTS),
        Card(Rank.JACK, Suit.HEARTS),
        Card(Rank.TEN, Suit.HEARTS),
        Card(Rank.TWO, Suit.CLUBS),
        Card(Rank.THREE, Suit.DIAMONDS),
    ]

    assert get_best_hand(hand) == HandRanks.ROYAL_FLUSH
