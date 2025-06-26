from manim import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import optuna_dashboard
import optuna
import io
from PIL import Image   
from optuna.pruners import PercentilePruner
from scipy.optimize import curve_fit
from manim_slides.slide import Slide, ThreeDSlide


plt.style.use('dark_background')

# study_number = 4
# study_id = "joint_network_optim" + str(study_number) # Unique identifier of the study.
# study_storage = "sqlite:////home/robocup/Juskeshino/catkin_ws/src/graspnet/{}.db".format(study_id)
# study = optuna.create_study(study_name=study_id,storage=study_storage, direction="minimize", load_if_exists=True, pruner=PercentilePruner(25.0,n_startup_trials=10,n_min_trials=10))

class GetRiemannRectanglesExample(Scene):
    def construct(self):
        ax = Axes(y_range=[-2, 10])
        quadratic = ax.plot(lambda x: 0.5 * x ** 2 - 0.5)

        # the rectangles are constructed from their top right corner.
        # passing an iterable to `color` produces a gradient
        rects_right = ax.get_riemann_rectangles(
            quadratic,
            x_range=[-4, -3],
            dx=0.25,
            color=(TEAL, BLUE_B, DARK_BLUE),
            input_sample_type="right",
        )

        # the colour of rectangles below the x-axis is inverted
        # due to show_signed_area
        rects_left = ax.get_riemann_rectangles(
            quadratic, x_range=[-1.5, 1.5], dx=0.15, color=YELLOW
        )

        bounding_line = ax.plot(
            lambda x: 1.5 * x, color=BLUE_B, x_range=[3.3, 6]
        )
        bounded_rects = ax.get_riemann_rectangles(
            bounding_line,
            bounded_graph=quadratic,
            dx=0.15,
            x_range=[4, 5],
            show_signed_area=False,
            color=(MAROON_A, RED_B, PURPLE_D),
        )

        self.add(
            ax, bounding_line, rects_right, rects_left, bounded_rects
        )

def mpl_image3d_plt(amp1,x):
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(projection='3d')
    ax.view_init(elev=40+3*np.sin(amp1), azim=20+10*np.cos(amp1))
    ax.voxels(x, edgecolor='k')
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    ax.axes.zaxis.set_ticklabels([])
    fig.canvas.draw()
    buf = fig.canvas.buffer_rgba()
    img = ImageMobject(buf).scale(1)
    plt.close(fig)
    return img


class MatplotExample(Scene):
    def construct(self):
        #self.camera.background_color= WHITE
        x=np.full((21,27,27),0)
        x[10,10,10]=1
        x[10,16,10]=1
        amp1=0
        amp2=TAU
        tr_amplitude = ValueTracker(amp1)
        image = mpl_image3d_plt(amp1, x)
        self.add(image)

        def update_image(mob):
            new_mob = mpl_image3d_plt(tr_amplitude.get_value(), x)
            mob.become(new_mob)

        image.add_updater(update_image)
        self.play(tr_amplitude.animate.set_value(amp2), run_time=4)

def mixture_to_mobj(show_mix = False, show_model = False):
    np.random.seed(1)
    data=np.concatenate((np.random.normal(1, .2, 5000), np.random.normal(1.6, .3, 2500)))
    fig = plt.figure(dpi=300)
    y,x,_=plt.hist(data, 100, alpha=.3, label='Real distribution',color='lightsteelblue')
    x=(x[1:]+x[:-1])/2 # for len(x)==len(y)

    #x, y inputs can be lists or 1D numpy arrays

    def gauss(x, mu, sigma, A):
        return A*np.exp(-(x-mu)**2/2/sigma**2)

    def bimodal(x, mu1, sigma1, A1, mu2, sigma2, A2):
        return gauss(x,mu1,sigma1,A1)+gauss(x,mu2,sigma2,A2)

    expected = (1, .2, 250, 2, .2, 125)
    params, cov = curve_fit(bimodal, x, y, expected)
    sigma=np.sqrt(np.diag(cov))
    x_fit = np.linspace(x.min(), x.max(), 500)
    #plot combined...
    
    if show_model:
        plt.plot(x_fit, bimodal(x_fit, *params), color='lavender', lw=3, label='Approximate density function')
    #...and individual Gauss curves
    if show_mix:
        plt.plot(x_fit, gauss(x_fit, *params[:3]), color='royalblue', lw=2, ls="--", label='Kernel 1')
        plt.plot(x_fit, gauss(x_fit, *params[3:]), color='royalblue', lw=2, ls=":", label='Kernel 2')
    #and the original data points if no histogram has been created before
    #plt.scatter(x, y, marker="X", color="black", label="original data")
    plt.legend()
    fig.canvas.draw()
    buf = fig.canvas.buffer_rgba()
    img = ImageMobject(buf)
    img.height = 6
    #img.next_to(titulo,DOWN,buff=0.5)
    plt.close(fig)
    return img


class mezclas(Slide):
    def construct(self):
        diap = Text("9").to_corner(UR,buff=0.4)
        titulo = Tex(r'Mixture Model').to_corner(UL,buff=0.5)
        #data generation
        img = mixture_to_mobj()
        img2 = mixture_to_mobj(show_mix=True)
        img3 = mixture_to_mobj(show_mix=True, show_model=True)
        
        self.add(diap)
        self.play(Write(titulo))
        self.play(FadeIn(img))
        self.next_slide()
        self.play(Transform(img,img2))
        self.next_slide()
        self.play(Transform(img2,img3))
        self.remove(img,img2)
        self.next_slide()
        self.play(img3.animate.shift(LEFT*3))

        templ = TexTemplate()
        templ.add_to_preamble(r"\usepackage{physics}")
        templ.add_to_preamble(r"\usepackage{amsmath}")

        probmix = MathTex(r"P(t|x)  = \sum_{i=1}^m \alpha_i(x)\phi_i(t|x) \qquad  \sum_{i}^m \alpha_i = 1", tex_template = templ)
        probmix.scale(0.6).move_to([4,2,0])
        gaussmix = MathTex(r"\phi_i (t|x) & = \mathcal{N}(\mu_i(x),\Sigma_i(x)) \\ P(t|x) & = \sum_{i=1} ^{m} \alpha_i(x) \mathcal{N}(\mu_i(x),\Sigma_i(x))", tex_template = templ)
        gaussmix.scale(0.6).next_to(probmix,DOWN,buff=0.5)
        likelihood = MathTex(r"\mathcal{L} \left( \mathcal{D} , \theta \right) = \prod_{i=1}^{N} P (x_i| \theta ) \qquad x_1, x_2,...,x_{N-1} \in \mathcal{D}", tex_template = templ)
        likelihood.scale(0.6).next_to(gaussmix,DOWN,buff=0.5)
        nll = MathTex(r"E=-\log(\mathcal{L}(\mathcal{D},\theta)) = -\sum_{i=1}^N\log(P(x_i|\theta))", tex_template = templ)
        nll.scale(0.6).next_to(likelihood,DOWN,buff=0.5)
        self.play(Create(probmix))
        self.next_slide()
        self.play(Create(gaussmix))
        self.next_slide()
        self.play(Create(likelihood))
        self.next_slide()
        self.play(Create(nll))

def pio_to_mobj():
    fig3 = optuna.visualization.plot_parallel_coordinate(study, params=["max_lr", "mdm_mixtures","kappa","weight_decay"],)
    fig3.update_layout(
    template="plotly_dark",
    #colorscale=px.colors.sequential.Reds
    #color = 'Trial',
    #color_continuous_scale="Viridis",
    )
    buf = io.BytesIO(fig3.to_image(format="png", width=1280, height=720, scale=3))
    #img = SVGMobject(fig3.to_image(format="svg", width=1280, height=720, scale=1))
    img = Image.open(buf)
    img = ImageMobject(img)
    img.height = 5.5
    return img

class contour(Scene):
    def construct(self):
        diap = Text("5").to_corner(UR,buff=0.4)
        titulo = Tex(r'Gráfica de contornos').to_corner(UL,buff=0.5)
        #data generation
        img = pio_to_mobj()
        
        self.add(diap)
        self.play(Write(titulo))
        self.play(FadeIn(img))
