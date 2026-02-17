import pytest

from src.utils import calculate_taxes


def test_calculate_taxes_basic(list_float):
    assert calculate_taxes(list_float, 10) == [110.0, 165.0, 22.55, 643.5]
    assert calculate_taxes(list_float, 0) == [100.0, 150.0, 20.5, 585.0]


def test_calculate_taxes_with_invalid_args(list_float):
    with pytest.raises(ValueError) as negative_rate:
        calculate_taxes(list_float, -5.0)
    assert str(negative_rate.value) == 'Неверный налоговый процент'

    with pytest.raises(ValueError) as negative_price:
        calculate_taxes([20.0, 55.5, -8.0], 5.0)
    assert str(negative_price.value) == 'Неверная цена'

    with pytest.raises(ValueError) as zero_price:
        calculate_taxes([20.0, 55.5, 0.0], 5.0)
    assert str(zero_price.value) == 'Неверная цена'


@pytest.mark.parametrize('prices, tax_rate, expected_result', [
    ([10.0, 15.0, 2.05, 58.5], 10.0, [11, 16.5, 2.255, 64.35]),
    ([], 5.0, []),
    ([100, 15, 50.5], 20.5, [120.5, 18.075, 60.8525])
])
def test_calculate_taxes(prices, tax_rate, expected_result):
    assert calculate_taxes(prices, tax_rate) == expected_result
