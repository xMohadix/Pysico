from GUI import Application
import math
import matplotlib.pyplot as plt

# Constants
DRAG_COEFFICIENT = 0.47
DIAMETER = 1

setting = None

class Body:
    def __init__(self, art):
        self._name = art[0]
        self._mass = float(art[1])
        self._initial_velocity_i = float(art[2])
        self._initial_velocity_j = float(art[3])
        self._x = float(art[6])
        self._y = float(art[7])

        self._force_i = self.find_force(self._mass, float(art[4]))
        self._force_j = self.find_force(self._mass, float(art[5]))
        self._force = self.find_vector(self._force_i, self._force_j)
        self._force_theta = self.find_theta(self._force_i, self._force_j)

        self._net_force_i = self.find_net_force_i(
            self._force_i, self._force_theta, setting, self._initial_velocity_i, self._initial_velocity_j
        )
        self._net_force_j = self.find_net_force_j(
            self._force_j, self._force_theta, setting, self._initial_velocity_j, self._initial_velocity_j
        )

        self._acceleration_i = self.find_acceleration(self._net_force_i, self._mass)
        self._acceleration_j = self.find_acceleration(self._net_force_j, self._mass)
        self._acceleration = self.find_vector(self._acceleration_i, self._acceleration_j)
        self._acceleration_theta = self.find_theta(self._acceleration_i, self._acceleration_j)

        self._time = 0

        self._velocity_i = self.find_velocity(self.acceleration_i, self._initial_velocity_i, self._time)
        self._velocity_j = self.find_velocity(self.acceleration_j, self._initial_velocity_j, self._time)
        self._velocity = self.find_vector(self._velocity_i, self._velocity_j)
        self._velocity_theta = self.find_theta(self._velocity_i, self._velocity_j)

        self._displacement_x = self.find_displacement(self._x, self._initial_velocity_i, self._acceleration_i, self._time)
        self._displacement_y = self.find_displacement(self._y, self._initial_velocity_i, self._acceleration_i, self._time)
        self._coordinate = self.find_coordinate(self._displacement_x, self._displacement_y)

    @classmethod
    def find_vector(cls, i_vector, j_vector):
        vector = i_vector**2 + j_vector**2
        return math.sqrt(vector)

    @classmethod
    def find_theta(cls, i_vector, j_vector):
        theta_rad = math.atan2(j_vector, i_vector)
        return theta_rad

    @classmethod
    def find_coordinate(cls, x, y):
        return (x, y)

    @classmethod
    def find_force(cls, mass, acceleration):
        return mass * acceleration

    @classmethod
    def find_net_force_j(cls, force_j, theta, settings, velocity_j, initial_velocity):
        air = 0
        gravity = 0

        if settings and isinstance(settings, list):
            air = 1 if settings[0] else 0
            gravity = 1 if settings[1] else 0

        initial_velocity = float(initial_velocity)
        velocity_j = float(velocity_j) if velocity_j != "" else initial_velocity

        net = (
            force_j
            + air * (0.5 * DRAG_COEFFICIENT * DIAMETER * float(settings[3][0]) *(velocity_j**2)) * math.sin(math.pi + theta)
            + gravity * float(settings[3][1])
        )
        return net

    @classmethod
    def find_net_force_i(cls, force_i, theta, settings, velocity_i, initial_velocity):
        air = 0

        if settings and isinstance(settings, list):
            air = 1 if settings[0] else 0

        initial_velocity = float(initial_velocity)
        velocity_i = float(velocity_i) if velocity_i != "" else initial_velocity

        net = (
            force_i
            + air * (0.5 * DRAG_COEFFICIENT * DIAMETER * float(settings[3][0]) * (velocity_i**2)) * math.sin(math.pi + theta)
        )
        return net

    @classmethod
    def find_acceleration(cls, net_force, mass):
        return net_force / mass

    @classmethod
    def find_velocity(cls, acceleration, initial_velocity, time):
        return initial_velocity + acceleration * time

    @classmethod
    def find_displacement(cls, x, initial_velocity, acceleration, time):
        return x + initial_velocity * time + 0.5 * acceleration * time**2

    def pass_time(self, time_step=0.001):
        self._time += time_step
        self._acceleration_i = self.find_acceleration(self._net_force_i, self._mass)
        self._acceleration_j = self.find_acceleration(self._net_force_j, self._mass)
        self._velocity_i = self.find_velocity(self.acceleration_i, self._initial_velocity_i, self._time)
        self._velocity_j = self.find_velocity(self.acceleration_j, self._initial_velocity_j, self._time)
        self._displacement_x = self.find_displacement(self._x, self._initial_velocity_i, self.acceleration_i, self._time)
        self._displacement_y = self.find_displacement(self._y, self._initial_velocity_j, self.acceleration_j, self._time)
        self._coordinate = self.find_coordinate(self._displacement_x, self._displacement_y)
        

    @property
    def name(self):
        return self._name

    @property
    def mass(self):
        return self._mass

    @property
    def velocity(self):
        return self._velocity

    @property
    def velocity_i(self):
        return self._velocity_i

    @property
    def velocity_j(self):
        return self._velocity_j

    @property
    def velocity_theta(self):
        return self._velocity_theta

    @property
    def acceleration(self):
        return self._acceleration

    @property
    def acceleration_i(self):
        return self._acceleration_i

    @property
    def acceleration_j(self):
        return self._acceleration_j

    @property
    def acceleration_theta(self):
        return self._acceleration_theta

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def coordinate(self):
        return self._coordinate

    @property
    def force(self):
        return self._force

    @property
    def force_theta(self):
        return self._force_theta

    @property
    def force_i(self):
        return self._force_i

    @property
    def force_j(self):
        return self._force_j

    @property
    def net_force_i(self):
        return self._net_force_i

    @property
    def net_force_j(self):
        return self._net_force_j

    @property
    def time(self):
        return self._time

    @property
    def displacement_x(self):
        return self._displacement_x

    @property
    def displacement_y(self):
        return self._displacement_y

def unpack_settings(a):
    global setting
    setting = []
    config = []
    for i in a:
        setting.append(i["Toggle"])
        config.append(i["Data"])
    setting.append(config)
    if not any(setting):
        setting = False

def unpack_objects(objects):
    if objects:
        return [[objectx[f"{i}"] for i in objectx] for objectx in objects]
    return False

def set_bodies(obj):
    obj = unpack_objects(obj)
    if obj:
        return [Body(i) for i in obj]
    return None
def pass_time(bodies):
    a=[]
    for body in bodies:
        for _ in range(1000):
            body.pass_time()
            dic={body.name:body.coordinate}
            a.append(dic)
        return a                    

def main():
    while True:
        app = Application()
        app.mainloop()
        if app.visual:
            unpack_settings(app.settings)
            bodies = set_bodies(app.objects)
            a=pass_time(bodies)
            print(a)
            
        elif app.graph:
            # For creating the graph of the object's arrtibutes
            objects = app.objects
            settings = app.settings
        elif app.close:
            break

if __name__ == "__main__":
    main()
