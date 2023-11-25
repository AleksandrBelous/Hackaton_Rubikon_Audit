import psutil


def get_Unix_CPU_Info() -> dict:
    # reading the cpuinfo file to print the name of the CPU present
    with open("/proc/cpuinfo", "r") as f:
        file_info = f.readlines()
    cpu_info = [x.strip().split(":")[1] for x in file_info if "model name" in x]
    return {f"Processor {str(index)}": item for index, item in enumerate(cpu_info)}


def get_Common_Cores_Info() -> dict:
    cpu_frequency = psutil.cpu_freq()
    result = {
        # This code will print the number of CPU cores present
        "Number of Physical cores": psutil.cpu_count(logical=False),
        "Number of Total cores": psutil.cpu_count(logical=True),
        # This will print the maximum, minimum and current CPU frequency
        "Max Frequency": f"{cpu_frequency.max:.2f}Mhz",
        "Min Frequency": f"{cpu_frequency.min:.2f}Mhz",
        "Current Frequency": f"{cpu_frequency.current:.2f}Mhz"
    }
    # This will print the usage of CPU per core
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        result[f"CPU Usage of Core {i}"] = f"{percentage}%"
    result["Total CPU Usage"] = f"{psutil.cpu_percent()}%"
    return result


if __name__ == '__main__':
    cpu_info = get_Common_Cores_Info()
    for k in cpu_info:
        print(f'{k} : {cpu_info[k]}')
    if psutil.LINUX:
        cpu_info = get_Unix_CPU_Info()
        for k in cpu_info:
            print(f'{k} : {cpu_info[k]}')
