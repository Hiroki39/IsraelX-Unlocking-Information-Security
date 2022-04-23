import time
import sys  # ignore
sys.path.insert(0, '.')  # ignore

real_password = "1234"


def check_password(password):  # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1)  # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True


def crack_password():
    pswd = ["0" for i in range(4)]
    for i in range(3):
        max_time = 0
        correct_digit = None
        for j in range(10):
            pswd[i] = str(j)
            start = time.time()
            check_password("".join(pswd))
            end = time.time()
            duration = end - start
            if duration > max_time:
                max_time = duration
                correct_digit = str(j)
        pswd[i] = correct_digit
    for i in range(10):
        pswd[3] = str(i)
        if check_password("".join(pswd)):
            return "".join(pswd)
