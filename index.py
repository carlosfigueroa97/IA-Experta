from experta import *

fruits_green = ["kiwi","apple","grapes","lemon","watermelon","avocado","pear","melon","blueberries","mango","coconut"]
fruits_red = ["strawberry","plum","apple","blackberry","cherry","raspberry","grapes"]
fruits_yellow = ["banana","platano","pitalla","melon","guayaba"]
fruits_blue = ["blueberries"]
fruits_purple = ["blackberry","currants","plum","figs","blueberries"]
fruits_brown = ["coconut","almond","hazelnut"]
fruits_orange = ["orange","mango","papaya"]

class Fruits(Fact):
    pass

class DivinerRobot(KnowledgeEngine):
    @Rule(Fruits(color="green"))
    def green_fruits(self, characteristic):
        if(characteristic == ""):
            print("The fruit is ...")
        elif(characteristic == ""):
            print("The fruit is ...")
        else:
            print("I don't know which is your fruit")

    @Rule(Fruits(color='red'))
    def red_fruits(self, characteristic):
        if(characteristic == ""):
            print("The fruit is ...")
        elif(characteristic == ""):
            print("The fruit is ...")
        else:
            print("I don't know which is your fruit")
        
    @Rule(Fruits(color='yellow'))
    def green_fruits(self, characteristic):
        if(characteristic == ""):
            print("The fruit is ...")
        elif(characteristic == ""):
            print("The fruit is ...")
        else:
            print("I don't know which is your fruit")
        
    @Rule(Fruits(color='blue'))
    def green_fruits(self, characteristic):
        if(characteristic == ""):
            print("The fruit is ...")
        elif(characteristic == ""):
            print("The fruit is ...")
        else:
            print("I don't know which is your fruit")

    @Rule(Fruits(color='purple'))
    def green_fruits(self, characteristic):
        if(characteristic == ""):
            print("The fruit is ...")
        elif(characteristic == ""):
            print("The fruit is ...")
        else:
            print("I don't know which is your fruit")

    @Rule(Fruits(color='brown'))
    def green_fruits(self, characteristic):
        if(characteristic == ""):
            print("The fruit is ...")
        elif(characteristic == ""):
            print("The fruit is ...")
        else:
            print("I don't know which is your fruit")

    @Rule(Fruits(color='orange'))
    def green_fruits(self, characteristic):
        if(characteristic == ""):
            print("The fruit is ...")
        elif(characteristic == ""):
            print("The fruit is ...")
        else:
            print("I don't know which is your fruit")

def questions():
    name_player = input("What's your name? ")
    print(f'Hi {name_player}, I will guess what fruit you think')
    color = input("Tell me a color of the fruit: ")
    characteristic = input("Tell me a characteristic of the fruit you think: ")
    question3 = input("3")
    question4 = input("4")
    question5 = input("5")
    question6 = input("6")
    question7 = input("7")
    question8 = input("8")
    question9 = input("9")
    question10 = input("10")
    return (name_player, color, characteristic, question3, question4, question5, question6, question7, question8, question9, question10)

def main():
    engine = DivinerRobot()
    engine.reset()
    response = questions()
    color = response[1].islower()
    engine.declare(Fruits(color=color))
    engine.run()

if __name__ == "__main__":
    main()