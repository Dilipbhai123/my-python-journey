# delivery order system Bike Ryder and Bicycle
class DeliveryPartner:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_payout(self, total_orders):
        print(f"[LOG] : {self.name} નો પગાર ગણાઈ રહ્યો છે .......")
        self.payout = self.base_salary + (total_orders * 20)
        return self.payout

# delivery order system BicyclePartner class
class BicyclePartner(DeliveryPartner):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

    def calculate_payout(self, total_orders):
        print(f"[LOG] : {self.name} નો પગાર ગણાઈ રહ્યો છે .......")
        self.payout = self.base_salary + (total_orders * 35)
        return self.payout

# delivery order system BikePartner class
class BikePartner(DeliveryPartner):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

    def calculate_payout(self, total_orders):
        return super().calculate_payout(total_orders) + 200

#assign object for BicyclePartner and BikePartner
p1 = BicyclePartner("રામભાઇ", 5000)
p2 = BikePartner("શ્યામભાઈ", 8000)

# Function print_salary_slip for handel BikePartner and BicyclePartner class hendal
def print_salary_slip(partner_object, orders):
    salary_ryder = partner_object.calculate_payout(orders)

    print(f"{salary_ryder}")

print_salary_slip(p1, 25)
print_salary_slip(p2, 35)