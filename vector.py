
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, vector):
        cateto_a = self.x - vector.x
        cateto_b = self.y - vector.y

        return round((cateto_a**2 + cateto_b**2)**0.5, 4) 

if __name__ == '__main__':
    v_0 = Vector(3,5)
    v_1 = Vector(1,9)

    print(v_0.distancia(v_1))