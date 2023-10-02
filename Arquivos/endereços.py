import re

def validar_endereco_ip(ip):

    ip_regex = r'^([1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$'
    if re.match(ip_regex, ip):
        return True
    else:
        return False

def separar_enderecos_ip(arquivo_entrada, arquivo_validos, arquivo_invalidos):
    try:
        with open(arquivo_entrada, 'r') as file_entrada, open(arquivo_validos, 'w') as file_validos, open(arquivo_invalidos, 'w') as file_invalidos:
            for linha in file_entrada:
                endereco_ip = linha.strip()
                if validar_endereco_ip(endereco_ip):
                    file_validos.write(endereco_ip + '\n')
                else:
                    file_invalidos.write(endereco_ip + '\n')
        print(f"Endereços IP separados em {arquivo_validos} e {arquivo_invalidos}.")
    except FileNotFoundError:
        print("Um dos arquivos não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

arquivo_entrada = 'enderecos_ip.txt'
arquivo_validos = 'enderecos_validos.txt'
arquivo_invalidos = 'enderecos_invalidos.txt'
separar_enderecos_ip(arquivo_entrada, arquivo_validos, arquivo_invalidos)