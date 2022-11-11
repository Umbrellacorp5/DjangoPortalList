from time import sleep
import paramiko
# Inicia un cliente SSH
dirip = '192.168.70.14' 
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

comando1 = input('ingrese el comando')
#for i in "ROBOTICA":

   # texto= "mkdir "+ i+ ".txt"
   # print(texto)

stdin, stdout, stderr = ssh.exec_command(comando1)
output = stdout.readlines()
print(' '.join(map(str, output)))