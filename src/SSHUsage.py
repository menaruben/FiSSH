import paramiko
from subprocess import run, Popen, PIPE, call
import sys
from sys import platform

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


class Host:
    def __init__(self, ip: str, username: str, password: str):
        self.IP = ip
        self.Username = username
        self.Password = password

    def ExecCommand(self, command: str):
        if command != '':
            client.connect(hostname=self.IP, username=self.Username, password=self.Password)
            # _, stdout, stderr = client.exec_command('bash')
            _, stdout, stderr = client.exec_command(command)

            if stderr != '':
                return stderr.read().decode()
            else:
                return stdout.read().decode()

        else:
            # ! sshpass needs to be installed on the system!
            # brew install hudochenkov/sshpass/sshpass
            # pacman -S sshpass
            ssh_command = f'ssh {self.Username}@{self.IP}\n'
            call(ssh_command, shell=True)


            # if sys.platform == "win32":
            #     ssh_command = f'ssh {self.Username}@{self.IP}\n'
            #     proc = Popen('cmd.exe', stdin=PIPE, stdout=PIPE)

            #     proc.stdin.write(bytes(ssh_command, 'utf-8'))
            #     # proc.stdin.write(bytes('yes\n', 'utf-8'))
            #     proc.stdin.write(bytes(f'{self.Password}\n', 'utf-8'))

            # else:
            #     ssh_command = f'sshpass -p {self.Password} ssh {self.Username}@{self.IP}'
            #     run(['konsole', '--hold', '-e', 'bash -c f"{ssh_command}; exec bash"'])
