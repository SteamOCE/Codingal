class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        if self.species == "Lion":
            return "Roar"
        elif self.species == "Deer":
            return "Bleat"
        else:
            return "Unknown sound"


lion_obj = Animal("Leo", "Lion")
dear_obj = Animal("Bambi", "Deer")

print(f"{lion_obj.name} the {lion_obj.species} says: {lion_obj.make_sound()}")
print(f"{dear_obj.name} the {dear_obj.species} says: {dear_obj.make_sound()}")


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        if self.species == "Lion":
            return "Roar"
        elif self.species == "Deer":
            return "Bleat"
        else:
            return "Unknown sound"

lion_obj = Animal("Leo", "Lion")
dear_obj = Animal("Bambi", "Deer")

print(f"{lion_obj.name} the {lion_obj.species} says: {lion_obj.make_sound()} and is a {lion_obj.get_diet()}.")
print(f"{dear_obj.name} the {dear_obj.species} says: {dear_obj.make_sound()} and is a {dear_obj.get_diet()}.")
