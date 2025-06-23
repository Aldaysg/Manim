from manim import *
from manim_slides.slide import Slide

class Portada(Slide):
    def construct(self):
        titulo = Tex(r"{0.5\textwidth}\centering Redes neuronales para manipulación de objetos en robots de servicio",tex_environment="minipage")
        sustentante = Tex(r'Germán Alday Salazar')
        director = Tex(r'Director de tesis:\\Dr. Marco Antonio Negrete Villanueva')
        
        #self.add(titulo)
        titulo.scale(1.4)
        titulo.to_edge(UP,buff=1)
        #sustentante.shift(UP*1)
        director.shift(DOWN)
        self.play(Write(titulo))
        self.next_slide()
        self.play(Write(sustentante),Write(director))

class division(Slide):
    def construct(self):
        capitulos = Tex(r'Secciones')
        secciones = Tex(r'\begin{itemize} ' \
        '\item Introducción ' \
        '\item Marco teórico ' \
        '\item Diseño e implementación ' \
        '\item Resultados ' \
        '\item Conclusiones ' \
        '\end{itemize}')
        diap = Text("1")

        capitulos.to_edge(UP,buff=0.5)
        diap.to_corner(UR,buff=0.4)

        self.add(diap)
        self.play(Write(capitulos))
        self.play(Write(secciones))
