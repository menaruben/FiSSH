from PyQt5.QtWidgets import *
import SSHUsage
import qdarkstyle

class Boxes:
    def __init__(self):
        pass

    def MessageBox(message: str, windowtitle: str):
        msgBox = QMessageBox()
        msgBox.setText(message)
        msgBox.setWindowTitle(windowtitle)
        msgBox.exec_()

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
        self.connectButton.clicked.connect(SSHWindow.ConnectSSH)
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
        output = host.ExecCommand(command)

        # Create a message box to display the output
        Boxes.MessageBox(str(output), "Output")

        # print output to terminal
        print(output)

        # return output
        # OutputWindow(stdout)

class StartupWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Startup Window')

        # Create a layout for the window
        self.layout = QVBoxLayout()

        # Buttons to open new windows..
        self.sshButton = QPushButton('Connect to Host')
        self.sshButton.clicked.connect(self.OpenSSHWindow)
        self.layout.addWidget(self.sshButton)

        # Set the layout for the window
        self.setLayout(self.layout)

    def OpenSSHWindow(self):
        self.sshWindow = SSHWindow()
        self.sshWindow.show()

if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    startupWindow = StartupWindow()
    startupWindow.show()
    app.exec_()


