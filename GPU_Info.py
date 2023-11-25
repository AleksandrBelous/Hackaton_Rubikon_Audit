import subprocess


def get_Unix_CGPU_Info() -> dict:
    gpu = subprocess.check_output(r"lspci | grep ' VGA ' | cut -d' ' -f1 | xargs -i lspci -v -s {}",
                                  universal_newlines=True, shell=True)
    gpu = gpu.split('\t')
    gpu = [line.rstrip('\n') for line in gpu]
    result = {"GPU Information": {}}
    count = 1
    for line in gpu:
        pair = line.split(': ')
        if len(pair) == 2:
            k, v = pair
            result["GPU Information"][k] = v
        else:
            k, v = count, pair[0]
            result["GPU Information"][k] = v
            count += 1
    return result


if __name__ == '__main__':
    gpu_info = get_Unix_CGPU_Info()
    for inf in gpu_info:
        print(inf)
        for k in gpu_info[inf]:
            print(f"{k} : {gpu_info[inf][k]}")
