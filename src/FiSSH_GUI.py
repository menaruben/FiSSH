from PyQt5.QtWidgets import *
import SSHUsage
import qdarkstyle
# import SSHTerminal
from sys import exit, argv, platform
from subprocess import call

class Boxes:
    def __init__(self):
        pass

    def MessageBox(message: str, windowtitle: str):
        msgBox = QMessageBox()
        msgBox.setText(message)
        msgBox.setWindowTitle(windowtitle)
        msgBox.exec_()

class Terminal(QMainWindow):
    def __init__(self, ip: str, port: int, username: str, password: str):
        super().__init__()
        self.IP = ip
        self.Port = port
        self.Username = username
        self.Password = password
        self.SSHhost = SSHUsage.Host(self.IP, self.Username, self.Password, self.Port)

        self.setWindowTitle("FiSSH - Slow SSHTerminal")
        self.setGeometry(100, 100, 800, 600)

        # Create the text area to display the terminal output
        self.textarea = QTextEdit()
        self.textarea.setReadOnly(True)

        # Create the input field for the user to type in commands
        self.inputfield = QLineEdit()
        self.inputfield.returnPressed.connect(self.execute_command)

        # Add the text area and input field to a vertical box layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.textarea)
        vbox.addWidget(self.inputfield)

        # Create a central widget and set the layout to the vertical box layout
        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

    def execute_command(self):
        # Get the user's input from the input field
        user_input = self.inputfield.text()

        # Echo the input to the terminal output
        stdout = self.SSHhost.ExecCommand(user_input)
        self.textarea.append(stdout)

        # Clear the input field
        self.inputfield.clear()

    @staticmethod
    def OpenSSHTerminal():
        window = QApplication.activeWindow()
        ip = window.input_box_1.text()
        username = window.input_box_2.text()
        passwd = window.input_box_3.text()
        port = int(window.input_box_5.text())

        if platform == "win32":
            terminal = Terminal(ip, port, username, passwd)
            terminal.show()

        # elif platform == "linux2":
        #     host = SSHUsage.Host(ip, username, passwd, port)
        #     host.openTerminal()

class SSHWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('FiSSH - SSH Client')

        # Create input boxes
        self.input_box_1 = QLineEdit()                      # IP Address
        self.input_box_2 = QLineEdit()                      # Username
        self.input_box_3 = QLineEdit()                      # Password
        self.input_box_3.setEchoMode(QLineEdit.Password)    # hides password with "*"
        self.input_box_4 = QLineEdit()                      # Command to execute
        self.input_box_5 = QLineEdit()                      # Port (standard is 22)

        # Add the input boxes to a layout
        self.layout = QVBoxLayout()                         # Vertical Layout

        self.layout.addWidget(QLabel('IP Address:'))
        self.layout.addWidget(self.input_box_1)

        self.layout.addWidget(QLabel('Username:'))
        self.layout.addWidget(self.input_box_2)

        self.layout.addWidget(QLabel('Password:'))
        self.layout.addWidget(self.input_box_3)

        self.layout.addWidget(QLabel('Command to execute:'))
        self.layout.addWidget(self.input_box_4)

        self.layout.addWidget(QLabel('Port:'))
        self.layout.addWidget(self.input_box_5)

        # Add a button to retrieve the contents of the input boxes
        self.connectButton = QPushButton('Connect!')
        if self.input_box_4.text() != "":
            self.connectButton.clicked.connect(SSHWindow.ConnectSSH)
        else:
            self.connectButton.clicked.connect(Terminal.OpenSSHTerminal)

        self.layout.addWidget(self.connectButton)

        # Set the layout for the window
        self.setLayout(self.layout)

    # Define a function to retrieve the contents of the input boxes
    @staticmethod
    def ConnectSSH():
        window = QApplication.activeWindow()
        ip = window.input_box_1.text()
        username = window.input_box_2.text()
        passwd = window.input_box_3.text()
        command = window.input_box_4.text()
        port = int(window.input_box_5.text())

        host = SSHUsage.Host(ip, username, passwd, port)

        # Create a message box to display the output
        output = host.ExecCommand(command)
        Boxes.MessageBox(str(output), "Output")

        # print output to terminal
        print(output)

        # return output
        # OutputWindow(stdout)

def main():
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    window = SSHWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
