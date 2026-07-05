import time


def follow_log(logfile):
    with open(logfile, 'r', encoding='utf-8') as file:
        file.seek(0, 2)

        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue
            yield line.strip()
