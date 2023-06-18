from stable_baselines3 import A2C,DQN
from stable_baselines3.common.env_util import make_vec_env

from Agente import Agente
from GridSearch import GridSearchRL






AMBIENTE = "LunarLander-v2"
SEED = 42
GAMMA = 0.99
ENT_COEF = 0.001
LEARNING_RATE = 5e-4
BUFFERSIZE = int(1e5)
TIMESTEPS = 100000
UPDATE_EVERY = 4
BATCH_SIZE = 64
EPISODIOS = 20
TAU = 1e-3
USEGRIDSEARCH = False


# Criando os ambientes
ambiente_treino = make_vec_env(AMBIENTE, n_envs=8)
ambiente_treino.seed(SEED)
ambiente_teste = make_vec_env(AMBIENTE, n_envs=1)
ambiente_teste.seed(SEED)



# Usando Grid Search para encontrar os melhores hiperparâmetros

if USEGRIDSEARCH:

    algoritmos = [DQN]

    hparams = {
        "gamma": [0.95, 0.99],
        #"ent_coef": [0.001, 0.1],
        "learning_rate": [0.0001, 0.001, 0.01]
    }


    for algoritmo in algoritmos:
        grid_search = GridSearchRL(hparams, ambiente_treino, algoritmo, TIMESTEPS, SEED)
        melhores_parametros = grid_search.run()



# Instanciando os agentes
if USEGRIDSEARCH:
    agentes = []
    for algoritmo in algoritmos:
        agentes.append(Agente(algoritmo("MlpPolicy", ambiente_treino, gamma=melhores_parametros["gamma"], ent_coef=melhores_parametros["ent_coef"], verbose=1, learning_rate=melhores_parametros["learning_rate"], seed=SEED), algoritmo.__name__))

else:
    agentes = (
        Agente(DQN("MlpPolicy", ambiente_treino, gamma=GAMMA,  verbose=1, learning_rate=LEARNING_RATE, seed=SEED, buffer_size=BUFFERSIZE, batch_size=BATCH_SIZE, target_update_interval=TAU), "DQN"),
        #Agente(A2C("MlpPolicy", ambiente_treino, gamma=GAMMA, ent_coef=ENT_COEF, verbose=1, learning_rate=LEARNING_RATE, seed=SEED), "A2C")
    )
# Treinando os agentes
for agente in agentes:
    agente.treinar(TIMESTEPS)

# Testando os agentes
for agente in agentes:
    agente.testar(EPISODIOS , ambiente_teste)

# Salvando os agentes
for agente in agentes:
    agente.salvar()