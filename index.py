from experta import *

bandera = None
array_colores = ["verde","rojo","amarillo","naranja"]

class Fruits(Fact):
    pass

class DivinerRobot(KnowledgeEngine):
    @Rule(Fruits(color='verde',dura=1,suave=0,dulce=0,acido=1,semilla=0,hueso=0,ss_nh=1,agradable=1,desagradable=0))
    def coco(self):
        print("Es el coco")
        bandera = True
        self.set_bandera(bandera)

    @Rule(Fruits(color='verde',dura=0,suave=1,dulce=0,acido=1,semilla=1,hueso=0,ss_nh=0,agradable=1,desagradable=0))
    def kiwi(self):
        print("Es el kiwi")
        bandera = True
        self.set_bandera(bandera)

    @Rule(Fruits(color='verde',dura=1,suave=0,dulce=0,acido=1,semilla=1,hueso=0,ss_nh=0,agradable=1,desagradable=0))
    def manzana_verde(self):
        print("Es la manzana")
        bandera = True
        self.set_bandera(bandera)

    @Rule(Fruits(color='rojo',dura=0,suave=1,dulce=1,acido=0,semilla=1,hueso=0,ss_nh=0,agradable=1,desagradable=0))
    def fresa(self):
        print("Es la fresa")
        bandera = True
        self.set_bandera(bandera)

    @Rule(Fruits(color='rojo',dura=1,suave=0,dulce=1,acido=0,semilla=1,hueso=0,ss_nh=0,agradable=1,desagradable=0))
    def manzana_roja(self):
        print("Es la manzana")
        bandera = True
        self.set_bandera(bandera)

    @Rule(Fruits(color='rojo',dura=0,suave=1,dulce=0,acido=1,semilla=1,hueso=0,ss_nh=0,agradable=0,desagradable=1))
    def zarzamora(self):
        print("Es la zarzamora")
        bandera = True
        self.set_bandera(bandera)

    @Rule(Fruits(color='amarillo',dura=1,suave=0,dulce=0,acido=1,semilla=1,hueso=0,ss_nh=0,agradable=1,desagradable=0))
    def manzana_amarilla(self):
        print("Es la manzana")
        bandera = True
        self.set_bandera(bandera)

    @Rule(Fruits(color='amarillo',dura=0,suave=1,dulce=1,acido=0,semilla=1,hueso=0,ss_nh=0,agradable=1,desagradable=0))
    def platano(self):
        print("Es el platano")
        bandera = True
        self.set_bandera(bandera)

    @Rule(Fruits(color='amarillo',dura=1,suave=0,dulce=1,acido=0,semilla=1,hueso=0,ss_nh=0,agradable=1,desagradable=0))
    def melon(self):
        print("Es el melon")
        bandera = True
        self.set_bandera(bandera)

    @Rule(Fruits(color='naranja',dura=0,suave=1,dulce=1,acido=0,semilla=1,hueso=0,ss_nh=0,agradable=1,desagradable=0))
    def naranja(self):
        print("Es la naranja")
        bandera = True
        self.set_bandera(bandera)

    @Rule(Fruits(color='naranja',dura=0,suave=1,dulce=1,acido=0,semilla=0,hueso=1,ss_nh=0,agradable=1,desagradable=0))
    def mango(self):
        print("Es la mango")
        bandera = True
        self.set_bandera(bandera)

    @Rule(Fruits(color='naranja',dura=0,suave=1,dulce=1,acido=0,semilla=1,hueso=0,ss_nh=0,agradable=1,desagradable=0))
    def papaya(self):
        print("Es la papaya")
        bandera = True
        self.set_bandera(bandera)

    def set_bandera(self, bandera):
        self.bandera = bandera

def preguntas():
    name_player = color = ""
    dura = suave = dulce = acido = semilla = hueso = ss_nh = agradable = desagradable = 0
    name_player = input("¿Cual es tu nombre? ")
    print(f'Hola {name_player}, trataré de adivinar la fruta en la que piensas')
    color = input("¿De que color es? ")
    color2 = color.lower()
    if(color2 in array_colores):
        dura = int(input("¿Tiene la piel dura? (1=si 2=no) "))
        if(dura == 2):
            suave = int(input("¿Tiene la piel suave? (1=si 2=no)"))
        dulce = int(input("¿Es dulce? (1=si 2=no)"))
        if(dulce == 2):
            acido = int(input("¿Es acido? (1=si 2=no)"))
        semilla = int(input("¿Tiene semilla? (1=si 2=no)"))
        if(semilla == 2):
            hueso = int(input("¿Tiene hueso? (1=si 2=no)"))
            if(hueso == 2):
                ss_nh = int(input("¿Sin semilla ni hueso? (1=si 2=no)"))
        if(ss_nh == 2 or ss_nh == "" or ss_nh == None):
            print("No seas hijueputa malparido perro del orto troll!")
        else:
            agradable = int(input("Aroma agradable? (1=si 2=no)"))
            if(agradable == 2):
                desagradable = int(input("Aroma desagradable? (1=si 2=no)"))
        return (color, dura, suave, dulce, acido, semilla, hueso, ss_nh, agradable, desagradable)
    else:
        return False

def main():
    response = preguntas()
    if(response == False):
        print("Lo siento solamente tenemos los colores: ", array_colores)
    else:
        engine = DivinerRobot()
        engine.reset()
        engine.declare(Fruits(color=response[0].lower(),dura=response[1],suave=response[2],dulce=response[3],acido=response[4],semilla=response[5],hueso=response[6],ss_nh=response[7],agradable=response[8],desagradable=response[9]))
        engine.run()
        if(not bandera):
            print("Una disculpa! No encontre una fruta en mi BD con esas características!")
            input("¿Que fruta era?")
            print("Lo anotare en las cosas que me valen verga!")
        else:
            print("Eres un marrano y me la pelas!")

if __name__ == "__main__":
    main()