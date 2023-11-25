from datetime import datetime
import psutil


def get_Unix_System_Uptime_Info() -> dict:
    # Using the psutil library to get the boot time of the system
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    # getting the system uptime from the uptime file at proc directory
    with open("/proc/uptime", "r") as f:
        uptime = f.read().split(" ")[0].strip()
    uptime = int(float(uptime))
    uptime_hours = uptime // 3600
    uptime_minutes = (uptime % 3600) // 60
    return {
        "System Boot Time": str(boot_time),
        "System Uptime": str(uptime_hours) + ":" + str(uptime_minutes) + " hours"
    }


if __name__ == '__main__':
    if psutil.LINUX:
        time_info = get_Unix_System_Uptime_Info()
        for k in time_info:
            print(f'{k} : {time_info[k]}')
