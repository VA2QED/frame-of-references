from manim import *

from objects.labeled_axes import *
from objects.observer import *
import numpy as np


class TitleScreen(Scene):
    def construct(self):
        title = Text("Relative Motion").scale(2).set_color_by_gradient(BLUE, RED)
        self.play(Write(title))
        self.wait()


# a number line contains a stationary observer
# and a car ontop of the number line,
# the car will move to the right along with the object.
# There will be two observers
class DemonstrationOfRelativeMotion(Scene):
    def construct(self):
        # Setting up number line
        number_line = NumberLine(color=WHITE, include_numbers=True, include_tip=True)
        label = Tex("$x$")
        label.move_to(np.array([6.5, -0.75, 0]))

        # setting up stationary observer
        stationary_observer = Observer(colour=RED)
        stationary_observer.scale(0.8).move_to(np.array([0, 2, 0]))
        stationary_observer.rotate(PI)

        moving_observer = Observer(colour=BLUE)
        moving_observer.scale(0.4).move_to(np.array([-4 - 0.75, 0.85, 0]))
        moving_observer.rotate(-PI / 2)
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

        # adding ball
        ball = Circle(radius=0.2, color=GREEN, fill_opacity=1, fill_color=GREEN)
        ball.move_to(np.array([-4, 0.85, 0]))

        # adding updater for ball and moving observer, notice -0.75 for the x position of moving observer, it follows
        # the ball by a bit behind
        ball.add_updater(lambda d: d.move_to(np.array([car.get_x(), 0.85, 0])))
        moving_observer.add_updater(lambda d: d.move_to(np.array([car.get_x() - 0.75, 0.85, 0])))

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
        stationary_observer = Observer(colour=RED)
        stationary_observer.scale(0.8).move_to(np.array([-4, 3, 0])).rotate(PI)
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


class MovingPerspectiveHideNumberLine(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
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
        moving_observer = Observer(colour=BLUE)
        moving_observer.move_to(np.array([-4 - 0.75, 0.5, 0]))
        moving_observer.scale(0.4).rotate(-PI / 2)

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


class Confusion(Scene):
    def construct(self):
        stationary_observer = Observer(colour=RED)
        stationary_observer.scale(0.8).move_to(2 * RIGHT)

        moving_observer = Observer(colour=BLUE)
        moving_observer.scale(0.8).move_to(2 * LEFT)

        question_marks = [
            Text("?").next_to(stationary_observer, direction=UP),
            Text("?").next_to(moving_observer, direction=UP)
        ]

        self.add(stationary_observer, moving_observer)
        self.wait()
        self.play(Write(question_marks[0]), Write(question_marks[1]))
        self.wait()


class ExplanationOfConflict(Scene):
    def construct(self):
        # this is the same scene as the one initially given but the moving observer has its own reference frame.

        # setting up stationary observer
        stationary_observer = Observer(colour=RED)
        stationary_observer.scale(0.8).move_to(np.array([0, 2, 0])).rotate(PI)

        # moving observer
        moving_observer = Observer(colour=BLUE)
        moving_observer.move_to(np.array([-4 - 0.75, 0.85, 0]))
        moving_observer.scale(0.4).rotate(-PI / 2)

        # adding ball
        ball = Circle(radius=0.2, color=GREEN, fill_opacity=1, fill_color=GREEN)
        ball.move_to(np.array([-4, 0.85, 0]))

        # Setting up number lines
        stationary_number_line = NumberLine(color=WHITE, include_numbers=True, include_tip=True)
        stationary_axis_label = Tex("$x$")
        stationary_axis_label.move_to(np.array([6.5, -0.75, 0]))

        moving_number_line = NumberLine(color=DARK_GREY, include_numbers=False, include_tip=True).scale(0.4)
        moving_number_line.move_to(moving_observer)
        moving_axis_label = Tex("$x'$")

        moving_axis_label.add_updater(lambda d: d.next_to(moving_number_line, direction=RIGHT + 0.5 * DOWN))
        moving_number_line.add_updater(lambda d: d.move_to(moving_observer))

        # setting up position labels for the two reference frames
        stationary_position_value_label = Tex("$x=$").move_to(np.array([4, 3, 0]))
        stationary_position_value = DecimalNumber(-4, num_decimal_places=3, include_sign=True, show_ellipsis=True)
        stationary_position_value.next_to(stationary_position_value_label, direction=RIGHT)
        stationary_position_value.add_updater(lambda d: d.set_value(ball.get_x()))

        moving_position_value_label = Tex("$x'=$").next_to(stationary_position_value_label, direction=DOWN)
        moving_position_value = DecimalNumber(0.75, num_decimal_places=3, include_sign=True, show_ellipsis=True)
        # No need to add an updater for the moving position value because it never changes, but don't tell anyone
        moving_position_value.next_to(moving_position_value_label, direction=RIGHT)

        # setting up moving car
        car = Rectangle(height=0.5, width=1, fill_opacity=1, fill_color=WHITE)
        # the car will be moved around and the observer and the ball will follow it in an updater
        car.move_to(np.array([stationary_number_line.point_to_number(-4), 0.5, 0]))
        moving_car_path = Line(start=np.array([-4, 0.5, 0]), end=np.array([5, 0.5, 0]))
        moving_number_line = NumberLine(color=WHITE, include_tip=True).scale(0.4).move_to(moving_observer)

        # adding updater for ball moving number line and moving observer, notice -0.75 for the x
        # position of moving observer, it follows the ball by a bit behind
        ball.add_updater(lambda d: d.move_to(np.array([car.get_x(), 0.85, 0])))
        moving_observer.add_updater(lambda d: d.move_to(np.array([car.get_x() - 0.75, 0.85, 0])))
        moving_number_line.add_updater(lambda d: d.move_to(moving_observer))
        moving_axis_label.add_updater(lambda d: d.next_to(moving_number_line, direction=RIGHT + 0.5 * DOWN))
        # self.add() now because we have seen the animations before
        self.add(stationary_axis_label, stationary_observer, car, ball, moving_observer, stationary_number_line)
        self.wait()
        self.play(ShowCreation(moving_number_line), Write(moving_axis_label))
        self.play(Write(stationary_position_value_label),
                  Write(stationary_position_value),
                  Write(moving_position_value),
                  Write(moving_position_value_label))
        self.wait()
        self.play(MoveAlongPath(car, moving_car_path), rate_func=linear, run_time=4)
        self.wait()


class WhichReferenceFrame(Scene):
    def construct(self):
        # stationary or moving observer?
        stationary_observer = Observer(colour=RED).move_to(LEFT)
        moving_observer = Observer(colour=BLUE).move_to(RIGHT)
        or_text = Text("or")
        question_mark = Text("?").next_to(moving_observer, direction=RIGHT)

        self.play(ShowCreation(stationary_observer), ShowCreation(moving_observer))
        self.play(Write(or_text), Write(question_mark))
        self.wait()
        self.clear()

        # side note, MarkupText is the preferred class for coloured text by the manim community
        # the Text class and the text2color parameter is just broken
        # here, try it for yourself
        # relative = Text('Motion is relative', t2c={'relative':GREEN})

        relative = MarkupText('Motion is <color col="GREEN">relative</color>')
        self.play(Write(relative))
        self.wait()
