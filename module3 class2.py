#inheritance
#dad -mr object
#mom -mrs classy
#son - inno
#daughter - multy

class Father:
    def skills(self):
        print("I can code in c++")


class Son(Father):
    pass


inno= Son()
inno.skills()

class Mom:
    def cooking(self):
        print("I can cook delicious Biriyani")

class Inno (Mom):
    pass

class Multi(Mom):
    pass

inno = Inno()
multi= Multi()



class Grandpa :
    def advice(self):
        print("Never ignore bugs")

class Father (Grandpa):
    def teacher(self):
        print("Practice c++ will make you more lofical and inmcrease thinking capability")


class Son(Father):
    pass

multi = Son()
multi.advice()

multi.teacher()
class Mother:
    def discioline(self):
        print("Go to bed at 10 pm")

class uncleLogic:
    def math(self):
        print("Solving equations")

class Daughter(Mother, uncleLogic):
    pass

class Reportcard:
    def marks(slef, math=None, english= None):
        if math is not None and english is not None:
            print(f"Math: {math}, English: {english}")
        elif math is not None:
            print(f"Math: {math}")    

        else:
            print("No marks given")

overloading
inno_report= Reportcard()
inno_report.marks(90)
inno_report.marks(90, 89)

#ovveriding
class parent:
    def role(self):
        print("I am the boss")

class Child(parent):
    def role(self):
        print("I run the show now!!")

multi = Child()
multi.role()

parent_obj=parent()
parent_obj.role()

encapsulation
class Family:
    def __init__(self):
        self.__secret_fund = 500
    def get_fund(self):
            return self.__secret_fund

dad = Family()
print(dad.get_fund())

polymorphism
class role:
    def act(self):
        pass

class Cook(role):
    def act(self):
        print("Cooking dinner")

class Doctor(role):
    def act(self):
        print("prescribing medicine")

def daily_roles(role):
    role.act()


daily_roles(Cook())
daily_roles(Doctor())