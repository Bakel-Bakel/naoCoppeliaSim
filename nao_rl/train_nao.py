import gymnasium as gym
from stable_baselines3 import PPO
from nao_gym_env import NaoCoppeliaEnv

# Initialize environment
env = NaoCoppeliaEnv()

# Train using PPO with logging enabled
model = PPO("MlpPolicy", env, verbose=2)

try:
    print("🚀 Training Started. Press Ctrl+C to stop safely...")
    model.learn(total_timesteps=100000)
except KeyboardInterrupt:
    print("\n🛑 Training interrupted by user. Saving model...")
    model.save("nao_ppo_model")
    env.close()
    print("✅ Model saved and environment closed properly.")
    exit(0)

# Save the trained model after training finishes
model.save("nao_ppo_model")
env.close()
