import subprocess


def get_dmi_info():
    dmi_info = {}
    try:
        # Выполняем команду grep и обрабатываем результат
        grep_output = subprocess.check_output(["ls",  "/sys/class/dmi/id/", "|", "grep", "[^bps]"]).decode('utf-8')
        print(grep_output)
        lines = grep_output.split('\n')

        # Помещаем каждую запись в словарь
        for line in lines:
            if line:
                key, value = line.split(":", 1)
                dmi_info[key.strip()] = value.strip()

    except Exception as e:
        print(f"Ошибка: {e}")

    return dmi_info

if __name__ == "__main__":
    dmi_info = get_dmi_info()

    print("Информация из /sys/class/dmi/id/:")
    for key, value in dmi_info.items():
        print(f"{key}: {value}")
