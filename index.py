from experta import *

fruits_green = ["kiwi","apple","grapes","lemon","watermelon","avocado","pear","melon","blueberries","mango","coconut"]
fruits_red = ["strawberry","plum","apple","blackberry","cherry","raspberry","grapes"]
fruits_yellow = ["banana","platano","pitalla","melon","guayaba"]
fruits_blue = ["blueberries","raisins"]
fruits_purple = ["blackberry","currants","plum","figs","blueberries"]
fruits_brown = ["coconut","almond","hazelnut"]
fruits_orange = ["orange","mango","papaya","mandarina"]

class Fruits(Fact):
    pass

class DivinerRobot(KnowledgeEngine):
    @Rule(Fruits(color='green'))
    def green_fruits(self):
        print("Color verde")

    @Rule(Fruits(color='red'))
    def red_fruits(self):
        print("Color rojo")
        
    @Rule(Fruits(color='yellow'))
    def yellow_fruits(self):
        print("Color yellow")
        
    @Rule(Fruits(color='blue'))
    def blue_fruits(self):
        print("Color blue")

    @Rule(Fruits(color='purple'))
    def purple_fruits(self):
        print("Print purple")

    @Rule(Fruits(color='brown'))
    def brown_fruits(self):
        print("Color brown")

    @Rule(Fruits(color='orange'))
    def orange_fruits(self):
        print("Color orange")

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
    color = response[1].lower()
    engine.declare(Fruits(color=color))
    engine.run()

if __name__ == "__main__":
    main()