import requests
import re
import time
from concurrent.futures import ThreadPoolExecutor

SIGN_IN_URL = "https://www.hifini.com/sg_sign.htm"


def sign_hifi():
    post_data = {"x-requested-with": "XMLHttpRequest"}
    cookies = {
        "enwiki_session": r"bbs_sid=4bh9alktdpajnn93jih89dgb6t; bbs_token=IVQuA0yigYg_2F2zC3WucQckhvwXYC_2BDjd4iWBWwmBeh8V1dRYKD4j8AcHuMVrLHYcrgBTcVwqlA_2BeC53P9Yyi39x19PQIZ7dD"}
    r1 = requests.post(url=SIGN_IN_URL, data=post_data, cookies=cookies)
    if r1.ok:
        html_text = r1.text
        for line in html_text.splitlines():
            if "今天已经签过" in line:
                print(line)
                return 1
            if "成功签到" in line:
                print(line)
                return 0
        print('可能签到失败')
        return 2
    print('登录失败')
    return 2


def main():
    thread_pool = ThreadPoolExecutor(max_workers=2)
    while True:
        cur_local_time = time.localtime(time.time())
        if cur_local_time.tm_hour == 23 and cur_local_time.tm_min == 59 and cur_local_time.tm_sec == 59:
            thread_pool.submit(sign_hifi)
        if cur_local_time.tm_hour == 0 and cur_local_time.tm_min == 0:
            thread_pool.submit(sign_hifi)
            break
        time.sleep(0.2)
    sign_hifi()
    return 0


if __name__ == '__main__':
    if main() != 0:
        print("Script execution error, abnormal exit !")
    pass
