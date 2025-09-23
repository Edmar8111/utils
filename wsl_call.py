import subprocess
import sys

class SubPro:
  def __init__(self, install=None, uninstall=None,id_service=None):
    try:
      if install==True and uninstall==None:
        pacote_arg=f'wls --install'
      elif uninstall==True and install==None:
        pacote_arg=f'dism.exe /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux /norestart'
    except ValueError as e:
      return f'Erro value -> {e}'  
    try:
      resultado=subprocess.run(pacote_arg,check=True,capture_output=True,text=True)
      return f'Pacote instalado com sucesso\n {resultado.stdout}'
    except subprocess.CalledProcessError as erro:
      print(f'ERRO AO TENTAR INSTALAR PACOTE -> {erro.returncode} \n{erro.stderr}')
      sys.exit(1)
    return
  def remover_os(self, os_name):
    pacote_arg=f'wls --unregister {os_name}'
    try:
      resultado=subprocess.run(pacote_arg,check=True,capture_output=True,text=True)
      return f'Pacote removido com sucesso\n {resultado.stdout}'
    except subprocess.CalledProcessError as erro:
      print(f'ERRO AO TENTAR REMOVER OS -> {erro.returncode} \n{erro.stderr}')
      sys.exit(1)
    return

    

if __name__=='__main__':
  print("🚀 WSL process...")
  SubPro('arg')
  print('Sera necessario o reinicio da maquina!')