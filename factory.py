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

class PizzaFactory:
    def createPizza(self, pizza_kind):
        if pizza_kind == "cheese":
            return CheesePizza()
        elif pizza_kind == "pepperoni":
            return PepperoniPizza()
        


pizza_factory = PizzaFactory()
pizza= pizza_factory.createPizza("pepperoni")
pizza.preparation()
