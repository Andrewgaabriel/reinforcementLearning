import tkinter as tk

class RLConfigApp:
    def __init__(self, callback):
        self.callback = callback
        self.window = tk.Tk()
        self.window.title("Configuração")
        
        # Labels, Entries, Checkbutton, Button...
        # Labels
        tk.Label(self.window, text="Gamma:").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self.window, text="Ent Coef:").grid(row=3, column=0, sticky=tk.W)
        tk.Label(self.window, text="Learning Rate:").grid(row=4, column=0, sticky=tk.W)
        tk.Label(self.window, text="Timesteps:").grid(row=5, column=0, sticky=tk.W)
        tk.Label(self.window, text="Episódios:").grid(row=6, column=0, sticky=tk.W)
        
        # Entries
        
        self.gamma_entry = tk.Entry(self.window)
        self.gamma_entry.grid(row=2, column=1)
        
        self.ent_coef_entry = tk.Entry(self.window)
        self.ent_coef_entry.grid(row=3, column=1)
        
        self.learning_rate_entry = tk.Entry(self.window)
        self.learning_rate_entry.grid(row=4, column=1)
        
        self.timesteps_entry = tk.Entry(self.window)
        self.timesteps_entry.grid(row=5, column=1)
        
        self.episodios_entry = tk.Entry(self.window)
        self.episodios_entry.grid(row=6, column=1)
        
        # Checkbutton
        self.use_grid_search_var = tk.BooleanVar()
        self.use_grid_search_checkbutton = tk.Checkbutton(self.window, text="Usar Grid Search",
                                                          variable=self.use_grid_search_var,
                                                          command=self.atualizar_campos)
        self.use_grid_search_checkbutton.grid(row=7, column=0, columnspan=2, sticky="w")
        
        # Button
        self.run_button = tk.Button(self.window, text="Executar", command=self.run_rl)
        self.run_button.grid(row=8, columnspan=2)


        self.atualizar_campos()

    def atualizar_campos(self):
        if self.use_grid_search_var.get():
            # Desabilitar os campos de parâmetros
            self.gamma_entry.config(state='disabled')
            self.ent_coef_entry.config(state='disabled')
            self.learning_rate_entry.config(state='disabled')
        else:
            # Habilitar os campos de parâmetros
            self.gamma_entry.config(state='normal')
            self.ent_coef_entry.config(state='normal')
            self.learning_rate_entry.config(state='normal')

    def run_rl(self):
        gamma = float(self.gamma_entry.get())
        ent_coef = float(self.ent_coef_entry.get())
        learning_rate = float(self.learning_rate_entry.get())
        timesteps = int(self.timesteps_entry.get())
        episodios = int(self.episodios_entry.get())
        use_grid_search = self.use_grid_search_var.get()
        
        # Chama a função de retorno (callback) passando os parâmetros configurados
        self.callback(gamma, ent_coef, learning_rate, timesteps, episodios, use_grid_search)
        
    def start(self):
        self.window.mainloop()
