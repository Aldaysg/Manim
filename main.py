from manim import *
from manim_slides.slide import Slide, ThreeDSlide
#from orientation import *

class Portada(Scene):
    def construct(self):
        titulo = Tex(r"{0.5\textwidth}\centering Redes neuronales para manipulación de objetos en robots de servicio",tex_environment="minipage")
        #self.add(titulo)
        self.play(Write(titulo))

class DefaultTemplate(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class Posicion(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(
            x_range=[-5,5,1],
            y_range=[-5,5,1],
            z_range=[-5,5,1],
            x_length=5,
            y_length=5,
            z_length=5
        )
        self.move_camera(phi=60*DEGREES)
        self.move_camera(theta=45*DEGREES)
        self.play(Create(ax))

class LinearTransformation3D(ThreeDScene):

    CONFIG = {
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "basis_i_color": GREEN,
        "basis_j_color": RED,
        "basis_k_color": GOLD
    }

    def create_matrix(self, np_matrix):

        m = Matrix(np_matrix)

        m.scale(0.5)
        m.set_column_colors(GREEN, RED, GOLD)

        m.to_corner(UP + LEFT)

        return m

    def construct(self):

        M = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, -1]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = Tex("$i$", ",", "$j$", ",", "$k$")
        # basis_vector_helper = Tex
        print(basis_vector_helper)
        basis_vector_helper[0].set_color(GREEN)
        basis_vector_helper[2].set_color(RED)
        basis_vector_helper[4].set_color(GOLD)

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color=GREEN)
        j_vec = Vector(np.array([0, 1, 0]), color=RED)
        k_vec = Vector(np.array([0, 0, 1]), color=GOLD)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=GREEN)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=RED)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=GOLD)

        self.play(
            #ShowCreation(cube),
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            # Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        # self.wait(7)

#----- Surfaces
class SurfacesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                1.0*np.cos(u)*np.cos(v),
                1.0*np.cos(u)*np.sin(v),
                1.0*np.sin(u)
            ]),
            v_range=[0,TAU],
            u_range=[-PI/2,PI/2],
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        
class QuaternionRotationOverlay(Scene):
    def construct(self):
        equations = VGroup(
            MathTex(
                "p", "\\rightarrow",
                "{}",
                "{}",
                "\\left(q_1",
                "p",
                "q_1^{-1}\\right)",
                "{}",
                "{}",
            ),
            MathTex(
                "p", "\\rightarrow",
                "{}",
                "\\left(q_2",
                "\\left(q_1",
                "p",
                "q_1^{-1}\\right)",
                "q_2^{-1}\\right)",
                "{}",
            ),
            MathTex(
                "p", "\\rightarrow",
                "\\left(q_3",
                "\\left(q_2",
                "\\left(q_1",
                "p",
                "q_1^{-1}\\right)",
                "q_2^{-1}\\right)",
                "q_3^{-1}\\right)",
            ),
        )
        for equation in equations:
            equation.set_color_by_tex_to_color_map({
                "1": GREEN, "2": RED, "3": BLUE,
            })
            equation.set_color_by_tex("rightarrow", WHITE)
            equation.to_corner(UL)

        equation = equations[0].copy()
        self.play(Write(equation))
        self.wait()
        for new_equation in equations[1:]:
            self.play(
                Transform(equation, new_equation)
            )
            self.wait(2)

class RubiksCube(VGroup):
    CONFIG = {
        "colors": [
            "#FFD500",  # Yellow
            "#C41E3A",  # Orange
            "#009E60",  # Green
            "#FF5800",  # Red
            "#0051BA",  # Blue
            "#FFFFFF"   # White
        ],
    }

    def __init__(self, **kwargs):
        # digest_config(self, kwargs)
        vectors = [OUT, RIGHT, UP, LEFT, DOWN, IN]
        faces = [
            self.create_face(color, vector)
            for color, vector in zip(self.CONFIG['colors'], vectors)
        ]
        VGroup.__init__(self,faces, **kwargs)
        self.set_shade_in_3d(True)

    def create_face(self, color, vector):
        squares = VGroup(*[
            self.create_square(color)
            for x in range(9)
        ])
        squares.arrange_in_grid(
            3, 3,
            buff=0
        )
        squares.set_width(2)
        squares.move_to(OUT, OUT)
        squares.apply_matrix(z_to_vector(vector))
        return squares

    def create_square(self, color):
        square = Square(
            stroke_width=3,
            stroke_color=BLACK,
            fill_color=color,
            fill_opacity=0.75,
            side_length=0.8,
        )
        square.flip()
        return square
        # back = square.copy()
        # back.set_fill(BLACK, 0.85)
        # back.set_stroke(width=0)
        # back.shift(0.5 * IN)
        # return VGroup(square, back)

    def get_face(self, vect):
        self.sort(lambda p: np.dot(p, vect))
        return self[-(12 + 9):]

class RotateCubeThreeTimes(ThreeDScene):
    def construct(self):
        cube = RubiksCube()
        cube.set_fill(opacity=0.8)
        cube.set_stroke(width=1)
        # randy = Randolph(mode="pondering")
        # randy.set_height(cube.get_height() - 2 * SMALL_BUFF)
        # randy.move_to(cube.get_edge_center(OUT))
        # randy.set_fill(opacity=0.8)
        # # randy.set_shade_in_3d(True)
        # cube.add(randy)
        #axes = self.get_axes()
        axes = ThreeDAxes()

        self.add(axes, cube)
        self.move_camera(
            phi=70 * DEGREES,
            theta=-140 * DEGREES,
        )
        self.begin_ambient_camera_rotation(rate=0.02)
        self.wait(2)
        self.play(Rotate(cube, TAU / 4, RIGHT, run_time=3))
        self.wait(2)
        self.play(Rotate(cube, TAU / 4, UP, run_time=3))
        self.wait(2)
        self.play(Rotate(cube, -TAU / 3, np.ones(3), run_time=3))
        self.wait(7)

class ComplexTo3D(ThreeDScene):

    def construct(self):
        self.add_plane()
        self.show_in_three_d()

    def add_plane(self):
        #plane = NumberPlane(y_length=10)
        plane = ComplexPlane().add_coordinates()
        axes = ThreeDAxes()


        self.add(axes, plane)
        self.play(
            Create(axes),
            Create(plane),

        )
        self.wait()

        self.plane = plane
        self.axes = axes

    def show_in_three_d(self):
        plane = self.plane
        axes = self.axes

        # back_plane = Rectangle().replace(plane, stretch=True)
        # back_plane.shade_in_3d = True
        # back_plane.set_fill(GREY_B, opacity=0.5)
        # back_plane.set_sheen(1, UL)
        # back_plane.shift(SMALL_BUFF * IN)
        # back_plane.set_stroke(width=0)
        # back_plane = ParametricSurface(
        #     lambda u, v: u * RIGHT + v * UP
        # )
        # back_plane.replace(plane, stretch=True)
        # back_plane.set_stroke(width=0)
        # back_plane.set_fill(GREY_B, opacity=0.5)

        sphere = Sphere()
        # sphere.set_fill(BLUE_E, 0.5)

        self.move_camera(
            phi=70 * DEGREES,
            theta=-110 * DEGREES,
            added_anims=[FadeOut(plane)],
            run_time=2
        )
        self.begin_ambient_camera_rotation()
        self.add(axes, sphere)
        self.play(
            Write(sphere)
            #felix.change, "confused"
        )
        self.wait()

        axis_angle_pairs = [
            (RIGHT, 90 * DEGREES),
            (OUT, 45 * DEGREES),
            (UR + OUT, 120 * DEGREES),
            (RIGHT, 90 * DEGREES),
        ]
        for axis, angle in axis_angle_pairs:
            self.play(Rotate(
                sphere, angle=angle, axis=axis,
                run_time=2,
            ))
        self.wait(2)

class QuaternionLabel(VGroup):
    CONFIG = {
        "decimal_config": {}
    }

    def __init__(self, quat, **kwargs):
        VGroup.__init__(self, **kwargs)
        dkwargs = dict(self.CONFIG['decimal_config'])
        decimals = VGroup()
        decimals.add(DecimalNumber(quat[0], color=YELLOW, **dkwargs))
        dkwargs["include_sign"] = True
        decimals.add(
            DecimalNumber(quat[1], color=GREEN, **dkwargs),
            DecimalNumber(quat[2], color=RED, **dkwargs),
            DecimalNumber(quat[3], color=GOLD, **dkwargs),
        )
        self.add(
            decimals[0],
            decimals[1], MathTex("i"),
            decimals[2], MathTex("j"),
            decimals[3], MathTex("k"),
        )
        self.arrange(RIGHT, buff=SMALL_BUFF)

        self.decimals = decimals

    def set_value(self, quat):
        for decimal, coord in zip(self.decimals, quat):
            decimal.set_value(coord)
        return self

class QuaternionTracker(ValueTracker):
    CONFIG = {
        "force_unit": True,
        "dim": 4,
    }

    def __init__(self, four_vector=None, **kwargs):
        Mobject.__init__(self, **kwargs)
        if four_vector is None:
            four_vector = np.array([1, 0, 0, 0])
        self.set_value(four_vector)
        if self.CONFIG['force_unit']:
            self.add_updater(lambda q: q.normalize())

    def set_value(self, vector):
        self.set_points(np.array(vector).reshape((1, 4)))
        return self

    def get_value(self):
        return self.get_points()[0]

    def normalize(self):
        self.set_value(normalize(
            self.get_value(),
            fall_back=np.array([1, 0, 0, 0])
        ))
        return self

class Gimbal(VGroup):
    CONFIG = {
        "inner_r": 1.2,
        "outer_r": 2.6,
    }

    def __init__(self, alpha=0, beta=0, gamma=0, inner_mob=None, **kwargs):
        VGroup.__init__(self, **kwargs)
        r1, r2, r3, r4, r5, r6, r7 = np.linspace(
            self.CONFIG['inner_r'], self.CONFIG['outer_r'], 7
        )
        rings = VGroup(
            self.get_ring(r5, r6,YELLOW),
            self.get_ring(r3, r4,TEAL_E),
            self.get_ring(r1, r2,PINK),
        )
        for i, p1, p2 in [(0, r6, r7), (1, r4, r5), (2, r2, r3)]:
            annulus = rings[i]
            lines = VGroup(
                Line(p1 * UP, p2 * UP),
                Line(p1 * DOWN, p2 * DOWN),
            )
            lines.set_stroke(RED)
            annulus.lines = lines
            annulus.add(lines)
        rings[1].lines.rotate(90 * DEGREES, about_point=ORIGIN)
        rings.rotate(90 * DEGREES, RIGHT, about_point=ORIGIN)
        rings.set_shade_in_3d(True)
        self.rings = rings
        self.add(rings)

        if inner_mob is not None:
            corners = [
                inner_mob.get_corner(v1 + v2)
                for v1 in [LEFT, RIGHT]
                for v2 in [IN, OUT]
            ]
            lines = VGroup()
            for corner in corners:
                corner[1] = 0
                line = Line(
                    corner, self.CONFIG['inner_r'] * normalize(corner),
                    color=WHITE,
                    stroke_width=1
                )
                lines.add(line)
            lines.set_shade_in_3d(True)
            rings[2].add(lines, inner_mob)

        # Rotations
        angles = [alpha, beta, gamma]
        for i, angle in zip(range(3), angles):
            vect = rings[i].lines[0].get_vector()
            rings[i:].rotate(angle=angle, axis=vect)

    def get_ring(self, in_r, out_r, rcolor, angle=TAU / 4):
        result = VGroup()
        for start_angle in np.arange(0, TAU, angle):
            start_angle += angle / 2
            sector = AnnularSector(
                inner_radius=in_r,
                outer_radius=out_r,
                angle=angle,
                start_angle=start_angle
            )
            sector.set_fill(rcolor, 0.8)
            arcs = VGroup(*[
                Arc(
                    angle=angle,
                    start_angle=start_angle,
                    radius=r
                )
                for r in [in_r, out_r]
            ])
            arcs.set_stroke(BLACK, 1, opacity=0.5)
            sector.add(arcs)
            result.add(sector)
        return result
    
class ShowSeveralQuaternionRotations(ThreeDSlide):
    CONFIG = {
        "quaternions": [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 1, 0],
            [1, 1, 1, -1],
            [0, -1, 2, 1],
            #[1, 0, 0, -1],
            #[1, -1, 0, 0],
            #[1, -1, 1, 0],
            #[1, -1, 1, -1],
            #[1, 0, 0, 0],
        ],
        "start_phi": 70 * DEGREES,
        "start_theta": -140 * DEGREES,
        "ambient_rotation_rate": 0.01,
    }

    def construct(self):
        diap = Text("9").to_corner(UR,buff=0.4)
        self.titulo = Tex(r'Cuaterniones').to_corner(UL,buff=0.5)
        self.add_fixed_in_frame_mobjects(self.titulo,diap)
        self.add(diap)
        self.play(Write(self.titulo))
        self.add_q_tracker()
        self.setup_labels()
        self.setup_camera_position()
        self.add_prism()
        self.add_axes()
        self.apply_quaternions()

    def add_q_tracker(self):
        self.q_tracker = QuaternionTracker()
        self.q_tracker.add_updater(lambda m: m.normalize())
        self.add(self.q_tracker)

    def setup_labels(self):
        left_q_label = QuaternionLabel([1, 0, 0, 0])
        right_q_label = QuaternionLabel([1, 0, 0, 0])
        for label in left_q_label, right_q_label:
            lp, rp = MathTex("("), MathTex(")")
            lp.next_to(label, LEFT, SMALL_BUFF)
            rp.next_to(label, RIGHT, SMALL_BUFF)
            label.add(lp, rp)
        point_label = MathTex(
            *"(xi+yj+zk)",
            tex_to_color_map={
                "i": GREEN,
                "j": RED,
                "k": BLUE,
            }
        ).scale(0.6)
        left_q_label.next_to(point_label, LEFT).scale(0.6)
        right_q_label.next_to(point_label, RIGHT).scale(0.6)
        group = VGroup(left_q_label, point_label, right_q_label)
        group.arrange(RIGHT)
        #group.set_width(FRAME_WIDTH - 1)
        group.to_edge(UP,buff=1.3)
        self.add_fixed_in_frame_mobjects(BackgroundRectangle(group))

        for label, text in zip(group, ["$q$", "Punto 3d", "$q^{-1}$"]):
            brace = Brace(label, DOWN)
            text_mob = Tex(text)
            if text_mob.get_width() > brace.get_width():
                text_mob.match_width(brace)
            text_mob.next_to(brace, DOWN, buff=SMALL_BUFF)
            text_mob.add_background_rectangle()
            label.add(brace, text_mob)

        self.add_fixed_in_frame_mobjects(*group)

        left_q_label.add_updater(
            lambda m: m.set_value(self.q_tracker.get_value())
        )
        left_q_label.add_updater(lambda m: self.add_fixed_in_frame_mobjects(m))
        right_q_label.add_updater(
            lambda m: m.set_value(quaternion_conjugate(
                self.q_tracker.get_value()
            ))
        )
        right_q_label.add_updater(lambda m: self.add_fixed_in_frame_mobjects(m))

    def setup_camera_position(self):
        self.set_camera_orientation(
            phi=self.CONFIG['start_phi'],
            theta=self.CONFIG['start_theta'],
        )
        self.begin_ambient_camera_rotation(self.CONFIG['ambient_rotation_rate'])

    def add_prism(self):
        prism = self.prism = self.get_prism()
        prism.add_updater(
            lambda p: p.become(self.get_prism(
                self.q_tracker.get_value()
            ))
        )
        self.add(prism)

    def add_axes(self):
        #axes = self.axes = always_redraw(self.get_axes)
        axes = ThreeDAxes()
        self.add(axes)

    def apply_quaternions(self):
        for quat in self.CONFIG['quaternions']:
            self.change_q(quat)
            self.wait(2)

    #
    def get_unrotated_prism(self):
        return RubiksCube().scale(1.1)

    def get_prism(self, quaternion=[1, 0, 0, 0]):
        prism = self.get_unrotated_prism()
        angle, axis = angle_axis_from_quaternion(quaternion)
        prism.rotate(angle=angle, axis=axis, about_point=ORIGIN)
        return prism.scale(0.8)

    def get_axes(self):
        prism = self.prism
        centers = [sm.get_center() for sm in prism[:6]]
        axes = VGroup()
        for i in range(3):
            for u in [-1, 1]:
                vect = np.zeros(3)
                vect[i] = u
                dots = [np.dot(normalize(c), vect) for c in centers]
                max_i = np.argmax(dots)
                ec = centers[max_i]
                prism.get_edge_center(vect)
                p1 = np.zeros(3)
                p1[i] = ec[i]
                p1 *= dots[max_i]
                p2 = 10 * vect
                axes.add(Line(p1, p2))
        axes.set_stroke(GREY_B, 1)
        axes.set_shade_in_3d(True)
        return axes.scale(0.8)

    def change_q(self, value, run_time=3, added_anims=None, **kwargs):
        if added_anims is None:
            added_anims = []
        self.play(
            self.q_tracker.animate.set_value(value),
            *added_anims,
            run_time=run_time,
            **kwargs
        )


class RotationMatrix(ShowSeveralQuaternionRotations):
    CONFIG = {
        "start_phi": 60 * DEGREES,
        "start_theta": -60 * DEGREES,
        "ambient_rotation_rate": 0.01,
    }

    def construct(self):
        self.add_q_tracker()
        self.setup_camera_position()
        self.add_prism()
        self.add_basis_vector_labels()
        self.add_axes()

        diap = Text("7").to_corner(UR,buff=0.4)

        title = Tex("Matriz de rotación")
        title.to_corner(UL,buff=0.5)
        self.add_fixed_in_frame_mobjects(title,diap)

        angle = 75 * DEGREES
        axis = [0.3, 1, 0.3]
        matrix = rotation_matrix(angle=angle, axis=axis)
        matrix_mob = DecimalMatrix(matrix, h_buff=1.6)
        matrix_mob.next_to(title, DOWN)
        matrix_mob.to_edge(LEFT)
        title.next_to(matrix_mob, UP)
        self.add_fixed_in_frame_mobjects(matrix_mob)

        colors = [GREEN, RED, BLUE]
        matrix_mob.set_column_colors(*colors)

        columns = matrix_mob.get_columns()
        column_rects = VGroup(*[
            SurroundingRectangle(c).match_color(c[0])
            for c in columns
        ])
        labels = VGroup(*[
            Tex(
                "Proyección de ", tex, " ",
                tex_to_color_map={tex: rect.get_color()}
            ).next_to(rect, DOWN)
            for letter, rect in zip(["\\i", "\\j", "k"], column_rects)
            for tex in ["$\\hat{\\textbf{%s}}$" % (letter)]
        ])
        labels.space_out_submobjects(0.8)

        quaternion = quaternion_from_angle_axis(angle, axis)

        self.play(Write(matrix_mob))
        self.change_q(quaternion)
        self.wait()
        last_label = VectorizedPoint(matrix_mob.get_bottom())
        last_rect = VMobject()
        for label, rect in zip(labels, column_rects):
            self.add_fixed_in_frame_mobjects(rect, label)
            self.play(
                FadeIn(label),
                FadeOut(last_label),
                Create(rect),
                FadeOut(last_rect)
            )
            self.wait()
            last_label = label
            last_rect = rect
        self.play(FadeOut(last_label), FadeOut(last_rect), Indicate(self.prism.arrows))
        self.wait(5)

    def get_unrotated_prism(self):
        prism = RubiksCube()
        prism.scale(1.5)
        arrows = VGroup()
        for i, color in enumerate([GREEN, RED, BLUE]):
            vect = np.zeros(3)
            vect[i] = 1
            arrow = Arrow(
                prism.get_edge_center(vect), 2 * vect,
                color=color,
                buff=0,
            )
            arrows.add(arrow)
        arrows.set_shade_in_3d(True)
        prism.arrows = arrows
        prism.add(arrows)
        return prism

    def add_basis_vector_labels(self):
        labels = VGroup(
            MathTex("\\hat{\\textbf{\\i}}"),
            MathTex("\\hat{\\textbf{\\j}}"),
            MathTex("\\hat{\\textbf{k}}"),
        )

        def generate_updater(arrow):
            return lambda m: m.move_to(
                arrow.get_end() + 0.2 * normalize(arrow.get_vector()),
            )

        for arrow, label in zip(self.prism.arrows, labels):
            label.match_color(arrow)
            label.add_updater(generate_updater(arrow))
            self.add_fixed_orientation_mobjects(label)

class EulerAnglesAndGimbal(ShowSeveralQuaternionRotations):
    def construct(self):
        self.setup_position()
        self.setup_angle_trackers()
        self.setup_gimbal()
        self.add_axes()
        self.add_title()
        self.show_rotations()

    def setup_position(self):
        self.set_camera_orientation(
            theta=-140 * DEGREES,
            phi=70 * DEGREES,
        )
        self.begin_ambient_camera_rotation(rate=0.015)

    def setup_angle_trackers(self):
        self.alpha_tracker = ValueTracker(0)
        self.beta_tracker = ValueTracker(0)
        self.gamma_tracker = ValueTracker(0)

    def setup_gimbal(self):
        gimbal = always_redraw(self.get_gimbal)
        self.gimbal = gimbal
        self.add(gimbal)

    def add_title(self):
        title = Tex("Ángulos de Euler")
        diap = Text("8").to_corner(UR,buff=0.4)
        #title.scale(1)
        title.to_corner(UL,buff=0.5)
        angle_labels = VGroup(
            MathTex("\\psi").set_color(YELLOW),
            MathTex("\\theta").set_color(TEAL_E),
            MathTex("\\phi").set_color(PINK),
        )
        angle_labels.scale(2)
        angle_labels.arrange(RIGHT, buff=MED_LARGE_BUFF)
        angle_labels.next_to(title, DOWN, aligned_edge=LEFT)
        self.angle_labels = angle_labels

        gl_label = VGroup(
            Arrow(LEFT, RIGHT, color=WHITE),
            Tex("Bloqueo del cardán").scale(1.1),
        )
        gl_label.arrange(RIGHT)
        gl_label.next_to(title, RIGHT)
        self.gimbal_lock_label = gl_label

        VGroup(title, angle_labels, gl_label).center().to_edge(UP)

        self.add_fixed_in_frame_mobjects(title, angle_labels, gl_label, diap)
        self.remove(angle_labels)
        self.remove(gl_label)

    def show_rotations(self):
        gimbal = self.gimbal
        alpha_tracker = self.alpha_tracker
        beta_tracker = self.beta_tracker
        gamma_tracker = self.gamma_tracker

        angles = [-60 * DEGREES, 50 * DEGREES, 45 * DEGREES]
        trackers = [alpha_tracker, beta_tracker, gamma_tracker]
        in_rs = [0.6, 0.5, 0.6]
        for i in range(3):
            tracker = trackers[i]
            angle = angles[i]
            in_r = in_rs[i]
            ring = gimbal.rings[i]

            vect = ring.lines[0].get_vector()
            line = self.get_dotted_line(vect, in_r=in_r)
            angle_label = self.angle_labels[i]
            line.match_color(angle_label)
            self.play(
                Create(line),
                FadeIn(angle_label)
            )
            self.play(
                tracker.animate.set_value(angle),
                run_time=2
            )
            self.play(FadeOut(line))
            self.wait()
        self.wait(1)
        self.play(Write(self.gimbal_lock_label))
        self.play(
            alpha_tracker.animate.set_value(0),
            beta_tracker.animate.set_value(0),
            run_time=2
        )
        self.play(
            alpha_tracker.animate.set_value(90 * DEGREES),
            gamma_tracker.animate.set_value(-90 * DEGREES),
            run_time=2
        )
        self.play(
            FadeOut(self.gimbal_lock_label),
            [t.animate.set_value(0) for t in trackers],
            run_time=2
        )
        self.play(
            alpha_tracker.animate.set_value(30 * DEGREES),
            beta_tracker.animate.set_value(120 * DEGREES),
            gamma_tracker.animate.set_value(-50 * DEGREES),
            run_time=2
        )
        self.play(
            alpha_tracker.animate.set_value(120 * DEGREES),
            beta_tracker.animate.set_value(-30 * DEGREES),
            gamma_tracker.animate.set_value(90 * DEGREES),
            run_time=2
        )
        self.play(
            beta_tracker.animate.set_value(150 * DEGREES),
            run_time=2
        )
        self.play(
            alpha_tracker.animate.set_value(0),
            beta_tracker.animate.set_value(0),
            gamma_tracker.animate.set_value(0),
            run_time=2
        )
        self.wait()

    #
    def get_gimbal(self):
        self.prism = RubiksCube().scale(0.5)
        return Gimbal(
            alpha=self.alpha_tracker.get_value(),
            beta=self.beta_tracker.get_value(),
            gamma=self.gamma_tracker.get_value(),
            inner_mob=self.prism
        )

    def get_dotted_line(self, vect, in_r=0, out_r=10):
        line = VGroup([
            DashedLine(
                in_r * normalize(u * vect),
                out_r * normalize(u * vect),
            )
            for u in [-1, 1]
        ])
        #line.sort(get_norm)
        line.set_shade_in_3d(True)
        line.set_stroke(YELLOW, 5)
        line.center()
        return line
    
