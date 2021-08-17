class Initpage:
    # 成功用例的数据
    login_success_data = [
        {"username": "root", "password": "root", "expect": "Student Login"}
    ]

    # 失败用例的数据：msg_uname
    login_pwd_error_data = [
        {"username": "root1", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"username": "root", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"username": "", "password": "11", "expect": "账户名错误或密码错误!别瞎弄!"},
        {'username': 'root', 'password': '', 'expect': '√'}
    ]
