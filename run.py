import random

class Advices:

    def __init__(self) -> None:
        self.__speeches = [
            'Melhor um passaro na mao do que dois voando',
            'Shrek e o melhor filme ja existente',
            'SE MELHORAR, VIRA FESTA!',
            'Resiliencia'
        ]
    
    def gimme_something(self):
        position = random.randint(0, 3)
        print(self.__speeches[position])

ball = Advices()

while True:
    input('Do you wanna some advice?')
    ball.gimme_something()