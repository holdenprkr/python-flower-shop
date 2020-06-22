class Arrangement:

    def __init__(self):
        self.flowers = []

    def enhance(self, flower):
        self.flowers.append(flower)


class MothersDay(Arrangement):

    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        try:
            if flower.stem_length == 4:
                self.flowers.append(flower)
            else:
                raise AttributeError
        except AttributeError:
            print(f"{flower} doesn\'t belong in this arrangement!")


class ValentinesDay(Arrangement):

    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        try:
            if flower.stem_length == 7:
                self.flowers.append(flower)
            else:
                raise AttributeError
        except AttributeError:
            print(f"{flower} doesn\'t belong in this arrangement!")


class ValentinesFlower:

    def __init__(self):
        self.stem_length = 7
        self.organically_grown = False


class MothersDayFlower:

    def __init__(self):
        self.stem_length = 4
        self.organically_grown = True


class Rose(ValentinesFlower):

    def __init__(self, color):
        super().__init__()
        self.color = color

    def __str__(self):
        return f"{self.color} Rose"


class Lilly(ValentinesFlower):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Lilly"


class Alstroemeria(ValentinesFlower):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Alstroemeria"


class Daisy(MothersDayFlower):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Daisy"


class BabysBreath(MothersDayFlower):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Baby's Breath"


class Poppy(MothersDayFlower):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Poppy"


if __name__ == "__main__":
    for_girlfriend = ValentinesDay()
    red_rose = Rose("Red")
    pink_rose = Rose("Pink")
    blue_rose = Rose("Blue")
    lilly = Lilly()
    alstroemeria = Alstroemeria()

    for_mother = MothersDay()
    daisy = Daisy()
    babys_breath = BabysBreath()
    poppy = Poppy()

    for_girlfriend.enhance(red_rose)
    for_girlfriend.enhance(pink_rose)
    for_girlfriend.enhance(blue_rose)
    for_girlfriend.enhance(lilly)
    for_girlfriend.enhance(alstroemeria)
    for_girlfriend.enhance(poppy)

    for_mother.enhance(daisy)
    for_mother.enhance(babys_breath)
    for_mother.enhance(poppy)
    for_mother.enhance(lilly)

    print()

    for flower in for_girlfriend.flowers:
        print(flower)

    print()

    for flower in for_mother.flowers:
        print(flower)
