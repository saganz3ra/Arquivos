def copiarArquivo(origem, destino):
    try:
        with open(origem, 'r') as arquivoOrigem, open(destino, 'w') as arquivoDestino:
            for linha in arquivoOrigem:
                if not linha.strip().startswith('//'):
                    arquivoDestino.write(linha)
        print(f"Conteúdo de {origem} copiado para {destino} (excluindo linhas comentadas).")
    except FileNotFoundError:
        print(f"Arquivo {origem} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

arquivoOrigem = 'arquivo_origem.txt'
arquivoDestino = 'arquivo_destino.txt'
copiarArquivo(arquivoOrigem, arquivoDestino)