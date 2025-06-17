from manim import *

templ = TexTemplate()
templ.add_to_preamble(r"\usepackage{ragged2e}")

class planteamiento(Scene):
    def construct(self):
        diap = Text("3").to_corner(UR,buff=0.4)
        titulo = Tex(r'Planteamiento del problema').to_edge(UP,buff=0.5)

        cont = Tex(r'\justifying La manipulación de objetos es una habilidad clave en los robots de servicio doméstico que se ha abordado mediante métodos analíticos y estadísticos, y más recientemente, con técnicas de aprendizaje automático. En este trabajo, se aborda el problema de proponer una pose adecuada del efector final para sujetar un objeto dada su nube de puntos parcial; es decir, se asume que no existe una vista completa del objeto.',tex_template = templ)
        cont.scale(0.7)

        self.add(diap)
        self.play(Write(titulo),Write(cont))

class hipotesis(Scene):
    def construct(self):
        diap = Text("4").to_corner(UR,buff=0.4)
        titulo = Tex(r'Hipótesis').to_edge(UP,buff=0.5)

        cont = Tex(r'\justifying Se plantean las siguientes hipótesis sobre las que se desarrolló el trabajo de investigación: \begin{itemize} \item El uso de redes neuronales es viable para diseñar sistemas de planeación de agarres para robots de servicio. \item La optimización de los recursos de entrenamiento así como una buena selección de hiperparámetros acelerará el proceso de desarrollo y ayudará a entrenar modelos con mejor desempeño. \end{itemize}',tex_template = templ)
        cont.scale(0.7)

        self.add(diap)
        self.play(Write(titulo),Write(cont))

class objetivos(Scene):
    def construct(self):
        diap = Text("5").to_corner(UR,buff=0.4)
        titulo = Tex(r'Objetivos').to_edge(UP,buff=0.5)
        general = Tex(r'\justifying Diseñar y entrenar una red neuronal para optimizar la configuración de agarre de un robot de servicio para la manipulación de objetos.',tex_template = templ)
        especificos = Tex(r'\textbf{Objetivos específicos} \\ \justifying \begin{itemize} \item Diseñar una arquitectura de red neuronal que genere propuestas de configuración de agarre para robots de servicio. \item Desarrollar un ambiente simulado para generar datos de entrenamiento y realizar las pruebas de desempeño. \item Construir un dataset para entrenar la red con las especificaciones del robot de servicio del laboratorio. \item Entrenar la red utilizando el dataset construido y otros externos. \item Comparar el desempeño de la red con el sistema actual. \end{itemize}', tex_template = templ)
        #cont = Tex(r'\justifying La manipulación de objetos es una habilidad clave en los robots de servicio doméstico que se ha abordado mediante métodos analíticos y estadísticos, y más recientemente, con técnicas de aprendizaje automático. En este trabajo, se aborda el problema de proponer una pose adecuada del efector final para sujetar un objeto dada su nube de puntos parcial; es decir, se asume que no existe una vista completa del objeto.',tex_template = templ)
        #cont.scale(0.7)

        general.scale(0.6).next_to(titulo,DOWN,buff=0.5)
        especificos.scale(0.6).next_to(general,DOWN,buff=0.5)

        self.add(diap)
        self.play(Write(titulo),Write(general),Write(especificos))