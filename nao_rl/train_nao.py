import gymnasium as gym
from stable_baselines3 import PPO
from nao_gym_env import NaoCoppeliaEnv

# Initialize environment
env = NaoCoppeliaEnv()

# Train using PPO with logging enabled
model = PPO("MlpPolicy", env, verbose=2)  # Set verbose=2 for detailed logs
model.learn(total_timesteps=100000)

# Save the trained model
model.save("nao_ppo_model")
env.close()
