from manim import *
from manim_slides.slide import Slide, ThreeDSlide

class PH(Slide):
    def init_slide(self, title, cont, diapn):
        self.title = title
        self.cont = cont
        self.diapn = str(diapn)

    def build(self):
        diap = Text(self.diapn).to_corner(UR,buff=0.4)
        titulo = Tex(r'{}'.format(self.title)).to_corner(UL,buff=0.5)

        cont = Tex(r'{}'.format(self.cont))
        cont.scale(0.7)

        self.add(diap)
        self.play(Write(titulo),Write(cont))

class vmf(PH):
    def construct(self):
        self.init_slide("VMF","Animación VMF placeholder",13)
        self.build()

class metodo_pca(PH):
    def construct(self):
        self.init_slide("Modelo PCA","Métodos de pca y vision placeholder",26)
        self.build()


