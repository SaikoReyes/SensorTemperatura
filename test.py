import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QProgressBar, QLabel
from PyQt5.QtCore import QTimer, Qt

valores = 10
min_temp = 23
max_temp = 80
a = True

# Open the serial port
#ser = serial.Serial('/dev/cu.usbmodem1301', 9600)
#Uncomment when Arduino is connected

def update_progress_bar():
    global valores
    global a
    if a:
        valores += 35
    if valores>=255:
        a = False
    if a==False:
        valores -=35
    if valores==10:
        valores += 35
        a=True
    #Erase values (ONLY TO TEST)

    # Read the value from the serial port
    #line = ser.readline()
    #valores = int(line)
    #Uncomment when Arduino is connected


    progress.setValue(valores)

    # Calculate temperature based on progress value
    temp = min_temp + (valores / progress.maximum()) * (max_temp - min_temp)

    # Update the label text with the current temperature (rounded to 3 decimals)
    label.setText(f"Temp: {temp:.3f}°C")

    # Adjust the fill color based on the progress value
    if valores <= 85:
        fill_color = 'green'
    elif valores <= 170:
        fill_color = 'orange'
    else:
        fill_color = 'red'

    # Update the style to change the appearance of the progress bar
    progress.setStyleSheet(f"QProgressBar {{ background-color: white; }} QProgressBar::chunk {{ background-color: {fill_color}; }}")

    # Schedule the next update
    QTimer.singleShot(1000, update_progress_bar)

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()
window.setWindowTitle("Termómetro")

# Create a frame to hold the progress bar
frame = QFrame(window)
frame.setGeometry(10, 10, 100, 400)
frame.setStyleSheet("QFrame { border: 1px solid black; }")

# Create the progress bar
progress = QProgressBar(frame)
progress.setGeometry(10, 10, 80, 380)
progress.setMaximum(255)
progress.setOrientation(Qt.Vertical)

# Create the label for temperature
label = QLabel(window)
label.setGeometry(200, 10, 100, 20)
label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

# Start the update loop
QTimer.singleShot(1000, update_progress_bar)

# Resize the window to match the dimensions of the progress bar
window.resize(frame.width() + 220, frame.height() + 20)

# Show the main window
window.show()

# Run the application
sys.exit(app.exec_())
