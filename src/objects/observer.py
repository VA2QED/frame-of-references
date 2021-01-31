from manim import *
from math import *


# The observer is a commonly used object in the animations, thus it will be generalised into a grouped object.
# The observer is a simple combination of a base coloured circle and a triangle indicating its orientation.
class Observer(VGroup):
    def __init__(self, colour=BLUE):
        super().__init__()

        radius = 0.5

        self.base = Circle(radius=0.5).set_fill(color=colour, opacity=1.0).set_stroke(width=0)

        # Multiplying the radius by a bit to make it larger when calculating the size of the triangle as it is somehow
        # a bit smaller than the circle.
        triangle_side_length = sqrt((2 - cos(120 * PI / 180)) * pow(radius * 1.1, 2))

        # The triangle indicates the orientation of the observer, the observer is facing the direction that the
        # triangle is pointing at.
        self.triangle = Triangle().set_width(triangle_side_length) \
            .set_fill(color=LIGHT_GREY, opacity=1.0).set_stroke(width=0) \
            .align_to(self.base, direction=UP)

        # Since the triangle itself is equilateral, a tip is added to reinforce the idea of the orientation of the
        # observer.
        self.triangle_tip = Triangle().set_width(triangle_side_length / 3) \
            .set_fill(color=WHITE, opacity=1.0).set_stroke(width=0) \
            .align_to(self.base, direction=UP)

        self.add(self.base, self.triangle, self.triangle_tip)

    # In the position and orientation animations, other objects are added into the observer group, this causes the
    # centre of mass of the observer to shift, causing objects that are supposed to be aligned to it to be misaligned.
    # By overriding the critical point method, the observer will always use its core as the centre of mass.
    def get_critical_point(self, direction):
        return self.base.get_critical_point(direction)

    # Use the parent implementation of the abstract method.
    def align_points_with_larger(self, larger_mobject):
        super(Observer, self).align_points_with_larger(larger_mobject)
