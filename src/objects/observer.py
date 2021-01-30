from manim import *
from math import *


# The observer is a commonly used object in the animations, thus it will be generalised into a grouped object.
# The observer is a simple combination of a base coloured circle and a triangle indicating its orientation.
class Observer(VGroup):
    def __init__(self, colour=BLUE):
        super().__init__()

        radius = 0.5

        self.base = Circle(radius=radius).set_fill(color=colour, opacity=1.0).set_stroke(color=colour)

        triangle_side_length = sqrt((2 - cos(120 * PI / 180)) * pow(radius, 2))
        triangle_height = sin(60 * PI / 180) * triangle_side_length
        print(triangle_side_length)
        print(triangle_height)
        self.triangle = Triangle().set_width(triangle_side_length) \
            .set_height(triangle_height) \
            .set_fill(color=WHITE, opacity=1.0).set_stroke(color=WHITE) \
            .align_to(self.base, direction=UP)

        self.add(self.base, self.triangle)

    # Use the parent implementation of the abstract method.
    def align_points_with_larger(self, larger_mobject):
        super(Observer, self).align_points_with_larger(larger_mobject)
