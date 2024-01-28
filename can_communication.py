import can
import time

# Set up the CAN interface
can_interface = 'can0'
bus = can.interface.Bus(channel=can_interface, bustype='socketcan')

try:
    while True:
        # Send a CAN message
        message = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], extended_id=False)
        bus.send(message)

        # Receive and print incoming CAN messages
        recv_message = bus.recv(timeout=1.0)
        if recv_message:
            print(f"Received: {recv_message}")

        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    bus.shutdown()
