import subprocess
import sys

class SubPro:
  def __init__(self, install=None, uninstall=None,id_service=None):
    if install==True and uninstall==None:
      pacote_arg=f'winget install --id {id_service} -e --source winget'
    elif uninstall==True and install==None:
      pacote_arg=f'winget install --id {id_service} -e'
    try:
      resultado=subprocess.run(pacote_arg,check=True,capture_output=True,text=True)
      print(f'Pacote instalado com sucesso\n {resultado.stdout}')
      return
    except subprocess.CalledProcessError as erro:
      print(f'ERRO AO TENTAR INSTALAR PACOTE -> {erro.returncode} \n{erro.stderr}')
      sys.exit(1)
    return

if __name__=='__main__':
  print("🚀 Iniciando instalação de pacote win_64 via winget...")
  SubPro('')