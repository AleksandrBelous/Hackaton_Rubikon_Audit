import platform


def get_Common_Basic_System_Details() -> dict:
    return {
        # the Architecture of the OS
        "Architecture": platform.architecture()[0],
        # Displaying the machine
        "Machine": platform.machine(),
        # the Operating System release information
        "OS Release": platform.release(),
        # the currently using system name
        "OS Name": platform.system(),
        # the version of Operating System
        "OS Version": platform.version(),
        # the Node or hostname of Operating System
        "Node": platform.node(),
        # system platform
        "Platform": platform.platform(),
        # the processor information
        "Processor": platform.processor()
    }


if __name__ == '__main__':
    base_details = get_Common_Basic_System_Details()
    for k in base_details:
        print(f"{k} : {base_details[k]}")
