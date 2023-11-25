import json
import Basic_System_Details
import CPU_Info
import Disk_Info
import GPU_Info
import Memory_Info
import Network_Info
import Peripherals_Info
import Software_Info
import System_Uptime
import Users_Info


def append_to_json() -> None:
    json_file_path = 'report.json'
    try:
        report = {
            "Общие данные о системе": Basic_System_Details.get_Common_Basic_System_Details(),
            "Системное время": System_Uptime.get_Unix_System_Uptime_Info(),
            "Пользователи": Users_Info.get_Common_Users_Info(),
            "Ядра ОС": CPU_Info.get_Common_Cores_Info(),
            "Процессоры": CPU_Info.get_Unix_CPU_Info(),
            "HDD/SSD устройства": Disk_Info.get_Common_Disk_Info(),
            "CD/DVD устройства": Disk_Info.get_CD_DVD_info(),
            "USB устройства": Peripherals_Info.get_Unix_USB_Devices(),
            "Данные о GPU": GPU_Info.get_Unix_CGPU_Info(),
            "Данные о RAM памяти": Memory_Info.get_Common_Memory_Info(),
            "Сетевые настройки": Network_Info.get_Common_Network_Info(),
            "Приложения": Software_Info.get_xdg_open_applications(),
            "Исполняемые файлы PATH": Software_Info.get_executables_in_PATH(),
        }
        # Запись отчёта в JSON файл
        with open(json_file_path, 'w') as file:
            json.dump(report, file, ensure_ascii=False, indent=2)
        print(f"Данные успешно добавлены в файл: {json_file_path}")
    except Exception as e:
        print(f"Произошла ошибка при добавлении данных в файл: {e}")


if __name__ == '__main__':
    append_to_json()
