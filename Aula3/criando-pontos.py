class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def ponto_medio(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def __str__(self):
        return "(x = %.2f\n     y = %.2f)\n" %(self.x, self.y)


print('Criando os objetos P1 e P2 \n')
P1 = Point()
P2 = Point()
print()

print(f'Coordenada x de P1: {P1.get_x()}')
print(f'Coordenada y de P1: {P1.get_y()}')
print()

print(f'Coordenada x de P2: {P2.get_x()}')
print(f'Coordenada y de P2: {P2.get_y()}')
print()

print('Criando o objeto P3: \n')
P3 = Point(10, 20)

print(f'Coordenada x de P3: {P3.get_x()}')
print(f'Coordenada y de P3: {P3.get_y()}')
print()

print('Criando os objetos P4 e P5 \n')
P4 = Point(3, -2)
P5 = Point(5, 15)

print("Distancia de P3 até a origem: %.2f" %(P3.distance_from_origin()))

print('Criando PM entre P4 e P5 \n')
PM = P4.ponto_medio(P5)
print(f'Coordenada x de PM: {PM.get_x()}')
print(f'Coordenada y de PM: {PM.get_y()}')
print()

print(f'P1: {P1}')
print(f'P2: {P2}')
print(f'P3: {P3}')
print(f'P4: {P4}')
print(f'P5: {P5}')
print(f'PM: {PM}')




