def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


def calculate_tax(price: float, tax_rate: float, discount=0, round_cost=2) -> float:
    if not isinstance(price, int | float) or not isinstance(tax_rate, int | float):
        raise TypeError('неверный тип аргумента')
    elif price < 0:
        raise ValueError('Неверная цена')

    elif tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')

    else:
        taxed_price = price + (price * tax_rate / 100)
        discount_price = taxed_price - (taxed_price * discount / 100)
        return round(discount_price, round_cost)
