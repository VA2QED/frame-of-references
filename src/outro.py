from manim import *


class ThanksForWatching(Scene):
    def construct(self):
        thanks_text = Text("Thank you for watching!").move_to(3*UP)\
            .set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)  # YES, ALL THE COLOURS OF THE RAINBOW!

        source_code = Text("The source code for this project can be found at "
                           "\n www.github.com/maffutaffu/frame-of-references").set_color(GREEN).scale(0.5)
        manim_logo = ManimBanner(dark_theme=True).scale(0.5)
        manim_logo.to_corner(DR)

        ashmita = [
            Text("Ashmita Bhattacharyya: ").move_to(UP+2*LEFT),
            Text("Narration and Editing").move_to(UP+2*RIGHT)
        ]
        jerry = [
            Text("Jerry Li: ").next_to(ashmita[0], direction=DOWN),
            Text("Animations and Script").next_to(ashmita[1], direction=DOWN)
        ]
        matthew = [
            Text("Jixin Chen: ").next_to(jerry[0], direction=DOWN),
            Text("Animations and Script").next_to(jerry[1], direction=DOWN)
        ]
        name_group = VGroup(ashmita[0], jerry[0], matthew[0]).scale(0.5)
        job_group = VGroup(ashmita[1], jerry[1], matthew[1]).scale(0.5)


        # this is epic
        self.play(Write(thanks_text), Write(source_code), rate_func=smooth, run_time=3)
        self.wait()
        self.play(ShowCreation(manim_logo))
        self.play(manim_logo.expand(), source_code.animate.next_to(thanks_text, direction=DOWN))
        self.wait()
        self.play(Write(name_group))
        self.play(FadeInFrom(job_group, direction=LEFT))
        self.wait(4)

