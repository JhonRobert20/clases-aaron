class Cat:
    "This class create cats"

    def __init__(self, name: str, size: int, color: str, sex: str):
        self.name = name
        self.size = size
        self.color = color
        self.sex = sex
        self.age = 0
        self.welfare = 100
    
    def __str__(self):
        return f"{self.name} has born with a size of {self.size} cm and is a {self.sex}"

    def meow(self):
        print("Meeeow!")     
    
    def assign_welfare(self, value: int, is_adding: bool):
        if is_adding:
            self.welfare += value
            if self.welfare > 100:
                self.welfare = 100

        else:
            self.welfare -= value
            if self.welfare < 0:
                self.welfare = 0

        if self.welfare <= 50:
            self.meow()


    def sleep(self):
        # if self.welfare < 100  :
        #     self.welfare += 20
        #     if self.welfare > 100:
        #         self.welfare = 100
        
        self.assign_welfare(20, True)

        print(f"{self.name} is sleeping")
    
    def play(self):
        self.assign_welfare(30, True)
            
        print(f"{self.name} is playing")
    
    def get_bored(self):
        self.assign_welfare(60, False)

        print(f"{self.name} is boring")

hercules = Cat("Hercules", 5, "Black", "M")

print(hercules)