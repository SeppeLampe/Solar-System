"""
Combined.py
Date: 23/1/20
Authors:
Seppe Lampe
Petio Todorov

This is a simplified model of the Solar System created
using the Vpython library. The program calculates
the forces between the celestial bodies in the system
in order calculate the position of each body
as a function of time.

Use the Main.py program to run the simulation.
"""
from math import *
from vpython import *
G = 6.67 * 10 ** -11

"""
General Notes:

All mass has units of kg
All radii have units of meters
orbitalPeriod is the orbital period, in Earth days (86400 seconds)
"""


class CelestialBody:
    """CelestialBody is the superclass of all types of celestial bodies"""
    def __init__(self, mass, radius, color, name):
        self.mass = mass
        self.radius = radius
        self.color = color
        self.name = name


class Star(CelestialBody):
    """
    A star is a celestial body without a parent. The properties of the Sun of our Solar System
    are set as the default arguments.
    """
    def __init__(self, mass=1.989 * 10**30, radius=6.95 * 10**8, color=color.yellow, name = "Sun"):
        super(Star, self).__init__(mass, radius, color, name)



class Satellite(CelestialBody):
    """
    This is a class that represents a body which revolves around another body.
    Parameters:
        parent (CelestialBody): is the object that the body revolves around
        distanceToParent (double): distance (in meters) between the body and the parent
        orbital period (float): is the orbital period of the body around the parent (in Earth days (86400 seconds))
        inclination (float): this is the angle (in degrees) between the plane in which
        the body revolves and the plane going through the central axes (xy) of the parent
    """
    def __init__(self, mass, radius, color, name, parent, distanceToParent, orbitalPeriod,
                 inclination=0.0):  # orbitalPeriod is the orbital period, in Earth days (86400 seconds)
        super(Satellite, self).__init__(mass, radius, color, name)
        self.parent = parent
        self.distanceToParent = distanceToParent
        self.orbitalPeriod = orbitalPeriod
        self.inclination = radians(inclination)



def gforce(body1, body2):
    """
    NOTE:
    This function is adapted from the following source:
    https://www.glowscript.org/#/user/wlane/folder/Let'sCodePhysics/program/Solar-System-1/edit
    Glowscript is a website that has many relevant examples for Vpython.
    This is a function that calculates the gravitational force exerted between two objects.
    The function computes the force exerted ON body1 BY body2.
    General formula for the force of gravity: Fgravity = G*M1*M2/d^2
    General formula for the force vector: Fvector = F*r^
    Parameters:
        body1 (CelestialBody): is a celestial body
        body2 (CelestialBody): is a celestial body which is not the same body as body1
    """
    dvector = body1.pos - body2.pos                     # Calculate distance vector between p1 and p2.
    d = mag(dvector)                                    # Calculate magnitude of distance vector.
    r_hat = dvector / d                                 # Calculate unit vector of distance vector.
    Fgravity = G * body1.mass * body2.mass / d ** 2     # Calculate force magnitude.
    return Fgravity * r_hat                             # Calculate force vector.


class RevolvingSystem:
    """This class represents a central body with satellites orbiting around it"""
    def __init__(self, centralBody):
        """
        The constructor the Revolving System class.
        It keeps track of the objects in the system using a list, "self.objects".
        The system also has a central body around which all other bodies revolve.
        It also creates a new canvas in which objects can be displayed.
        (Note no objects are added TO THE CANVAS in the constructor.)
        """
        self.canvas = canvas(height=450, width=1000)
        self.objects = []
        self.centralBody = centralBody
        centralBody.momentum = vector(0,0,0)
        centralBody.pos = vector(0,0,0)

    def addSatellite(self, body):
        """
        This is a method that adds a satellite to the RevolvingSystem.
        Because every satellite has a parent (central body), the checkParent
        function is used to check if the parent (central body) of the satellite
        is the same as the central body of the revolving system.
        Otherwise, if the parent of the satellite is the same as the central body of the
        revolving system then we update the bodies position and momentum and also add
        it to the list of objects in the system.
        Parameters:
            body (CelestialBody): is a celestial body to be added to the system
        """
        if not self.checkParent(body):
            print("body has the wrong parent")
        else:
            self.generatePos(body)
            self.generateMomentum(body)
            self.objects.append(body)

    def checkParent(self, body):
        """
        This method checks if this particular body can be added to this particular
        revolving system. It does so by recursively checking if the parent of the body
        is the same as the central of the revolving system. (Imagine multiple layers of
        nesting.)

        Base Case:
        If the parent of the body is the same as the central body of the system,
        then the function returns True.
        If the parent of the body is a star and it is not the same as the central body of this
        revolving system, then the function returns False. For example, because Pluto is a
        planet which revolves around the sun (parent) we should not be able to add it to a
        revolving system where Jupiter is the central body.

        Recursive Call:
        In the case where the parent is not the same as the central body of the system
        and where the parent is also not a Star, then we run checkParent on the parent.
        For example, what happens if we want to add the moon to the Solar System? The parent
        of the moon is the Earth and the central body of the system is the Sun. The moon's parent
        is not the sun, so the first if condition is False. The moon's parent is also not a Star,
        it's a planet, so the second if condition is False. Finally we run checkParent on the moon's
        parent (i.e. the Earth). There the first if condition is True because the parent of the earth
        is the sun so the function returns True meaning that it's acceptable for this body
        to be added to this revolving system.

        Parameters:
            body (CelestialBody): is a celestial body to be added to the system
        """
        if body.parent == self.centralBody:
            return True
        if isinstance(body.parent, Star):
            return False
        return self.checkParent(body.parent)

    def generatePos(self, body):
        """
        This method generates the initial position of each body in the Revolving System.
        The position is based on the distance to its parent body and its inclination relative
        to the parent body.

        Parameters:
            body (CelestialBody): is a celestial body
        """
        if self.centralBody == body.parent:
            body.pos = vector(body.distanceToParent * cos(body.inclination), 0,
                            body.distanceToParent * sin(body.inclination))
        else:
            if body.parent.pos == vector(0,0,0):
                self.generatePos(body.parent)
            body.pos = body.parent.pos + vector(body.distanceToParent * cos(body.inclination), 0,
                            body.distanceToParent * sin(body.inclination))

    def generateMomentum(self, body):
        """
        This method generates the initial momentum of each body in the Revolving System.
        The momentum is based on the distance to its parent body, the current body's mass
        and the current body's orbital period around its parent.

        Parameters:
            body (CelestialBody): is a celestial body
        """
        if self.centralBody == body.parent:
            body.momentum = vector(0, body.mass * ((body.distanceToParent * 2 * pi) / (body.orbitalPeriod * 86400)), 0)
        else:
            if body.parent.pos == vector(0, 0, 0):
                self.generateMomentum(body.parent)
            body.momentum = body.parent.momentum / body.parent.mass * body.mass + vector(0, body.mass * (
                        (body.distanceToParent * 2 * pi) / (body.orbitalPeriod * 86400)), 0)

    def show(self, body):
        """
        This method shows the body on the canvas. It does so by creating a Vpython sphere object.
        Calling the sphere vpython function automatically creates the sphere physically on the canvas.

        Parameters:
            body (CelestialBody): is a celestial body
        """
        body.visualisation = sphere(pos=body.pos, radius=body.radius, color=body.color,
                                          mass=body.mass, momentum=body.momentum, force=vector(0,0,0), make_trail=True, name=body.name)

    def simulate(self, dt):
        """
        This is the fundamental method for showing and then updating the position of bodies in the revolving
        system on the canvas.

        First the method shows every body in the objects list of the revolving system on the canvas.
        Then there is an infinite loop (which ends only when the user closes the simulation browser window).
        Otherwise, the simulation continues to run indefinitely. In this loop, the forces, momentum, and then
        position are updated for every object in the solar system except for the central body which remains
        stationary.

        An important element of the simulation method is the rate(100) function call. This is a function which
        controls the animation speed of the canvas. In our case it will recompute the position only once every
        0.01 seconds. The following link is the documentation of the Vpython rate function:
        https://www.glowscript.org/docs/VPythonDocs/rate.html

        Parameters:
            dt (float): is the current time step of the simulation (units Earth days/second)
        """
        # This converts the time step from Earth days to seconds.
        # Normally this would mean multiplying it by 3600*24 but here we multiply it by 36*24.
        # As the loop is later executed 100 times per second, defined by the rate(100).
        dt *= 36 * 24
        for x in range(len(self.objects)):
            self.show(self.objects[x])
        self.show(self.centralBody)
        while True:
            rate(100)
            for x in range(len(self.canvas.objects)):
                # This if statement is to prevent the sun from calculating a force which results eventually in a slight,
                # continuous position shift for the sun
                if self.canvas.objects[x].name != self.centralBody.name:
                    self.updateForce(self.canvas.objects[x])
                    self.updateMomentum(self.canvas.objects[x], dt)
            self.updatePositions(dt)

    def updateForce(self, body):
        """
        This method computes the force on the input parameter body, by summing the forces on it from
        all other bodies of the revolving system which are shown on the canvas, except for the body itself.

        self.canvas.objects is a list of all of the objects shown on the Vpython canvas.

        Parameters:
            body (CelestialBody): is a celestial body

        """
        body.force = vector(0, 0, 0)
        for x in range(len(self.canvas.objects)):
            if self.canvas.objects[x] != body:
                body.force += gforce(self.canvas.objects[x], body)

    def updateMomentum(self, body, dt):
        """
        This method computes the change in momentum on the input parameter body at a particular time step, dt.
        This is based on the formula F=ma where a = dv/dt so F = m*(dv/dt) so F*(dt) = m*(dv) = momentum.

        Parameters:
            body (CelestialBody): is a celestial body
            dt (float): is the current time step of the simulation
        """
        body.momentum += body.force * dt

    def updatePositions(self, dt):
        """
        This method computes the updated position of all objects on the canvas of this revolving system
        for this current simulation time step, dt.

        It does so by adding the change in position, momentum divided by mass multiplied by the time step, to
        the current position of the object on the canvas.

        Parameters:
            dt (float): is the current time step of the simulation
        """
        for x in range(len(self.canvas.objects)):
            self.canvas.objects[x].pos += self.canvas.objects[x].momentum / self.canvas.objects[x].mass * dt