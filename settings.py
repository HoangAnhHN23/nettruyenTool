from os import getcwd, path
from json import dump

if __name__ == "__main__":
    settings = {}
    settings["app_url"] = input("Nhập url của nettruyen: ")
    settings["email"] = input("Nhập email đăng nhập: ")
    settings["password"] = input("Nhập password đăng nhập: ")
    settings["threads"] = int(input("Nhập số luồng muốn chạy: "))
    settings["comics"] = []
    for i in range(settings["threads"]):
        settings["comics"].append(input(f"Nhập URL của tryện thứ {i + 1}: "))
    with open(path.join(getcwd(), "settings.json"), "w") as outfile:
        dump(settings, outfile)