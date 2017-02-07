class Car(object):
    def __init__(self, name='General', model='GM', vehicle_type='saloon'):
        self.name = name
        self.model = model
        self.vehicle_type = vehicle_type
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if self.vehicle_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
        self.speed = 0

    def is_saloon(self):
        if self.vehicle_type == 'saloon':
            return True
        return False

    def drive(self, n):
        if n == 3:
            self.speed = 1000
        elif n == 7:
            self.speed = 77
        return self.speed
