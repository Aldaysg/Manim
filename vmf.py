import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import vonmises_fisher
from matplotlib.colors import Normalize
from manim import *
from manim_slides.slide import Slide

plt.style.use('dark_background')

n_grid = 128
u = np.linspace(0, np.pi, n_grid)
v = np.linspace(0, 2 * np.pi, n_grid)
u_grid, v_grid = np.meshgrid(u, v)
vertices = np.stack([np.cos(v_grid) * np.sin(u_grid),
                     np.sin(v_grid) * np.sin(u_grid),
                     np.cos(u_grid)],
                    axis=2)
x = np.outer(np.cos(v), np.sin(u))
y = np.outer(np.sin(v), np.sin(u))
z = np.outer(np.ones_like(u), np.cos(u))
def plot_vmf_density(ax, x, y, z, vertices, mu, kappa):
    vmf = vonmises_fisher(mu, kappa)
    pdf_values = vmf.pdf(vertices)
    pdfnorm = Normalize(vmin=pdf_values.min(), vmax=pdf_values.max())
    ax.plot_surface(x, y, z, rstride=1, cstride=1,
                    facecolors=plt.cm.viridis(pdfnorm(pdf_values)))
    ax.set_aspect('equal')
    ax.view_init(azim=-130, elev=-40)
    ax.axis('off')
    #ax.set_title(rf"$\kappa={kappa}$")

def plot_to_mobj(mu, k):
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(projection='3d')
    plot_vmf_density(ax, x, y, z, vertices, mu, k)
    #plt.subplots_adjust(top=1, bottom=0.0, left=0.0, right=1.0, wspace=0.)
    fig.canvas.draw()
    buf = fig.canvas.buffer_rgba()
    img = ImageMobject(buf)
    img.height = 6
    plt.close(fig)
    return img

class vmf(Slide):
    def construct(self):
        diap = Text("15").to_corner(UR,buff=0.4)
        titulo = Tex(r'Modelo de mezclas VMF').to_corner(UL,buff=0.5)
        templ = TexTemplate()
        templ.add_to_preamble(r"\usepackage{physics}")
        templ.add_to_preamble(r"\usepackage{amsmath}")

        #data generation
        mu = np.array([-np.sqrt(0.5), -np.sqrt(0.5), 0])
        vmfplot = plot_to_mobj(mu,5).to_edge(LEFT)
        mathdef = MathTex(r"f_x(x;\mu, \kappa) = C_d(\kappa)\exp{(\kappa \mathbf{x}^T\mu)} \\ C_d(\kappa) = \frac{\kappa^{d/2 - 1}}{(2\pi)^{d/2} I_{d/2-1}(\kappa)}", tex_template = templ)
        mathdef.scale(0.6).move_to([3.5,2,0])

        self.add(diap)
        self.play(Write(titulo))
        self.play(Create(mathdef),FadeIn(vmfplot))
        

        k_label = Tex('$\kappa = $').next_to(mathdef,DOWN,buff=0.5)
        k_tracker = ValueTracker(5)
        k_num = DecimalNumber(5).next_to(k_label,RIGHT,buff=0.1)
        self.play(Create(k_label),Create(k_num))
        
        def update_image(mob):
            new_mob = plot_to_mobj(mu, k_tracker.get_value())
            new_mob.to_edge(LEFT)
            mob.become(new_mob)

        self.next_slide()
        vmfplot.add_updater(update_image)
        k_num.add_updater(lambda d: d.set_value(k_tracker.get_value()))
        
        self.play(k_tracker.animate.set_value(300), run_time=3)
        self.next_slide()
        self.play(k_tracker.animate.set_value(5), run_time=2)
        self.next_slide()
        self.play(k_tracker.animate.set_value(200), run_time=2)

        self.next_slide()
        vmfplot.clear_updaters()
        k_num.clear_updaters()

        probmix = MathTex(r"P(t|x)  = \sum_{i=1}^m \alpha_i(x)\phi_i(t|x) \qquad  \sum_{i}^m \alpha_i = 1", tex_template = templ)
        probmix.scale(0.6).move_to([4,2,0])
        vmfdef = MathTex(r"\phi_i (t|x) & = \mathcal{K}(\mu_i(x),\kappa_i(x))\\ P(t|x) & = \sum_{i=1} ^{m} \alpha_i(x) \mathcal{K}(\mu_i(x),\kappa_i(x))", tex_template = templ)
        vmfdef.scale(0.6).next_to(probmix,DOWN,buff=0.5)
        likelihood = MathTex(r"\mathcal{L} \left( \mathcal{D} , \theta \right) = \prod_{i=1}^{N} P (x_i| \theta ) \qquad x_1, x_2,...,x_{N-1} \in \mathcal{D}", tex_template = templ)
        likelihood.scale(0.6).next_to(vmfdef,DOWN,buff=0.5)
        nll = MathTex(r"E=-\log(\mathcal{L}(\mathcal{D},\theta)) = -\sum_{i=1}^N\log(P(x_i|\theta))", tex_template = templ)
        nll.scale(0.6).next_to(likelihood,DOWN,buff=0.5)
        self.play(Unwrite(mathdef),FadeOut(k_label,k_num))
        self.play(Write(probmix))
        self.play(Write(vmfdef))
        self.next_slide()
        self.play(Create(likelihood))
        #self.next_slide()
        self.next_slide()
        self.play(Create(nll))
        