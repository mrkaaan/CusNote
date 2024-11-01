import pyautogui as pg
import time

time.sleep(10)

post_1 = pg.locateOnScreen('but.png')
goto_post = pg.center(help)

pg.moveTo(goto_post,duration=1)
pg.click()
pg.moveRel(None,508,duration=1)
pg.click()
