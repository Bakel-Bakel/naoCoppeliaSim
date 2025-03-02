import gymnasium as gym
from stable_baselines import PPO2
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.tf_layers import mlp
from nao_gym_env import NaoCoppeliaEnv
import tensorflow as tf

class CustomTFPolicy(MlpPolicy):
    def __init__(self, *args, **kwargs):
        super(CustomTFPolicy, self).__init__(*args, **kwargs,
            net_arch=[dict(pi=[128, 128], vf=[128, 128])])  # 2 Hidden Layers

env = NaoCoppeliaEnv()

# ✅ Use TensorFlow PPO with a custom network
model = PPO2(CustomTFPolicy, env, verbose=1)

model.learn(total_timesteps=100000)
model.save("nao_custom_tf_model")

