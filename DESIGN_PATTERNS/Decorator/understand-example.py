from abc import ABC, abstractmethod

# Base interface for pizza
class BasePizza(ABC):
    @abstractmethod
    def cost(self) -> int:
        pass

# Concrete pizza implementations
class Farmhouse(BasePizza):
    def cost(self) -> int:
        return 200

class VegDelight(BasePizza):
    def cost(self) -> int:
        return 120

class Margheretta(BasePizza):
    def cost(self) -> int:
        return 100

# Base decorator class
class ToppingDecorator(BasePizza):
    def __init__(self, wrapped_pizza: BasePizza):
        self.wrapped_pizza = wrapped_pizza

    @abstractmethod
    def cost(self) -> int:
        pass

# Concrete decorators
class ExtraCheese(ToppingDecorator):
    def __init__(self, wrapped_pizza: BasePizza):
        super().__init__(wrapped_pizza)
    
    def cost(self) -> int:
        return self.wrapped_pizza.cost() + 10

class Mushrooms(ToppingDecorator):
    def __init__(self, wrapped_pizza: BasePizza):
        super().__init__(wrapped_pizza)
    
    def cost(self) -> int:
        return self.wrapped_pizza.cost() + 15

# Main Execution
if __name__ == '__main__':
    pizza = ExtraCheese(Margheretta())
    print(f"Cost of Margheretta with Extra Cheese: {pizza.cost()}")

    pizza = Mushrooms(ExtraCheese(Margheretta()))
    print(f"Cost of Margheretta with Extra Cheese and Mushrooms: {pizza.cost()}")
