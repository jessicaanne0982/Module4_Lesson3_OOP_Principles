# Encapsulation in Personal Budget Management

class BudgetCategory:
    def __init__(self, category_name, budget):
        self.__category_name = category_name
        self.__budget = budget
        self.__allocated_budget = budget
        
    # getter for allocated budget    
    def get_allocated_budget(self):
        return self.__allocated_budget
 
    # getter for category name
    def get_category_name(self):
        return self.__category_name
 
    # setter for category name
    def set_category_name(self, new_category):
        self.__category_name = new_category
 
    # getter for budget
    def get_budget(self):
      return self.__budget

    # setter for budget
    def set_budget(self, initial_budget):
        if initial_budget < 0:
            raise ValueError("Budget must be a positive number")
        self.__budget = initial_budget

    def add_expense(self, expense):
        if 0 < expense <= self.get_budget():
          self.set_budget(self.get_budget() - expense)
        else:
            print("Invalid expense amount or insufficient funds.")
 
    def display_category_summary(self):
        print(f"\nBudget Details: \nCategory Name - {self.get_category_name()}"
              f"\nAllocated budget - ${self.get_allocated_budget()}" 
              f"\nRemaining Balance after expenses - ${self.get_budget()}") 
 
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()