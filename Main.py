"""
Main.py
Date: 13/1/20
Authors:
Seppe Lampe
Petio Todorov

This is the Main class for our solar System model.

You can run the following three systems separately
by uncommenting each of these sections:
Section 1- The entire Solar System
Section 2- Earth System with moon
Section 3- Jupiter System with moons
"""

from SolarSystemProject import *

"""
General Notes:

All mass has units of kg
All radii have units of meters
orbitalPeriod is the orbital period, in Earth days (86400 seconds)
"""

sun = Star()
mercury = Satellite(mass=3.30 * 10 ** 23, radius=2.439 * 10 ** 6, distanceToParent=0.58 * 10 ** 11, orbitalPeriod=87.969,
                          color=color.white, inclination=3.38, parent = sun, name = "Mercury")
venus = Satellite(mass=4.86 * 10 ** 24, radius=6.051 * 10 ** 6, distanceToParent=1.08 * 10 ** 11, orbitalPeriod=224.70,
                        color=color.yellow, inclination=3.86, parent = sun, name = "Venus")
earth = Satellite(mass=5.97 * 10 ** 24, radius=6.371 * 10 ** 6, distanceToParent=1.50 * 10 ** 11, orbitalPeriod=365.25,
                        color=color.blue, inclination=7.155, parent = sun, name = "Earth")
mars = Satellite(mass=6.4 * 10 ** 23, radius=3.389 * 10 ** 6, distanceToParent=2.27 * 10 ** 11, orbitalPeriod=686.97,
                       color=color.red, inclination=5.65, parent = sun, name = "Mars")
jupiter = Satellite(mass=1.89 * 10 ** 27, radius=6.9911 * 10 ** 7, distanceToParent=7.78 * 10 ** 11,
                          orbitalPeriod=4332.59, color=color.orange, inclination=6.09, parent = sun, name = "Jupiter")
saturn = Satellite(mass=5.68 * 10 ** 26, radius=5.8232 * 10 ** 7, distanceToParent=1.43 * 10 ** 12,
                         orbitalPeriod=10759.22, color=color.white, inclination=5.51, parent = sun, name = "Saturn")
uranus = Satellite(mass=8.68 * 10 ** 25, radius=2.5362 * 10 ** 7, distanceToParent=2.871 * 10 ** 12,
                         orbitalPeriod=30688.5, color=color.blue, inclination=6.48, parent = sun, name = "Uranus")
neptune = Satellite(mass=1.02 * 10 ** 26, radius=2.4622 * 10 ** 7, distanceToParent=4.50 * 10 ** 12, orbitalPeriod=60182,
                          color=color.blue, inclination=6.43, parent = sun, name = "Neptune")

# Pluto was added to the system because it has a more distinct inclination than the planets.
# By visualising Pluto it is clear that the inclination is implemented.
pluto = Satellite(mass=1.30 * 10 * 22, radius=2.376*10**6, distanceToParent=5.9 * 10 ** 12, orbitalPeriod=90560,
                        color=color.white, inclination=11.88, parent = sun, name = "Pluto")


earthMoon = Satellite(mass=7.34 * 10 ** 22, radius=1.737*10**6, distanceToParent=3.84399 * 10 ** 8, orbitalPeriod=27.321,
                 color=color.white, inclination = 1.54, parent=earth, name = "Moon")

ganymede = Satellite(mass=1.48 * 10 ** 23, radius=2.634, distanceToParent=1.07 * 10 ** 9, orbitalPeriod=7.1546,
                color=color.green, inclination = 0.204, parent=jupiter, name = "Ganymede")
io = Satellite(mass=8.931*10**22, radius=1.826*10**6, distanceToParent=4.22*10**8, orbitalPeriod=1.769137786,
                color=color.yellow, inclination = 0.05, parent=jupiter, name = "Io")
europa = Satellite(mass=4.800*10**22, radius=1.56*10**6, distanceToParent=6.71*10**8, orbitalPeriod=3.551181,
                color=color.orange, inclination = 0.471, parent=jupiter, name = "Europa")
callisto = Satellite(mass=1.076*10**23, radius=2.410*10**6, distanceToParent=1.882*10**9, orbitalPeriod=16.6890184,
                color=color.white, inclination = 0.205, parent=jupiter, name = "Callisto")

"""
#Section 1- Entire Solar System

theSystem = RevolvingSystem(sun)
theSystem.addSatellite(mercury)
theSystem.addSatellite(venus)
theSystem.addSatellite(earth)
theSystem.addSatellite(earthMoon)
theSystem.addSatellite(mars)
theSystem.addSatellite(jupiter)
theSystem.addSatellite(ganymede)
theSystem.addSatellite(io)
theSystem.addSatellite(europa)
theSystem.addSatellite(callisto)
theSystem.addSatellite(saturn)
theSystem.addSatellite(uranus)
theSystem.addSatellite(neptune)
theSystem.addSatellite(pluto)
theSystem.simulate(10)
"""

"""
#Section 2- Earth System with moon

earthSystem = RevolvingSystem(earth)
earthSystem.addSatellite(earthMoon)
earthSystem.simulate(1)
"""

"""
#Section 3- Jupiter System with moons

jupiterSystem = RevolvingSystem(jupiter)
jupiterSystem.addSatellite(ganymede)
jupiterSystem.addSatellite(io)
jupiterSystem.addSatellite(europa)
jupiterSystem.addSatellite(callisto)
jupiterSystem.simulate(0.1)
"""

