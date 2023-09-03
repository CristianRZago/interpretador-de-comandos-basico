import os

class ComandoInterpreter:
    def __init__(self):
        self.comandos_validos = ["dir", "cd", "mkdir", "rmdir", "echo"]
        self.buffer_de_comandos = []

    def executar_comando(self, comando):
        if comando not in self.comandos_validos:
            return "Comando inválido. Digite 'ajuda' para ver a lista de comandos válidos."
        
        self.buffer_de_comandos.append(comando)  # Adiciona o comando ao buffer
        
        if comando == "dir":
            return os.listdir()  # Lista arquivos e diretórios do diretório atual
        elif comando == "cd":
            novo_diretorio = input("Digite o novo diretório: ")
            try:
                os.chdir(novo_diretorio)  # Altera o diretório atual
                return f"Diretório alterado para {novo_diretorio}"
            except FileNotFoundError:
                return f"Diretório não encontrado: {novo_diretorio}"
        elif comando == "mkdir":
            novo_diretorio = input("Digite o nome do novo diretório: ")
            os.mkdir(novo_diretorio)  # Cria um novo diretório
            return f"Diretório '{novo_diretorio}' criado com sucesso."
        elif comando == "rmdir":
            diretorio_a_remover = input("Digite o diretório a ser removido: ")
            try:
                os.rmdir(diretorio_a_remover)  # Remove um diretório vazio
                return f"Diretório '{diretorio_a_remover}' removido com sucesso."
            except OSError:
                return f"Não foi possível remover o diretório '{diretorio_a_remover}'."
        elif comando == "echo":
            mensagem = input("Digite a mensagem a ser exibida: ")
            return mensagem

    def listar_comandos(self):
        return self.buffer_de_comandos

    def ajuda(self):
        return "Comandos disponíveis: " + ", ".join(self.comandos_validos)

# Exemplo de uso
interpreter = ComandoInterpreter()

while True:
    comando = input("Digite um comando: ").strip()
    
    if comando == "sair":
        break
    
    if comando == "ajuda":
        print(interpreter.ajuda())
    elif comando == "buffer":
        print("Buffer de comandos:")
        for cmd in interpreter.listar_comandos():
            print(cmd)
    else:
        resultado = interpreter.executar_comando(comando)
        print(resultado)
