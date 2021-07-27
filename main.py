import requests

SIGN_IN_URL = "https://www.hifini.com/sg_sign.htm"

def main():
    post_data = {"x-requested-with": "XMLHttpRequest"}
    cookies = {"enwiki_session":r"bbs_sid=1o2dvf9jdef91njnp6loip6pk2; Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1627347356,1627347488,1627347805; bbs_token=BCwTQeQThsyfaov4vEF1lVZfQYisNqHvLmo_2BH6YXYtVNlhfjgjXLO4MORSo_2FoEjOfBhAVwFLpftSfBmjzwoYmYDqqySiNPu2; Hm_lpvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1627349789"}
    r1 = requests.post(url=SIGN_IN_URL, data=post_data, cookies=cookies)
    print(r1.text)
    return 0

if __name__ == '__main__':
    if main() != 0:
        print("Script execution error, abnormal exit !")
    pass

