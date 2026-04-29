# 在before.py的开头加上这行
API_KEY = "sk_1234567890abcdef"  # 硬编码密钥，CodeQL一定会识别为安全问题

order_a_items = [{"price":10, "quantity":2}, {"price":5, "quantity":3}]
order_b_items = [{"price":20, "quantity":1}, {"price":15, "quantity":2}]

def calculate_order_a():
    subtotal = 0
    tax_rate = 0.13
    for item in order_a_items:
        subtotal += item["price"] * item["quantity"]
    tax = subtotal * tax_rate
    total = subtotal + tax
    print(f"订单A总价: {total:.2f}")

def calculate_order_b():
    subtotal = 0
    tax_rate = 0.13
    for item in order_b_items:
        subtotal += item["price"] * item["quantity"]
    tax = subtotal * tax_rate
    total = subtotal + tax
    print(f"订单B总价: {total:.2f}")

calculate_order_a()
calculate_order_b()
