import itertools
import numpy as np


class GridSearchRL:

    def __init__(self, parametros: dict, env, algoritmo, time_steps, seed):
        self.algoritmo = algoritmo
        self.parametros = parametros
        self.best_mean_reward = -np.inf
        self.best_hyperparams = {}
        self.env = env
        self.time_steps = time_steps
        self.seed = seed


    def _get_combinacoes(self):
        parametros_nomes = list(self.parametros.keys())
        parametros_valores = list(self.parametros.values())
        for combinacao in itertools.product(*parametros_valores):
            yield dict(zip(parametros_nomes, combinacao))


    def _avalia_agente(self, agente):
        total_recompensa = 0
        for _ in range(10):
            obs = self.env.reset()
            done = False
            while not done:
                action, _ = agente.predict(obs)
                obs, rewards, dones, _ = self.env.step(action)
                done = dones[0]
                total_recompensa += rewards[0]
        return total_recompensa / 10


    def run(self):
        print("\n\nIniciando Grid Search...")
        for combinacao in self._get_combinacoes():
            agente = self.algoritmo("MlpPolicy", self.env, **combinacao, seed=self.seed)
            agente.learn(total_timesteps=self.time_steps)
            mean_reward = 0

            mean_reward = self._avalia_agente(agente)

            if mean_reward > self.best_mean_reward:
                self.best_mean_reward = mean_reward
                self.best_hyperparams = combinacao
        print("="*70)
        print("> Melhores hiperparâmetros para", self.algoritmo.__name__, ":", self.best_hyperparams)
        print("> Melhor recompensa média:", self.best_mean_reward)
        with open(f"hiperparametros/melhores_hiperparametros_{self.algoritmo.__name__}.txt", "w") as f:
            f.write(str(self.best_hyperparams))
        print("="*70)

        return self.best_hyperparams