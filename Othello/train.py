import os
os.environ["KERAS_BACKEND"] = "tensorflow"
from othello import OthelloEnv
import tensorflow as tf
import numpy as np
import pandas as pd
import keras
from keras import layers
import pandas as pd
import seaborn as sns
import random
import math


# class Environment:
#     def __init__(self):
#         self.game = OthelloEnv()


# class Agent():
#     def __init__(self):
#         self.memory_cap  = 100000
#         self.batch_size = 32
#         self.gamma = 0.8
#         self.max_eps = 1
#         self.min_eps = 0.001
#         self.learning_rate = 0.00025
#         self.epsilon = 1
#         self.steps = 0


#     def network(self, weights=None):
#         pass

gamma = 0.99
epsilon = 1.0
epsilon_min = 0.1
epsilon_max = 1.0
epsilon_interval = (epsilon_max-epsilon_min)
batch_size = 32
max_steps_per_episode = 1000
max_episodes = 2

# class InputMaskingLayer(layers.Layer):
#     def __init__(self,units=32):
#         super().__init__()
#         self.units = units
    
#     def build(self,input_shape):
#         self.kernel = self.add_weight(
#             shape=(input_shape[-1],self.units),
#             initializer=
#         )

env = OthelloEnv()
num_actions = 64
def create_q_model():
    return keras.Sequential(
        [
            layers.Lambda(
                lambda tensor: keras.ops.transpose(tensor, [0, 2, 3, 1]),
                output_shape = (8,8),
                input_shape = (8,8)
            ),
            layers.Dense(128,activation="relu"),
            layers.Dense(256,activation="relu"),
            layers.Dense(128,activation="relu"),
            layers.Dense(num_actions,activation="linear")
        ]
    )

model = create_q_model()
model_target = create_q_model()

optimizer = keras.optimizers.Adam(learning_rate=0.00025,clipnorm=1.0)
action_history = []
state_history = []
state_next_history = []
rewards_history = []
done_history = []
episode_reward_history = []
running_reward = 0
episode_count = 0

update_after_actions = 4
# How often to update the target network
update_target_network = 10000
# Using huber loss for stability
loss_function = keras.losses.Huber()