import serial.tools.list_ports
import matplotlib.pyplot as plt
import time

from pynput import keyboard

is_running = True

def on_press(key):
    pass
    # print('{0} pressed'.format(
    #     key))

def on_release(key):
    # print('{0} release'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        global is_running
        is_running = False
        return False

# Collect events until released
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

ports = list(serial.tools.list_ports.comports())

print("\n\n===================================================")
print("PLEASE CHOOSE ONE OF THE FOLLOWING PORTS")
print("For Windows, type COM#")
print("ex. COM6\n")
for p in ports:
    print(p)

greeting_msg = "\nType Port Here: "
selected_port = input(greeting_msg)

print("\nSTARTING TO READ "+selected_port)
print("PRESS ESC TO END THE RECORDING")
print("===================================================")

# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = selected_port
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 115200

# Start the clock
t0 = time.time()
# Oopen a serial connection
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
# Start recording the file in this variable
file_text = ""
readings = []
time_stamps = []
while is_running:

    # using ser.readline() assumes each line contains a single reading
    # sent using Serial.println() on the Arduino
    reading = ser.readline().decode('utf-8')
    # reading is a string
    print(reading)
    readings.append(int(reading))
    # Cur time is a float
    cur_time = time.time() - t0
    time_stamps.append(cur_time)

    file_text = file_text+str(cur_time)+","+str(int(reading))+"\n"


f = open("data.csv", "w")
f.write(file_text)
f.close()

plt.plot(time_stamps,readings)
plt.title('Serial Readings over Time')
plt.ylabel('Variable Magnitude')
plt.xlabel('Time (s)')
plt.show()