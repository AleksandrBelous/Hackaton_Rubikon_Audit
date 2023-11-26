import os


def get_Unix_DMI_id_Info():
    dmi_info = {}
    try:
        dmi_path = "/sys/class/dmi/id/"

        # Получаем список файлов в директории
        files = os.listdir(dmi_path)

        # Фильтруем файлы по заданным условиям и добавляем их в словарь
        filtered_files = [file for file in files if file.startswith(('b', 's', 'p'))]
        for file in filtered_files:
            file_path = os.path.join(dmi_path, file)
            if os.access(file_path, os.R_OK) and os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    content = f.read().strip()
                    dmi_info[file] = content

    except Exception as e:
        print(f"Ошибка: {e}")

    return dmi_info


if __name__ == "__main__":
    print(get_Unix_DMI_id_Info())
