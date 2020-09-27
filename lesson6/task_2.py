class Road:
    _lenght = 100
    _width = 5

    def mass(self):
        self.mass_per_sq_m = 10
        self.thickness = 10
        all_mass = (Road._lenght * Road._width * self.mass_per_sq_m * self.thickness)/1000
        print(f'Масса асфальта {all_mass} тонн')

m=Road()
m.mass()

# done