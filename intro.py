from manim import *
from manim_slides.slide import Slide

templ = TexTemplate()
templ.add_to_preamble(r"\usepackage{ragged2e}")

class planteamiento(Slide):
    def construct(self):
        diap = Text("1").to_corner(UR,buff=0.4)
        titulo = Tex(r'Problem setting').to_edge(UP,buff=0.5)

        cont = Tex(r"\justifying Object manipulation is a key skill in domestic service robots that has been addressed using analytical and statistical methods, and more recently, with machine learning techniques. In this work, we address the problem of proposing a suitable final effector pose to grasp an object given an object's partial point cloud, i.e., we assume that there is no full view of the object.",tex_template = templ)
        cont.scale(0.7)

        cont2 = Tex(r"\justifying We propose a DNN architecture composed of two main parts: a stage for getting the final effector position and another one, to get the orientation. To propose orientations, we used two approaches: geodesic regression and a kernel mixture model. ",tex_template = templ)
        cont2.scale(0.7)

        self.add(diap)
        self.play(Write(titulo),Write(cont))
        self.next_slide()
        self.play(Transform(cont,cont2))

class hipotesis(Slide):
    def construct(self):
        diap = Text("2").to_corner(UR,buff=0.4)
        titulo = Tex(r'Hypothesis').to_edge(UP,buff=0.5)

        cont = Tex(r'\justifying This work was developed following these hypothesis: \begin{itemize} \item Deep neural networks can be applied to the problem of finding suitable grasp proposals for object manipulation.  \item The optimization of training resources and the appropiate tuning of hyperparameters will result in models with better performance. \end{itemize}',tex_template = templ)
        cont.scale(0.7)

        self.add(diap)
        self.play(Write(titulo),Write(cont))

class objetivos(Slide):
    def construct(self):
        diap = Text("3").to_corner(UR,buff=0.4)
        titulo = Tex(r'Objectives').to_edge(UP,buff=0.5)
        general = Tex(r'\justifying Design and train a neural network to generate a suitable gripper pose of a service robot for object manipulation from a partial pointcloud.',tex_template = templ)
        especificos = Tex(r'\textbf{Specific objectives} \\ \justifying \begin{itemize} \item Design the neural network architecture. \item Create a simulated environment for the generation of training data and testing. \item Create a grasp dataset to train the network. \item Compare the performance of the network to the system currenty implemented. \end{itemize}', tex_template = templ)
        #cont = Tex(r'\justifying La manipulación de objetos es una habilidad clave en los robots de servicio doméstico que se ha abordado mediante métodos analíticos y estadísticos, y más recientemente, con técnicas de aprendizaje automático. En este trabajo, se aborda el problema de proponer una pose adecuada del efector final para sujetar un objeto dada su nube de puntos parcial; es decir, se asume que no existe una vista completa del objeto.',tex_template = templ)
        #cont.scale(0.7)

        general.scale(0.6).next_to(titulo,DOWN,buff=0.5)
        especificos.scale(0.6).next_to(general,DOWN,buff=0.5)

        self.add(diap)
        self.play(Write(titulo),Write(general),Write(especificos))

class conclusiones(Slide):
    def construct(self):
        diap = Text("24").to_corner(UR,buff=0.4)
        titulo = Tex(r'Conclusion').to_edge(UP,buff=0.5)

        cont = Tex(r"\justifying We trained a network that is capable of approximating the probability distribution of suitable grasp proposals directly from a point cloud and sampling from it with reasonable accuracy for most objects. ",tex_template = templ)
        cont.scale(0.7)

        cont2 = Tex(r"\justifying When comparing to the current implemented system we found that the network has similar albeit slightly worse accuracy. However, it's important to note that the current system requires robust image processing techniques like object segmentation, contour detection and filtering since this method is very sensitive to outliers and noise. In comparison, the neural network model can achieve similar performance without these methods since it only requires a bounding box around the object and it is not necessary to eliminate the background.",tex_template = templ)
        cont2.scale(0.7)

        self.add(diap)
        self.play(Write(titulo),Write(cont))
        self.next_slide()
        #self.play(Unwrite(cont))
        self.play(Transform(cont,cont2))

class conclusiones2(Slide):
    def construct(self):
        diap = Text("29").to_corner(UR,buff=0.4)
        titulo = Tex(r'Conclusiones').to_edge(UP,buff=0.5)

        cont = Tex(r'\justifying Del mismo modo se encontró que un manejo adecuado de los recursos de cómputo y una selección apropiada de hiperparámetros de entrenamiento pueden mejorar considerablemente el rendimiento de estos sistemas. Demostrando que es posible optimizar estos modelos sin necesidad de modificar la arquitectura de la red.',tex_template = templ)
        cont.scale(0.7)

        self.add(diap)
        self.play(Write(titulo),Write(cont))