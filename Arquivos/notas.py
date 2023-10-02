def calcularMedia(notas):
    notas = [float(nota) for nota in notas.split()]
    return sum(notas) / len(notas)

def gerar(arquivoAlunos, arquivoNotas, arquivoSaida):
    try:
        with open(arquivoAlunos, 'r') as file_alunos, open(arquivoNotas, 'r') as file_notas, open(arquivoSaida, 'w') as file_saida:
            for nome, notas_str in zip(file_alunos, file_notas):
                nome = nome.strip()
                notas = notas_str.strip()
                media = calcularMedia(notas)
                file_saida.write(f"{nome}: {media:.2f}\n")
        print(f"Relatório gerado com sucesso em {arquivoSaida}.")
    except FileNotFoundError:
        print("Um dos arquivos não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

arquivoAlunos = 'alunos.txt'
arquivoNotas = 'notas.txt'
arquivoSaida = 'relatorio.txt'
gerar(arquivoAlunos, arquivoNotas, arquivoSaida)