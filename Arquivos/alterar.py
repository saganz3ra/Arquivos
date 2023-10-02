def alterar_nota(aluno, notaAntiga, notaNova, arquivoAlunos, arquivoNotas):
    try:
        with open(arquivoAlunos, 'r') as fileAlunos, open(arquivoNotas, 'r') as fileNotas:
            nomes = fileAlunos.readlines()
            notas = fileNotas.readlines()

        encontrado = False
        for i in range(len(nomes)):
            if nomes[i].strip() == aluno:
                notasAluno = notas[i].split()
                if notaAntiga in notasAluno:
                    index_notaAntiga = notasAluno.index(notaAntiga)
                    notasAluno[index_notaAntiga] = notaNova
                    notas[i] = ' '.join(notasAluno) + '\n'
                    encontrado = True
                    break

        if encontrado:
            with open(arquivoNotas, 'w') as fileNotas:
                fileNotas.writelines(notas)
            print(f"Nota do aluno {aluno} alterada com sucesso.")
        else:
            print(f"Aluno {aluno} não encontrado ou nota antiga não encontrada.")
    except FileNotFoundError:
        print("Um dos arquivos não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

arquivoAlunos = 'alunos.txt'
arquivoNotas = 'notas.txt'
aluno = 'Aluno1'
notaAntiga = '8.5'
notaNova = '9.0'
alterar_nota(aluno, notaAntiga, notaNova, arquivoAlunos, arquivoNotas)