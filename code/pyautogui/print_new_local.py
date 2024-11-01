import pyautogui as pg

last_post = pg.position()

try:
  while True:
    new_post=pg.position()
    if last_post != new_post:
      print(new_post)
      last_post = new_post
# 补货异常
except KeyboardInterrupt:
  print('\nExit')


