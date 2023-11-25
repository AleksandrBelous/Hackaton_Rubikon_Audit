import psutil


def get_Common_Disk_Info() -> dict:
    # accessing all the disk partitions
    disk_partitions = psutil.disk_partitions()

    # get read/write statistics since boot
    disk_rw = psutil.disk_io_counters()

    # writing a function to convert bytes to Giga bytes
    def bytes_to_GB(bytes):
        gb = bytes / (1024 * 1024 * 1024)
        gb = round(gb, 2)
        return gb

    # displaying the partition and usage information
    result = dict()
    for partition in disk_partitions:
        disk_usage = psutil.disk_usage(partition.mountpoint)
        result[partition.device] = {
            "Partition Device": partition.device,
            "File System": partition.fstype,
            "Mount point": partition.mountpoint,
            "Total Disk Space": f"{bytes_to_GB(disk_usage.total)} GB",
            "Free Disk Space": f"{bytes_to_GB(disk_usage.free)} GB",
            "Used Disk Space": f"{bytes_to_GB(disk_usage.used)} GB",
            "Percentage Used": f"{disk_usage.percent} %"
        }

    result["Total Read since boot"] = f"{bytes_to_GB(disk_rw.read_bytes)} GB"
    result["Total Write since boot"] = f"{bytes_to_GB(disk_rw.write_bytes)} GB"
    return result


if __name__ == '__main__':
    disk_info = get_Common_Disk_Info()
    for k in disk_info:
        if isinstance(disk_info[k], dict):
            print('new disk')
            for key in disk_info[k]:
                print(f"{key} : {disk_info[k][key]}")
        else:
            print(f'{k} : {disk_info[k]}')
