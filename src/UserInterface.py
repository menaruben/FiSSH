from PyQt5.QtWidgets import *
import SSHUsage

class OutputWindow(QWidget):
    def __init__(self, output):
        super().__init__()
        self.setWindowTitle('Output Window')
        self.setGeometry(100, 100, 500, 500)
        layout = QVBoxLayout()
        label = QLabel(output)
        layout.addWidget(label)
        self.setLayout(layout)
        self.show()

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 500, 500)    
    window.setWindowTitle('FiSSH - SSH Client')

    # Create two input boxes
    input_box_1 = QLineEdit()
    input_box_2 = QLineEdit()
    input_box_3 = QLineEdit()
    input_box_3.setEchoMode(QLineEdit.Password)
    input_box_4 = QLineEdit()

    # Add the input boxes to a layout
    layout = QVBoxLayout()
    
    layout.addWidget(QLabel('IP Address:'))
    layout.addWidget(input_box_1)

    layout.addWidget(QLabel('Username:'))
    layout.addWidget(input_box_2)

    layout.addWidget(QLabel('Password:'))
    layout.addWidget(input_box_3) 

    layout.addWidget(QLabel('Command to execute:'))
    layout.addWidget(input_box_4)    

    # Set the layout for the window
    window.setLayout(layout)

    # Define a function to retrieve the contents of the input boxes
    def Connect():
        ip = input_box_1.text()
        username = input_box_2.text()
        passwd = input_box_3.text()
        command = input_box_4.text()
        # print(f'Input: {input_1}, {input_2}, {input_2}')

        Host = SSHUsage.Host(ip, username, passwd)
        stdout = Host.ExecCommand(command)
        print(stdout)
        # return stdout
        # OutputWindow(stdout)

    # Add a button to retrieve the contents of the input boxes
    ConnectButton = QPushButton('Connect!')
    ConnectButton.clicked.connect(Connect)
    layout.addWidget(ConnectButton)

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
