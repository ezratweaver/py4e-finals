class Category():
    
    def __init__(self, category_name):
        self.category_name = category_name
        self.balance = 0
        self.ledger = []

    def __str__(self):
        stars = "*" * round((30 - len(self.category_name)) / 2)
        title_string = f"{stars}{self.category_name}{stars}\n"
        class_display = title_string
        for action in self.ledger:
            display_amount = format(action["amount"], ".2f")
            display_amount = display_amount[:7]
            spliced_description = action["description"][:23]
            white_space = " " * (30 - (len(spliced_description) + len(display_amount)))
            ledger_line = f"{spliced_description}{white_space}{display_amount}\n"
            class_display = class_display + ledger_line
        total_number = format(self.balance, ".2f")
        total_line = f"Total: {total_number}"
        return class_display + total_line


    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True

    def deposit(self, amount, description=""):
        self.balance = self.balance + amount
        self.ledger.append({"amount": amount, "description" : description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance = self.balance - amount
            self.ledger.append({"amount": amount * -1, "description" : description})
            return True
        return False
    
    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.category_name}"):
            category.deposit(amount, f"Transfer from {self.category_name}")
            return True
        return False

    def get_balance(self):
        return self.balance



def create_spend_chart(categories):
    amount_spent = []
    category_names = []

    for category in categories:
        total_spent = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                total_spent += round(abs(transaction["amount"]))
        amount_spent.append(total_spent)
        category_names.append(category.category_name)

    percentages = [(amount / sum(amount_spent) * 100) // 10 * 10 for amount in amount_spent]

    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_name_length = max(len(name) for name in category_names)

    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i != max_name_length - 1:
            chart += "\n"

    return chart
