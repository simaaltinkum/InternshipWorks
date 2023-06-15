class Car:
    def __init__(self, model, plaque):
        self.model = model
        self.plaque = plaque

    #def show_info(self):
        #return f"Car's Model: {self.model}, Cars' Plaque: {self.plaque}"
##    def compare(self):
##        model = print(input("Model: "))
##        plaque = print(input("Plaque: "))
      
            
car1 = Car("Renault Kangoo", "09 SK 117")
car2 = Car("Renault Clio", "09 SA 472")
car3 = Car("Renault Captur", "09 SM 520")
car4 = Car("Renault Megane", "09 SM 756")
car5 = Car("Peugeot 208", "09 JK 372")
car6 = Car("Peugeot 3008", "09 JL 723")
car7 = Car("Peugeot 308", "09 SI 451")
car8 = Car("Peugeot 408", "09 JR 981")
car9 = Car("Fiat Egea", "09 JM 32")
car10 = Car("Fiat Egea", "09 SP 289")
car11 = Car("Renault Megane", "09 SS 366")
car12 = Car("Renault Clio", "09 S 504")
car13 = Car("Volkwagen Passat", "09 SA 647")
car14 = Car("Volkswagen Passat", "09 JO 45")
car15 = Car("Volkswagen Golf", "09 SR 113")
car16 = Car("Volkswagen Golf", "09 JL 839")
car17 = Car("Volkswagen Polo", "09 S 562")
car18 = Car("Fiat Linea", "09 SP 947")
car19 = Car("Fiat Linea", "09 JH 73")
car20 = Car("Fiat Linea", "09 JF 852")


myCar_model = input("Model: ")
myCar_plaque = input("Plaque: ")
def Compare(myCar_model, myCar_plaque):
    if (myCar_model == car1.model) and (myCar_plaque == car1.plaque):
        print("Welcome!")
    elif (myCar_model == car2.model) and (myCar_plaque == car2.plaque):
        print("Welcome!")
    elif (myCar_model == car3.model) and (myCar_plaque == car3.plaque):
        print("Welcome!")
    elif (myCar_model == car4.model) and (myCar_plaque == car4.plaque):
        print("Welcome!")
    elif (myCar_model == car5.model) and (myCar_plaque == car5.plaque):
        print("Welcome!")
    elif (myCar_model == car6.model) and (myCar_plaque == car6.plaque):
        print("Welcome!")
    elif (myCar_model == car7.model) and (myCar_plaque == car7.plaque):
        print("Welcome!")
    elif (myCar_model == car8.model) and (myCar_plaque == car8.plaque):
        print("Welcome!")
    elif (myCar_model == car9.model) and (myCar_plaque == car9.plaque):
        print("Welcome!")
    elif (myCar_model == car10.model) and (myCar_plaque == car10.plaque):
        print("Welcome!")
    elif (myCar_model == car11.model) and (myCar_plaque == car11.plaque):
        print("Welcome!")
    elif (myCar_model == car12.model) and (myCar_plaque == car12.plaque):
        print("Welcome!")
    elif (myCar_model == car13.model) and (myCar_plaque == car13.plaque):
        print("Welcome!")
    elif (myCar_model == car14.model) and (myCar_plaque == car14.plaque):
        print("Welcome!")
    elif (myCar_model == car15.model) and (myCar_plaque == car15.plaque):
        print("Welcome!")
    elif (myCar_model == car16.model) and (myCar_plaque == car16.plaque):
        print("Welcome!")
    elif (myCar_model == car17.model) and (myCar_plaque == car17.plaque):
        print("Welcome!")
    elif (myCar_model == car18.model) and (myCar_plaque == car18.plaque):
        print("Welcome!")
    elif (myCar_model == car19.model) and (myCar_plaque == car19.plaque):
        print("Welcome!")
    elif (myCar_model == car20.model) and (myCar_plaque == car20.plaque):
        print("Welcome!")
    else:
        print("You can not park here")
Compare(myCar_model, myCar_plaque)
