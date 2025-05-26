import os
import time

def toggler():
    # Define the path to the mods directory
    mods_dir = os.path.expandvars(r"%APPDATA%\.minecraft\mods")

    # Collect .jar and .jar.DISABLED files
    mods = [f for f in os.listdir(mods_dir) if f.endswith(".jar") or f.endswith(".jar.DISABLED")]

    # Check if there are any mod files
    if not mods:
        print("No .jar or .jar.DISABLED files found in the mods folder.")
        exit()

    # Display the mods with numbers
    print("Available mods:")
    for i, mod in enumerate(mods, start=1):
        if mod.endswith(".DISABLED"):
            print(f"[///{i}///] {mod}")
        else:
            print(f"[{i}] {mod}")

    print("")

    # User selects a file by number
    try:
        choice = int(input("Enter the number of the mod you want to toggle: "))
        if not (1 <= choice <= len(mods)):
            raise ValueError
    except ValueError:
        print("Invalid selection. Exiting.")
        exit()

    selected_file = mods[choice - 1]
    print("")
    print(f"You selected: {selected_file}")
    print("")
    confirm = input("Confirm? (Y/N): ").strip().upper()

    if confirm != "Y":
        print("Operation cancelled.")
        exit()

    # Determine full path and new name
    full_path = os.path.join(mods_dir, selected_file)

    # Toggle the .DISABLED suffix
    if selected_file.endswith(".DISABLED"):
        new_name = selected_file[:-9]  # remove '.DISABLED'
    else:
        new_name = selected_file + ".DISABLED"

    new_path = os.path.join(mods_dir, new_name)

    # Rename the file
    os.rename(full_path, new_path)
    print("")
    print(f"File renamed to: {new_name}")

    print("")
    confirm = input("Would you like to make another selection? (Y/N): ").strip().upper()
    if confirm != "Y":
        print("Closing...")
        time.sleep(1)
        exit()

    for i in range(4):
        print("")


logo = """█   █  ████    █   █  ███  ████     █   █  ███  █   █  ███   ████ █████ ████  
██ ██ █        ██ ██ █   █ █   █    ██ ██ █   █ ██  █ █   █ █     █     █   █ 
█ █ █ █        █ █ █ █   █ █   █    █ █ █ █████ █ █ █ █████ █  ██ ████  ████  
█   █ █        █   █ █   █ █   █    █   █ █   █ █  ██ █   █ █   █ █     █   █ 
█   █  ████    █   █  ███  ████     █   █ █   █ █   █ █   █  ███  █████ █   █ """

print("Welcome to:")
print("")
print(logo)
print("")
time.sleep(2)
while True:
    toggler()