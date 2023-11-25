import os
import psutil
from datetime import datetime


def get_executables_in_PATH() -> dict:
    # Получаем значение переменной окружения PATH
    path_dirs = os.getenv("PATH").split(os.pathsep)

    executables_info = {}

    # Перебираем все каталоги в переменной PATH
    for path_dir in path_dirs:
        try:
            # Получаем список файлов в каталоге
            files = os.listdir(path_dir)
            # Фильтруем только исполняемые файлы
            for file_name in files:
                file_path = os.path.join(path_dir, file_name)
                if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                    # Получаем информацию о файле
                    stat_info = os.stat(file_path)

                    executable_info = {
                        'name': file_name,
                        'size': stat_info.st_size,
                        'date_modified': datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                        'owner': stat_info.st_uid,
                        'group': stat_info.st_gid,
                        'date_created': datetime.fromtimestamp(stat_info.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
                    }

                    executables_info[executable_info['name']] = executable_info

        except OSError as e:
            print(f"Ошибка при чтении каталога {path_dir}: {e}")

    return dict(sorted(executables_info.items()))


def get_xdg_open_applications() -> dict:
    applications = {}

    # Каталог, где хранятся .desktop файлы системных приложений
    system_app_dir = '/usr/share/applications'
    # Каталог, где хранятся .desktop файлы пользовательских приложений
    user_app_dir = os.path.expanduser('~/.local/share/applications')

    app_dirs = [system_app_dir, user_app_dir]

    for app_dir in app_dirs:
        try:
            # Получаем список файлов в каталоге
            files = os.listdir(app_dir)
            # Фильтруем только .desktop файлы
            desktop_files = [f for f in files if f.endswith('.desktop')]

            # Извлекаем имена приложений из .desktop файлов и дополнительную информацию
            for desktop_file in desktop_files:
                app_info = {'name': None, 'size': None, 'date_modified': None, 'owner': None, 'group': None,
                            'date_created': None}
                with open(os.path.join(app_dir, desktop_file), 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        if line.startswith('Name='):
                            app_info['name'] = line.strip()[5:]
                            break

                file_path = os.path.join(app_dir, desktop_file)
                try:
                    stat_info = os.stat(file_path)
                    app_info['size'] = stat_info.st_size
                    app_info['date_modified'] = datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                    app_info['owner'] = stat_info.st_uid
                    app_info['group'] = stat_info.st_gid
                    app_info['date_created'] = datetime.fromtimestamp(stat_info.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
                except OSError as e:
                    print(f"Ошибка при получении информации о файле {file_path}: {e}")

                applications[app_info['name']] = app_info

        except OSError as e:
            print(f"Ошибка при чтении каталога {app_dir}: {e}")

    return dict(sorted(applications.items()))


if __name__ == "__main__":
    if psutil.LINUX:
        executables = get_executables_in_PATH()
        print("Исполняемые файлы в PATH:")
        for executable_name, executable_info in executables.items():
            print(f"Name: {executable_name}")
            print(f"Size: {executable_info['size']} bytes")
            print(f"Date Modified: {executable_info['date_modified']}")
            print(f"Owner: {executable_info['owner']}")
            print(f"Group: {executable_info['group']}")
            print(f"Date Created: {executable_info['date_created']}")
            print("\n")
        print(50 * '#')
        print()
        xdg_open_applications = get_xdg_open_applications()
        print("Приложения, доступные через xdg-open:")
        for app, info in xdg_open_applications.items():
            print(f"Application: {app}")
            print(f"Size: {info['size']} bytes")
            print(f"Date Modified: {info['date_modified']}")
            print(f"Owner: {info['owner']}")
            print(f"Group: {info['group']}")
            print(f"Date Created: {info['date_created']}")
            print("\n")
