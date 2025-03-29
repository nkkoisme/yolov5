import serial
import time
import logging
from typing import Optional

class ArmController:
    def __init__(self, platform: str = 'development'):
        """Initialize arm controller with platform mode.
        
        Args:
            platform: 'development' (simulated) or 'production' (real hardware)
        """
        self.platform = platform
        self.serial = None  # Fixed typo: 'none' → 'None'
        self._setup_logging()

        if platform == 'production':
            self._connect_arm('/dev/ttyACM0')  # Fixed port path
        else:
            self.logger.warning("DEVELOPMENT MODE: Arm commands simulated")  # Fixed method name

    def _connect_arm(self, port: str):
        """Connect to physical arm (RPi only)"""
        try:
            self.serial = serial.Serial(port, 115200, timeout=1)  # Fixed baud rate
            time.sleep(2)  # Fixed delay for Arduino boot
            self.logger.info(f"Connected to arm on {port}")  # Fixed f-string
        except Exception as e:
            self.logger.error(f"Arm connection failed: {e}")
            raise  # Fixed typo: 'rollen' → 'raise'

    def send_gcode(self, command: str) -> bool:
        """Send command to arm (simulated in VS Code, real on RPi)
        
        Args:
            command: G-code string to send
            
        Returns:
            bool: True if successful
        """
        if self.platform == 'production' and self.serial:  # Fixed syntax
            self.serial.write(f"{command}\n".encode())  # Fixed formatting
            return self._wait_for_ack()  # Fixed method name
        
        self.logger.debug(f"[SIM] {command}")
        return True  # Fixed capitalization: 'true' → 'True'

    def _wait_for_ack(self) -> bool:  # Fixed method name
        """Wait for Arduino acknowledgement (RPi only)
        
        Returns:
            bool: True if 'OK' received
        """
        try:
            response = self.serial.readline().decode().strip()
            return response == "OK"
        except Exception as e:
            self.logger.error(f"Arm communication error: {e}")
            return False

    def _setup_logging(self):
        """Configure logging for both platforms"""
        self.logger = logging.getLogger('ArmController')
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)