def format_price(price):
	price = int(price)
	return (str('Price:') + str(price) + str(' rub'))

display_price = format_price(56.24)
print(display_price)