﻿import st00.main
import st04.main
import st10.main
import st24.main
#import st41.main
#	добавить импорт своего модуля по шаблону 
#	import st<номер по журналу>.main

MENU = [
        ["[00] Образец", st00.main.main],
        ["[04] Багаутдинов", st04.main.main],
	["[10] Трифонов", st10.main.main],
        ["[24] Короленко", st24.main.main],
#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<номер по журналу>] <Фамилия>", <ссылка на функцию>],
	]

def menu():
	print("------------------------------")
	i = 0
	for item in MENU:
		print("{0:2}. {1}".format(i, item[0]))
		i += 1
	print("------------------------------")
	return int(input())

try:
	while True:
		MENU[menu()][1]()
except:
	print("bye")
