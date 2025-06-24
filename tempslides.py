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
        self.img = ImageMobject(self.imgpath)
        self.img.height = 5.5
        #self.add(titulo)
        titulo.scale(1.4)
        titulo.to_corner(UL,buff=0.5)
        #sustentante.shift(UP*1)
        self.add(diap)
        self.play(Write(titulo))
        self.play(FadeIn(self.img))
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
        self.init_slide("Entorno de pruebas",23,"./figs/env.jpg")
        self.build()

class contour(TempImg):
    def construct(self):
        self.init_slide("Gráfica de contornos",20,"./figs/contour.png")
        self.build()

class parallel(TempImg):
    def construct(self):
        self.init_slide("Gráfica de coordenadas paralelas",21,"./figs/parallel.png")
        self.build()
        
class gpumid(TempImg):
    def construct(self):
        self.init_slide("Utilización de recursos",22,"./figs/gpu_mid.png")
        self.build()
        img2 = ImageMobject("./figs/gpu_full.png")
        img2.height = 5.5
        self.next_slide()
        self.play(FadeTransform(self.img,img2))

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
        #self.init_slide("Resultados experimentales",26,"./figs/tabla1.png")
        #self.build()
        templ = TexTemplate()
        diap = Text("26").to_corner(UR,buff=0.4)
        #templ.documentclass = r"\documentclass[preview,dvisvgm]{standalone}"
        templ.add_to_preamble(r"\usepackage{amsmath}")
        templ.add_to_preamble(r"\usepackage{booktabs}")
        templ.add_to_preamble(r"\usepackage{quiver}")
        #templ.add_to_preamble(r"\tikzset{every picture/.style={line width = 1.6pt}}")
        titulo = Tex(r"Resultados experimentales").to_corner(UL,buff=0.5)
        tab = Tex(r'\begin{table} \centering \begin{tabular}{@{}llc@{}} \toprule \textbf{Objeto YCB}      & \textbf{Forma del objeto} & \textbf{Exactitud[\%]} \\ \midrule 001\_chips\_can          & Cilíndrico           & 79.5                    \\ 002\_master\_chef\_can   & Cilíndrico           & 71                      \\ 003\_cracker\_box        & Caja grande          & 70.5                    \\ 004\_sugar\_box          & Caja grande          & 64.5                    \\ 005\_tomato\_soup\_can   & Cilíndrico           & 69.5                    \\ 006\_mustard\_bottle     & Botella plana        & 69                      \\ 007\_tuna\_fish\_can     & Cilíndrico           & 59                      \\ 008\_pudding\_box        & Caja pequeña         & 67.5                    \\ 009\_gelatin\_box        & Caja pequeña         & 72.5                    \\ 010\_potted\_meat\_can   & Caja pequeña         & 68.5                    \\ 011\_banana              & Otro                 & 53                      \\ 019\_pitcher\_base       & Cilíndrico           & 51.5                    \\ 021\_bleach\_cleanser    & Botella plana        & 44                      \\ 024\_bowl                & Otro                 & 62.5                    \\ 025\_mug                 & Cilíndrico           & 58                      \\ 035\_power\_drill        & Otro                 & 26                      \\ 036\_wood\_block         & Caja grande          & 78                      \\ 037\_scissors            & Herramienta          & 22.5                    \\ 040\_large\_marker       & Herramienta          & 21.5                    \\ 048\_hammer              & Herramienta          & 9                       \\ 051\_large\_clamp        & Herramienta          & 11.5                    \\ 052\_extra\_large\_clamp & Herramienta          & 24                      \\ 056\_tennis\_ball        & Esférico             & 60                      \\ 061\_foam\_brick         & Caja pequeña         & 67.5                    \\ 077\_rubiks\_cube        & Cubo                 & 70.5                    \\ \bottomrule \end{tabular} \label{tab:obj_acc} \end{table}', tex_template = templ)
        tab2 = Tex(r"\begin{table}[H] \centering \label{tab:shape_acc} \begin{tabular}{@{}lc@{}} \toprule \textbf{Forma del objeto} & \textbf{Exactitud[\%]} \\ \midrule Cilíndrico           & 64.75                   \\ Esférico             & 60                      \\ Caja grande          & 71                      \\ Caja pequeña         & 69                      \\ Cubo                 & 70.5                    \\ Botella plana        & 56.5                    \\ Herramienta          & 17.7                    \\ Otro                 & 47.166                  \end{tabular} \end{table}",tex_template = templ)
        tab.scale(0.38).to_edge(DOWN)
        tab2.scale(0.38)

        self.add(diap)
        self.play(Write(titulo),Write(tab))
        self.next_slide()
        self.play(tab.animate.to_edge(LEFT,buff=3))
        tab2.next_to(tab,RIGHT,buff=1)
        self.play(Write(tab2))

class tabla_itzel(TempImg):
    def construct(self):
        #self.init_slide("Comparación con modelo actual",27,"./figs/tabla2.png")
        #self.build()
        templ = TexTemplate()
        diap = Text("27").to_corner(UR,buff=0.4)
        #templ.documentclass = r"\documentclass[preview,dvisvgm]{standalone}"
        templ.add_to_preamble(r"\usepackage{amsmath}")
        templ.add_to_preamble(r"\usepackage{booktabs}")
        templ.add_to_preamble(r"\usepackage{quiver}")
        #templ.add_to_preamble(r"\tikzset{every picture/.style={line width = 1.6pt}}")
        titulo = Tex(r"Comparación con modelo actual").to_corner(UL,buff=0.5)
        tab = Tex(r'\begin{table} \begin{center} \begin{tabular}{| c | c | c | c | c | c | c |} \hline Tipo & Objeto & Dimensiones & Intentos & tipo de & Agarres & tasa \\ & & [m] & & agarre & exitosos & $\%$ \\ \hline prismático & pringles & 0.2x0.08x0.08 & 5 & lateral & 3 & 60 \\ prismático & pringles & 0.2x0.08x0.08 & 5 & superior & 5 & 100 \\ caja & jugo & 0.1x0.05x0.03 & 5 & superior & 4 & 80\\ cubico & taza & 0.06x0.07x0.06 & 5 & superior & 3 & 60\\ prismático & lata de & 0.07x0.07x0.06 & 5 & superior & 4 & 80\\ & refresco & & & & & \\ esferoide & manzana & 0.07x0.06x0.06 & 5 & superior & 3 & 60 \\ caja & caja de & 0.3x0.2x0.05 & 5 & lateral & 4 & 80\\ & cereal & & & & & \\ prismático & lata de & 0.012x0.07x0.07 & 5 & superior & 4 & 80\\ & conservas & & & & & \\ box & jamón en & 0.07x0.12x0.06 & 5 & superior & 4 & 80\\ & lata & & & & & \\ prismático & copa & 0.23x0.09x0.09 & 5 & lateral & 4 & 80\\ cuboide & pera & 0.08x0.06x0.05 & 5 & superior & 4 & 80\\ prismático & mostaza & 0.13x0.07x0.04 & 4 & lateral & 3 & 60\\ prismático & desinfectante & 0.25x0.1x0.1 & 5 & lateral & 5 & 100\\ prismático & desodorante & 0.1x0.05x0.05 & 5 & superior & 3 & 60\\ \hline \end{tabular}  \label{tab:grasping} \end{center} \end{table}',tex_template = templ)
        #tab2 = Tex(r"\begin{table}[H] \centering \label{tab:shape_acc} \begin{tabular}{@{}lc@{}} \toprule \textbf{Forma del objeto} & \textbf{Exactitud[\%]} \\ \midrule Cilíndrico           & 64.75                   \\ Esférico             & 60                      \\ Caja grande          & 71                      \\ Caja pequeña         & 69                      \\ Cubo                 & 70.5                    \\ Botella plana        & 56.5                    \\ Herramienta          & 17.7                    \\ Otro                 & 47.166                  \end{tabular} \end{table}",tex_template = templ)
        tab.scale(0.48)
        #tab2.scale(0.38)

        self.add(diap)
        self.play(Write(titulo),Write(tab))

