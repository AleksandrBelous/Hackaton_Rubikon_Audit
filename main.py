import flet as ft
import report
import paramiko


# import paramiko
#
#
# def execute_remote_command(remote_host, remote_user, remote_password, command):
#     # Создаем SSH-клиент
#     ssh = paramiko.SSHClient()
#
#     # Настраиваем автоматическое подтверждение ключей хоста (обычно используется при подключении впервые)
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#     try:
#         # Подключаемся к удаленному хосту
#         ssh.connect(remote_host, username=remote_user, password=remote_password)
#
#         # Выполняем команду на удаленной машине
#         stdin, stdout, stderr = ssh.exec_command(command)
#
#         # Получаем вывод выполненной команды
#         result = stdout.read().decode('utf-8')
#         return result
#
#     except Exception as e:
#         return f"Ошибка: {e}"
#     finally:
#         # Закрываем соединение
#         ssh.close()
#
#
# if __name__ == "__main__":
#     # Получаем параметры от пользователя (админа)
#     remote_host = input("Введите IP-адрес удаленного хоста: ")
#     remote_user = input("Введите имя пользователя на удаленном хосте: ")
#     remote_password = input("Введите пароль для подключения к удаленному хосту: ")
#     command_to_execute = input("Введите команду для выполнения на удаленном хосте: ")
#
#     # Выполняем команду на удаленном хосте
#     result = execute_remote_command(remote_host, remote_user, remote_password, command_to_execute)
#
#     # Выводим результат выполнения команды
#     print(f"Результат выполнения команды на удаленном хосте:\n{result}")


def main(page: ft.Page):
    page.title = 'Total Scan'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = 'always'

    possibilities = [
        "Общие данные о системе",
        "Системное время",
        "Пользователи",
        "Ядра ОС",
        "Процессоры",
        "HDD/SSD устройства",
        "CD/DVD устройства",
        "USB устройства",
        "Данные о GPU",
        "Данные о RAM памяти",
        "Сетевые настройки",
        "Приложения",
        "Исполняемые файлы PATH"
    ]

    keys = set()

    def all_selected(_):
        for e in menu[1:-1]:
            e.value = True
            keys.add(e.label)
        page.update()

    def box_clicked(box: ft.ControlEvent):
        if box.control.value:
            keys.add(box.control.label)
        else:
            keys.remove(box.control.label)
        print(keys)
        page.update()

    def start_button_clicked(_):
        report.create_reports(sorted(keys, key=lambda x: possibilities.index(x)))
        page.update()

    menu = [ft.Checkbox(label="Выбрать всё", label_position=ft.LabelPosition.LEFT, on_change=all_selected)]
    menu += [ft.Checkbox(label=p, on_change=box_clicked) for p in possibilities[0:-2]]
    menu += [ft.Checkbox(label="Приложения", on_change=box_clicked, label_position=ft.LabelPosition.LEFT)]
    menu += [ft.Checkbox(label="Исполняемые файлы PATH", on_change=box_clicked, label_position=ft.LabelPosition.LEFT)]
    menu.append(ft.ElevatedButton(text="Запуск", on_click=start_button_clicked))

    page.add(
        ft.Row([
            ft.Column(menu)
        ],
            alignment=ft.MainAxisAlignment.CENTER)
    )


if __name__ == '__main__':
    ft.app(target=main)
