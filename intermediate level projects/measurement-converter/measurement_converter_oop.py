import math

from PyQt5 import QtWidgets, QtGui

class MeasurementConverter:
    # Initialize the converter with a list of supported conversions
    def __init__(self):
        self.conversions = {
            'length': {
                'mm': {'m': 0.001},
                'cm': {'m': 0.01},
                'm': {'mm': 1000, 'cm': 100},
                'in': {'m': 0.0254},
                'ft': {'m': 0.3048},
                'yd': {'m': 0.9144}
            },
            'mass': {
                'mg': {'kg': 0.000001},
                'g': {'kg': 0.001},
                'kg': {'mg': 1000000, 'g': 1000},
                'oz': {'kg': 0.0283495},
                'lb': {'kg': 0.453592}
            },
            'angle': {
                'rad': {'deg': 180/math.pi},
                'deg': {'rad': math.pi/180}
            }
        }
    
    # Convert a value from one unit to another
    def convert(self, value, from_unit, to_unit):
        try:
            # Check if the conversion is supported
            conversion_factor = self.conversions[from_unit][to_unit]
        except KeyError:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
        # Check if the value is a valid number
        try:
            value = float(value)
        except ValueError:
            raise ValueError(f"Invalid value: {value}")
        
        # Convert the value and return it
        return value * conversion_factor
    
    # Add more functions for specific conversions here
    
    
    # Create the GUI
    def create_gui(self):
        # Create the main window
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle("Measurement Converter")
        self.window.setGeometry(100, 100, 500, 500)
        
        # Create the main widget and set it as the central widget
        self.main_widget = QtWidgets.QWidget()
        self.window.setCentralWidget(self.main_widget)
        
        # Create the layout for the main widget
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        
        # Create the input widgets
        self.value_label = QtWidgets.QLabel("Enter the value to convert:")
        self.value_input = QtWidgets.QLineEdit()
        self.from_unit_label = QtWidgets.QLabel("Enter the unit to convert from:")
        self.from_unit_input = QtWidgets.QLineEdit()
        self.to_unit_label = QtWidgets.QLabel("Enter the unit to convert to:")
        self.to_unit_input = QtWidgets.QLineEdit()
        
  
        # Create the convert button and connect it to the convert method
        self.convert_button = QtWidgets.QPushButton("Convert")
        self.convert_button.clicked.connect(self.on_convert_button_clicked)

        # Create the result label and set it as read-only
        self.result_input = QtWidgets.QLineEdit()
        self.result_input.setReadOnly(True)

        # Add the input widgets and the convert button to the layout
        self.main_layout.addWidget(self.value_label)
        self.main_layout.addWidget(self.value_input)
        self.main_layout.addWidget(self.from_unit_label)
        self.main_layout.addWidget(self.from_unit_input)
        self.main_layout.addWidget(self.to_unit_label)
        self.main_layout.addWidget(self.to_unit_input)
        self.main_layout.addWidget(self.convert_button)
        self.main_layout.addWidget(self.result_input)

        # Show the main window
        self.window.show()

    # Handle errors during the conversion process
    def handle_error(self, error):
        QtWidgets.QMessageBox.critical(self.window, "Error", str(error))
    
    # Create the on_convert_button_clicked function
    def on_convert_button_clicked(self):
        # Get the input values
        value = self.value_input.text()
        from_unit = self.from_unit_input.text()
        to_unit = self.to_unit_input.text()
        
        try:
            # Convert the value and display the result
            result = self.convert(value, from_unit, to_unit)
            self.result_input.setText(str(result))
        except ValueError as error:
            # Handle errors during the conversion process
            self.handle_error(error)

# Create the QApplication instance
app = QtWidgets.QApplication([])

# Create the converter instance and the GUI
converter = MeasurementConverter()
converter.create_gui()

# Run the application
app.exec_()