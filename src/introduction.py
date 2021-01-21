from manim import *


class SelfIntroduction(Scene):
    def construct(self):
        title = Tex("Frames of References") \
            .scale(3) \
            .set_color_by_gradient(GREEN, YELLOW)
        # TODO: make sure i spell ashmita's name right, yes it's the
        #  same as the names on our portals... but can you be sure???
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
        number_plane = NumberPlane(axis_config={"stroke_width": 4})
        origin = Dot(point=number_plane.coords_to_point(0, 0, 0))
        origin_word = Tex("Origin").next_to(origin, direction=DOWN + LEFT)
        moving_object = Dot(stroke_width=10, color=GREEN).move_to(number_plane.coords_to_point(1, 1, 1))
        coord_x = Tex("$x:$", color=YELLOW).move_to(3 * UP + 4 * RIGHT)
        coord_y = Tex("$y:$", color=YELLOW).next_to(coord_x, direction=DOWN)
        moving_object_coordinate_x = DecimalNumber(1,
                                                   show_ellipsis=False,
                                                   num_decimal_places=3,
                                                   include_sign=True,
                                                   color=YELLOW
                                                   ).next_to(coord_x)
        moving_object_coordinate_y = DecimalNumber(1,
                                                   show_ellipsis=False,
                                                   num_decimal_places=3,
                                                   include_sign=True,
                                                   color=YELLOW
                                                   ).next_to(coord_y)
        moving_object_coordinate_x.add_updater(lambda d: d.set_value(moving_object.get_x()))
        moving_object_coordinate_y.add_updater(lambda d: d.set_value(moving_object.get_y()))

        self.play(ShowCreation(number_plane), run_time=4)
        self.wait()
        self.play(ShowCreation(origin), Write(origin_word))
        self.play(
            Write(coord_x),
            Write(coord_y),
            Write(moving_object_coordinate_x),
            Write(moving_object_coordinate_y),
            ShowCreation(moving_object)
        )

        moving_object_path_1 = Line(number_plane.coords_to_point(1, 1, 0), number_plane.coords_to_point(2, 3, 0))
        moving_object_path_2 = Line(number_plane.coords_to_point(2, 3, 0), number_plane.coords_to_point(-4, -3, 0))
        moving_object_path_3 = Line(number_plane.coords_to_point(-4, -3, 0),
                                    number_plane.coords_to_point(0.420, 0.69, 0))

        self.play(
            # Moving the object along the path of the line moving_object_path_1, pycharm throws an error here
            # nothing to worry about, manim doesn't care.
            MoveAlongPath(moving_object, moving_object_path_1, rate_func=rate_functions.smooth)
        )
        self.wait()
        self.play(
            MoveAlongPath(moving_object, moving_object_path_2, rate_func=rate_functions.smooth)
        )
        self.wait()
        self.play(
            MoveAlongPath(moving_object, moving_object_path_3, rate_func=rate_functions.smooth)

        )
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
        SelfIntroduction.clear(self)
        ReferenceFrameDefWords.construct(self)
        ReferenceFrameDefWords.clear(self)
        ReferenceFrameExample.construct(self)
        ReferenceFrameExample.clear(self)
        InertialReferenceFrameDisclaimer.construct(self)
        InertialReferenceFrameDisclaimer.clear(self)
