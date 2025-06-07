from __future__ import annotations
import random

### Character class ###
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
    
    ## Health section ##
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

    @property
    def is_alive(self) -> bool:
        return self.__current_health > 0
    ## ##

    ## Luck section ##
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
    ## ##

    ## Rolling and basic attack section ##
    def roll_attempt(self, threshold: float) -> bool:
        roll = random.random()
        return roll <= self.__current_luck
    
    def basic_attack(self, target: Character) -> bool:
        charge = self.roll_attempt(self.current_luck)
        if charge:
            target.change_health(-1)
        return charge
    ## ##
### ###

### Characters in the game as subclasses of Character ###
class Gladiator(Character):
    def __init__(self):
        super().__init__("Gladiator", 3, 0.5)
    
    def special_ability(self, target: Character):
        print("Special ability: EXTRA CHARGE!")
        roll = random.random()

        if self.roll_attempt(self.current_luck):
            print(f"Success. Gladiator's extra charge on {target.name} is successful - opponent loses 1 health.")
            target.change_health(-1)
        else:
            print(f"Unlucky. Gladiator's extra charge misses. He gets angrier and more impulsive - his luck decreases by 0.15.")
            self.change_luck(-0.15)

class Knight(Character):
    def __init__(self):
        super().__init__("Knight", 2, 0.4)
    
    def special_ability(self, target: Character):
        print("Special ability: Fight for Honor!")
        roll = random.random()

        if self.roll_attempt(self.current_luck):
            print(f"Success. Opponent loses 1 health.")
            target.change_health(-1)
        else:
            print(f"Unlucky. {target.name} defended knight's attack. However, they got scared by it - their luck decreases by 0.1.")
            target.change_luck(-0.1)

class Witch(Character):
    def __init__(self):
        super().__init__("Witch", 1, 0.55)
    
    def special_ability(self, target: Character):
        print("Special ability: Forgetful Witch")
        roll = random.random()

        if self.roll_attempt(self.current_luck):
            print(f"Success. Witch remembered the correct spell and hexed the opponent. {target.name}'s luck decreases by 0.15.")
            target.change_luck(-0.15)
        else:
            print("Unlucky. Witch cast a wrong spell and hexed herself! Her luck decreases by 0.2.")
            self.change_luck(-0.2)

class Warlock(Character):
    def __init__(self):
        super().__init__("Warlock", 2, 0.4)

    def special_ability(self, target: Character):
        print("Special ability: Call to Darkness")
        roll = random.random()

        if self.roll_attempt(self.current_luck):
            print(f"Success. Warlock steals {target.name}'s health.")
            target.change_health(-1)
            self.change_health(1)
        else:
            print(f"Unlucky. The darkness overpowers Warlock's abilities - his health decreases by 1 and his luck decreases by 0.15.")
            self.change_health(-1)
            self.change_luck(-0.15)

class Priest(Character):
    def __init__(self):
        super().__init__("Priest", 3, 0.45)

    def special_ability(self, target: Character):
        print("Special ability: Light")
        roll = random.random()

        if self.roll_attempt(self.current_luck):
            print(f"Success. Priest heals up by 1 life.")
            self.change_health(1)
        else:
            print(f"Unlucky. The light didn't answer Priest's call - nothing happens.")

class Jester(Character):
    def __init__(self):
        super().__init__("Jester", 2, 0.5)

    def special_ability(self, target: Character):
        print("Special ability: Jokes All Around")
        roll = random.random()

        if self.roll_attempt(self.current_luck):
            print(f"Success. Jester uses his magic to decrease opponent's luck by the amount of their health/10.")
            target.change_luck(-target.current_health/10)
        else:
            print(f"Unlucky. Jester's magic backfires and his luck decreases by 0.3.")
            self.change_luck(-0.3)
### ###

all_game_characters = [Gladiator, Knight, Witch, Warlock, Priest, Jester]

### Allocation of characters to teams ###
def team_choice(team_name: str) -> list[Character]:
    chosen_characters = random.sample(all_game_characters, 3)
    return [cls() for cls in chosen_characters]
### ###

### Single battle process ###
def battle(ch1: Character, ch2: Character) -> Character | None:
    print(f"Battle: {ch1.name} health {ch1.current_health} versus {ch2.name} health {ch2.current_health}")

    attacker, defender = ch1, ch2

    while attacker.is_alive and defender.is_alive:
        hit = attacker.basic_attack(defender)
        print(f"{attacker.name} basic attack {'hits' if hit else 'misses'}.")

        if not defender.is_alive:
            return attacker
        
        if hit:
            attacker.special_ability(defender)
            if not defender.is_alive:
                return attacker
            
        attacker, defender = defender, attacker
    return None
### ###

### Main game simulation running function ###
def run():
    team_A = team_choice("A")
    team_B = team_choice("B")

    print("\nTeam A characters:")
    for i, ch in enumerate(team_A, start= 1):
        print(f"{i}: {ch.name} - max health {ch.max_health}, current luck {round(ch.current_luck, 4)}")
    
    print("\nTeam B characters:")
    for i, ch in enumerate(team_B, start= 1):
        print(f"{i}: {ch.name} - max health {ch.max_health}, current luck {round(ch.current_luck, 4)}")
    
    print("\n")

    n_rounds = 3

    score_team_A = 0
    score_team_B = 0

    for i in range(n_rounds):
        ch_team_A = team_A[i]
        ch_team_B = team_B[i]

        winner = battle(ch_team_A, ch_team_B)
        if winner is ch_team_A:
            score_team_A += 1
            print(f"Round {i+1} winner: {winner.name} from team A.")
            print("\n")
        elif winner is ch_team_B:
            score_team_B += 1
            print(f"Round {i+1} winner: {winner.name} from team B.")
            print("\n")
        else:
            print(f"Round {i+1} was a tie.")
            print("\n")

    print("Final score:")
    print(f"Team A score: {score_team_A}")
    print(f"Team B score: {score_team_B}")

    if score_team_A > score_team_B:
        print("Team A won the game!")
    elif score_team_A < score_team_B:
        print("Team B won the game!")
    else:
        print("The game was a draw.")
### ###

if __name__ == "__main__":
    run()