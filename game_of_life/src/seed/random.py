from random import uniform

class Seeder:
    def _random_tup(self, frm, til):
        return tuple([
            int(uniform(frm, til)) 
            for _ in range(2)
        ])

    def _generate(self, number, frm, til):
        return [self._random_tup(frm, til) for _ in range(number)]

    def seeds(self):
        return self._generate(25, 0, 200)
    
    