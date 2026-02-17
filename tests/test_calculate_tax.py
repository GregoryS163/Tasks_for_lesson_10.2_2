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
    assert calculate_tax(price, tax_rate, discount) == expected_result


@pytest.mark.parametrize('price, tax_rate, discount, round_cost, expected_result', [
    (87, 4, 10, 1, 81.4),
    (50, 7, 7.5, 3, 49.487),
    (100, 20.55, 10.5, 4, 107.8923),
    (0, 22, 0, 1, 0),
    (181, 8.5, 10, 0, 177)
])
def test_calculate_tax_with_all_args(price, tax_rate, discount, round_cost, expected_result):
    assert calculate_tax(price, tax_rate, discount, round_cost) == expected_result


def test_calculate_tax_invalid_value_args():
    with pytest.raises(ValueError) as negative_price:
        calculate_tax(-11, 10)
    assert str(negative_price.value) == 'Неверная цена'

    with pytest.raises(ValueError) as negative_tax_rate:
        calculate_tax(200, -20)
    assert str(negative_tax_rate.value) == 'Неверный налоговый процент'

    with pytest.raises(ValueError) as tax_rate_equals_100:
        calculate_tax(200, 100)
    assert str(tax_rate_equals_100.value) == 'Неверный налоговый процент'

    with pytest.raises(ValueError) as tax_rate_more_100:
        calculate_tax(30, 101)
    assert str(tax_rate_more_100.value) == 'Неверный налоговый процент'


def test_calculate_tax_invalid_type_args():
    with pytest.raises(TypeError) as invalid_type:
        calculate_tax('120', 15)
    assert str(invalid_type.value) == 'неверный тип аргумента'

    with pytest.raises(TypeError) as invalid_type:
        calculate_tax(120, [12])
    assert str(invalid_type.value) == 'неверный тип аргумента'

    with pytest.raises(TypeError) as invalid_type:
        calculate_tax({}, 10)
    assert str(invalid_type.value) == 'неверный тип аргумента'

    with pytest.raises(TypeError) as invalid_type:
        calculate_tax('50', (10,))
    assert str(invalid_type.value) == 'неверный тип аргумента'

