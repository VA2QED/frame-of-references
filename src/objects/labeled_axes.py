from manim import *
import numpy as np


# Instead of using the built-in Axes, define a separate class to represents Axes for the purpose of the position and
# orientation visualisation.
# This is because that the built-in Axes class only supports arrows on two directions (x+ and y+), and only supports
# labels there.
# To not be restricted (and to increase my labour intensity of having to do coordinates calculations manually), the
# LabeledAxes class is made such that a set of Axes with four arrows can be created supporting labels on all 4 sides.
# The class extends VGroup, which allows a collection of MObjects to be controlled together.
class LabeledAxes(VGroup):
    def __init__(self, size: float, up_label="", down_label="", left_label="", right_label=""):
        super().__init__()

        origin = np.array([0, 0, 0])

        self.up_arrow = Arrow(origin, np.array([0, size, 0]), buff=0)
        self.up_label = Text(up_label).scale(0.8).next_to(self.up_arrow.end, direction=UP)

        self.down_arrow = Arrow(origin, np.array([0, -size, 0]), buff=0)
        self.down_label = Text(down_label).scale(0.8).next_to(self.down_arrow.end, direction=DOWN)

        self.left_arrow = Arrow(origin, np.array([-size, 0, 0]), buff=0)
        self.left_label = Text(left_label).scale(0.8).next_to(self.left_arrow.end, direction=LEFT)

        self.right_arrow = Arrow(origin, np.array([size, 0, 0]), buff=0)
        self.right_label = Text(right_label).scale(0.8).next_to(self.right_arrow.end, direction=RIGHT)

        self.add(self.up_arrow, self.up_label,
                 self.left_arrow, self.left_label,
                 self.down_arrow, self.down_label,
                 self.right_arrow, self.right_label)

    # Returns an animation group of transforming all four labels.
    def transform_labels(self, new_up_label, new_down_label, new_left_label, new_right_label):
        animation_group = AnimationGroup(
            Transform(self.up_label, new_up_label.scale(0.8)
                      .next_to(self.get_center() + self.up_arrow.end, direction=UP)),
            Transform(self.down_label, new_down_label.scale(0.8)
                      .next_to(self.get_center() + self.down_arrow.end, direction=DOWN)),
            Transform(self.left_label, new_left_label.scale(0.8)
                      .next_to(self.get_center() + self.left_arrow.end, direction=LEFT)),
            Transform(self.right_label, new_right_label.scale(0.8)
                      .next_to(self.get_center() + self.right_arrow.end, direction=RIGHT))
        )

        return animation_group

    # Use the parent implementation of the abstract method.
    def align_points_with_larger(self, larger_mobject):
        super(LabeledAxes, self).align_points_with_larger(larger_mobject)
