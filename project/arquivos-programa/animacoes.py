def carregamento(barra_progresso, janela):
    progresso = 0
    while progresso < 100:
        progresso += 1
        barra_progresso["value"] = progresso
        janela.update_idletasks()
        janela.after(2)