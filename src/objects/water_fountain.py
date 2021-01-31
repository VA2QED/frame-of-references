from manim import *


class WaterFountain(VGroup):
    def __init__(self):
        super().__init__()

        self.walls = RegularPolygon(n=6).set_fill(GREY, opacity=1.0).set_stroke(width=0).scale(1.2)
        self.water = RegularPolygon(n=6).set_fill(DARK_BLUE, opacity=1.0).set_stroke(width=0)
        self.center = Circle(radius=0.2).set_fill(GREY, opacity=1.0).set_stroke(width=0)

        self.add(self.walls, self.water, self.center)

    # Use the parent implementation of the abstract method.
    def align_points_with_larger(self, larger_mobject):
        super(WaterFountain, self).align_points_with_larger(larger_mobject)
