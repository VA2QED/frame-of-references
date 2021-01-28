from manim import *
import numpy as np


class TitleScreen(Scene):
    def construct(self):
        title = Text("Relative Motion").scale(2).set_color_by_gradient(BLUE, RED)
        self.play(Write(title))
        self.wait()


# TODO: the eye illustration is an object of class ImageMObject so a lot of animation things aren't available
#  I find the sudden snap into existence of the things to be very jarring. I'm somehow going to find a way
#  to have it fade in instead.
class DemonstrationOfRelativeMotion(Scene):
    def construct(self):
        """
        a number line contains a stationary observer
        and a car ontop of the number line,
        the car will move to the right along with the object.
        There will be two observers
        """
        # Setting up number line
        number_line = NumberLine(color=WHITE, include_numbers=True, include_tip=True)
        label = Tex("$x$")
        label.move_to(np.array([6.5, -0.75, 0]))

        # setting up stationary observer
        stationary_observer = ImageMobject("./assets/manim/eye.png")
        stationary_observer.scale(0.4).move_to(np.array([0, 2, 0])).set_color(RED)

        # setting up moving car, observer, and ball
        car = Rectangle(height=0.5, width=1, fill_opacity=1, fill_color=WHITE)
        # the car will be moved around and the observer and the ball will follow it in an updater
        car.move_to(np.array([number_line.point_to_number(-4), 0.5, 0]))
        moving_car_path = Line(start=np.array([-4, 0.5, 0]), end=np.array([5, 0.5, 0]))

        # value to indicate the position of the car
        position_label = Tex("$x=$")
        position_label.move_to(np.array([4, 3, 0]))
        position_number = DecimalNumber(-4, include_sign=True, num_decimal_places=3, show_ellipsis=True)
        position_number.next_to(position_label, direction=RIGHT)
        position_number.add_updater(lambda d: d.set_value(car.get_x()))

        # value to indicate the time elapsed
        time_label = Tex("$t=$")
        time_label.next_to(position_label, direction=DOWN)
        time_number = DecimalNumber(0, num_decimal_places=3, show_ellipsis=True, unit="s")
        time_number.next_to(time_label, direction=RIGHT)
        # I'm sorry, I can't think of a better way of keeping track of time other than keeping track of
        # the position of an object move from 0 to 4 on the number line.
        time_dot = Dot(ORIGIN, fill_opacity=0)  # you don't see anything
        time_number.add_updater(lambda d: d.set_value(time_dot.get_x()))
        time_dot_path = Line(np.array([0, 0, 0]), np.array([4, 0, 0]))

        # adding observer and ball
        ball = Circle(radius=0.2, color=GREEN, fill_opacity=1, fill_color=GREEN)
        ball.move_to(np.array([-4, 0.85, 0]))

        moving_observer = ImageMobject("./assets/manim/eye.png")
        moving_observer.move_to(np.array([-4 - 0.75, 0.85, 0])).set_color(BLUE)
        moving_observer.scale(0.2)

        # adding updater for ball and moving observer, notice -0.75 for the x position of moving observer, it follows
        # the ball by a bit behind
        ball.add_updater(lambda d: d.move_to(np.array([car.get_x(), 0.85, 0])))
        moving_observer.add_updater(lambda d: d.move_to(np.array([car.get_x()-0.75, 0.85, 0])))

        # Adding number line
        self.play(ShowCreation(number_line))
        self.play(Write(label))
        self.wait()
        # Adding stationary object
        self.play(FadeIn(stationary_observer))
        self.wait()
        # adding car and position label
        self.play(ShowCreation(car))
        self.play(ShowCreation(ball))
        self.play(Write(position_label), Write(position_number))
        self.wait()
        # adding moving observer
        self.play(FadeIn(moving_observer))
        self.wait()
        # adding time indicator
        self.play(Write(time_label), Write(time_number))
        self.wait()
        # playing animation
        self.play(
            MoveAlongPath(car, moving_car_path),
            MoveAlongPath(time_dot, time_dot_path),
            rate_func=linear, run_time=4)
        self.wait()


class StationaryPerspective(Scene):
    def construct(self):
        """
        a bracket tracks the ball's position relative to the origin
        """
        # Setting up number line
        number_line = NumberLine(color=WHITE, include_numbers=True, include_tip=True)
        label = Tex("$x$")
        label.move_to(np.array([6.5, -0.75, 0]))

        # setting up observer
        stationary_observer = ImageMobject("./assets/manim/eye.png")
        stationary_observer.scale(0.4).move_to(np.array([-4, 3, 0])).set_color(RED)
        # setting up ball
        ball = Circle(radius=0.2, color=GREEN, fill_opacity=1, fill_color=GREEN)
        ball.move_to(np.array([-4, 0, 0]))
        moving_ball_path = Line(start=np.array([-4, 0, 0]), end=np.array([5, 0, 0]))

        # setting up a brace that tracks the position of the ball
        brace_to_ball = Brace(Line(np.array([0, -1, 0]), np.array([-4, -1, 0])), direction=DOWN)
        brace_to_ball.add_updater(lambda d: d.become(Brace(Line(np.array([ball.get_x(), -1, 0]), ORIGIN))))

        # setting up a number that tracks the position
        ball_position = DecimalNumber(-4, num_decimal_places=3, include_sign=True, show_ellipsis=True)
        ball_position.next_to(brace_to_ball, direction=DOWN)
        ball_position.add_updater(lambda d: d.set_value(ball.get_x()))
        ball_position.add_updater(lambda d: d.next_to(brace_to_ball, direction=DOWN))

        # adding number line
        self.play(ShowCreation(number_line))
        self.play(Write(label))
        self.wait()
        # adding ball, brace and the number for the ball's position
        self.play(ShowCreation(ball), ShowCreation(brace_to_ball), Write(ball_position))
        self.play(FadeIn(stationary_observer))
        self.wait()
        # playing animation
        self.play(MoveAlongPath(ball, moving_ball_path), rate_func=linear, run_time=4)
        self.wait()


# this scene may be quite repetitive, we can just go straight to the hiding number line scene

# This one will play with the camera focusing on the car, it is meant to give a general idea
# on the motion of the ball that is relative to blue, the next scene will remove the number line
# to show that blue really has no idea that the ball is moving relative to something else
"""
class MovingPerspective(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):

        # same as before, except moving perspective and is Moving Camera Scene
        
        # Setting up number line
        number_line = NumberLine(color=WHITE, include_numbers=True, include_tip=True)
        label = Tex("$x$")
        label.move_to(np.array([6.5, -0.75, 0]))

        # setting up camera
        self.camera_frame.save_state()

        # setting up ball
        ball = Circle(radius=0.2, color=GREEN, fill_opacity=1, fill_color=GREEN)
        ball.move_to(np.array([-4, 0.5, 0]))
        moving_ball_path = Line(start=np.array([-4, 0.5, 0]), end=np.array([5, 0.5, 0]))

        # setting up moving observer
        moving_observer = ImageMobject("./assets/manim/eye.png")
        moving_observer.move_to(np.array([-4 - 0.75, 0.85, 0])).set_color(BLUE)
        moving_observer.scale(0.2)
        moving_observer.add_updater(lambda d: d.next_to(ball, direction=1.5*LEFT))

        # adding numberline
        self.play(ShowCreation(number_line))
        self.add(label)
        self.wait()
        # TODO: make camera zoom ins less janky.
        self.play(self.camera_frame.animate.scale(0.5).move_to(ball))
        # adding ball
        self.play(ShowCreation(ball))
        self.add(moving_observer)
        self.wait()
        # moving camera
        self.camera_frame.add_updater(lambda d: d.move_to(ball.get_center()))
        # moving object
        self.play(MoveAlongPath(ball, moving_ball_path), rate_func=linear, run_time=4)
        self.play(Restore(self.camera_frame))  # considering not zooming out
"""


class MovingPerspectiveHideNumberLine(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        """
        same as before, except
        """
        # Setting up number line
        number_line = NumberLine(color=WHITE, include_numbers=True, include_tip=True)
        label = Tex("$x$")
        label.move_to(np.array([6.5, -0.75, 0]))

        # setting up camera
        self.camera_frame.save_state()

        # setting up ball
        ball = Circle(radius=0.2, color=GREEN, fill_opacity=1, fill_color=GREEN)
        ball.move_to(np.array([-4, 0.5, 0]))

        # setting up moving observer
        moving_observer = ImageMobject("./assets/manim/eye.png")
        moving_observer.move_to(np.array([-4 - 0.75, 0.5, 0])).set_color(BLUE)
        moving_observer.scale(0.2)

        # value to indicate the time elapsed
        time_label = Tex("$t=$")
        time_label.next_to(moving_observer, direction=UP)
        time_number = DecimalNumber(0, num_decimal_places=3, show_ellipsis=True, unit="s")
        time_number.next_to(time_label, direction=RIGHT)
        # I'm sorry, I can't think of a better way of keeping track of time other than keeping track of
        # the position of an object move from 0 to 4 on the number line.
        time_dot = Dot(ORIGIN, fill_opacity=0)  # you don't see anything
        time_number.add_updater(lambda d: d.set_value(time_dot.get_x()))
        time_dot_path = Line(np.array([0, 0, 0]), np.array([4, 0, 0]))

        # adding number line
        self.play(ShowCreation(number_line))
        self.play(Write(label))
        self.wait()
        # zooming in
        self.play(self.camera_frame.animate.scale(0.5).move_to(ball))
        # adding ball and observer
        self.play(ShowCreation(ball))
        self.play(FadeIn(moving_observer))
        self.wait()
        # moving camera
        self.camera_frame.add_updater(lambda d: d.move_to(ball.get_center()))
        self.play(Write(time_label), Write(time_number))
        # If you are reading this code, think about why I didn't need to animate the ball moving
        # removing number line
        self.play(FadeOutAndShift(number_line, direction=DOWN))
        self.play(MoveAlongPath(time_dot, time_dot_path), rate_func=linear, run_time=4)
        self.wait()
        self.play(Restore(self.camera_frame))  # considering not zooming out
        self.wait()


# this scene visualises the different reference frame of the moving observer
class OwnReferenceFrame(Scene):
    def construct(self):
        """
        there will be a main number line present and then another number line indicating the reference frame of the
        observer shows up ontop of the observer.
        """
        number_line = NumberLine(color=GREY,
                                 x_min=-1,
                                 x_max=2,
                                 number_at_center=0.5,
                                 unit_size=3,
                                 include_ticks=False,
                                 include_tip=True,
                                 include_numbers=False,
                                 )
        moving_observer = ImageMobject("./assets/manim/eye.png")
        moving_observer.move_to(np.array(1.8*LEFT + UP))

        ball = Circle(radius=0.2, color=GREEN, fill_opacity=1, fill_color=GREEN)
        ball.next_to(moving_observer, direction=2.25*RIGHT)

        moving_observer.set_color(BLUE)
        moving_observer.scale(0.2)

        label = Tex("$x'$")  # \prime looks ridiculously large on the x lmao, so an apostrophe will suffice
        label.move_to(np.array([3.5, -0.75, 0]))

        self.play(ShowCreation(number_line), Write(label))
        self.play(FadeIn(moving_observer), ShowCreation(ball))
        self.wait()
