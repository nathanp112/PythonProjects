import paramiko
from datetime import datetime


class SSHClientHandler:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.__username = username
        self.__password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.hostname, port=self.port, username=self.__username, password=self.__password)
        self.shell = None
        print("SSH connection established.")

    def invoke_shell(self):
        if self.client:
            self.shell = self.client.invoke_shell()
            print("Invoked shell")
        else:
            raise ConnectionError("SSH connection not established.")

    def send_shell_command(self, command):
        if self.shell:
            self.shell.send(command + "\n")
            while True:
                if self.shell.recv_ready():
                    output = self.shell.recv(1024).decode("utf-8")
                    break
            print(f"Shell command output:\n {output}")
            self.__save_output(command, output)
        else:
            raise AttributeError("Shell is not invoked")

    def exec_command(self, command):
        if self.client:
            stdin, stdout, stderr = self.client.exec_command(command)
            output = stdout.read().decode('utf-8')
            print(f"Exec command output: \n {output}")
            self.__save_output(command, output)
        else:
            raise ConnectionError("SSH connection is not established")

    @staticmethod
    def __save_output(command, output):

        timestamp = datetime.now().strftime("%d_%B_%Y-%H%M")
        filename = f"{command}_{timestamp}.txt"

        with open(filename, 'w') as f:
            f.write(output)
        print(f"Saved output to {filename}")

    def __del__(self):
        if self.client:
            self.client.close()
        print("SSH connection is closed")
