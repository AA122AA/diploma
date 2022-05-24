import time
import random
import datetime

def rand_nums():
    while True:
        # code things
        r = random.randint(0,10000)
        f = open('/var/log/number.log', 'a')
        if r < 10 :
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            f.write("[ERROR] I fell asleep at time {timestamp}\n".format(timestamp=st))
        else :
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            f.write("[LOG] I guessed {rn} at time {timestamp}\n".format(rn=random.randint(0,10000),timestamp=st))
        f.close()
        time.sleep(10)

rand_nums()
