from manim import *


class SelfIntroduction(Scene):
    def construct(self):
        title = Tex("Frames of References") \
            .scale(3) \
            .set_color_by_gradient(GREEN, YELLOW)
        names = Tex("Ashmita Bhattacharyya, Bokuan Li, Jixin Chen") \
            .set_color(BLUE) \
            .next_to(title, direction=DOWN)

        self.play(Write(title))
        self.wait(2)
        self.play(Write(names))
        self.wait(2)


# TODO: make the bold text coloured
class ReferenceFrameDefWords(Scene):
    def construct(self):
        def_of_fr = Tex("""
                        Definition: A reference frame is composed of an \\\\ 
                        \\textbf{origin} and methods of describing the\\\\ 
                        \\textbf{position} and \\textbf{orientation}
                        of an object \\textbf{relative} to an\\\\ 
                        \\textbf{observer}
                        """).set_color_by_gradient(BLUE, GREEN)
        warning = Tex("""
                    Please note that an observer doesn't have to be \\\\
                    at the \\textbf{origin} of the graph.\\\\
                    However, let us assume that the \\\\
                    observer is at the origin for ease.
                      """).set_color_by_gradient(RED, YELLOW)  # set_color_by_gradient() is so pretty :)
        self.play(Write(def_of_fr))
        self.wait(5)
        self.play(ReplacementTransform(def_of_fr, warning))
        self.wait(5)


class ReferenceFrameExample(Scene):
    def construct(self):
        # Setting up number plane
        number_plane = NumberPlane(axis_config={"stroke_width": 4})
        origin = Dot(point=number_plane.coords_to_point(0, 0, 0))
        origin_word = Tex("Origin").next_to(origin, direction=DOWN + LEFT)

        # Setting up moving object
        moving_object = Dot(stroke_width=10, color=GREEN).move_to(number_plane.coords_to_point(1, 1, 0))
        moving_object_paths = [Line(number_plane.coords_to_point(1, 1, 0), number_plane.coords_to_point(2, 3, 0)),
                               Line(number_plane.coords_to_point(2, 3, 0), number_plane.coords_to_point(-4, -3, 0)),
                               Line(number_plane.coords_to_point(-4, -3, 0), number_plane.coords_to_point(.420, .69, 0))
                               ]

        # Setting up moving object walking distance
        # Change note: instead of using two separate lines for horizontal and vertical braces, use one singular line to
        # cover the entire distance diagonally.
        line_to_moving_object = Line(number_plane.center_point, moving_object.get_center())

        # A horizontally (facing down) oriented brace will cover the bottom of the diagonal line.
        brace_to_moving_object_bottom = Brace(line_to_moving_object, direction=DOWN)
        # A vertically (facing right) oriented brace will cover the right of the diagonal line.
        brace_to_moving_object_right = Brace(line_to_moving_object, direction=RIGHT)

        # During animation, the point will move constantly, thus the two braces are added updaters, which will change
        # their position and size automatically when the point moves.
        # Note that this has to be accomplished by updating the braces directly instead of updating the line and then
        # using the line to update the brace, as the value of the line variable in this scope does not actually change
        # during animation, likely to prevent other bugs.
        brace_to_moving_object_bottom.add_updater(lambda brace: brace.become(
            Brace(Line(number_plane.center_point, moving_object.get_center()), direction=DOWN)))
        brace_to_moving_object_right.add_updater(lambda brace: brace.become(
            Brace(Line(number_plane.center_point, moving_object.get_center()), direction=RIGHT)))

        # Playing number plane
        self.play(ShowCreation(number_plane))
        self.wait()
        self.play(ShowCreation(origin), Write(origin_word))
        self.wait()

        # Playing moving object
        self.play(ShowCreation(moving_object))

        # Playing braces to moving object. Add the braces together instead of individually.
        self.play(ShowCreation(brace_to_moving_object_bottom), ShowCreation(brace_to_moving_object_right))
        self.wait()

        for moving_object_path in moving_object_paths:
            self.play(MoveAlongPath(moving_object, moving_object_path, rate_func=rate_functions.smooth))
            self.wait()


class InertialReferenceFrameDisclaimer(Scene):
    def construct(self):
        no_acceleration = Tex("""
        Inertial reference frames are frames of references\\\\
        that do not experience any types of acceleration.\\\\
        """).set_color_by_gradient(BLUE, GREEN)
        self.play(Write(no_acceleration))
        self.wait(5)


# Use this class to render everything in this file in order.
# don't mind the Expected type 'SelfIntroduction', got 'Everything' instead error
class Everything(Scene):
    def construct(self):
        SelfIntroduction.construct(self)
        self.clear()
        ReferenceFrameDefWords.construct(self)
        self.clear()
        ReferenceFrameExample.construct(self)
        self.clear()
        InertialReferenceFrameDisclaimer.construct(self)
        self.clear()