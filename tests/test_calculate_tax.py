import pytest

from src.utils import calculate_tax


@pytest.mark.parametrize('price, tax_rate, expected_result', [
    (50, 10, 55.0),
    (100, 20, 120.0),
    (0, 22, 0)
])
def test_calculate_tax_basic(price, tax_rate, expected_result):
    assert calculate_tax(price, tax_rate) == expected_result


def test_calculate_tax_invalid_args():
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
