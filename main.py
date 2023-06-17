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
count = 0
resultados = []

while True:
    if count >= 20:
        break

    action, _states = agent.predict(obs)
    # print("Action: ", action)
    obs, rewards, dones, info = test_env.step(action)
    # print("Reward: ", rewards[0])
    # print("Done: ", dones)
    results.append(rewards[0])
    # sleep(0.5)
    # results.append({"obs": obs, "rewards": rewards, "dones": dones, "info": info})
    if dones[0]:
        print("Episodio Finalizado!")
        print("Recompensas: ", results)
        print("Score: ", sum(results))
        if sum(results) > 200:
            print("Episodio bem sucedido!")
        else:
            print("Episodio mal sucedido!")
        resultados.append({ "id": count, "score": sum(results), "status": "sucesso" if sum(results) > 200 else "fracasso"})
        results = []
        count += 1
        obs = test_env.reset()
    test_env.render()

test_env.close()

# Resultados

for i in resultados:
    print(i)
    print("\n")

# porcentagem de sucesso

sucessos = 0
fracassos = 0

for i in resultados:
    if i["status"] == "sucesso":
        sucessos += 1
    else:
        fracassos += 1

print("Porcentagem de sucesso: ", (sucessos / (sucessos + fracassos)) * 100, "%")

# media de score

soma = 0
for i in resultados:
    soma += i["score"]

print("Media de score: ", soma / len(resultados))



