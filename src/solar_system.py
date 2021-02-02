from manim import *
import random
from math import *


def make_planet(radius, colour, distance):
    # Give planets random orientations
    rad = random.random() * 2 * PI
    return Circle(radius=radius).set_fill(colour, opacity=1.0).set_stroke(width=0).shift(
        np.array([distance * cos(rad), distance * sin(rad), 0]))


run_time_in_years = 20
rotate_run_time = 5


def rotate_planet(planet, year_length):
    return Rotating(planet, about_point=np.array([0, 0, 0]),
                    radians=run_time_in_years / rotate_run_time * 365 * 2 * PI / year_length,
                    run_time=rotate_run_time)


class SolarSystem(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
        self.camera_frame.scale(8.0)

    def construct(self):
        sun = Circle(radius=2.0).set_fill(YELLOW, opacity=1.0).set_stroke(width=0)

        mercury = make_planet(0.2, GREY, 3.0)
        venus = make_planet(0.5, YELLOW_E, 4.0)
        earth = make_planet(0.5, BLUE, 5.0)
        mars = make_planet(0.4, RED, 6.0)

        jupiter = make_planet(1.5, GREY_BROWN, 10.0)
        saturn = make_planet(1.2, LIGHT_BROWN, 15.0)

        uranus = make_planet(0.8, BLUE_A, 22.0)
        neptune = make_planet(0.8, DARK_BLUE, 27.0)

        self.add(sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune)
        self.play(rotate_planet(mercury, 88), rotate_planet(venus, 225), rotate_planet(earth, 365),
                  rotate_planet(mars, 687), rotate_planet(jupiter, 4333), rotate_planet(saturn, 10759),
                  rotate_planet(uranus, 30687), rotate_planet(neptune, 60190))

        self.camera_frame.move_to(earth)
        self.add(self.camera_frame)

        self.camera_frame.add_updater(lambda c: c.move_to(earth))

        self.play(rotate_planet(mercury, 88), rotate_planet(venus, 225), rotate_planet(earth, 365),
                  rotate_planet(mars, 687), rotate_planet(jupiter, 4333), rotate_planet(saturn, 10759),
                  rotate_planet(uranus, 30687), rotate_planet(neptune, 60190))
