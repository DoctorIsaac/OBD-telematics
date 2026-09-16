import obd 
import time
from datetime import datetime

portstr = "/dev/ttys004"  # replace with your OBD-II adapter's port
baudrate = 38400  # replace with your OBD-II adapter's baud rate
connection = obd.OBD(portstr=portstr, baudrate=baudrate)  # auto-connects to emulator

commands = [
            ("RPM", obd.commands.RPM),
            ("Speed", obd.commands.SPEED),
            ("Coolant Temperature", obd.commands.COOLANT_TEMP)
        ]

try:
    while True:
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for name, cmd in commands:
            response = connection.query(cmd)
            if response.is_null():
                print(f"{name}: No data")
            else:
                print(f"{name}: {response.value}")
        time.sleep(1)  # wait for 1 second before the next query
except KeyboardInterrupt:
    print("Exiting...")
    connection.close()
