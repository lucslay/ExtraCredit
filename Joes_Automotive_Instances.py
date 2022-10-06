import Joes_Automotive_Shop as joes

customer1 = joes.Customer("Lucas Layton", "3344 S 2nd St", "2145054470")
customer1 = joes.Customer("Lucas Layton", "3344 S 2nd St", "2145054470")

car1 = joes.Car("Jeep", "Wrangler", 2010)
car2 = joes.Car("Mazda", "cx5", 2020)

quote = joes.ServiceQuote(10000, 30000)
print(quote.get_labor_charges())
print(quote.get_parts_charges())


