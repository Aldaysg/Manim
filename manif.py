from manim import *
import geomstats.backend as gs
from geomstats.geometry.hypersphere import Hypersphere



class TangentSpace(ThreeDScene):

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

        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        self.play(Write(plane))
        self.wait()
        self.play(Write(ut),Write(vt))
        self.wait()
        #self.play(TransformFromCopy(ut,um2))
        self.play(ReplacementTransform(ut2,um),FadeOut(ut2.get_tip()))
        #self.add_fixed_orientation_mobjects(um)
        self.play(ReplacementTransform(vt2,vm),FadeOut(vt2.get_tip()))
        #self.play(ReplacementTransform(vt.copy(),vm2))
        #self.play(Create(um))

class GradientDescentAnimation(ThreeDScene):
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
        
        self.set_camera_orientation(phi=45 * DEGREES, theta=-40 * DEGREES)
        self.play(Create(axes), Create(surface))
        
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