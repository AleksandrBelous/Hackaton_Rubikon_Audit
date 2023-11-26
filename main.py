import flet as ft
import report


def main(page: ft.Page):
    page.title = 'Total Scan'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

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
        report.append_to_json(sorted(keys, key=lambda x: possibilities.index(x)))
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
