import psutil


def get_Common_Memory_Info() -> dict:
    # writing a function to convert bytes to GigaByte
    def bytes_to_GB(bytes):
        gb = bytes / (1024 * 1024 * 1024)
        gb = round(gb, 2)
        return gb

    # Using the virtual_memory() function it will return a tuple
    virtual_memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {
        # This will print the primary memory details
        "Total Memory present": f"{bytes_to_GB(virtual_memory.total)} Gb",
        "Total Memory Available": f"{bytes_to_GB(virtual_memory.available)} Gb",
        "Total Memory Used": f"{bytes_to_GB(virtual_memory.used)} Gb",
        "Percentage Total Memory Used": f"{virtual_memory.percent} %",
        # This will print the swap memory details if available
        "Total swap memory": bytes_to_GB(swap.total),
        "Free swap memory": bytes_to_GB(swap.free),
        "Used swap memory": bytes_to_GB(swap.used),
        "Percentage Swap Used": f"{swap.percent} %"
    }


if __name__ == '__main__':
    mem_info = get_Common_Memory_Info()
    for k in mem_info:
        print(f'{k} : {mem_info[k]}')
