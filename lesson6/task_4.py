import random

class Car:
    speed = 100
    color = 'red'
    name = 'saloon'
    is_police = False

    def show_speed(self):
        self.speed = random.randint(20, 101)
        print(self.speed)
        return self.speed


    def go(self):
        print(f'Car {Car.name} goes')

    def stop(self):
        print(f'Car {Car.name} sopped')

    def turn(self):
        direction = ['Straight', 'Left', 'Right', 'No one knows']
        where = random.choice(direction)
        print(f'Car turned {where}')

class TownCar(Car):
    speed = 150
    color = 'black'
    name = 'BMW'
    is_police = False

    def show_speed(self):
        a = Car()
        real_speed = int(a.show_speed())
        if real_speed > 60:
            print(f'Машина {TownCar.name} {TownCar.color} цвета превысила скорость! Скорость равна {real_speed} км/ч! Ограничение 60 км/ ч! Сбавьте!')
        else:
            print(f'Скорость машины {TownCar.name} {TownCar.color} цвета равна {real_speed} км/ч')



class SportCar(Car):
    speed = 300
    color = 'red'
    name = 'Ferrari'
    is_police = False


class WorkCar(Car):
    speed = 200
    color = 'white'
    name = 'T-1000'
    is_police = False

    def show_speed(self):
        a = Car()
        real_speed = int(a.show_speed())
        if real_speed > 40:
            print(f'Машина {WorkCar.name} {WorkCar.color} цвета превысила скорость! Скорость равна {real_speed} км/ч! Ограничение 40 км/ ч! Сбавьте!')
        else:
            print(f'Скорость машины {WorkCar.name} {WorkCar.color} цвета равна {real_speed} км/ч')


class PoliceCar(Car):
    speed = 300
    color = 'blue'
    name = 'kozel'
    is_police = True

a = Car()
print(f'Максимальная скорость машины типа {a.name} {a.color} цвета равна {a.speed}')

a = TownCar()
print(f'Максимальная скорость машины типа {a.name} {a.color} цвета равна {a.speed}')

a = WorkCar()
print(f'Максимальная скорость машины типа {a.name} {a.color} цвета равна {a.speed}')

a = PoliceCar()
print(f'Максимальная скорость машины типа {a.name} {a.color} цвета равна {a.speed}')

a = SportCar()
print(f'Максимальная скорость машины типа {a.name} {a.color} цвета равна {a.speed}')

a = TownCar() # проверка экзмепляр машина в городе
a.show_speed()


a = WorkCar() # проверка экзмепляр машина в городе
a.show_speed()


# done