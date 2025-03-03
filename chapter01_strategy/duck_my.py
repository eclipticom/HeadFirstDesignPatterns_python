
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

#region Fly Behaviour
class FlyBehaviour(ABC):
    
    @abstractmethod
    def fly(self):
        pass

    def __str__(self):
        return "FlyBehaviour(ABC)"

class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("I'm flying with wings!!")   

    def __str__(self):
        return f"{super().__str__()} --> FlyWithWings(FlyBehaviour)"
    

class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("I can't fly")

    def __str__(self):
        return f"{super().__str__()} --> FlyNoWay(FlyBehaviour)"        

class FlyRocketPowered(FlyBehaviour):
    def fly(self):
        print("I can fly with rockets")

    def __str__(self):
        return f"{super().__str__()} --> FlyRocketPowered(FlyBehaviour)"        

#endregion

#region Quack Behaviour
class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

    def __str__(self):
        return "QuackBehavior(ABC)"    

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

    def __str__(self):
        return f"{super().__str__()} --> Quack(QuackBehavior)"
    
class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")

    def __str__(self):
        return f"{super().__str__()} --> MuteQuack(QuackBehavior)"

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")    

    def __str__(self):
        return f"{super().__str__()} --> Squeak(QuackBehavior)"

#endregion

#region Duck
class Duck(ABC):
    _fly_behavior = None
    _quack_behavior = None

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior):
        self._fly_behavior = fly_behavior

    def perform_fly(self):
        self.fly_behavior.fly()


    @property
    def quack_behavior(self):
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior):
        self._quack_behavior = quack_behavior


    def perform_fly(self):
        self.fly_behavior.fly()       

    def perform_quack(self):
        self.quack_behavior.quack()

    @abstractmethod
    def display(self):
        pass
      
    # common methods
    def swim(self):
        print("All ducks float, even decoys!")


@dataclass
class MallardDuck(Duck):

    _fly_behavior: FlyBehaviour = field(default=FlyWithWings())
    _quack_behavior: QuackBehavior = field(default=Quack())

    def display(self):
        print("I'm a Mallard Duck")

    def __str__(self):
        return f"Mallard Duck"


@dataclass
class RubberDuck(Duck):
    _fly_behavior: FlyBehaviour = field(default=FlyNoWay())
    _quack_behavior: QuackBehavior = field(default=Squeak())

    def display(self):
        print("I'm a rubber duckie")

    def __str__(self):
        return f"Rubber Duck"        

@dataclass
class DecoyDuck(Duck):
    _fly_behavior: FlyBehaviour = field(default=FlyNoWay())
    _quack_behavior: QuackBehavior = field(default=MuteQuack())

    def display(self):
        print("I'm a duck Decoy")

    def __str__(self):
        return f"Decoy Duck"

@dataclass
class ModelDuck(Duck):
    _fly_behavior: FlyBehaviour = field(default=FlyNoWay())
    _quack_behavior: QuackBehavior = field(default=Squeak())

    def display(self):
        print("I'm a real Mallard duck")

    def __str__(self):
        return f"Model Duck"        

@dataclass
class RedHeadDuck(Duck):
    _fly_behavior: FlyBehaviour = field(default=FlyWithWings())
    _quack_behavior: QuackBehavior = field(default=Quack())

    def display(self):
        print("I'm a real Red Headed duck")

    def __str__(self):
        return f"RedHead Duck"
#endregion
        

def mini_duck_simulator():
    mallard = MallardDuck()
    print(mallard)
    mallard.perform_quack()
    mallard.perform_fly()
    print()

    model = ModelDuck()
    print(model)
    model.perform_fly()
    model.fly_behavior = FlyRocketPowered()
    model.perform_fly()        
        

if __name__ == '__main__':
    mini_duck_simulator()