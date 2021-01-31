from manim import *
import numpy as np


# Represents a compass object, contains inner and outer circles and a coloured needle.
class Compass(VGroup):
    def __init__(self):
        super().__init__()

        # Using circle layers instead of border to make sure that the border width is consistent.
        self.outer_circle = Circle(radius=1.1).set_stroke(width=0).set_fill(GREY, opacity=1.0)
        self.inner_circle = Circle(radius=1.0).set_stroke(width=0).set_fill(BLUE_E, opacity=1.0)
        self.north_triangle = Polygon([-0.2, 0, 0], [0.2, 0, 0], [0, 0.8, 0]) \
            .set_stroke(width=0).set_fill(RED, opacity=1.0)

        self.south_triangle = Polygon([-0.2, 0, 0], [0.2, 0, 0], [0, -0.8, 0]) \
            .set_stroke(width=0).set_fill(WHITE, opacity=1.0)

        self.add(self.outer_circle, self.inner_circle, self.north_triangle, self.south_triangle)

    # Use the parent implementation of the abstract method.
    def align_points_with_larger(self, larger_mobject):
        super(Compass, self).align_points_with_larger(larger_mobject)
