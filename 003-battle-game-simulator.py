import random


# Character class

class Character():
    baseline_health = 2
    baseline_luck = 0.2
    max_luck = 1.0

    def __init__(self, name: str, health_extra: int, luck_extra: float):
        self.name = name

        # Setting up the starting health parameters
        if health_extra < 0:
            raise ValueError("Extra health cannot be negative.")
        self.__health_extra = health_extra
        self.__max_health = Character.baseline_health + health_extra
        self.__current_health = self.__max_health

        # Setting up the starting luck parameters
        if luck_extra < 0 or (Character.baseline_luck + luck_extra) > Character.max_luck:
            raise ValueError(f"Luck must be between {Character.baseline_luck} and {Character.max_luck}")
        self.__luck_extra = luck_extra
        self.__starting_luck = Character.baseline_luck + luck_extra
        self.__current_luck = self.__starting_luck
        self.__luck_total = self.__starting_luck


    # -- Health section --
    
    @property
    def health_extra(self) -> int:
        return self.__health_extra
    
    @health_extra.setter
    def health_extra(self, value: int):
        if value < 0:
            raise ValueError("Extra health cannot be negative.")
        self.__health_extra = value
        self.__max_health = Character.baseline_health + value

        if self.__current_health > self.__max_health:
            self.__current_health = self.__max_health
    
    @property
    def max_health(self) -> int:
        return self.__max_health
    
    @property
    def current_health(self) -> int:
        return self.__current_health
    
    @current_health.setter
    def current_health(self, value: int):
        if value < 0 or value > self.__max_health:
            raise ValueError(f"Current health must be between 0 and {self.__max_health}.")
        self.__current_health = value

    def change_health(self, delta: int):
        new_health = self.__current_health + delta
        if new_health < 0:
            new_health = 0
        elif new_health > self.__max_health:
            new_health = self.__max_health
        self.__current_health = new_health

    # (Check if character is alive)
    @property
    def is_alive(self) -> bool:
        return self.__current_health > 0
    

    # -- Luck section --
    
    @property
    def luck_extra(self) -> float:
        return self.__luck_extra
    
    @luck_extra.setter
    def luck_extra(self, value: float):
        if value < 0 or (Character.baseline_luck + value) > Character.max_luck:
            raise ValueError(f"Extra luck must be between 0 and {Character.max_luck - Character.baseline_luck}.")
        self.__luck_extra = value
        self.__luck_total = Character.baseline_luck + value
        if self.__current_luck > self.__luck_total:
            self.__current_luck = self.__luck_total

    @property
    def luck_total(self) -> float:
        return self.__luck_total

    @property
    def current_luck(self) -> float:
        return self.__current_luck
    
    @current_luck.setter
    def current_luck(self, value: float):
        if value < 0 or value > self.__luck_total:
            raise ValueError(f"Current luck cannot be negative and higher than {self.__luck_total}.")
        self.__current_luck = value
    
    def change_luck(self, delta: float):
        new_luck = self.__current_luck + delta
        if new_luck < 0:
            new_luck = 0
        elif new_luck > self.__luck_total:
            new_luck = self.__luck_total
        self.__current_luck = new_luck


# Game character classes (subclasses of Character)

class Gladiator(Character):
    def __init__(self):
        super().__init__("Gladiator", 3, 0.5)
    
    def special_ability(self, target: Character):
        print("CHARGE!")
        roll = random.random()

        if roll <= self.current_luck:
            print(f"Gladiator's charge on {target.name} is successful. Opponent loses 1 health.")
            target.change_health(-1)
        else:
            print(f"Gladiator misses. He gets angrier and more impulsive - his luck decreases by 0.15.")
            self.change_luck(-0.15)


class Knight(Character):
    def __init__(self):
        super().__init__("Knight", 2, 0.4)
    
    def special_ability(self, target: Character):
        print("I fight for honor!")
        roll = random.random()

        if roll <= self.current_luck:
            print(f"Knight's attack is successful. Opponent loses 1 health.")
            target.change_health(-1)
        else:
            print("The opponent defended knight's attack, but got scared by it. Opponent's luck decreases by 0.1.")
            target.change_luck(-0.1)


class Witch(Character):
    def __init__(self):
        super().__init__("Witch", 1, 0.55)
    
    def special_ability(self, target: Character):
        print("Your luck is running out. Wait... which spell was it?")
        roll = random.random()

        if roll <= self.current_luck:
            print(f"The Witch remembered the correct spell and hexed the opponent. {target.name}'s luck decreases by 0.25.")
            target.change_luck(-0.25)
        else:
            print("The Witch cast a wrong spell and hexed herself! Her luck decreases by 0.25.")
            self.change_luck(-0.25)


class Warlock(Character):
    def __init__(self):
        super().__init__("Warlock", 1, 0.55)

    def special_ability(self, target: Character):
        print("The darkness is on my side, but not on yours...")
        roll = random.random()

        if roll <= self.current_luck:
            print(f"Warlock steals {target.name}'s health.")
            target.change_health(-1)
            self.change_health(1)
        else:
            print(f"The darkness overpowers Warlock's abilities - his health decreases by 1 and his luck decreases by 0.15.")
            self.change_health(-1)
            self.change_luck(-0.15)


class Priest(Character):
    def __init__(self):
        super().__init__("Priest", 3, 0.4)

    def special_ability(self, target: Character):
        print("The light will heal me!")
        roll = random.random()

        if roll <= self.current_luck:
            print(f"Priest's powers are successful and heal him by 1 life.")
            self.change_health(1)
        else:
            print(f"The light didn't answer Priest's call. Nothing happens.")


class Jester(Character):
    def __init__(self):
        super().__init__("Jester", 2, 0.6)

    def special_ability(self, target: Character):
        print("We all love jokes, don't we?")
        roll = random.random()

        if roll <= self.current_luck:
            print(f"Jester uses his magic to decrease opponent's luck by the amount of their health/10.")
            target.change_luck(-target.current_health/10)
        else:
            print(f"Jester's magic backfires and his luck decreases by 0.3.")
            self.change_luck(-0.3)