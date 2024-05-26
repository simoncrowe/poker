"""Core poker and French deck model."""
import collections
import itertools

SUITS = 'CDHS'
VALUES = '23456789TJQKA'


def build_deck():
    return [val + suit for suit in SUITS for val in VALUES]


def iter_all_hands(count):
    return itertools.combinations(build_deck(), count)


def list_all_hands(count):
    return list(iter_all_hands(count))


def is_royal_flush(hand):
    if not is_flush(hand):
        return False

    hand_vals, _ = zip(*hand)
    return not set('TJQKA').difference(hand_vals)


def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)


def is_four_of_a_kind(hand):
    hand_values, _ = zip(*hand)
    value_counter = collections.Counter(sorted(hand_values))
    return max(value_counter.values()) == 4


def is_full_house(hand):
    hand_values, _ = zip(*hand)
    value_counter = collections.Counter(sorted(hand_values))
    return not {2, 3}.difference(value_counter.values())


def is_flush(hand):
    _, hand_suites = zip(*hand)
    suite_counter = collections.Counter(sorted(hand_suites))
    return max(suite_counter.values()) >= 5


def is_straight(hand):
    hand_vals, _ = zip(*hand)
    ranks = (VALUES.find(val) for val in hand_vals)

    contiguous_count = 0
    for a, b in itertools.pairwise(sorted(ranks)):
        diff = b - a

        if diff == 0:
            continue
        if diff == 1:
            contiguous_count += 1
        else:
            contiguous_count = 0

    return contiguous_count >= 4


def is_three_of_a_kind(hand):
    hand_values, _ = zip(*hand)
    value_counter = collections.Counter(sorted(hand_values))
    return max(value_counter.values()) == 3


def is_two_pair(hand):
    hand_values, _ = zip(*hand)
    values_counter = collections.Counter(sorted(hand_values))
    count_counter = collections.Counter(sorted(values_counter.values()))
    return count_counter.get(2) == 2


def is_pair(hand):
    hand_values, _ = zip(*hand)
    value_counter = collections.Counter(sorted(hand_values))
    return max(value_counter.values()) == 2
