class FootballPlayer:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    #def __str__(self):
        #return f"Name: {self.name} Soyad: {self.surname} Age: {self.age}"
    def __repr__(self):
        return "repr is working"
    #when __str__ does not work __repr__ will work
    #i add "#" __str__ method to observe how __repr__ works

player1 = FootballPlayer("Sima", "Altinkum", 21)
print(player1)
