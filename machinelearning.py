from manim import *
from manim_slides.slide import Slide, ThreeDSlide

from manim_ml.neural_network import Convolutional2DLayer, FeedForwardLayer, NeuralNetwork, EmbeddingLayer,VectorLayer

# This changes the resolution of our rendered videos
# config.pixel_height = 700
# config.pixel_width = 1900
# config.frame_height = 7.0
# config.frame_width = 7.0

# Here we define our basic scene
class BasicScene(ThreeDScene):

    # The code for generating our scene goes here
    def construct(self):
        # Make the neural network
        nn = NeuralNetwork([
                Convolutional2DLayer(1, 7, 3, filter_spacing=0.32,activation_function="ReLU"),
                Convolutional2DLayer(3, 5, 3, filter_spacing=0.32),
                Convolutional2DLayer(5, 3, 3, filter_spacing=0.18),
                FeedForwardLayer(4,rectangle_stroke_width=0),
                FeedForwardLayer(4,rectangle_stroke_width=0),
                VectorLayer(3),
                #EmbeddingLayer()
            ],
            layer_spacing=0.25,
        )
        # Center the neural network
        nn.move_to(ORIGIN)
        self.add(nn)
        # Make a forward pass animation
        forward_pass = nn.make_forward_pass_animation(run_time=1)
        # Play animation
        self.play(forward_pass)

class fullyconnected(ThreeDScene):

    # The code for generating our scene goes here
    def construct(self):
        # Make the neural network
        nn = NeuralNetwork([
                FeedForwardLayer(10,rectangle_stroke_width=0),
                FeedForwardLayer(8,rectangle_stroke_width=0),
                FeedForwardLayer(5,rectangle_stroke_width=0),
                EmbeddingLayer()
            ],
            layer_spacing=0.5,
        )
        # Center the neural network
        nn.move_to(ORIGIN).scale(2)
        self.add(nn)
        # Make a forward pass animation
        forward_pass = nn.make_forward_pass_animation(run_time=5)
        # Play animation
        self.play(forward_pass)