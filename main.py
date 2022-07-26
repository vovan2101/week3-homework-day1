class Animal:
    
    def __init__(self, name, energy=100):
        self.name = name
        self.energy = energy
        
    def eat (self, eat_food):
        energy_increase = eat_food + 20
        self.energy += energy_increase
        print(f"{self.name} eat a lot of food. Now he has {self.energy} energy")
    
    def sleep(self, go_sleep):
        energy_increase_2 = go_sleep + 50
        self.energy += energy_increase_2
        print(f"{self.name} was sleep for all night. Now he has {self.energy} energy")
        
    def play(self, go_play):
        energy_decrease = go_play - 50
        self.energy -= energy_decrease
        print(f"{self.name} was playing for all day. Now he has {self.energy} energy")
    
bird = Animal("Buddy")
bird.eat(0)
bird.sleep(0)
bird.play(0)

        