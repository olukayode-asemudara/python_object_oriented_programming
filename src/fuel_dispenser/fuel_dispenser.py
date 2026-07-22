from transactions import Fuel, Transaction

class DispenserSystem:
    def __init__(self):
        self.fuel_menu = [
            Fuel("Petrol", 650),
            Fuel("Diesel", 720),
            Fuel("Kerosene", 550),
            Fuel("Gas", 480)
        ]
        self.transaction_history = []

    def start_system(self):
        while True:
            print("\nWelcome to GBeda Station!")
            print("Available petroleum")
            print("1. Buy Petroleum")
            print("2. Show Transaction History")

            operation_choice = input("Enter operation: ").strip()

            if operation_choice == "1":
                self.handle_purchase()
            elif operation_choice == "2":
                self.show_all_history()
            else:
                print("Invalid option! Please enter 1 or 2.")

    def handle_purchase(self):
        print("\nAvailable petroleum")
        for index, fuel in enumerate(self.fuel_menu):
            print(f"{index + 1}. {fuel.name:<10} {fuel.price_per_liter}/Liter")

        try:
            fuel_choice_index = int(input("Enter operation: ")) - 1
            if fuel_choice_index < 0 or fuel_choice_index >= len(self.fuel_menu):
                print("Invalid fuel selection!")
                return
        except ValueError:
            print("Please enter a valid number!")
            return

        selected_fuel = self.fuel_menu[fuel_choice_index]
        mode_choice = input("Liter or Amount: ").strip().lower()

        final_liters = 0.0
        final_amount = 0.0


        if mode_choice == "liter":
            while True:
                try:
                    input_liters = float(input(
                        f"How Many Liters of {selected_fuel.name.lower()} are you buying (${selected_fuel.price_per_liter}/L): "))

                    if 1 <= input_liters <= 50:
                        final_liters = input_liters
                        final_amount = input_liters * selected_fuel.price_per_liter
                        break
                    else:
                        print("Liters must be between 1-50 !!!")
                except ValueError:
                    print("Please enter a numeric value.")


        elif mode_choice == "amount":
            while True:
                try:
                    input_amount = float(input("Enter the amount of money you want to spend: "))

                    if input_amount >= selected_fuel.price_per_liter:
                        final_amount = input_amount
                        final_liters = input_amount / selected_fuel.price_per_liter
                        break
                    else:
                        print("Amount must be above a liter price !!!")
                except ValueError:
                    print("Please enter a numeric value.")
        else:
            print("Invalid purchase mode selected!")
            return


        print("\nCustomers Transaction Receipt")
        new_receipt = Transaction(selected_fuel.name, final_amount, final_liters)
        new_receipt.display_receipt()

        print("Saving Transaction History. . . . . .")
        self.transaction_history.append(new_receipt)

    def show_all_history(self):
        print("\nAll Transactions")
        if not self.transaction_history:
            print("No transactions recorded yet.")
        else:
            for receipt in self.transaction_history:
                receipt.display_receipt()