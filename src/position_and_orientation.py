from objects.labeled_axes import *
from objects.observer import Observer
from objects.point2d import Point2D
from objects.compass import Compass
from objects.pathlines import PathLines
from objects.water_fountain import WaterFountain

from manim import *


class Introduction(Scene):
    def construct(self):
        title = Text("Position and Orientation").set_color_by_gradient(BLUE, ORANGE)
        title.scale(1.5)
        self.play(Write(title))
        self.wait()


class PositionAndOrientation(MovingCameraScene):
    def __init__(self, camera_class=MovingCamera, **kwargs):
        super().__init__(camera_class)
        self.blue_position = Point2D(-5, -1)
        self.orange_position = Point2D(5, -1)

        self.question_position = Point2D(0, 4)

        # Make number planes have a wider reach.
        config.frame_x_radius = 12
        config.frame_y_radius = 9

    def setup(self):
        MovingCameraScene.setup(self)
        self.camera_frame.scale(1.25)

    def construct(self):
        self.create_and_rotate_object()
        self.create_and_show_observers()
        self.create_axes()

        self.pose_question("Which way is the triangle facing?")
        self.wait()

        self.focus_on_blue_observer()
        self.show_blue_observer_axes()
        self.highlight_blue_observer_direction()
        self.hide_blue_observer_axis()
        self.unfocus_on_blue_observer()

        self.focus_on_orange_observer()
        self.show_orange_observer_axes()
        self.highlight_orange_observer_direction()
        self.hide_orange_observer_axis()
        self.unfocus_on_orange_observer()

        self.question_marks_on_observers()
        self.highlight_direction_disagreement()
        self.hide_observer_axes()

        self.hide_scene()

        self.show_compass()
        self.show_compass_axes()
        self.wait()
        self.clear_compass()

        self.unhide_scene()

        self.highlight_question()

        self.show_both_observer_axes()
        self.show_observer_compasses()
        self.change_observer_axes()
        self.highlight_direction_agreement()
        self.hide_observer_axes()

        self.clear_question()
        
        self.pose_question("Where is the triangle?")
        self.wait()

        self.focus_on_blue_observer()
        self.show_blue_grid()
        self.show_blue_distance_lines()
        self.wait(0.5)
        self.recount_blue_distance()
        self.wait(0.5)
        self.hide_blue_distance_lines_and_grid()
        self.unfocus_on_blue_observer()

        self.focus_on_orange_observer()
        self.show_orange_grid()
        self.show_orange_distance_lines()
        self.wait(0.5)
        self.recount_orange_distance()
        self.wait(0.5)
        self.hide_orange_distance_lines_and_grid()
        self.unfocus_on_orange_observer()
        self.show_both_position_texts()

        self.question_marks_on_observers()
        self.highlight_position_disagreement()
        self.hide_both_position_texts()

        self.create_and_show_water_fountain()
        self.shake_water_fountain()

        self.highlight_question()

        self.show_water_fountain_grid()
        self.show_water_fountain_distance_lines()
        self.show_both_position_texts()
        self.change_position_texts()
        self.hide_water_fountain_grid_and_distance_lines()
        self.highlight_position_agreement()

        self.hide_scene_after_fountain()

        self.wait()

    def create_and_rotate_object(self):
        # The object has a z-index of 2, this is to make sure that the axes and lines are not drawn over them.
        triangle = self.triangle = Polygon([-0.5, 0, 0], [0.5, 0, 0], [0, 2, 0]) \
            .scale(0.5).rotate(PI / 2) \
            .set_fill(WHITE, opacity=1.0).set_stroke(width=0) \
            .set_y(2).set_z_index(2)

        self.play(DrawBorderThenFill(triangle, run_time=1))
        self.play(Rotate(triangle, angle=-PI / 2))

    def create_and_show_observers(self):
        # The blue observer is facing right
        blue_observer = self.blue_observer = Observer(BLUE) \
            .set_x(self.blue_position.x).set_y(self.blue_position.y)

        # The orange observer is facing left
        orange_observer = self.orange_observer = Observer(ORANGE) \
            .set_x(self.orange_position.x).set_y(self.orange_position.y)

        # Display the observers
        self.play(DrawBorderThenFill(blue_observer, run_time=1), DrawBorderThenFill(orange_observer, run_time=1))

        # Rotate the observers to their orientation and then wiggle them to highlight it.
        self.play(Rotate(blue_observer, angle=-PI / 2), Rotate(orange_observer, angle=PI / 2))
        self.play(WiggleOutThenIn(blue_observer, n_wiggles=5, rotation_angle=PI / 10),
                  WiggleOutThenIn(orange_observer, n_wiggles=5, rotation_angle=PI / 10))

    def create_axes(self):
        self.blue_axes = LabeledAxes(2, up_label="Left", down_label="Right",
                                     left_label="Back", right_label="Front") \
            .move_to(self.blue_observer)
        self.orange_axes = LabeledAxes(2, up_label="Right", down_label="Left",
                                       left_label="Front", right_label="Back") \
            .move_to(self.orange_observer)

    def pose_question(self, question: str):
        question = self.question = Text(question) \
            .set_x(self.question_position.x) \
            .set_y(self.question_position.y)

        self.play(Write(question))

    def highlight_question(self):
        self.play(Indicate(self.question))

    def clear_question(self):
        self.play(FadeOut(self.question, run_time=0.5))

    def focus_on_blue_observer(self):
        self.camera_frame.save_state()
        # Darken the orange observer and focus the camera near the blue observer.
        self.play(self.orange_observer.animate.set_opacity(0),
                  self.camera_frame.animate.set_x(-2.5).scale(0.9))

    def show_blue_observer_axes(self):
        # Z index doesn't work
        self.bring_to_back(self.blue_axes)

        self.play(FadeInFromPoint(self.blue_axes, self.blue_observer.get_center()))

    def highlight_blue_observer_direction(self):
        self.play(
            # Colour the arrow.
            Indicate(self.blue_axes.up_arrow), Indicate(self.blue_axes.up_label),
            # Colour the triangle
            Indicate(self.triangle))

    def hide_blue_observer_axis(self):
        self.play(FadeOut(self.blue_axes, run_time=0.5))

    def unfocus_on_blue_observer(self):
        self.play(Restore(self.camera_frame), self.orange_observer.animate.set_opacity(1.0))

    def focus_on_orange_observer(self):
        self.camera_frame.save_state()
        self.play(self.blue_observer.animate.set_opacity(0),
                  self.camera_frame.animate.set_x(2.5).scale(0.9))

    def show_orange_observer_axes(self):
        self.bring_to_back(self.orange_axes)

        self.play(FadeInFromPoint(self.orange_axes, self.orange_observer.get_center()))

    def highlight_orange_observer_direction(self):
        self.play(
            # Colour the arrow.
            Indicate(self.orange_axes.up_arrow), Indicate(self.orange_axes.up_label),
            # Colour the triangle
            Indicate(self.triangle))

    def hide_orange_observer_axis(self):
        self.play(FadeOut(self.orange_axes, run_time=0.5))

    def unfocus_on_orange_observer(self):
        self.play(Restore(self.camera_frame), self.blue_observer.animate.set_opacity(1.0))

    def question_marks_on_observers(self):
        blue_question_mark = self.blue_question_mark = Text("?") \
            .next_to(self.blue_observer, direction=np.array([0.5, 0, 0]))
        orange_question_mark = self.orange_question_mark = Text("?") \
            .next_to(self.orange_observer, direction=np.array([-0.5, 0, 0]))

        self.play(FadeInFromPoint(blue_question_mark, blue_question_mark.get_center(), run_time=0.5),
                  FadeInFromPoint(orange_question_mark, orange_question_mark.get_center(), run_time=0.5))
        self.play(WiggleOutThenIn(blue_question_mark, n_wiggles=5, rotation_angle=PI / 10),
                  WiggleOutThenIn(orange_question_mark, n_wiggles=5, rotation_angle=PI / 10))
        self.play(FadeOut(blue_question_mark, run_time=0.5), FadeOut(orange_question_mark, run_time=0.5))

    def highlight_direction_disagreement(self):
        self.bring_to_back(self.blue_axes, self.orange_axes)
        self.play(FadeInFromPoint(self.blue_axes, self.blue_observer.get_center(), run_time=0.5),
                  FadeInFromPoint(self.orange_axes, self.orange_observer.get_center(), run_time=0.5))
        self.play(Indicate(self.blue_axes.up_arrow, run_time=1.5), Indicate(self.blue_axes.up_label, run_time=1.5),
                  Indicate(self.orange_axes.up_arrow, run_time=1.5), Indicate(self.orange_axes.up_label, run_time=1.5))

    def hide_observer_axes(self):
        # Funny enough, when fading out the observer axes the second time, likely due to the fact that the components
        # of the axes are changed through transforms, the axes go on top of the observers.
        # And even more comical, when the axes are placed back with self.bring_to_back, the axes come back after
        # being faded out, which is just astonishing, even bringing the observers to the front would not work.
        # I cannot even manage to recreate this issue elsewhere - it's incredible.
        # But hey, manually setting the opacity works, so I'm delighted - what happened in the fadeout animation?
        self.bring_to_back(self.blue_axes, self.orange_axes)
        self.play(self.blue_axes.animate.set_opacity(0.0), self.orange_axes.animate.set_opacity(0.0))

    def hide_scene(self):
        self.play(FadeOut(self.blue_observer), FadeOut(self.orange_observer),
                  FadeOut(self.question), FadeOut(self.triangle))

    def hide_scene_after_fountain(self):
        # Using opacity instead of fade out, see `hide_observer_axes`
        self.play(self.blue_observer.animate.set_opacity(0), self.orange_observer.animate.set_opacity(0),
                  FadeOut(self.question), FadeOut(self.triangle), FadeOut(self.water_fountain),
                  FadeOut(self.blue_position_texts), FadeOut(self.orange_position_texts))

    def unhide_scene(self):
        self.play(FadeInFromLarge(self.blue_observer), FadeInFromLarge(self.orange_observer),
                  FadeInFromLarge(self.question), FadeInFromLarge(self.triangle))

    def show_compass(self):
        compass = self.compass = Compass().scale(1.5)
        self.play(DrawBorderThenFill(compass, run_time=1.0))

    def show_compass_axes(self):
        # Use scale instead of size to increase the thickness of the arrows as well.
        compass_axes = self.compass_axes = LabeledAxes(2, up_label="North", down_label="South",
                                                       left_label="West", right_label="East").scale(1.5)
        compass_axes.up_arrow.set_color(RED)
        compass_axes.up_label.set_color(RED)
        self.bring_to_back(compass_axes)
        self.play(FadeInFromPoint(compass_axes, self.compass))

    def clear_compass(self):
        self.play(FadeOut(self.compass), FadeOut(self.compass_axes))

    def show_observer_compasses(self):
        blue_compass = self.blue_compass = Compass().scale(0.3) \
            .next_to(self.blue_observer, direction=np.array([0.3, 0.3, 0]))
        orange_compass = self.orange_compass = Compass().scale(0.3) \
            .next_to(self.orange_observer, direction=np.array([-0.3, 0.3, 0]))

        self.play(DrawBorderThenFill(blue_compass), DrawBorderThenFill(orange_compass))
        # Add the compasses to the observer groups so they are included in the observer's fade in and out animations.
        self.blue_observer.add(blue_compass)
        self.orange_observer.add(orange_compass)

    def show_both_observer_axes(self):
        self.bring_to_back(self.blue_axes, self.orange_axes)
        self.blue_axes.set_opacity(1.0)
        self.orange_axes.set_opacity(1.0)
        self.play(FadeInFromPoint(self.orange_axes, self.orange_observer, run_time=0.5),
                  FadeInFromPoint(self.blue_axes, self.blue_observer, run_time=0.5))

    def change_observer_axes(self):
        self.play(self.blue_axes.transform_labels(
            Text("North").set_color(RED), Text("South"), Text("West"), Text("East")),
            self.blue_axes.up_arrow.animate.set_color(RED),

            self.orange_axes.transform_labels(
                Text("North").set_color(RED), Text("South"), Text("West"), Text("East")),
            self.orange_axes.up_arrow.animate.set_color(RED))

    def highlight_direction_agreement(self):
        self.play(Indicate(self.blue_axes.up_arrow, run_time=1.5), Indicate(self.blue_axes.up_label, run_time=1.5),
                  Indicate(self.orange_axes.up_arrow, run_time=1.5), Indicate(self.orange_axes.up_label, run_time=1.5),
                  Indicate(self.triangle, run_time=1.5))

    def show_blue_grid(self):
        blue_grid = self.blue_grid = NumberPlane().move_to(self.blue_observer)
        self.bring_to_back(blue_grid)

        self.play(ShowCreation(blue_grid))

    def show_blue_distance_lines(self):
        # Using shift instead of move_to because move_to moves the centre of the group to the observer.
        blue_distance_lines = self.blue_distance_lines = PathLines(Point2D(5, 3)) \
            .shift(np.array([self.blue_position.x, self.blue_position.y, 0]))

        # Prevent the lines from covering the observer while not putting it under the gridlines, unfortunately,
        # bringing the observer to the front does not work :/
        self.bring_to_back(blue_distance_lines)
        self.bring_to_back(self.blue_grid)
        self.play(ShowCreation(blue_distance_lines))

    def hide_blue_distance_lines_and_grid(self):
        self.play(Uncreate(self.blue_distance_lines), Uncreate(self.blue_grid))

    def recount_blue_distance(self):
        north_text = Text("3 units north").scale(0.8).next_to(self.blue_observer, direction=DOWN)
        east_text = Text("5 units east").scale(0.8).next_to(north_text, direction=DOWN)

        self.blue_position_texts = VGroup(north_text, east_text)

        self.play(Transform(self.blue_distance_lines.vertical_brace.label, north_text),
                  Transform(self.blue_distance_lines.horizontal_brace.label, east_text))

    def show_orange_grid(self):
        orange_grid = self.orange_grid = NumberPlane().move_to(self.orange_observer)
        self.bring_to_back(orange_grid)

        self.play(ShowCreation(orange_grid))

    def show_orange_distance_lines(self):
        orange_distance_lines = self.orange_distance_lines = PathLines(Point2D(-5, 3)) \
            .shift(np.array([self.orange_position.x, self.orange_position.y, 0]))

        self.bring_to_back(orange_distance_lines)
        self.bring_to_back(self.orange_grid)
        self.play(ShowCreation(orange_distance_lines))

    def hide_orange_distance_lines_and_grid(self):
        self.play(Uncreate(self.orange_distance_lines), Uncreate(self.orange_grid))

    def recount_orange_distance(self):
        north_text = Text("3 units north").scale(0.8).next_to(self.orange_observer, direction=DOWN)
        west_text = Text("5 units west").scale(0.8).next_to(north_text, direction=DOWN)

        self.orange_position_texts = VGroup(north_text, west_text)

        self.play(Transform(self.orange_distance_lines.vertical_brace.label, north_text),
                  Transform(self.orange_distance_lines.horizontal_brace.label, west_text))

    def change_position_texts(self):
        self.play(Transform(self.blue_position_texts.submobjects[0],
                            Text("4 units north").scale(0.8).set_color(GREEN)
                            .next_to(self.blue_observer, direction=DOWN)),
                  Transform(self.blue_position_texts.submobjects[1],
                            Text("2 units west").scale(0.8).set_color(GREEN)
                            .next_to(self.blue_position_texts.submobjects[0], direction=DOWN)),
                  Transform(self.orange_position_texts.submobjects[0],
                            Text("4 units north").scale(0.8).set_color(GREEN)
                            .next_to(self.orange_observer, direction=DOWN)),
                  Transform(self.orange_position_texts.submobjects[1],
                            Text("2 units west").scale(0.8).set_color(GREEN)
                            .next_to(self.orange_position_texts.submobjects[0], direction=DOWN)))

        blue_relative_to_fountain_text = Text("to the fountain").scale(0.8).set_color(GREEN)\
            .next_to(self.blue_position_texts.submobjects[1], direction=DOWN)
        orange_relative_to_fountain_text = Text("to the fountain").scale(0.8).set_color(GREEN)\
            .next_to(self.orange_position_texts.submobjects[1], direction=DOWN)

        self.blue_position_texts.add(blue_relative_to_fountain_text)
        self.orange_position_texts.add(orange_relative_to_fountain_text)

        self.play(Write(blue_relative_to_fountain_text), Write(orange_relative_to_fountain_text))

    def show_both_position_texts(self):
        self.play(Write(self.blue_position_texts, run_time=0.5), Write(self.orange_position_texts, run_time=0.5))

    def hide_both_position_texts(self):
        self.play(FadeOut(self.blue_position_texts), FadeOut(self.orange_position_texts))

    def highlight_position_disagreement(self):
        self.play(Indicate(self.blue_position_texts, run_time=1.5), Indicate(self.orange_position_texts, run_time=1.5),
                  Indicate(self.triangle, run_time=1.5))

    def create_and_show_water_fountain(self):
        water_fountain = self.water_fountain = WaterFountain().shift(np.array([2, -2, 0])).scale(0.75)

        self.play(DrawBorderThenFill(water_fountain))

    def shake_water_fountain(self):
        self.play(WiggleOutThenIn(self.water_fountain, n_wiggles=5, rotation_angle=PI / 10))

    def show_water_fountain_grid(self):
        water_fountain_grid = self.water_fountain_grid = NumberPlane().move_to(self.water_fountain)
        self.bring_to_back(water_fountain_grid)

        self.play(ShowCreation(water_fountain_grid))

    def show_water_fountain_distance_lines(self):
        water_fountain_distance_lines = self.water_fountain_distance_lines = PathLines(Point2D(-2, 4)) \
            .shift(np.array([2, -2, 0]))

        self.bring_to_back(water_fountain_distance_lines)
        self.bring_to_back(self.water_fountain_grid)

        self.play(ShowCreation(water_fountain_distance_lines))

    def hide_water_fountain_grid_and_distance_lines(self):
        self.play(Uncreate(self.water_fountain_grid), Uncreate(self.water_fountain_distance_lines))

    def highlight_position_agreement(self):
        self.play(Indicate(self.blue_position_texts, run_time=1.5),
                  Indicate(self.orange_position_texts, run_time=1.5),
                  Indicate(self.triangle, run_time=1.5))
