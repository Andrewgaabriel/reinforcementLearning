import gymnasium as gym
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env




# Criando o ambiente
env_id = "LunarLander-v2"
env = make_vec_env(env_id, n_envs=8)

GAMMA = 0.995
ENT_COEF = 0.001
LEARNING_RATE = 0.0007


# Instanciando os agentes
agent = A2C("MlpPolicy", env, gamma=GAMMA, ent_coef=ENT_COEF, verbose=1, learning_rate=LEARNING_RATE)


# Treinando o agente
agent.learn(total_timesteps=100000)


# Salvando o agente
agent.save("a2c_lunar")



# Carregando o agente
del agent
agent = A2C.load("a2c_lunar")


# Cria o ambiente de teste
test_env = make_vec_env(env_id, n_envs=1)

# Testa o agente
obs = test_env.reset()

results = []
try:
    while True:
        action, _states = agent.predict(obs)
        obs, rewards, dones, info = test_env.step(action)
        results.append({"obs": obs, "rewards": rewards, "dones": dones, "info": info})
        test_env.render()
except KeyboardInterrupt:
    test_env.close()
    print("Teste finalizado!")
    print("Resultados: ", results)
