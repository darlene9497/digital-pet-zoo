import random

class Pet:
    def __init__(self, name, pet_type="🐶"):
        self.name = name
        self.hunger = random.randint(0, 10)     # 0 = full, 10 = very hungry
        self.energy = random.randint(0, 10)     # 0 = tired, 10 = fully rested
        self.happiness = random.randint(0, 10)  # 0 = sad, 10 = happy
        self.tricks = []
        self.pet_type = pet_type
        self.sounds = self.get_sounds()

    def eat(self):
        print(f"{self.pet_type} {self.name} is eating... {self.sounds['eat']}")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        print(f"{self.pet_type} {self.name} is sleeping... {self.sounds['sleep']}")
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy == 0:
            print(f"{self.pet_type} {self.name} is too tired to play")
            return
        print(f"{self.pet_type} {self.name} is playing... {self.sounds['play']}")
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        if trick not in self.tricks:
            print(f"{self.pet_type} {self.name} has learned how to {trick} 🤩")
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
        else:
            print(f"{self.pet_type} {self.name} already knows how to {trick} 😎")

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.pet_type} {self.name} doesn't know any tricks yet 😅")
        else:
            print(f"{self.pet_type} {self.name}'s tricks: {', '.join(self.tricks)} 🎉")

    def get_status(self):
        print(f"\n📋 {self.pet_type} {self.name}'s current state:")
        print(f"Hunger: {self.hunger} 🍗")
        print(f"Energy: {self.energy} ⚡")
        print(f"Happiness: {self.happiness} 😊")
        print(f"Tricks: {self.tricks if self.tricks else 'none yet ☹️'}\n")

    def get_sounds(self):
        return {
            "🐶": {"play": "ruff ruff 🐕", "eat": "munch munch 🦴", "sleep": "zzz 🛏️"},
            "🐱": {"play": "meowww 🐱", "eat": "nom nom 🐟", "sleep": "purr 💤"},
            "🐰": {"play": "boing boing 🐇", "eat": "crunch crunch 🥕", "sleep": "snuggle 🧺"}
        }.get(self.pet_type, {"play": "wheeeee 🐾", "eat": "yummmm 🥣", "sleep": "brrrrrr 😴"})