from stable_baselines3.common.base_class import BaseAlgorithm

class Agente:

    def __init__(self,model: BaseAlgorithm, nome: str):
        self.model = model
        self.nome = nome

    def treinar(self, total_timesteps: int):
        print("="*70)
        print("Treinando o agente ", self.nome, "...\n\n")
        print("="*70)
        self.model.learn(total_timesteps=total_timesteps)

    def salvar(self):
        print("="*70)
        print("Salvando o agente...")
        print("="*70)
        self.model.save("agentes/" + self.nome)

    def carregar(self, nome: str):
        print("="*70)
        print("Carregando o agente...")
        print("="*70)
        self.model = self.model.load(nome)

    

    def testar(self, total_timesteps: int, env):
        print("="*70)
        print("Testando o agente ", self.nome, "...\n\n")
        print("="*70)
        obs = env.reset()

        results = []
        count = 0
        resultados = []

        while True:

            if count >= total_timesteps:
                break

            action, _ = self.model.predict(obs)
            obs, rewards, dones, _ = env.step(action)
            results.append(rewards[0])
            if dones[0]:
                print("Episodio ", count, " Finalizado!")
                if sum(results) > 200:
                    print("> Episodio bem sucedido!")
                else:
                    print("> Episodio mal sucedido!")
                print("> Score: ", sum(results))
                print("="*70)
                resultados.append({"id": count, "score": sum(results), "status": "sucesso" if sum(results) > 200 else "fracasso"})
                results = []
                count += 1
                obs = env.reset()
            env.render()

        env.close()

        print("="*70)
        print("\tResultados: ")
        print("="*70)

        # Resultados
        for i in resultados:
            print("Episodio ", i["id"], ": Score: ", i["score"], " - ", i["status"])
        print("="*70)

        print("\n\n")
        print("="*70)
        print("\tEstatisticas: ")
        print("="*70)


        # Porcentagens
        sucesso = len([i for i in resultados if i["status"] == "sucesso"])
        fracasso = len([i for i in resultados if i["status"] == "fracasso"])
        print("> Total de episodios: ", sucesso + fracasso)
        print("> % de sucesso: ", (sucesso / (sucesso + fracasso)) * 100, "%")
        print("> % de fracasso: ", (fracasso / (sucesso + fracasso)) * 100, "%")
        

        # Media de score
        media = sum([i["score"] for i in resultados]) / len(resultados)
        print("> Media score: ", media)
        print("="*70)
        print("\n\n")

