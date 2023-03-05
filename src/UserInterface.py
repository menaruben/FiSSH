from PyQt5.QtWidgets import *
import SSHUsage


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
    def ConnectSSH():
        ip = input_box_1.text()
        username = input_box_2.text()
        passwd = input_box_3.text()
        command = input_box_4.text()
        # print(f'Input: {input_1}, {input_2}, {input_2}')

        host = SSHUsage.Host(ip, username, passwd)
        stdout = host.exec_command(command)
        print(stdout)
        # return stdout
        # OutputWindow(stdout)

    # Add a button to retrieve the contents of the input boxes
    connectButton = QPushButton('Connect!')
    connectButton.clicked.connect(ConnectSSH)
    layout.addWidget(connectButton)

    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
