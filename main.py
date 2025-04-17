import random
from pet import Pet

# function for a pet's day with 3 random actions
def random_pet_day(pet, random_trick):
    print(f"\n{pet.pet_type} {pet.name}'s day:")

    actions = ["eat", "sleep", "play", "train"]
    selected_actions = random.sample(actions, 3)

    for action in selected_actions:
        if action == "train":
            trick = random.choice(random_trick)
            pet.train(trick)
        else:
            getattr(pet, action)()

    pet.get_status()

tricks_list = [
    "stay",
    "give a high five",
    "spin in circles",
    "fetch the ball",
    "sit nicely",
    "play with the ball",
    "roll over",
    "play dead"
]

# create pets
simba_the_dog = Pet("Simba", pet_type="🐶")
garfield_the_cat = Pet("Garfield", pet_type="🐱")
sungura_the_rabbit = Pet("Sungura", pet_type="🐰")

# each pet's random day
random_pet_day(simba_the_dog, tricks_list)
random_pet_day(garfield_the_cat, tricks_list)
random_pet_day(sungura_the_rabbit, tricks_list)