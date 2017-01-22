# # EXCERCISE 5
import random

#########################
class Tables(object):

class Roulette(Tables):

    def minbet(self):
        self.minbet = random.choice([50,100,200])

class Craps(Tables):
    def minbet(self):
        self.minbet = random.choice([0,25,50])

##########################
class Employees(object):

class Croupiers(Employees):
     def __init__(self, fixed_wage):
            self.total_wage = fixed_wage

     def var_wage(self,profit):
            self.total_wage += 0.05*profit

###########################
class Barmen(Employees):
    def __init__(self, fixed_wage):
          self.total_wage = fixed_wage

    def tips(self, tips):
         self.total_wage += tips

#############################
class Customers(object):
    def drinks(self, budget):
        if budget >= 60 :
          self.drinks = random.choice([20,40])

    def tips(self,budget):
        if budget >= 60:
          self.tips = randint(0,20)
          return self.tips

class Returning(Customers):
    def budget(self, budget):
        self.budget = randint(100,300)
        return self.budget

    def bet(self, minbet, budget):
        if budget >= minbet :
            return minbet
        else:
            return 0


class one_time(Customers):
    def budget(self,budget):
        self.budget = randint(200, 300)
    def bet(self, budget):
        self.bet = randint(0, budget/3)

class bachelors(Customers):
    def budget(self, budget):
        self.budget = randint(200, 500)

    def total_budget(self,promotion):
        self.budget +=promotion

    def bet(self, minbet, budget):
        self.bet = randint(0, budget)
