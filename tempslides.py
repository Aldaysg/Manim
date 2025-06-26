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
        self.init_slide("Gazebo simulator",13,"./figs/gazebo.jpg")
        self.build()
        
class restriccion_conica(TempImg):
    def construct(self):
        self.init_slide("Dataset generation",14,"./figs/restriccionconica.png")
        self.build()

class optim(TempImg):
    def construct(self):
        self.init_slide("Bayesian optimization",15,"./figs/trials.png")
        self.build()

class entorno(TempImg):
    def construct(self):
        self.init_slide("Testing environment",19,"./figs/env.jpg")
        self.build()

class contour(TempImg):
    def construct(self):
        self.init_slide("Contour plot",16,"./figs/contour.png")
        self.build()

class parallel(TempImg):
    def construct(self):
        self.init_slide("Parallel coordinates plot",17,"./figs/parallel.png")
        self.build()
        
class gpumid(TempImg):
    def construct(self):
        self.init_slide("Resource management",18,"./figs/gpu_mid.png")
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
        self.init_slide("Aproximate distribution",20,"./figs/muestrasguardadas.png")
        self.build()

class ejemplo_agarre(TempImg):
    def construct(self):
        self.init_slide("Pose sample",21,"./figs/cbg.png")
        self.build()

class tabla_resultados(TempImg):
    def construct(self):
        #self.init_slide("Resultados experimentales",26,"./figs/tabla1.png")
        #self.build()
        templ = TexTemplate()
        diap = Text("22").to_corner(UR,buff=0.4)
        #templ.documentclass = r"\documentclass[preview,dvisvgm]{standalone}"
        templ.add_to_preamble(r"\usepackage{amsmath}")
        templ.add_to_preamble(r"\usepackage{booktabs}")
        templ.add_to_preamble(r"\usepackage{quiver}")
        #templ.add_to_preamble(r"\tikzset{every picture/.style={line width = 1.6pt}}")
        titulo = Tex(r"Experimental Results").to_corner(UL,buff=0.5)
        tab = Tex(r'\begin{table} \centering \begin{tabular}{@{}llc@{}} \toprule \textbf{YCB Object}      & \textbf{Object shape} & \textbf{Accuracy[\%]} \\ \midrule 001\_chips\_can          & Cylindrical           & 79.5                    \\ 002\_master\_chef\_can   & Cylindrical           & 71                      \\ 003\_cracker\_box        & Big Box          & 70.5                    \\ 004\_sugar\_box          & Big Box          & 64.5                    \\ 005\_tomato\_soup\_can   & Cylindrical           & 69.5                    \\ 006\_mustard\_bottle     & Flat bottle        & 69                      \\ 007\_tuna\_fish\_can     & Cylindrical           & 59                      \\ 008\_pudding\_box        & Small box         & 67.5                    \\ 009\_gelatin\_box        & Small box         & 72.5                    \\ 010\_potted\_meat\_can   & Small box         & 68.5                    \\ 011\_banana              & Otro                 & 53                      \\ 019\_pitcher\_base       & Cylindrical           & 51.5                    \\ 021\_bleach\_cleanser    & Flat bottle        & 44                      \\ 024\_bowl                & Otro                 & 62.5                    \\ 025\_mug                 & Cylindrical           & 58                      \\ 035\_power\_drill        & Otro                 & 26                      \\ 036\_wood\_block         & Big Box          & 78                      \\ 037\_scissors            & Tool          & 22.5                    \\ 040\_large\_marker       & Tool          & 21.5                    \\ 048\_hammer              & Tool          & 9                       \\ 051\_large\_clamp        & Tool          & 11.5                    \\ 052\_extra\_large\_clamp & Tool          & 24                      \\ 056\_tennis\_ball        & Spherical             & 60                      \\ 061\_foam\_brick         & Small box         & 67.5                    \\ 077\_rubiks\_cube        & Cube                 & 70.5                    \\ \bottomrule \end{tabular} \label{tab:obj_acc} \end{table}', tex_template = templ)
        tab2 = Tex(r"\begin{table}[H] \centering \label{tab:shape_acc} \begin{tabular}{@{}lc@{}} \toprule \textbf{Object shape} & \textbf{Accuracy[\%]} \\ \midrule Cylindrical           & 64.75                   \\ Spherical             & 60                      \\ Big Box          & 71                      \\ Small box         & 69                      \\ Cube                 & 70.5                    \\ Flat bottle        & 56.5                    \\ Tool          & 17.7                    \\ Other                 & 47.166                  \end{tabular} \end{table}",tex_template = templ)
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
        diap = Text("23").to_corner(UR,buff=0.4)
        #templ.documentclass = r"\documentclass[preview,dvisvgm]{standalone}"
        templ.add_to_preamble(r"\usepackage{amsmath}")
        templ.add_to_preamble(r"\usepackage{booktabs}")
        templ.add_to_preamble(r"\usepackage{quiver}")
        #templ.add_to_preamble(r"\tikzset{every picture/.style={line width = 1.6pt}}")
        titulo = Tex(r"Comparison with current system").to_corner(UL,buff=0.5)
        tab = Tex(r'\begin{table} \begin{center} \begin{tabular}{| c | c | c | c | c | c | c |} \hline Type & Object & Dimensions & Attempts & type of & successful & rate \\ & & [m] & & grasp & grasps & $\%$ \\ \hline prismatic & pringles & 0.2x0.08x0.08 & 5 & side & 3 & 60 \\ prismatic & pringles & 0.2x0.08x0.08 & 5 & top & 5 & 100 \\ box & juice & 0.1x0.05x0.03 & 5 & top & 4 & 80\\ cubic & cup & 0.06x0.07x0.06 & 5 & top & 3 & 60\\ prismatic & can & 0.07x0.07x0.06 & 5 & top & 4 & 80\\ & soda & & & & & \\ spheroid & apple & 0.07x0.06x0.06 & 5 & top & 3 & 60 \\ box & box of & 0.3x0.2x0.05 & 5 & side & 4 & 80\\ & cereal & & & & & \\ prismatic & can of & 0.012x0.07x0.07 & 5 & top & 4 & 80\\ & preserves & & & & & \\ box & ham in & 0.07x0.12x0.06 & 5 & top & 4 & 80\\ & can & & & & & \\ prismatic & cup & 0.23x0.09x0.09 & 5 & side & 4 & 80\\ Cube & pear & 0.08x0.06x0.05 & 5 & top & 4 & 80\\ prismatic & mustard & 0.13x0.07x0.04 & 4 & side & 3 & 60\\ prismatic & disinfectant & 0.25x0.1x0.1 & 5 & side & 5 & 100\\ prismatic & deodorant & 0.1x0.05x0.05 & 5 & superior & 3 & 60\\ \hline \end{tabular} \label{tab:grasping} \end{center} \end{table}',tex_template = templ)
        #tab2 = Tex(r"\begin{table}[H] \centering \label{tab:shape_acc} \begin{tabular}{@{}lc@{}} \toprule \textbf{Forma del objeto} & \textbf{Exactitud[\%]} \\ \midrule Cylindrical           & 64.75                   \\ Spherical             & 60                      \\ Big Box          & 71                      \\ Small box         & 69                      \\ Cube                 & 70.5                    \\ Flat bottle        & 56.5                    \\ Tool          & 17.7                    \\ Otro                 & 47.166                  \end{tabular} \end{table}",tex_template = templ)
        tab.scale(0.48)
        #tab2.scale(0.38)

        self.add(diap)
        self.play(Write(titulo),Write(tab))

