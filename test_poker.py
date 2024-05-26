import pytest

import poker


@pytest.mark.parametrize(
    'hand,is_match',
    [
        (('TC', 'JC', 'QC', 'KC', 'AC'), True),
        (('TD', 'JD', 'QD', 'KD', 'AD'), True),
        (('TH', 'JH', 'QH', 'KH', 'AH'), True),
        (('TS', 'JS', 'QS', 'KS', 'AS'), True),
        (('TC', 'JD', 'QH', 'KS', 'AC'), False),
        (('9D', 'JD', 'QD', 'KD', 'AD'), False),
        (('2C', '8C', 'JC', '4D', '2H'), False),
    ],
)
def test_is_royal_flush(hand, is_match):
    if is_match:
        assert poker.is_royal_flush(hand)
    else:
        assert not poker.is_royal_flush(hand)


@pytest.mark.parametrize(
    'hand,is_match',
    [
        (('2C', '3C', '4C', '5C', '6C'), True),
        (('8D', '9D', 'TD', 'JD', 'QD'), True),
        (('9S', 'TS', 'JS', 'QS', 'KS'), True),
        (('3H', '4H', '5H', '6H', '7H'), True),
        (('5C', '9D', '9H', '9S', 'AC'), False),
        (('9D', 'JD', 'QD', 'KD', 'AD'), False),
        (('2C', '8C', 'JC', '4D', '2H'), False),
    ],
)
def test_is_straight_flush(hand, is_match):
    if is_match:
        assert poker.is_straight_flush(hand)
    else:
        assert not poker.is_straight_flush(hand)


@pytest.mark.parametrize(
    'hand,is_match',
    [
        (('2C', '5D', '3H', '3S', '6S'), False),
        (('9C', '9D', 'KD', '6H', 'JS'), False),
        (('6C', '6D', '6H', '9H', '6S'), True),
        (('AC', 'AD', 'AH', 'AS', '2D'), True),
    ],
)
def test_is_four_of_a_kind(hand, is_match):
    if is_match:
        assert poker.is_four_of_a_kind(hand)
    else:
        assert not poker.is_four_of_a_kind(hand)


@pytest.mark.parametrize(
    'hand,is_match',
    [
        (('2C', '2C', '3H', '3C', '3S'), True),
        (('AS', 'AD', 'KH', 'KS', 'KD'), True),
        (('9C', '9D', 'KD', '6H', 'JS'), False),
        (('6C', '6D', '6H', '9H', '6S'), False),
        (('2C', '3C', '4C', '5C', '6D'), False),
    ],
)
def test_is_full_house(hand, is_match):
    if is_match:
        assert poker.is_full_house(hand)
    else:
        assert not poker.is_full_house(hand)


@pytest.mark.parametrize(
    'hand,is_match',
    [
        (('2C', '2C', '3H', '3C', '3S'), False),
        (('9C', '9D', 'KD', '6H', 'JS'), False),
        (('AD', '2D', '7D', '9D', 'JS'), False),
        (('AS', '2S', '7S', '9S', 'JS'), True),
    ],
)
def test_is_flush(hand, is_match):
    if is_match:
        assert poker.is_flush(hand)
    else:
        assert not poker.is_flush(hand)


@pytest.mark.parametrize(
    'hand,is_match',
    [
        (('2C', '3C', '4H', '5C', '3S'), False),
        (('TS', 'JS', 'KD', 'QS', '2S'), False),
        (('4S', '5S', '6D', '7S', '8S'), True),
        (('6S', '9S', '8D', '7S', 'TS'), True),
    ],
)
def test_is_straight(hand, is_match):
    if is_match:
        assert poker.is_straight(hand)
    else:
        assert not poker.is_straight(hand)


@pytest.mark.parametrize(
    'hand,is_match',
    [
        (('4S', '5S', '6D', '7S', '8S'), False),
        (('2C', '2D', '2H', '5C', '3S'), True),
        (('6C', '5S', '2H', '5C', '5S'), True),
    ],
)
def test_is_three_of_a_kind(hand, is_match):
    if is_match:
        assert poker.is_three_of_a_kind(hand)
    else:
        assert not poker.is_three_of_a_kind(hand)


@pytest.mark.parametrize(
    'hand,is_match',
    [
        (('JD', '6H', 'TH', 'AH', '7S'), False),
        (('4D', 'AD', '9H', 'TH', 'JS'), False),
        (('4C', '3D', '8D', '5H', '4S'), False),
        (('8C', 'AC', '3H', '8H', '3S'), True),
        (('2D', 'JD', 'KH', 'JS', 'KS'), True),
    ],
)
def test_is_two_pair(hand, is_match):
    if is_match:
        assert poker.is_two_pair(hand)
    else:
        assert not poker.is_two_pair(hand)


@pytest.mark.parametrize(
    'hand,is_match',
    [
        (('5C', 'AC', 'KD', '2H', 'TH'), False),
        (('3D', 'TD', 'QD', '7S', 'AS'), False),
        (('3C', '6C', '8H', '3S', 'AS'), True),
        (('6H', '7H', '8H', '8S', '9S'), True),
    ],
)
def test_is_pair(hand, is_match):
    if is_match:
        assert poker.is_pair(hand)
    else:
        assert not poker.is_pair(hand)
