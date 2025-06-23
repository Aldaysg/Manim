from manim import *
from manim_slides.slide import Slide, ThreeDSlide

class TempImg(Slide):
    def init_slide(self,title, diapn, imgpath):
        self.title = title
        self.diapn = str(diapn)
        self.imgpath = imgpath

    def build(self):
        #self.init_slide("siu",4,"./figs/trials.png")
        titulo = Tex(r"{}".format(self.title))
        diap = Text(self.diapn).to_corner(UR,buff=0.4)
        img = ImageMobject(self.imgpath)
        img.height = 5
        #self.add(titulo)
        titulo.scale(1.4)
        titulo.to_corner(UL,buff=0.5)
        #sustentante.shift(UP*1)
        self.add(diap)
        self.play(Write(titulo))
        self.play(FadeIn(img))
        #self.next_slide()

class mezclas(TempImg):
    def construct(self):
        self.init_slide("Modelo de mezclas",11,"./figs/mix.png")
        self.build()

class earth(TempImg):
    def construct(self):
        self.init_slide("Variedades",12,"./figs/earth.png")
        self.build()

class gazebo(TempImg):
    def construct(self):
        self.init_slide("Simulador",17,"./figs/gazebo.jpg")
        self.build()
        
class restriccion_conica(TempImg):
    def construct(self):
        self.init_slide("Restricciones",18,"./figs/restriccionconica.png")
        self.build()

class optim(TempImg):
    def construct(self):
        self.init_slide("Optimización bayesiana",19,"./figs/trials.png")
        self.build()

class entorno(TempImg):
    def construct(self):
        self.init_slide("Entorno de pruebas",20,"./figs/env.jpg")
        self.build()

class contour(TempImg):
    def construct(self):
        self.init_slide("Gráfica de contornos",21,"./figs/contour.png")
        self.build()

class parallel(TempImg):
    def construct(self):
        self.init_slide("Gráfica de coordenadas paralelas",21,"./figs/parallel.png")
        self.build()
        
class gpumid(TempImg):
    def construct(self):
        self.init_slide("Utilización de recursos",22,"./figs/gpu_mid.png")
        self.build()

class gpufull(TempImg):
    def construct(self):
        self.init_slide("Utilización de recursos",23,"./figs/gpu_full.png")
        self.build()

class distribucion_final(TempImg):
    def construct(self):
        self.init_slide("Distribución aproximada",24,"./figs/muestrasguardadas.png")
        self.build()

class ejemplo_agarre(TempImg):
    def construct(self):
        self.init_slide("Ejemplo agarre",25,"./figs/cbg.png")
        self.build()

class tabla_resultados(TempImg):
    def construct(self):
        self.init_slide("Resultados experimentales",26,"./figs/tabla1.png")
        self.build()
    
class tabla_itzel(TempImg):
    def construct(self):
        self.init_slide("Comparación con modelo actual",27,"./figs/tabla2.png")
        self.build()

