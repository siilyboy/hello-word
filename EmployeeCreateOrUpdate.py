import requests

with open("PublicKey.txt", "r", encoding='UTF-8') as f:
    publicKey = f.read()

#定义请求参数headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + publicKey,
    # "Host": "10.1.2.90:5600",
    # "Content-Length": "385",
    # "Accept": "application/json, text/plain, */*",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    # "Content-Type": "application/json",
    # "Origin": "http://10.1.2.90:5600",
    # "Referer": "http://10.1.2.90:5600/login",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "zh-CN,zh;q=0.9",
    # "Connection": "close"
}

#定义请求参数body
body = {
    "fullName": "人员00002",
    "employeeType": 0,
    "employeeNo": "000000004",
    "departmentId": 1,
    "jobTitleId": "5a43652b-cb4b-41d8-a39f-69eb410b32db",
    "workTypeId": "2c222f41-6a26-46c6-b5cf-5129c4bcb63e",
    "phone": "13145467889",
    "undergroundPhone": "13146549879",
    "cardNo": "564684653",
    "cardType": 0,
    "sex": 0,
    "birthDay": "2022-05-19",
    "idNumber": "500228199411164642",
    "mainWorkPlace": "主要工作地点",
    "education": 1,
    "bloodType": 0,
    "maritalStatus": 0,
    "address": "家庭住址",
    "familyPhone": "13164687979",
    "nationality": 2,
    "credentialsExpired": "2023-06-30"
}
req = requests.post(url="http://10.1.2.90:5600/api/Employee/EmployeeCreateOrUpdate", headers=headers,json=body)

print(req.status_code)
print(req.text)

