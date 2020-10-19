class Fish:
    def __init__(self, first_name, Last_name="Fish", skeleton = "bone", eyelids=False):
        self.first_name = first_name
        self.last_name = Last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
            print("The fish is swimming")

    def swim_backwards(self):
            print("The fish can swim backwards")


class Trout(Fish):
    def __init__(self, water= "freshwater"):
        self.water = water
        super().__init__(self)
    

terry = Trout()
terry.first_name = "Terry"
print(terry.first_name + "" + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()
print(terry.water)



class Clownfish(Fish):
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone")

casey = Clownfish("Casey")
print(casey.first_name+ "" + casey.last_name)
casey.swim()
casey.live_with_anemone()

class Shark(Fish):
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backward, but can sink backwards.")

sharkey = Shark("Sharkey")
print(sharkey.first_name + " " + sharkey.last_name)
sharkey.swim()
sharkey.swim_backwards()
print(sharkey.eyelids)
print(sharkey.skeleton)
