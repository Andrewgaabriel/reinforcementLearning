import re
from time import sleep
import gymnasium as gym
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env




# Criando o ambiente
env_id = "LunarLander-v2"
env_seed = 42
env = make_vec_env(env_id, n_envs=8)
env.seed(env_seed)

GAMMA = 0.995
ENT_COEF = 0.01
LEARNING_RATE = 0.007


# Instanciando os agentes
agent = A2C("MlpPolicy", env, gamma=GAMMA, ent_coef=ENT_COEF, verbose=1, learning_rate=LEARNING_RATE, seed=env_seed)


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
        # print("Action: ", action)
        obs, rewards, dones, info = test_env.step(action)
        # print("Reward: ", rewards[0])
        # print("Done: ", dones)
        results.append(rewards[0])
        # sleep(0.5)
        # results.append({"obs": obs, "rewards": rewards, "dones": dones, "info": info})
        if dones[0]:
            print("Episode finished!")
            print("Rewards: ", results)
            print("Total rewards: ", sum(results))
            if sum(results) > 200:
                print("Sucesso!")
            else:
                print("Falha!")
            results = []
            obs = test_env.reset()
        test_env.render()
except KeyboardInterrupt:
    test_env.close()
    print("Teste finalizado!")
    print("Resultados: ", results)

