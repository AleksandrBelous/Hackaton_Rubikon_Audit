import psutil


def get_Common_Network_Info() -> dict:
    # writing a function to convert the bytes into gigabytes
    def bytes_to_GB(bytes):
        gb = bytes / (1024 * 1024 * 1024)
        gb = round(gb, 2)
        return gb

    # gathering all network interfaces (virtual and physical) from the system
    if_addrs = psutil.net_if_addrs()

    # the information of each network interfaces
    result = {
        interface_name: {
            count: {
                "Address": address.address,
                "Netmask": address.netmask,
                "Broadcast": address.broadcast,
                "point to point": address.ptp
            } for address in if_addrs[interface_name] if (count := count + 1)
        } for interface_name in if_addrs if (count := 0) or True
    }

    # getting the read/write statistics of network since boot
    net_io = psutil.net_io_counters()
    result["Total Bytes Sent"] = f"{bytes_to_GB(net_io.bytes_sent)} GB"
    result["Total Bytes Received"] = f"{bytes_to_GB(net_io.bytes_recv)} GB"
    return result


if __name__ == '__main__':
    net_info = get_Common_Network_Info()
    for int_name in net_info:
        if isinstance(net_info[int_name], dict):
            print(f'\ninterface : {int_name}\n')
            for addr in net_info[int_name]:
                print()
                for k in net_info[int_name][addr]:
                    print(f"{k} : {net_info[int_name][addr][k]}")
        else:
            print(f"{int_name} : {net_info[int_name]}")
