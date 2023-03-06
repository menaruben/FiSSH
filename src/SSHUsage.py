import paramiko
from subprocess import run, Popen, PIPE, call
from sys import platform
from time import sleep

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


class Host:
    def __init__(self, ip: str, username: str, password: str, port: int = 22):
        self.IP = ip
        self.Username = username
        self.Password = password
        self.Port = port
        self.PROMPT = ">"

    def ExecCommand(self, command: str) -> str:
        try:
            if command != '':
                try:
                    ssh.connect(hostname=self.IP, username=self.Username, password=self.Password, port=self.Port)
                    channel = ssh.invoke_shell()
                    channel.send(command + "\n")
                    sleep(1)
                    output = channel.recv(65535).decode("utf-8")

                except Exception as e:
                    return f"ERROR: {str(e)}"


                if ssh.get_transport().is_active():
                    print("SSH connection established successfully!")

                    ssh.close()
                    return str(output)
                    # return str(stdout.read().decode('utf-8')), str(stderr.read().decode('utf-8'))

                else:
                    print("Error establishing SSH connection.")

                    ssh.close()
                    return str(output)
                    # return str(stderr.read().decode('utf-8'))


                # if stderr != '':
                #     client.close()
                #     return str(stderr.read().decode())
                # else:
                #     client.close()
                #     return str(stdout.read().decode())

            # if no command is given then a terminal should pop up, opening the ssh connection
            else:
                # ! sshpass needs to be installed on the system!
                # brew install hudochenkov/sshpass/sshpass
                # pacman -S sshpass
                ssh_command = f'ssh {self.Username}@{self.IP}\n'
                call(ssh_command, shell=True)

        except Exception as e:
            return f"ERROR: {str(e)}"

            # if sys.platform == "win32":
            #     ssh_command = f'ssh {self.Username}@{self.IP}\n'
            #     proc = Popen('cmd.exe', stdin=PIPE, stdout=PIPE)

            #     proc.stdin.write(bytes(ssh_command, 'utf-8'))
            #     # proc.stdin.write(bytes('yes\n', 'utf-8'))
            #     proc.stdin.write(bytes(f'{self.Password}\n', 'utf-8'))

            # else:
            #     ssh_command = f'sshpass -p {self.Password} ssh {self.Username}@{self.IP}'
            #     run(['konsole', '--hold', '-e', 'bash -c f"{ssh_command}; exec bash"'])
