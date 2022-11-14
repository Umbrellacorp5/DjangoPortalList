from time import sleep
import paramiko
import sys
sys.path.append('c:\\Users\\Cristian\\Desktop\\djangoproject\\DjangoPortalList\\PortalList\\administracion')#Cambiar a puntitos, .. una carpeta atras . carpeta en la que estoy
print(sys.path)
from administracion.views import IA
print(sys.path)
# Inicia un cliente SSH
dirip = '192.168.1.7'
usssh = 'ubuntu'
clavessh = 'admin'
port= 22

ssh= paramiko.SSHClient()
# Establecer política por defecto para localizar la llave del host localmente
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Conectarse
ssh.connect(hostname=dirip,username=usssh, password=clavessh, port=port, look_for_keys=False, allow_agent=False)
#ssh_client.connect(dirip, 22, usssh, clavessh)
# Ejecutar un comando de forma remota capturando entrada, salida y error estándar
commands = ['ls', 'sudo -S -u postgres psql', '\c PortalList', 'SELECT * FROM administrador;']
comando1 = 'sudo -S -u postgres psql'
comando2 = '\c PortalList'
comando3 = 'SELECT * FROM administrador;'
comando4 = 'ls'

#for i in "ROBOTICA":

   # texto= "mkdir "+ i+ ".txt"
   # print(texto)
for command in commands:
   stdin, stdout, stderr = ssh.exec_command(command)
   sleep(1)
   output = stdout.readlines()
   error = stderr.readlines()
   print(' '.join(map(str, output)))
   print(' '.join(map(str, error)))

ssh.close()

