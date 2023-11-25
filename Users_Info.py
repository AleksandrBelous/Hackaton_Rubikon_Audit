import psutil


def get_Common_Users_Info() -> dict:
    users = psutil.users()
    return {
        user.name: {
            "name": user.name,
            "terminal": user.terminal,
            "host": user.host,
            "started": f"{user.started} seconds since the epoch",
            "pid": user.pid
        }
        for user in users}


if __name__ == '__main__':
    users_info = get_Common_Users_Info()
    for k in users_info:
        print(f'{k} : {users_info[k]}')
