import paramiko
from subprocess import run

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


class Host():
    def __init__(self, IP: str, Username: str, Password: str):
        self.IP = IP
        self.Username = Username
        self.Password = Password

    def ExecCommand(self, Command: str):
        if Command != '':
            client.connect(hostname=self.IP, username=self.Username, password=self.Password)
            stdin, stdout, stderr = client.exec_command('bash')
            stdin, stdout, stderr = client.exec_command(Command)
            
            return stdout.read().decode()
            client.close()
        
        else:
            # ! sshpass needs to be installed on the system! 
            # brew install hudochenkov/sshpass/sshpass

            ssh_command = f'sshpass -p {self.Password} ssh {self.Username}@{self.IP}'
            run(['open', '-a', 'Terminal', '-W', ssh_command])

    def SaveHost(self):
        pass