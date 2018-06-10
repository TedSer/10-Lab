class Dish:
    total_price = 0

    def __init__(self, type_of_dish="Zupa", complexity_of_cooking="Medium", country="Poland", price_for_portion=50,
                 rating="77/100"):
        self.type_of_dish = type_of_dish
        self.complexity_of_cooking = complexity_of_cooking
        self.__county = country
        self.price_for_portion = price_for_portion
        self.rating = rating
        Dish.total_price += price_for_portion

    def to_string(self):
        print("Type of the dish :" + self.type_of_dish + " ; Complexity of the dish :" + self.complexity_of_cooking +
              " ; Country" + self.county + " ; Price for the portion :" + str(self.price_for_portion) + " ; Rating :" +
              self.rating)

    def print_sum(self):
        print("Price of" + str(self.type_of_dish) + " " + str(self.rating) + " is " + str(self.price_for_portion))

    @staticmethod
    def print_static_sum():
        print("Total for dish is " + str(Dish.total_price))


if __name__ == '__main__':
    zupa = Dish()
    borshch = Dish("Borshch", "Hard", "Ukraine", 70, "99/100")
    miso = Dish("Misoshuro", "Very hard", "Japan", 90, "55/100")

    zupa.to_string()
    borshch.to_string()
    miso.to_string()

    zupa.print_sum()
    borshch.print_sum()
    miso.print_sum()
    Dish.print_static_sum()


    
    dict((3, 5, 6), {3, 4,})

