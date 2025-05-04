from GUI import Application
import math
import matplotlib.pyplot as plt
setting=None
class Body:   
    def __init__(self,art):
        self._name=art[0]
        self._mass=float(art[1])
        self._velocity_i=float(art[2])
        self._velocity_j=float(art[3])
        self._velocity=self.find_vector(self._velocity_i,self._velocity_j)
        self._velocity_theta=self.find_theta(self._velocity_i,self._velocity_j)
        self._accelaration_i=float(art[4])
        self._accelaration_j=float(art[5])
        self._accelaration=self.find_vector(self._accelaration_i,self._accelaration_j)
        self._accelaration_theta=self.find_theta(self._accelaration_i,self._accelaration_j)
        self._x=float(art[6])
        self._y=float(art[7])
        self._coordinate=self.find_coordinate(self._x,self._y)
        self._force=self.find_force(self._mass,self._accelaration)
        self._force_theta=self._accelaration_theta
        self._force_i=self.find_i(self._force,self._force_theta)
        self._force_j=self.find_j(self._force,self._force_theta)
    @classmethod
    def find_vector(cls,i_vector,j_vector):
        vector=i_vector**2+j_vector**2
        return math.sqrt(vector)
    
    @classmethod
    def find_theta(cls, i_vector, j_vector):
        theta_rad = math.atan2(j_vector, i_vector)
        return (theta_rad)

    @classmethod
    def find_coordinate(cls,x,y):
        return (x,y)
    
    @classmethod
    def find_i(cls,vector,theta):
        return vector*math.cos(theta)
    
    @classmethod
    def find_j(cls,vector,theta):
        return vector*math.sin(theta)
    
    @classmethod
    def find_force(cls,mass,accelaration):
        return mass*accelaration
    
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
    def accelaration(self):
        return self._accelaration
    @property
    def accelaration_i(self):
        return self._accelaration_i
    @property
    def accelaration_j(self):
        return self._accelaration_j
    @property
    def accelaration_theta(self):
        return self._accelaration_theta
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
    
    
def unpack_settings(a):
    global setting
    setting=[]
    config=[]
    for i in a:
       setting.append(i["Toggle"])
       config.append(i["Data"])
    setting.append(config)  
    if not True in setting:
        setting=False

def unpack_objects(objects):
    if objects:
        a=[]
        for objectx in objects:
            b=[]
            for i in objectx:
                b.append(objectx[f"{i}"])
            a.append(b)
        return a 
    else:
        return False

def set_bodies(obj):
    obj=unpack_objects(obj)
    if obj:    
        bodies=[]
        for i in obj:
            a=Body(i)
            bodies.append(a)
        return bodies
    return None


    


def main():
    while True:
        app = Application()
        app.mainloop()  # GUI runs here and closes after start is pressed
        if app.visual:
            unpack_settings(app.settings)
            bodies=set_bodies(app.objects)
            for body in bodies:
                print(f"{body.name}:{calc_displacement(body)}")
        elif app.graph:
            #For creating the Graph of the objects accelaration 
            objects=app.objects
            settings=app.settings
        elif app.close:
            break

if __name__ == "__main__":
    main()