import playground
import random
import numpy


class Atom:
    def __init__(self, x, y, rad, speed_x, speed_y, color):
        """
        Inicializator třídy Atom
        :param x: souřadnice X
        :param y: soouřadnice Y
        :param rad: poloměr
        :param color: barva
        """
        self.x = x
        self.y = y
        self.rad = rad
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        pass

    def to_tuple(self):
        """Vrátí n-tici hodnot 
        příklad: x = 10, y = 12, rad = 15, color = 'green' -> (10,12,15,'green')
        """
        return (self.x,self.y,self.rad,self.color)
        pass

    def move(self, width, height):
        constSpeed = 15
        self.x += self.speed_x * constSpeed
        self.y += self.speed_y * constSpeed
        if(width <= (self.x + self.rad) or 0 >= (self.x - self.rad)):
            self.speed_x *= -1
            self.move(width, height)
        if(height <= (self.y + self.rad) or 0 >= (self.y - self.rad)):
            self.speed_y *= -1
            self.move(width, height)
        pass
    def move_oneAxis(self, width, height):
        constSpeed = 15
        self.x += self.speed_x * constSpeed
        self.y += self.speed_y * constSpeed
        if(width <= (self.x + self.rad) or 0 >= (self.x - self.rad)):
            self.speed_x *= -1
            self.speed_y *= -1
            self.move(width, height)
        if(height <= (self.y + self.rad) or 0 >= (self.y - self.rad)):
            self.speed_y *= -1
            self.speed_x *= -1
            self.move(width, height)
        pass

class FallDownAtom(Atom):
    def __init__(self, x, y, rad, speed_x, speed_y, color, g = 3, damping = 0.8):
        super().__init__(x, y, rad, speed_x, speed_y, color)
        self.g = g
        self.damping = damping
    def move(self, width, height):
        constSpeed = 12
        self.x += self.speed_x * constSpeed
        self.y += self.speed_y * (constSpeed + self.g)
        if(width <= (self.x + self.rad) or 0 >= (self.x - self.rad)):
            self.speed_x *= -1
            #self.move(width, height)
        if(height <= (self.y + self.rad) or 0 >= (self.y - self.rad)):
            if(height <= (self.y + self.rad)):
                self.speed_x *= self.damping
                self.speed_y *= self.damping
                """if(self.speed_x * constSpeed < 0.001):
                    self.speed_x = 0
                if(self.speed_y * constSpeed < 0.001):
                    self.speed_y = 0"""
            self.speed_y *= -1
            #self.move(width, height)
        pass
    def move_oneAxis(self, width, height):
        constSpeed = 12
        self.x += self.speed_x * (constSpeed + self.g) 
        self.y += self.speed_y * (constSpeed + self.g)
        if(width <= (self.x + self.rad) or 0 >= (self.x - self.rad)):
            self.speed_x *= -1
            self.speed_y *= -1
            #self.move(width, height)
        if(height <= (self.y + self.rad) or 0 >= (self.y - self.rad)):
            if(height <= (self.y + self.rad)):
                self.speed_x *= self.damping
                self.speed_y *= self.damping
            self.speed_y *= -1
            self.speed_x *= -1
            #self.move(width, height)
        pass

class ExampleWorld(object):

    def __init__(self, size_x, size_y, count):
        self.width = size_x
        self.height = size_y
        self.atoms = []
        self.count = count
        for i in range(0,self.count):
            self.random_atom()

    def random_atom(self):
        randColor = random.randint(0, 1)
        color = ""
        match randColor:
            case 0:
                color = "red"
            case 1:
                color = "green"
            case _:
                color = "blue"
        atom = FallDownAtom(random.randint(30,670),random.randint(30,370),random.randint(15, 30),random.random(),random.random(),color)
        self.atoms.append(atom)
        pass

    def tick(self):
        """This method is called by playground. Sends a tuple of atoms to rendering engine.

        :param size_x: world size x dimension
        :param size_y: world size y dimension
        :return: tuple of atom objects, each containing (x, y, radius) coordinates 
        """
        counter = 0
        arrayOfTuples = []
        for atom in self.atoms:
           arrayOfTuples.append(atom.to_tuple())
           #atom.move(self.width, self.height)
           if(counter % 2 == 0):
               atom.move(self.width, self.height)
           else:
               atom.move_oneAxis(self.width, self.height)
           counter += 1
        result = tuple([tuple(row) for row in arrayOfTuples])
        return result


if __name__ == '__main__':
    size_x, size_y = 700, 400

    world = ExampleWorld(size_x, size_y, 2)
    playground.run((size_x, size_y), world)
