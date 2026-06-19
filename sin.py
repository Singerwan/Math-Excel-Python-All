from manim import *

class sin(Scene):
    def construct(self):
        ax = Axes().add_coordinates()
        self.play(Create(ax),run_time=2)
        
        curve = ax.plot(lambda x: 2 * np.sin(x), color=PURE_RED)
        self.play(Create(curve),run_time=4)
        
        area = ax.get_area(
            curve,
            x_range=(PI / 2, 3 * PI / 2),
            color=(BLUE, LOGO_WHITE),
            opacity=1,
        )
        self.play(FadeIn(area),run_time=3)
        
        area1 = ax.get_area(
            curve,
            x_range=(-2*PI, -PI),
            color=(YELLOW, LOGO_WHITE),
            opacity=1,
        )
        
        self.play(FadeIn(area1),run_time=3)
    
        label1 = ax.get_graph_label(
            graph=curve,
            label= MathTex(r"\frac{\pi}{2}"),
            x_val=PI / 2,
            dot=True,
            direction=UP,color=MAROON
        )
        
        lines = ax.get_vertical_lines_to_graph(
            curve, x_range=[-1.5, 1.5], num_lines=30, color=BLUE
        )
        self.play(Create(lines),run_time=3)
        
        label2 = ax.get_graph_label(
            graph=curve,
            label= MathTex(r"-\frac{\pi}{2}"),
            x_val=-PI / 2,
            dot=True,
            direction=DOWN,color=LOGO_WHITE
        )
        label3 = ax.get_graph_label(
            graph=curve,
            label= MathTex(r"-\frac{3\pi}{2}"),
            x_val=-3*PI / 2,
            dot=True,
            direction=UP,color=YELLOW
        )
        label4 = ax.get_graph_label(
            graph=curve,
            label= MathTex(r"\frac{3\pi}{2}"),
            x_val=3*PI / 2,
            dot=True,
            direction=DOWN,color=LOGO_WHITE
        )


        self.play(Create(label1),run_time=2)
        self.play(Create(label2),run_time=2)
        self.play(Create(label3),run_time=2)
        self.play(Create(label4),run_time=2)
        self.wait(2)
 
        self.play(Flash(
            label1, line_length=1,
            num_lines=30, color=PURE_GREEN,
            flash_radius=0.7+SMALL_BUFF,
            time_width=0.5, run_time=3,
            rate_func = rush_from  ))     
        
        self.play(FadeOut(label1),run_time=2)
        self.play(FadeOut(label2),run_time=2)
        self.play(FadeOut(label3),run_time=2)
        self.play(FadeOut(label4),run_time=2)
        
        self.play(FadeOut(area),run_time=2)
        self.play(FadeOut(area1),run_time=2)
        self.play(FadeOut(lines),run_time=2)
        self.play(FadeOut(curve),run_time=2)
        self.play(FadeOut(ax),run_time=2)       