class Vehicle:
    def __init__(self, color, doors, gas_powered):
        self.__color = color
        self.__doors = doors
        self.__gas_powered = gas_powered

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        allowed_colors = ["red", "grey", "black", "white", "blue"]
        if color in allowed_colors:
            self.__color = color
        else:
            raise ValueError("Not an allowed color")

    @property
    def doors(self):
        return self.__doors

    @doors.setter
    def doors(self, door):
        allowed_doors = [2, 4, 5]
        if door in allowed_doors:
            self.__doors = door
        else:
            raise ValueError("Invalid door number count")

    @property
    def gas_powered(self):
        return self.__gas_powered

    @gas_powered.setter
    def gas_powered(self, gas_powered):
        if isinstance(gas_powered, bool):
            self.__gas_powered = gas_powered
        else:
            raise ValueError("Invalid gas powered value")

    def __str__(self):
        return f"Vehicle: Color: {self.__color}, Doors: {self.__doors}, Gas Powered: {self.__gas_powered}"

    def is_eco_friendly(self):
        return self.__doors == 2 and not self.__gas_powered


class Truck(Vehicle):
    def __init__(self, color, doors, gas_powered, seats, trunk_space):
        super().__init__(color, doors, gas_powered)
        self.__seats = seats
        self.__trunk_space = trunk_space

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, seats):
        if seats > 0:
            self.__seats = seats
        else:
            raise ValueError("Invalid number of seats")

    @property
    def trunk_space(self):
        return self.__trunk_space

    @trunk_space.setter
    def trunk_space(self, trunk_space):
        if trunk_space > 0:
            self.__trunk_space = trunk_space
        else:
            raise ValueError("Invalid trunk space")

    def __str__(self):
        return (f"Truck: Color: {self.__color}, Doors: {self.__doors}, "
                f"Gas Powered: {self.gas_powered}, Seats: {self.__seats},"
                f"Trunk Space: {self.__trunk_space}")

    def is_eco_friendly(self):
        return super().is_eco_friendly() and self.__seats <= 2 and self.__trunk_space == 1


