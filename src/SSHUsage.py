import paramiko
from subprocess import call

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


class Host:
    def __init__(self, ip: str, username: str, password: str):
        self.IP = ip
        self.Username = username
        self.Password = password

    def exec_command(self, command: str):
        if command != '':
            client.connect(hostname=self.IP, username=self.Username, password=self.Password)
            stdin, stdout, stderr = client.exec_command('bash')
            stdin, stdout, stderr = client.exec_command(command)

            if stderr != '':
                print(stderr)

            print(stdout)

            client.close()
            return stdout.read().decode()

        else:
            # ! sshpass needs to be installed on the system! 
            # brew install hudochenkov/sshpass/sshpass
            # pacman -S sshpass

            ssh_command = f'sshpass -p {self.Password} ssh {self.Username}@{self.IP}'
            call(['konsole', '--hold', '-e', 'bash -c "{}; exec bash"'.format(ssh_command)])
