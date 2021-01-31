from manim import *
from objects.point2d import Point2D
import numpy as np
from math import *


# Represents the path from an origin to a point, drawing horizontal and vertical lines parallel and perpendicular
# to the graph's axes to show the distance in each dimension.
class PathLines(VGroup):
    def __init__(self, target: Point2D):
        super().__init__()

        origin = np.array([0, 0, 0])
        target_coords = np.array([target.x, target.y, 0])

        self.horizontal_axis_line = Line(origin, np.array([target.x, 0, 0])).set_color(YELLOW)
        self.vertical_axis_line = Line(origin, np.array([0, target.y, 0])).set_color(YELLOW)

        self.horizontal_line_to_object = DashedLine(np.array([0, target.y, 0]), target_coords)
        self.vertical_line_to_object = DashedLine(np.array([target.x, 0, 0]), target_coords)

        # Orient the braces to not get in the way of the graph.
        # Use absolute values to indicate distance.
        if target.y < 0:
            self.horizontal_brace = BraceLabel(self.horizontal_axis_line, abs(target.x).__str__(), brace_direction=UP)
        else:
            self.horizontal_brace = BraceLabel(self.horizontal_axis_line, abs(target.x).__str__(), brace_direction=DOWN)

        if target.x < 0:
            self.vertical_brace = BraceLabel(self.vertical_axis_line, abs(target.y).__str__(), brace_direction=RIGHT)
        else:
            self.vertical_brace = BraceLabel(self.vertical_axis_line, abs(target.y).__str__(), brace_direction=LEFT)

        self.add(self.horizontal_axis_line, self.vertical_axis_line,
                 self.horizontal_line_to_object, self.vertical_line_to_object,
                 self.horizontal_brace, self.vertical_brace)

    # Use the parent implementation of the abstract method.
    def align_points_with_larger(self, larger_mobject):
        super(PathLines, self).align_points_with_larger(larger_mobject)