import json # Lidar com arquivo JSON
from pathlib import Path # Lidar com caminhos do WIN

class BancoFake:

    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar() 

    def _carregar(self):
        """
        Carrega dados do arquivo JSON, se existir.
        caso não exista, inicia com dados vazios
        """           
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            # abrindo arquivo no modo leitura em UTF-8 (PT-BR)
            with open(caminho, 'r', encoding="utf-8") as data:
                # salvando dados que ja existem no arquivo
                # na variavel dados
                self.dados = json.load(data)
        else:
            self._salvar()
    def _salvar(self):
        """
        Salvar o conteudo de self.dados no arquivo JSON
        """    
        # Abrindo arquivo no modo W (escrita)        
        with open(self.arquivo_db, 'w', encoding="utf-8") as data:
            # Realizando DUMP (Python para JSON) para salvar no banco
            json.dump(self.dados, data, ensure_ascii=False, indent=4)

    def adicionar_cliente(self, cliente_dict):
        self.dados["clientes"].append(cliente_dict)
        self._salvar()

    def listar_clientes(self):
        return self.dados["clientes"]                