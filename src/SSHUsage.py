import paramiko
from subprocess import call
from platform import system
from time import sleep
import SSHTerminal

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

                    # it is recommended (if it is a unix host) to remove the execute flag
                    # on the /etc/update-motd.d/* to remove the welcome message when login
                    # in with ssh (for a clean output message). this command takes care of it: 
                    # sudo chmod -x /etc/update-motd.d/*

                    return str(output)
                    # return str(stdout.read().decode('utf-8')), str(stderr.read().decode('utf-8'))

                else:
                    print("Error establishing SSH connection.")

                    ssh.close()
                    return str(output)

            # if no command is given then a terminal should pop up, opening the ssh connection

        except Exception as e:
            return f"ERROR: {str(e)}"
