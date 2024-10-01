import os
import time

user = os.getlogin()
print(f"Welcome {user} !")

os.system(f"mkdir C:\\Users\\{user}\\AppData\\Local\\Roblox\\Versions\\version-b591875ddfbc4294\\ClientSettings")
print("New folder is creating at "+"C:\\Users\\{user}\\AppData\\Local\\Roblox\\Versions\\version-b591875ddfbc4294\\ClientSettings")
time.sleep(3)
os.system("cls")
os.system(f"copy settings\\ClientAppSettings.json C:\\Users\\{user}\\AppData\\Local\\Roblox\\Versions\\version-b591875ddfbc4294\\ClientSettings")
print("All settings was changed for maximum performance , good games !")
time.sleep(2)
os.system("cls")
print("Roblox is running...")