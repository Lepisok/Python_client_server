import json


def write_order_to_json(item: str, quantity: int, price: float,
                        buyer: str, date: str) -> None:
    with open('data/orders.json', 'r', encoding='utf-8') as source:
        data = json.load(source)
    order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    data['orders'].append(order)
    with open('data/orders.json', 'w', encoding='utf-8') as target:
        json.dump(data, target, indent=4, ensure_ascii=False)


write_order_to_json('Компьютер ASUS', 1, 328_800.44, 'Иванов', '1980-12-03')
write_order_to_json('Клавиатура Thermaltake', 2, 15_999.00, 'Петров', '1980-12-03')
