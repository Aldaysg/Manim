from manim import *
from main import RubiksCube

class posicion(ThreeDScene):
    def construct(self):
        diap = Text("6").to_corner(UR,buff=0.4)
        titulo = Tex(r'Definición de la pose').to_corner(UL,buff=0.5)
        axes = ThreeDAxes()
        ax_label = axes.get_axis_labels()
        RC = RubiksCube().scale(0.5)
        RC.move_to([4,1,2])
        vec = Arrow3D(ORIGIN,RC.get_center(),color=GREEN)
        self.add_fixed_in_frame_mobjects(diap,titulo)

        self.add(diap,titulo)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-30*DEGREES)
        self.play(Write(axes),Write(ax_label))
        self.play(Create(RC))
        self.wait()
        self.play(Write(vec))

# class orientacion(Scene):
#     def construct(self):
#         diap = Text("5").to_corner(UR,buff=0.4)
#         titulo = Tex(r'Representación de orientación').to_edge(UP,buff=0.5)

#         tab =Table(
#             [[MathTex(r'SO(3)'), MathTex(r'\mathbb{R}^{3')],
#             [MathTex(r'\mathbb{H}_1'), MathTex(r'\mathbb{R}^{4')],
#             [MathTex(r'SO(2) \times 3'), MathTex(r'\mathbb{R}^{3')]],
#             row_labels=[Tex("Parametrización "), Tex("Dimensinalidad")],
#             col_labels=[Tex("Matriz de rotación"), Tex("Ángulos de Euler"), Tex("Cuaterniones")],
#             top_left_entry=Tex("Representación"),
#             include_outer_lines=True,
#             arrange_in_grid_config={"cell_alignment": RIGHT}, element_to_mobject=MathTex)

#         self.add(diap)
#         self.play(Write(titulo),Write(tab))


class orientacion(Scene):
    def construct(self):
        diap = Text("7").to_corner(UR,buff=0.4)
        titulo = Tex(r'Representación de orientación').to_edge(UP,buff=0.5)
        rep = Tex(r'\begin{itemize} ' \
        '\item Matrices de rotación ' \
        '\item Ángulos de Euler ' \
        '\item Cuaterniones ' \
        '\end{itemize}')

        self.add(diap)
        self.play(Write(titulo))
        self.play(Write(rep))
        
class cuaternion(ThreeDScene):
    def construct(self):
        diap = Text("10").to_corner(UR,buff=0.4)
        titulo = Tex(r'Cuaterniones').to_edge(UP,buff=0.5)