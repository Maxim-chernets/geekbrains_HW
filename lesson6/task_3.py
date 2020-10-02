salary = {
    'wage': 100000,
    'bonus': 200000
}

class Worker:
    name = 'Ivan'
    sirname = 'Ivanxhikov'
    position = 'cleaning manager'
    _income = sum(salary.values())



class Position(Worker):
    def get_full_name(self):
        print(Worker.name + ' ' + Worker.sirname)

    def get_total_income(self):
        print(Worker._income)

a = Position()
a.get_full_name()
a.get_total_income()