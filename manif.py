from manim import *
from manim_slides.slide import Slide, ThreeDSlide
import geomstats.backend as gs
from geomstats.geometry.hypersphere import Hypersphere



class TangentSpace(ThreeDSlide):

    def exp_map(self, t):
        tan_vector = self.direc * t
        space = Hypersphere(2,equip=True)
        exp_vect = space.metric.exp(tan_vector, self.base)*2
        return exp_vect
    
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
            checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        diap = Text("14").to_corner(UR,buff=0.4)
        titulo = Tex(r'Modelo geodésico').to_corner(UL,buff=0.5)
        self.add_fixed_in_frame_mobjects(diap,titulo)

        self.set_camera_orientation(phi=60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.05)

        plane = NumberPlane(x_length=4,y_length=4, x_range=[-PI,PI], y_range=[-PI,PI])
        plane.move_to([0,0,2])

        ut = Vector([1,0,0],color = GOLD).scale(2)
        vt = Vector([0,-1,0],color = GREEN).scale(2)
        ut.move_to([1,0,2])
        vt.move_to([0,-1,2])
        self.direc = np.array([1,0,0])
        self.base = np.array([0,0,1])
        um = ParametricFunction(self.exp_map,t_range=(0,1.5),color = GOLD, stroke_width = 6)
        self.direc = np.array([0,-1,0])
        vm = ParametricFunction(self.exp_map,t_range=(0,1.5),color = GREEN, stroke_width = 6)
        
        print(vm.get_center())
        #um.move_to([0.5,0.3,0.8])
        #vm.move_to([-1,-0.5,0.5])
        #print(vm.get_center())

        um2 = CurvedArrow([0,0,2],[2,0,0], color=GOLD)
        vm2 = CurvedArrow([0,0,2],[0,-2,0], color=GREEN)

        ut2 = ut.copy()
        vt2 = vt.copy()
        #um2.rotate()
        #self.add_fixed_orientation_mobjects(um2)

        self.add(axes, diap)
        self.play(Write(sphere),Write(plane), Write(titulo))
        self.wait()

        templ = TexTemplate()
        templ.add_to_preamble(r"\usepackage{physics}")
        templ.add_to_preamble(r"\usepackage{amsmath}")
        expmap = MathTex(r"\gamma \left[ \mathcal{E},\mathcal{U} \right] = \exp (\hat{e}, \hat{u})", tex_template = templ)
        expmap.scale(0.8).move_to([3,3,0])
        err = MathTex(r"E = d(q_o,q_t)^2 = arccos(\langle\,q_o,q_t\rangle)^2")
        err.scale(0.8).move_to([-3,-3,0])
        self.add_fixed_in_frame_mobjects(expmap, err)

        self.play(Write(ut),Write(vt))
        self.wait()
        #self.play(TransformFromCopy(ut,um2))
        self.play(ReplacementTransform(ut2,um),FadeOut(ut2.get_tip()),Write(expmap))
        #self.add_fixed_orientation_mobjects(um)
        self.play(ReplacementTransform(vt2,vm),FadeOut(vt2.get_tip()),Write(err))
        self.wait()
        #self.play(ReplacementTransform(vt.copy(),vm2))
        #self.play(Create(um))

class GradientDescentAnimation(ThreeDSlide):
    def construct(self):
        def f(x, y):
            return 0.7* x**2 + 0.7 * y**2
        
        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: axes.c2p(u, v, f(u, v)),
            u_range=(-2, 2),
            v_range=(-2, 2),
            fill_opacity=0.5
        )
        diap = Text("12").to_corner(UR,buff=0.4)
        titulo = Tex(r'Descenso del gradiente').to_corner(UL,buff=0.5)

        templ = TexTemplate()
        templ.add_to_preamble(r"\usepackage{physics}")
        templ.add_to_preamble(r"\usepackage{amsmath}")
        grad = MathTex(r"\nabla E(\Vec{\omega}) & = \left[ \pdv{E}{\omega_0}, \pdv{E}{\omega_1}, ... \pdv{E}{\omega_n} \right] \\ \omega_i & \longleftarrow \omega_i + \Delta \omega_i \\ \Delta \omega_i & = - \iota \nabla E(\Vec{\omega_i})", tex_template = templ)
        #grad.scale(0.8).next_to(axes,RIGHT,buff=0)
        
        self.add_fixed_in_frame_mobjects(diap,titulo)
        self.set_camera_orientation(phi=45 * DEGREES, theta=-40 * DEGREES)
        self.add(diap)
        self.play(Create(axes), Create(surface), Write(titulo))
        
        grad.scale(0.8).move_to([4,-0.5,0])
        self.add_fixed_in_frame_mobjects(grad)
        self.play(Write(grad))
        dot = Sphere(radius=0.08).move_to(axes.c2p(1.5, 1.5, f(1.5, 1.5)))
        dot.set_color(RED_A)

        def update_dot(dot, dt):
            x, y, _ = axes.p2c(dot.get_center())
            grad_x, grad_y = 0.7*2*x, 0.7*2*y
            x -= 0.01 * grad_x
            y -= 0.01 * grad_y
            dot.move_to(axes.c2p(x, y, f(x, y)))
        
        dot.add_updater(update_dot)
        self.play(Create(dot))
        self.wait(5)
        dot.remove_updater(update_dot)