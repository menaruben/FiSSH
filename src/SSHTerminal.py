from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLineEdit
import SSHUsage

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

# if __name__ == "__main__":
#     # Create the application and the terminal window
#     app = QApplication(sys.argv)
#     terminal = Terminal(ip="127.0.0.1", port=2222, username="vagrant", password="vagrant")
#     terminal.show()

#     # Run the application loop
#     sys.exit(app.exec_())
