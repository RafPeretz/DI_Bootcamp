from ExerciseXP import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *dogs):

        for dog in dogs:
            print(f'{dog.name} all plays together.')

    def do_a_trick(self):
        if self.trained == True:
            print(f"{self.name} does a barrel roll")
            print(f"{self.name} stands on his back legs")
            print(f"{self.name} stands on his back legs")
            print(f"{self.name} plays dead")
