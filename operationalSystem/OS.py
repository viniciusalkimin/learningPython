import platform
import getpass
from datetime import datetime


print("Device name:...", platform.node())
print("Architecture:...", platform.architecture())
print("Operational System:...", platform.system())
print("OS version:...", platform.release())
print("Processor:...", platform.processor())
print("Python version:...", platform.python_version())

print("Timestamp of now:...", datetime.now())

print(getpass.getuser())
print(getpass.getpass("Digite sua senha:"))