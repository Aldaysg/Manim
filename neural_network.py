from manim import *
from manim_slides.slide import Slide

#from manim_ml.neural_network import Convolutional2DLayer, FeedForwardLayer, ImageLayer, NeuralNetwork
#from manim_tikz import Tikz
#from manim.animation.composition

config.disable_caching = False

class definicion_nn(Slide):

    def construct(self):
        templ = TexTemplate()
        diap = Text("13").to_corner(UR,buff=0.4)
        #templ.documentclass = r"\documentclass[preview,dvisvgm]{standalone}"
        templ.add_to_preamble(r"\usepackage{amsmath}")
        templ.add_to_preamble(r"\usepackage{tikz-cd}")
        templ.add_to_preamble(r"\usepackage{quiver}")
        #templ.add_to_preamble(r"\tikzset{every picture/.style={line width = 1.6pt}}")
        titulo = Tex(r"Definición de la red")
        #mathdef = MathTex(r"f:c \to g").scale(1.5)
        mathdef = Tex(r'\[\begin{tikzcd} c && g \arrow["{f(c)}", from=1-1, to=1-3] \end{tikzcd}\]',tex_template=templ,stroke_width = 0.8)

        pcd = Tex(r"$c \in \mathbb{R} ^ {H \times W \times C} \quad$ Nube de puntos").shift(DOWN).scale(0.8)
        grasp = Tex(r"$g = \{p \in \mathbb{R} ^3, q \in \mathbb{H}_1 \} \quad $ Pose del EF").shift(DOWN*2).scale(0.8)
        pcd.add_updater(lambda x: x.next_to(mathdef,DOWN,buff=0.5))
        grasp.add_updater(lambda x: x.next_to(mathdef,DOWN*3,buff=0.5))
        
        self.add(diap)
        self.play(Create(titulo))
        #self.play(titulo.animate.shift(UP*2))
        self.play(titulo.animate.to_edge(UP, buff=0.2))
        self.play(Create(mathdef), Write(pcd), Write(grasp))
        self.play(mathdef.animate.next_to(titulo,DOWN,buff=0.4))