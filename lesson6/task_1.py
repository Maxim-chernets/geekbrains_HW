import time

class TrafficLight:

    __color = ['red', 'yellow', 'green']

    def running(self):
        self.count = 0
        while self.count != 3:
            print(TrafficLight.__color[0])
            time.sleep(7.0)
            print(TrafficLight.__color[1])
            time.sleep(2.0)
            print(TrafficLight.__color[2])
            time.sleep(5.0)
            self.count += 1
        print('Парампарампам! Конец!')

lights = TrafficLight()
lights.running()

# done