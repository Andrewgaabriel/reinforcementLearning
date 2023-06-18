from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env

from Agente import Agente
from GridSearch import GridSearchRL
from RLConfigApp import RLConfigApp

def rl_callback(gamma, ent_coef, learning_rate, timesteps, episodios, use_grid_search):

    print("Parâmetros configurados:")
    print("Gamma:", gamma)
    print("Ent Coef:", ent_coef)
    print("Learning Rate:", learning_rate)
    print("Timesteps:", timesteps)
    print("Episódios:", episodios)
    print("Usar Grid Search:", use_grid_search)


    ambiente = "LunarLander-v2"
    seed = 42
    # GAMMA = 0.95
    # ENT_COEF = 0.001
    # LEARNING_RATE = 0.001
    # TIMESTEPS = 100
    # EPISODIOS = 20
    # USEGRIDSEARCH = True


    # Criando os ambientes
    ambiente_treino = make_vec_env(ambiente, n_envs=8)
    ambiente_treino.seed(seed)
    ambiente_teste = make_vec_env(ambiente, n_envs=1)
    ambiente_teste.seed(seed)



    # Usando Grid Search para encontrar os melhores hiperparâmetros

    if use_grid_search:

        algoritmos = [A2C]

        hparams = {
            "gamma": [0.95, 0.99],
            "ent_coef": [0.001, 0.1],
            "learning_rate": [0.0001, 0.001, 0.01]
        }


        for algoritmo in algoritmos:
            grid_search = GridSearchRL(hparams, ambiente_treino, algoritmo, timesteps, seed)
            melhores_parametros = grid_search.run()



    # Instanciando os agentes
    if use_grid_search:
        agentes = []
        for algoritmo in algoritmos:
            agentes.append(Agente(algoritmo("MlpPolicy", ambiente_treino, gamma=melhores_parametros["gamma"], ent_coef=melhores_parametros["ent_coef"], verbose=1, learning_rate=melhores_parametros["learning_rate"], seed=seed), algoritmo.__name__))

    else:
        agentes = (
            Agente(A2C("MlpPolicy", ambiente_treino, gamma=gamma, ent_coef=ent_coef, verbose=1, learning_rate=learning_rate, seed=seed), "A2C"),
        )
    # Treinando os agentes
    for agente in agentes:
        agente.treinar(timesteps)

    # Testando os agentes
    for agente in agentes:
        agente.testar(episodios , ambiente_teste)

    # Salvando os agentes
    for agente in agentes:
        agente.salvar()
    app.stop()

app = RLConfigApp(rl_callback)
app.start()