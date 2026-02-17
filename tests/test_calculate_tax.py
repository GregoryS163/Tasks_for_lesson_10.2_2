import pytest

from src.utils import calculate_tax


@pytest.mark.parametrize('price, tax_rate, expected_result', [
    (50, 7, 53.5),
    (100, 20, 120),
    (0, 22, 0),
])
def test_calculate_tax_basic(price, tax_rate, expected_result):
    assert calculate_tax(price, tax_rate) == expected_result


@pytest.mark.parametrize('price, tax_rate, discount, expected_result', [
    (50, 7, 7, 49.76),
    (100, 20, 10, 108),
    (0, 22, 0, 0),
    (181, 8.5, 10, 176.75)
])
def test_calculate_tax_with_discount(price, tax_rate, discount, expected_result):
    assert calculate_tax(price, tax_rate, discount=discount) == expected_result


@pytest.mark.parametrize('price, tax_rate, discount, round_price, expected_result', [
    (87, 4, 10, 1, 81.4),
    (50, 7, 7.5, 3, 49.487),
    (100, 20.55, 10.5, 4, 107.8923),
    (0, 22, 0, 1, 0),
    (181, 8.5, 10, 0, 177)
])
def test_calculate_tax_with_all_args(price, tax_rate, discount, round_price, expected_result):
    assert calculate_tax(price, tax_rate, discount=discount, round_price=round_price) == expected_result


def test_calculate_tax_invalid_negative_price():
    with pytest.raises(ValueError) as negative_price:
        calculate_tax(-11, 10)
    assert str(negative_price.value) == 'Неверная цена'


@pytest.mark.parametrize('price, tax_rate', [(200, -20),
                                             (200, 100),
                                             (30, 101),
                                             ])
def test_calculate_tax_invalid_invalid_tax_rate(price, tax_rate):
    with pytest.raises(ValueError) as invalid_tax_rate:
        calculate_tax(price, tax_rate)
    assert str(invalid_tax_rate.value) == 'Неверный налоговый процент'


@pytest.mark.parametrize('price, tax_rate, discount, round_price', [('87', 4, 10, 1),
                                                                    (50, [7], 7.5, 3),
                                                                    (100, 20.55, (10.5,), 4),
                                                                    (0, 22, 0, '0'),
                                                                    ])
def test_calculate_tax_invalid_type_args(price, tax_rate, discount, round_price):
    with pytest.raises(TypeError) as invalid_type:
        calculate_tax(price, tax_rate, discount=discount, round_price=round_price)
    assert str(invalid_type.value) == 'Ошибка типа данных'


def test_calculate_tax_invalid_kwargs():
    with pytest.raises(TypeError):
        calculate_tax(100, 10, 20, 3)
