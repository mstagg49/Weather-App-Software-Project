import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Weather Application")

        # Set vertical layout
        self.setLayout(qtw.QVBoxLayout()) # this is vertical box layout - use QHBoxLayout for horizontal)

        # Create a Label
        my_label = qtw.QLabel("This is the weather today!")
        # Chane font size of label
        my_label.setFont(qtg.QFont("Helvetica", 18))
        self.layout().addWidget(my_label) # necessary to add label to layout

        # Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field") # create a name to reference this later on
        my_entry.setText("")
        self.layout().addWidget(my_entry) # necessary to add label to layout

        # Create a button
        my_button = qtw.QPushButton("Press me!", clicked = lambda: press_it()) # links a function to button
        self.layout().addWidget(my_button)  # necessary to add label to layout

        # show the app (won't show otherwise!!)
        self.show()     # will show app when starting

        def press_it():
            # Add name to label
            my_label.setText(f"Hello {my_entry.text()} !")
            # Clear the entry box
            my_entry.setText("")


app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()


# NOTES
# - Labels don't resize that well but Buttons do a little better