import os
import time


def main():
  print('PID - {0}'.format(os.getpid()))
  while True:
    print('{0} - Press CTRL+C to exit'.format(time.time()))
    time.sleep(5)
