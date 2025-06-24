from manim import *
from manim_slides.slide import Slide, ThreeDSlide

from manim_ml.neural_network import Convolutional2DLayer, FeedForwardLayer, NeuralNetwork, EmbeddingLayer,VectorLayer

# This changes the resolution of our rendered videos
# config.pixel_height = 700
# config.pixel_width = 1900
# config.frame_height = 7.0
# config.frame_width = 7.0

# Here we define our basic scene
class BasicScene(ThreeDSlide):

    # The code for generating our scene goes here
    def construct(self):
        # Make the neural network
        diap = Text("11").to_corner(UR,buff=0.4)
        titulo = Tex(r'Redes neuronales convolucionales').to_corner(UL,buff=0.5)
        conv = MathTex(r'\mathbf{C}(x,y)=\mathbf{I} * \mathbf{K} =\sum_{i=-a}^a{\sum_{j=-b}^b{ I (i,j)K(x-i,y-j)}}')
        self.add_fixed_in_frame_mobjects(diap,titulo)

        nn = NeuralNetwork([
                Convolutional2DLayer(1, 7, 3, filter_spacing=0.32),
                Convolutional2DLayer(3, 5, 3, filter_spacing=0.32,activation_function="ReLU"),
                Convolutional2DLayer(5, 3, 3, filter_spacing=0.18,activation_function="ReLU"),
                FeedForwardLayer(4,rectangle_stroke_width=0,activation_function="ReLU"),
                FeedForwardLayer(4,rectangle_stroke_width=0,activation_function="ReLU"),
                VectorLayer(3),
                #EmbeddingLayer()
            ],
            layer_spacing=0.25,
        )
        # Center the neural network
        nn.to_edge(DOWN,buff=2).scale(1.7)
        conv.next_to(nn,UP,buff=0.5).scale(0.7)
        self.add(diap,nn)
        self.play(Write(titulo),Write(conv))
        self.next_slide()
        #self.play(FadeIn(nn))
        # Make a forward pass animation
        forward_pass = nn.make_forward_pass_animation(run_time=8)
        # Play animation
        self.play(forward_pass)

class fullyconnected(ThreeDSlide):

    # The code for generating our scene goes here
    def construct(self):
        # Make the neural network
        diap = Text("10").to_corner(UR,buff=0.4)
        titulo = Tex(r'Redes neuronales artificiales').to_corner(UL,buff=0.5)
        layer = MathTex(r'\mathbf{a}^{(n+1)} &= \sigma \left(  \mathbf{W}^{(n)} \mathbf{a}^{(n)} + \mathbf{b}^{(n)} \right)')
        self.add_fixed_in_frame_mobjects(diap,titulo)

        nn = NeuralNetwork([
                FeedForwardLayer(3,rectangle_stroke_width=0),
                FeedForwardLayer(8,rectangle_stroke_width=0),
                FeedForwardLayer(8,rectangle_stroke_width=0),
                #FeedForwardLayer(8,rectangle_stroke_width=0),
                FeedForwardLayer(8,rectangle_stroke_width=0),
                FeedForwardLayer(8,rectangle_stroke_width=0),
                FeedForwardLayer(3,rectangle_stroke_width=0),
                VectorLayer(3)
            ],
            layer_spacing=0.7,
        )
        # Center the neural network
        nn.to_edge(DOWN,buff=2).scale(1.8)
        layer.next_to(nn,UP,buff=0.5).scale(0.7).shift(LEFT*0.8)
        self.add(diap,nn)
        self.play(Write(titulo),Write(layer))
        self.next_slide()
        # Make a forward pass animation
        forward_pass = nn.make_forward_pass_animation(run_time=9)
        # Play animation
        self.play(forward_pass)