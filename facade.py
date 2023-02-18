class Pizza:
    def preparation(self):
        pass
    def baking(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass
class CheesePizza(Pizza):
    def preparation(self):
        print('Making chesse pizza')

class PepperoniPizza(Pizza):
    def preparation(self):
        print('Making pepperoni pizza')

class PizzaFacade:
    def __init__(self):
        self.cheesePizza = CheesePizza()
        self.pepperoniPizza = PepperoniPizza()

    def make_cheesePizza(self):
        self.cheesePizza.preparation()
        self.cheesePizza.baking()
        self.cheesePizza.cut()
        self.cheesePizza.box()

    def make_pepperoniPizza(self):
        self.pepperoniPizza.preparation()
        self.pepperoniPizza.baking()
        self.pepperoniPizza.cut()
        self.pepperoniPizza.box()

pizza_facade = PizzaFacade()
pizza_facade.make_pepperoniPizza()