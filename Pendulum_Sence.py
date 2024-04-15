from manim import *
import numpy as np
from Double_Pendulum import *

#Ensure this variable is the same in two files.
FPS = 60

class Pendulum_Sence(Scene):
    def construct(self):
        axes = NumberPlane().set_opacity(0.2)
        self.add(axes)
        time_span = (0, 20)

        L1 = 1.5 # Length of arm 1
        L2 = 1 # Length of arm 2
        m1 = 1.6 # Mass of pendulum 1
        m2 = 2 # Mass of pendulum 2

        d1 = 90 # Pendulum initial degree of mass 1
        d2 = 190 # Pendulum initial degree of mass 2
        v1 = 0.5 # Pendulum initial velocity of mass 1
        v2 = 0.9 # Pendulum initial velocity of mass 2

        pendulum_anim = Double_Pendulum(L1,L2,m1,m2)
        ini_state = [d1, d2, v1, v2]
        x1, y1, x2, y2 = pendulum_anim.update(ini_state, time_span)

        # Animation setups
        Center = Dot()
        Circle1 = Dot(radius=0.04 * m1).move_to(x1[0] * RIGHT + y1[0] * UP).set_color(BLUE)
        Circle2 = Dot(radius=0.04 * m2).move_to(x2[0] * RIGHT + y2[0] * UP).set_color(BLUE)

        Line1 = Line(Center.get_center(), Circle1.get_center()).set_stroke(width=2)
        Line2 = Line(Circle1.get_center(), Circle2.get_center()).set_stroke(width=2)

        self.add(Line1, Line2, Center, Circle1, Circle2)

        # Animation
        num_frames = len(x1) - 1
        for i in range(num_frames):
            self.remove(Line1, Line2)
            Line1 = Line(Center.get_center(), Circle1.get_center()).set_stroke(width=2)
            Line2 = Line(Circle1.get_center(), Circle2.get_center()).set_stroke(width=2)
            self.add(Line1, Line2)
            self.play(
                Transform(Circle1, Dot(radius=0.04 * m1).move_to(x1[i + 1] * RIGHT + y1[i + 1] * UP).set_color(BLUE)),
                Transform(Circle2, Dot(radius=0.04 * m2).move_to(x2[i + 1] * RIGHT + y2[i + 1] * UP).set_color(BLUE)),
                run_time=1 / FPS)

