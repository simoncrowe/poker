import pytest

import jacks_or_better


@pytest.mark.parametrize(
    'hand,is_match',
    [
        (('9D', 'JD', 'AD', '3H', 'AH'), True),
        (('AC', '5D', '8D', 'KD', 'KS'), True),
        (('QC', '4D', '5D', 'QD', '4S'), True),
        (('JH', 'JD', '6D', 'AH', '7S'), True),
        (('3C', '6C', 'QC', '3H', '7S'), False),
        (('2C', '8D', '4S', '5S', '7S'), False),
        (('3C', '9D', 'AD', '4H', '2S'), False),
        (('TS', '4H', '5H', '6H', 'TH'), False),
    ],
)
def test_is_pair_jacks_or_better(hand, is_match):
    if is_match:
        assert jacks_or_better.is_pair(hand)
    else:
        assert not jacks_or_better.is_pair(hand)
