import requests, time, os, json

invite_userid = os.environ.get("wps_userid")

def start(*arg):
    invite_sid = [
        "V02StVuaNcoKrZ3BuvJQ1FcFS_xnG2k00af250d4002664c02f",
        "V02SWIvKWYijG6Rggo4m0xvDKj1m7ew00a8e26d3002508b828",
        "V02Sr3nJ9IicoHWfeyQLiXgvrRpje6E00a240b890023270f97",
        "V02SBsNOf4sJZNFo4jOHdgHg7-2Tn1s00a338776000b669579",
        "V02S2oI49T-Jp0_zJKZ5U38dIUSIl8Q00aa679530026780e96",
        "V02ShotJqqiWyubCX0VWTlcbgcHqtSQ00a45564e002678124c",
        "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
        "V02S7tldy5ltYcikCzJ8PJQDSy_ElEs00a327c3c0026782526",
        "V02SPoOluAnWda0dTBYTXpdetS97tyI00a16135e002684bb5c",
        "V02Sb8gxW2inr6IDYrdHK_ywJnayd6s00ab7472b0026849b17",
        "V02SwV15KQ_8n6brU98_2kLnnFUDUOw00adf3fda0026934a7f",
        "V02SC1mOHS0RiUBxeoA8NTliH2h2NGc00a803c35002693584d",
        "V02S8T6bKMNIWqoAqyYVvGAaG6psH-o00a2615bc000e1fc45a",
        ]
    if "\\n" in "invite_userid":
        ulist = invite_userid.split("\\n")
    else:
        ulist = invite_userid.split("\n")
    msg = ""
    for i in range(0, len(ulist)):
        u = ulist[i]
        for index,i in enumerate(invite_sid):
            res = requests.post('http://zt.wps.cn/2018/clock_in/api/invite', headers={'sid': i}, data={'invite_userid': u}).json()
            c = 0
            while res["msg"] == "tryLater":
                time.sleep(2)
                res = requests.post('http://zt.wps.cn/2018/clock_in/api/invite', headers={'sid': i}, data={'invite_userid': u}).json()
                c += 1
                if res["msg"] == "maxInviteNum":
                    break
                elif c == 30:
                    # 防止卡死
                    break
            if res["msg"] == "maxInviteNum":
                msg += f"{u}已邀请完成\n"
                break
    print(msg[:-1])
    return msg[:-1]

def main(*arg):
    return start()

if __name__ == '__main__':
    if invite_userid:
        print("----------WPS开始尝试邀请----------")
        main()
        print("记得手动打卡.jpg")
        print("----------WPS邀请执行完毕----------")
