# encoding: utf-8
#
import requests

XSS_FILE_PATH="./data/valid_xss.txt"
NORMAL_FILE_PATH="./data/valid_normal.txt"

xss_data_sum = 0
xss_sensitive_data_sum = 0
normal_data_sum = 0
normal_sensitive_data_sum = 0

normal_right = ""
normal_wrong = ""


with open(XSS_FILE_PATH) as f:
    str = f.readlines()
    for payload in str:
        xss_data_sum += 1
        post_data = {'username': payload, 'password': '', 'login': 'Login'}

        r = requests.post("http://192.168.1.68/login.php", data=post_data)

        if "Forbidden" in r.text:
            xss_sensitive_data_sum += 1
        else:
            print(xss_data_sum)
            print(payload)

with open(NORMAL_FILE_PATH) as f:
    str = f.readlines()
    for payload in str:
        normal_data_sum += 1
        post_data = {'username': payload, 'password': '', 'login': 'Login'}

        r = requests.post("http://192.168.1.68/login.php", data=post_data)

        if "Forbidden" in r.text:
            normal_sensitive_data_sum += 1


print("xss_data_sum is ", xss_data_sum)
print("xss_sensitive_data_sum is ", xss_sensitive_data_sum)
print("检测率为：", float(xss_sensitive_data_sum)/float(xss_data_sum))

print("normal_data_sum is ", normal_data_sum)
print("sensitive_data_sum is ", normal_sensitive_data_sum)
print("误报率为：", float(normal_sensitive_data_sum)/float(normal_data_sum))

print("acc 为：", float(xss_sensitive_data_sum + normal_data_sum - normal_sensitive_data_sum)/float(xss_data_sum + normal_data_sum))

