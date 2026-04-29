order_a_items = [{"price":10, "quantity":2}, {"price":5, "quantity":3}]
order_b_items = [{"price":20, "quantity":1}, {"price":15, "quantity":2}]

# 把重复逻辑提取成通用函数
def calculate_order_total(items, order_name):
    subtotal = 0
    tax_rate = 0.13
    for item in items:
        subtotal += item["price"] * item["quantity"]
    tax = subtotal * tax_rate
    total = subtotal + tax
    print(f"{order_name}总价: {total:.2f}")

# 调用通用函数，消除重复代码
calculate_order_total(order_a_items, "订单A")
calculate_order_total(order_b_items, "订单B")
