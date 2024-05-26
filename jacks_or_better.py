import collections
import enum

import poker


class Hands(enum.Enum):
    ROYAL_FLUSH = 1
    STRAIGHT_FLUSH = 2
    FOUR_OF_KIND = 3
    FULL_HOUSE = 4
    FLUSH = 5
    STRAIGHT = 6
    THREE_OF_A_KIND = 7
    TWO_PAIR = 8
    PAIR_JACKS_OR_BETTER = 9
    


def is_pair(hand):
    """Jacks-or-better variant of is_pair"""
    hand_values, _ = zip(*hand)
    hand_ranks = sorted(poker.VALUES.find(val) for val in hand_values)
    rank_counter = collections.Counter(hand_ranks)

    for rank, count in rank_counter.items():
        if count == 2 and rank >= poker.VALUES.find("J"):
            return True

    return False


def rank_hand(hand):
    if poker.is_royal_flush(hand):
        return Hands.ROYAL_FLUSH.value
    elif poker.is_straight_flush(hand):
        return Hands.STRAIGHT_FLUSH.value
    elif poker.is_four_of_a_kind(hand):
        return Hands.FOUR_OF_KIND.value
    elif poker.is_full_house(hand):
        return Hands.FULL_HOUSE.value
    elif poker.is_flush(hand):
        return Hands.FLUSH.value
    elif poker.is_straight(hand):
        return Hands.STRAIGHT.value
    elif poker.is_three_of_a_kind(hand):
        return Hands.THREE_OF_A_KIND.value
    elif poker.is_two_pair(hand):
        return Hands.TWO_PAIR.value
    elif is_pair(hand):
        return Hands.PAIR_JACKS_OR_BETTER.value

    return 0
