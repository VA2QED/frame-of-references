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
        self.play(ShowCreation(number_line))
        self.add(label)
        self.wait()

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

        # adding observer and ball
        ball = Circle(radius=0.2, color=GREEN, fill_opacity=1, fill_color=GREEN)
        ball.move_to(np.array([-4, 0.85, 0]))

        moving_observer = ImageMobject("./assets/manim/eye.png")
        moving_observer.move_to(np.array([-4 - 0.75, 0.85, 0])).set_color(BLUE)
        moving_observer.scale(0.2)

        # adding updater for ball and moving observer, notice plus or minus 0.4 for the x position,
        # this is to ensure the observer is left of the car and ball is right of the car at all times
        ball.add_updater(lambda d: d.move_to(np.array([car.get_x(), 0.85, 0])))
        moving_observer.add_updater(lambda d: d.move_to(np.array([car.get_x()-0.75, 0.85, 0])))

        self.add(stationary_observer)
        self.wait()
        self.play(ShowCreation(car))
        self.play(ShowCreation(position_label), ShowCreation(position_number))
        self.wait()
        self.add(moving_observer)
        self.play(ShowCreation(ball))
        self.wait()
        self.play(MoveAlongPath(car, moving_car_path), rate_func=linear, run_time=4)
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
        self.play(ShowCreation(number_line))
        self.add(label)
        self.wait()

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

        self.play(ShowCreation(ball), ShowCreation(brace_to_ball), ShowCreation(ball_position))
        self.add(stationary_observer)
        self.wait()
        self.play(MoveAlongPath(ball, moving_ball_path), rate_func=linear, run_time=4)
        self.wait()


class MovingPerspective(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        """
        same as before, except moving perspective and is Moving Camera Scene
        """
        # Setting up number line
        number_line = NumberLine(color=WHITE, include_numbers=True, include_tip=True)
        label = Tex("$x$")
        label.move_to(np.array([6.5, -0.75, 0]))
        self.play(ShowCreation(number_line))
        self.add(label)
        self.wait()

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

        # TODO: make camera zoom ins less janky.
        self.play(self.camera_frame.animate.scale(0.5).move_to(ball))
        self.play(ShowCreation(ball))
        self.add(moving_observer)
        self.wait()

        self.camera_frame.add_updater(lambda d: d.move_to(ball.get_center()))

        self.play(MoveAlongPath(ball, moving_ball_path), rate_func=linear, run_time=4)
        self.play(Restore(self.camera_frame))


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
        self.play(ShowCreation(number_line))
        self.add(label)
        self.wait()

        # setting up camera
        self.camera_frame.save_state()

        # setting up ball
        ball = Circle(radius=0.2, color=GREEN, fill_opacity=1, fill_color=GREEN)
        ball.move_to(np.array([-4, 0.5, 0]))

        # setting up moving observer
        moving_observer = ImageMobject("./assets/manim/eye.png")
        moving_observer.move_to(np.array([-4 - 0.75, 0.5, 0])).set_color(BLUE)
        moving_observer.scale(0.2)

        self.play(self.camera_frame.animate.scale(0.5).move_to(ball))
        self.play(ShowCreation(ball))
        self.add(moving_observer)
        self.wait()
        self.camera_frame.add_updater(lambda d: d.move_to(ball.get_center()))

        # If you are reading this code, think about why I didn't need to animate the ball moving
        self.remove(number_line)
        self.wait(6)
        self.play(Restore(self.camera_frame))
        self.wait()
