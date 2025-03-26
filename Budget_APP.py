
class Category:
    def __init__(self, name):
        self.ledger =[] # transactions
        self.name = name # category name
        self.balance = 0.0
    def deposit(self,amount, description=""):
        self.ledger.append({'amount':amount, 'description': description})
        self.balance =self.balance + amount
    def withdraw(self,amount,description=""):
        
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance = self.balance - amount
            return True
        else: return False
    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {other.name}')
            other.deposit(amount,f'Transfer from {self.name}')
            return True
        else: return False
    def get_balance(self):
        return self.balance
    def check_funds(self,amount):
        if amount<= self.balance : return True
        else: return False
    def __str__(self):
        title = f'{self.name:*^30}\n'
        bill = ''
        for i in self.ledger:
            description = i['description'][:23]
            amount = f"{i['amount']:.2f}"
            bill += f"{description:<23}{amount:>7}\n"
        Total= f'Total: {self.balance:.2f}'
        return title + bill + Total


def create_spend_chart(categories):
    Title = "Percentage spent by category\n"
    withdrawals = []

    # Calculate total withdrawals for each category
    for category in categories:
        spent = abs(sum(item['amount'] for item in category.ledger if item['amount'] < 0))
        withdrawals.append(spent)

    total_amount = sum(withdrawals)

    # Ensure valid percentage calculation
    if total_amount == 0:
        total_perc = [0 for _ in categories]
    else:
        total_perc = [(spent / total_amount * 100) // 10 * 10 for spent in withdrawals]  # Always round down

    # Chart Bars
    for i in range(100, -1, -10):
        Title += f"{i:>3}| " + "".join("o  " if perc >= i else "   " for perc in total_perc) + "\n"

    # Separator Line
    Title += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category Names (Vertical)
    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        Title += "     "  # Left Padding
        for name in names:
            Title += (name[i] + "  ") if i < len(name) else "   "
        if i != max_length - 1:  # Avoid newline at the end
            Title += "\n"

    return Title









# food = Category('Food')
# food.deposit(1000, 'deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# print(food)
# print(create_spend_chart([food ,clothing]))
