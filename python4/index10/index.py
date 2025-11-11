class father:
    def skill(self):
        print("I can drive a car")

class mother:
    def skill(self):
        print("I can cook food")

class child(father, mother):
    def skill(self):
        father.skill(self)
        mother.skill(self)
        print("I can play football")

child = child()
child.skill()
