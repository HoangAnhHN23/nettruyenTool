# Import thư viện
from threading import Thread
from undetected_chromedriver import ChromeOptions, Chrome
from time import sleep
from os import getcwd, path
from json import load


def nettruyen(app_url: str, email: str, password: str, comic_url: str, MAX: int):
    options = ChromeOptions()
    options.add_argument("--window-size=350,550")
    options.add_argument("--app=" + app_url)
    driver = Chrome(options=options)
    driver.implicitly_wait(15)

    # Đăng nhập tài khoản

    driver.execute_script('document.querySelector(".login-link > a").click();')
    sleep(2)
    driver.execute_script(
        'document.getElementById("ctl00_mainContent_login1_LoginCtrl_UserName").value = "' + email + '";')
    sleep(2)
    driver.execute_script(
        'document.getElementById("ctl00_mainContent_login1_LoginCtrl_Password").value = "' + password + '";')
    sleep(2)
    driver.execute_script(
        'document.getElementById("ctl00_mainContent_login1_LoginCtrl_Login").click();')
    sleep(10)

    # Bắt đầu cày điểm
    while True:
        try:
            driver.execute_script(
                'window.location.href = "' + comic_url + '";')
            sleep(2)
            driver.execute_script(
                'document.querySelector(".read-action > a").click();')
            sleep(2)
            for _ in range(MAX):
                for j in range(7000):
                    driver.execute_script(f'scroll(0,{j*3});')
                driver.execute_script('window.alert = {};')
                driver.execute_script(
                    'document.querySelector(".a_next").click();')
        except Exception as e:
            print(e)
            driver.quit()
            return


if __name__ == '__main__':
    # Đọc thông tin từ file settings
    with open(path.join(getcwd(), "settings.json"), "r") as infile:
        settings = load(infile)
        
    # Chạy trương chình
    n = settings["threads"]
    for i in range(n):
        Thread(target=nettruyen, args=(
            settings["app_url"], settings["email"], settings["password"], settings["comics"][i], 100)).start()
