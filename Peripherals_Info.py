import psutil
import subprocess
import re


def get_Unix_USB_Devices() -> dict:
    devices = dict()
    device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    df = subprocess.check_output("lsusb", universal_newlines=True)
    count = 1
    for i in df.split('\n'):
        if i:
            _inf = device_re.match(i)
            if _inf:
                dinfo = _inf.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                devices[f"usb {count}"] = dinfo
                count += 1
    return devices


if __name__ == '__main__':
    if psutil.LINUX:
        usb_info = get_Unix_USB_Devices()
        for k in usb_info:
            print(f'{k} : {usb_info[k]}')
