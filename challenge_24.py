class NetflixPlan:
    def __init__(self,plan_name,price):
        self.plan_name = plan_name
        self.__price = price

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"🍿 પ્લાન: {self.plan_name} | કિંમત: ₹{self.__price}"

    def __add__(self, other):
        all_plan = self.__price + other.price
        return NetflixPlan("Combo Plan", all_plan)

plan1 = NetflixPlan("Mobile Screen", 199)
plan2 = NetflixPlan("4K TV Screen", 649)

print(plan1)
print(plan2)

Combo_Plan = plan1 + plan2

print(Combo_Plan)