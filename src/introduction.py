from manim import *
import numpy as np


class SelfIntroduction(Scene):
    def construct(self):
        title = Tex("Frames of References") \
            .scale(3) \
            .set_color_by_gradient(GREEN, YELLOW)
        # TODO: make sure i spell ashmita's name right
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
                        of an object \\textbf{relative} to an \\textbf{observer}
                        """)
        warning = Tex("""
                    Please note that an observer doesn't have to be \\\\
                    at the \\textbf{origin} of the graph.\\\\
                    However, let us assume that the \\\\
                    observer is at the origin for ease.
                      """)
        self.play(Write(def_of_fr))
        self.wait(5)
        self.play(ReplacementTransform(def_of_fr, warning))
        self.wait(5)

