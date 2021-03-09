
# BOMBSHOT v1.0 | BY BOUMER7
# Licensed under Mozilla Public License 2.0

import os
import sys
import re

import time
import random

import requests
import json
import threading
from threading import Thread

from transliterate import translit
import proxyscrape
import urllib.request
from fake_useragent import UserAgent

from pathlib import Path

# file with APIs
import apis_services

# https://stackoverflow.com/a/287944
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class bombshot:

	def colored_input():
		u_input = input(bcolors.OKCYAN + 'Ввод' + bcolors.FAIL + ' >> ' + bcolors.WARNING)
		return u_input

	def error_output(text = None):
		return bcolors.FAIL + text

	def warning_output(text = None):
		return bcolors.WARNING + text

	def okcyan_output(text = None):
		return bcolors.OKCYAN + text

	def okgreen_output(text = None):
		return bcolors.OKGREEN + text

	def exiting_program(text = None):
		bombshot.clear()
		print(bombshot.warning_output('[ПРЕДУПРЕЖДЕНИЕ]: Выход из программы...'))
		exit()

	def exiting_program_error(text = None):
		print(bombshot.error_output('[ОШИБКА]: ' + str(text) + ' Выход из программы...'))
		exit()

	def clear():
		os.system('cls' if os.name == 'nt' else 'clear')

	def logo():
		logo = (bcolors.FAIL + 'BOMBSHOT v2.0 💣' + bcolors.OKCYAN + 
			' | ' + 'BY BOUMER7\n')
		print(logo, end='')
		print(bcolors.WARNING + 'Инструмент для пентестинга.')

	# https://stackoverflow.com/a/15924160
	def is_non_zero_file(fpath):
		fpath = Path(fpath)
		try:
			return os.path.isfile(fpath) and os.path.getsize(fpath) > 0
		except OSError as e:
			return e

	# https://stackoverflow.com/a/765436
	def is_bad_proxy(proxy, proxy_timeout = 0.5):
		ua = UserAgent() 

		try:
			proxy_handler = urllib.request.ProxyHandler({'http': proxy})
			opener = urllib.request.build_opener(proxy_handler)
			opener.addheaders = [('User-Agent', ua.random)]
			urllib.request.install_opener(opener)
			req = urllib.request.Request('http://proxyjudge.us/azenv.php')
			sock = urllib.request.urlopen(req, timeout = proxy_timeout)

		except urllib.error.HTTPError:
			return True

		except Exception as detail:
			return True

		return False

	def get_proxies(desired_amount : int = 1, proxy_timeout = 0.5):

		proxies = []

		# https://stackoverflow.com/a/59531141
		try:
			collector_1 = proxyscrape.get_collector('collector-http')

		except proxyscrape.errors.CollectorNotFoundError:
			collector_1 = proxyscrape.create_collector('collector-http', 'http')

		full_list = list(collector_1.get_proxies())

		for item in full_list:
			proxies.append(item.host + ':' + item.port)

		print('Найдено', str(len(proxies)), 'HTTP прокси')
		print('Проверка на работоспособность прокси...')
		print(bcolors.WARNING + '[Ctrl + Z - Выйти из программы]')


		time.sleep(2.5)
		bombshot.clear()
		start_time = time.time()

		cnt = 0

		print(bcolors.WARNING + 'Проверено' + bcolors.FAIL + ' 0 ' + bcolors.WARNING + 'из', bcolors.FAIL + str(len(proxies)), bcolors.WARNING + 'прокси с задержкой', bcolors.OKGREEN + str(proxy_timeout), bcolors.WARNING + 'cек...')
		print(bcolors.WARNING + 'Выбрано' + bcolors.FAIL, str(cnt), bcolors.WARNING + 'из', bcolors.FAIL + str(desired_amount), bcolors.WARNING + 'прокси с задержкой', bcolors.OKGREEN + str(proxy_timeout), bcolors.WARNING + 'cек...')
		print(bcolors.WARNING + '[Ctrl + Z - Выход из программы]')

		checked_proxy = []
		
		for ind, item in enumerate(proxies, start = 1):

			if cnt < desired_amount:

				if bombshot.is_bad_proxy(item, proxy_timeout):
					print(bcolors.WARNING + '[BAD PROXY]')
				else:
					checked_proxy.append(item) 
					cnt += 1
			else:
				break


			bombshot.clear()
			print(bcolors.WARNING + 'Проверено' + bcolors.FAIL, str(ind) + bcolors.WARNING, 'из', bcolors.FAIL + str(len(proxies)), bcolors.WARNING + 'прокси с задержкой', bcolors.OKGREEN + str(proxy_timeout), bcolors.WARNING + 'cек...')
			print(bcolors.WARNING + 'Выбрано' + bcolors.FAIL, str(cnt) + bcolors.WARNING, 'из', bcolors.FAIL + str(desired_amount), bcolors.WARNING + 'прокси с задержкой', bcolors.OKGREEN + str(proxy_timeout), bcolors.WARNING + 'cек...')
			print(bcolors.OKCYAN + '[Не выходите из программы, если вы не хотите потерять выбранные прокси]')
			print(bcolors.WARNING + '[Ctrl + Z - Выход из программы]')


		end_time = time.time()

		extra_message = bcolors.WARNING + '[Добавлено ' + bcolors.FAIL + str(cnt) + bcolors.WARNING + ' прокси с задержкой {} сек. в proxy_list.txt'.format(str(proxy_timeout))
		time_passed = bcolors.WARNING + ' за {} сек.]'.format(round(end_time - start_time, 2))
		extra_message = extra_message + time_passed

		with open('proxy_list.txt', 'a') as infl:
			for item in checked_proxy:
				infl.write(''.join(item) + '\n')

		bombshot.print_full_main_screen(extra_message)

	def to7(phone):
		phone = str(phone)

		if phone[0] in ('7', '8'):
			if len(phone) == 11:
				if phone[0] == '8':
					phone = '7' + phone[1:]
				return phone
			else:
				return False
		else:
			return False

	def generate_credentials():

		vocabulary = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

		name_vocabulary = [
		'Павел', 'Михаил', 'Иван', 'Матвей', 'Игорь', 'Владимир',
		'Михаил', 'Георгий', 'Савелий', 'Никита', 'Александр', 
		'Андрей', 'Родион', 'Максим', 'Даниил', 'Кирилл', 'Лев', 
		'Алексей', 'Роман', 'Марк', 'Макар', 'Егор', 'Тихон', 
		'Тимофей', 'Степан'
		]

		surname_vocabulary = [
		'Смирнов', 'Яковлев', 'Воробьев', 'Фомин', 'Миронов',
		'Капустин', 'Соболев', 'Захаров', 'Акимов', 'Кравцов',
		'Новиков', 'Афанасьев', 'Колосов', 'Антонов', 'Денисов',
		'Алексеев', 'Александров', 'Романов', 'Бочаров', 'Павлов',
		'Зубков', 'Мещеряков', 'Андреев'
		]

		patronymic_vocabulary = [
		'Артёмович', 'Александрович', 'Леонидович', 'Георгиевич',
		'Андреевич', 'Игоревич', 'Максимович', 'Романович', 
		'Давидович', 'Викторович', 'Егорович', 'Олегович',
		'Сергеевич', 'Фёдорович'
		]

		email_vocabulary = [
		'gmail.com', 'yandex.ru', 'ya.ru', 'bk.ru', 'mail.ru',
		'yahoo.com', 'list.ru', 'ya.kz', 'yandex.ua', 'ya.ua',
		'yandex.kz', 'ya.kz', 'inbox.ru','internet.ru', 'inbox.ru',
		'yandex.by', 'ya.by'
		]

		password = ''
		for x in range(12):
			password += random.choice(vocabulary)

		rand_end = random.randint(1, 3)

		# randomizing the ending of email, 1 - just random number, 2 - random full year, 3 - random shortened year
		if rand_end == 1:
			rand_end = random.randint(500, 999)
		elif rand_end == 2:
			rand_end = random.randint(1965, 1999)
		else:
			rand_end = str(random.randint(1965, 1999))[2:]

		# random separator
		# write name_surname or namesurname or name-surname (underscore True or False)
		rand_sep = random.randint(1, 3)
		if rand_sep == 1:
			rand_sep = '_'
		elif rand_sep == 2:
			rand_sep = '-'
		else:
			rand_sep = ''

		name = random.choice(name_vocabulary)
		latin_name = translit(name, 'ru', reversed=True).replace("'", "").replace('j', 'y')

		surname = random.choice(surname_vocabulary)
		latin_surname = translit(surname, 'ru', reversed=True).replace("'", "").replace('j', 'y')

		patronymic = random.choice(patronymic_vocabulary)

		email_value = latin_name.lower() + rand_sep + latin_surname.lower() + str(rand_end)

		email = "{}@{}".format(email_value, random.choice(email_vocabulary))

		return name, surname, patronymic, latin_name, email, password

	def update_value():
		return bombshot.okcyan_output(', - Обновить значения')

	def zero_to_exit():
		return bombshot.error_output('0 - Выход из программы')

	def go_back():
		return bombshot.okgreen_output('. - Назад')

	def preinstalled_list():
		print(bombshot.okcyan_output('Выберите жертву:'), end='')
		print(bcolors.WARNING)
		with open('class_surnames.txt', 'r') as infl:
			for ind, i in enumerate(infl, start = 1):
				print(ind, '-', i, end='')

		print(bombshot.go_back())
		print(bombshot.zero_to_exit())

		# len of people
		return ind

	def random_name_generator():
		bombshot.clear()
		creds = bombshot.generate_credentials()
		print('ФИО:', creds[1], creds[0], creds[2])
		latin_full_name = creds[1] + ' ' + creds[0] + ' ' + creds[2]

		print('Имя на латинице:', translit(latin_full_name, 'ru', reversed = True).replace("'", "").replace('j', 'y').replace('J', 'Y'))

		print('Почта:', creds[4])
		print('Пароль:', creds[5])

		print(bombshot.go_back())
		print(bombshot.update_value())
		print(bombshot.zero_to_exit())

		next_input = bombshot.colored_input()

		if next_input == '.':
			bombshot.clear()
			bombshot.print_full_main_screen()

		elif next_input == '0':
			print(bombshot.exiting_program())
			exit()

		elif next_input == ',':
			bombshot.random_name_generator()

		else:
			bombshot.exiting_program_error('Опция не найдена.')

	def shuffle_proxies():
		proxies = []
		with open('proxy_list.txt', 'r') as infl:
			for i in infl:
				proxies.append(i.replace('\n', ''))

		random.shuffle(proxies)

		with open('proxy_list.txt', 'w') as infl:
			for i in proxies:
				infl.write(i + '\n')

		colors = [bcolors.OKBLUE, bcolors.OKGREEN, bcolors.OKCYAN, bcolors.HEADER, bcolors.ENDC]

		c1 = random.choice(colors)
		c2 = random.choice(colors)

		while c2 == c1:
			c2 = random.choice(colors)

		bombshot.print_full_main_screen(bombshot.warning_output('%s[Успешно перемешано %s %sпрокси в proxy_list.txt]' % (c1, bcolors.FAIL + str(len(proxies)), c2) ))

	def count_services():
		apis_file = open('apis_services.py')
		apis_content = apis_file.read()

		services_count = apis_content.count('requests.post') + apis_content.count('requests.get')
		print(bombshot.warning_output('Сервисы:'), str(bombshot.error_output(str(services_count))))

	def print_proxy_screen():
		bombshot.clear()
		print(bombshot.warning_output('Введите количество прокси:'))
		print(bombshot.go_back())
		print(bombshot.zero_to_exit())

		next_input = bombshot.colored_input()

		if next_input == '.':
			bombshot.print_full_main_screen()

		elif next_input == '0':
			bombshot.exiting_program()

		elif next_input.isdigit():

			if 1 <= int(next_input) <= 1000:
				bombshot.clear()
				print(bombshot.warning_output('Введите задержку прокси (в секундах, от 0.1 до 10):\nЧем выше задержка, тем дольше будет поиск.'))
				print(bombshot.go_back())
				print(bombshot.zero_to_exit())
				print(bombshot.warning_output('[Введите N/n, чтобы искать со значением задержки по умолчанию (0.5 сек.)]'))

				proxy_timeout = bombshot.colored_input()

				if proxy_timeout == '.':
					bombshot.print_full_main_screen()

				elif proxy_timeout == '0':
					bombshot.exiting_program()

				elif proxy_timeout == 'N' or proxy_timeout == 'n':
					bombshot.get_proxies(int(next_input), 0.5)

				elif isinstance(float(proxy_timeout), float) or isinstance(int(proxy_timeout), int):

					if 0.1 <= float(proxy_timeout) <= 10.0:

						bombshot.get_proxies(int(next_input), float(proxy_timeout))
					else:
						bombshot.print_full_main_screen()
						print(bombshot.error_output('[ОШИБКА]: Неверное значение задержки прокси'))

				else:
					bombshot.exiting_program_error('Опция не найдена.')
			else:
				bombshot.print_full_main_screen()
				print(bombshot.error_output('[ОШИБКА]: Неверное значение количества прокси'))

		else:
			bombshot.exiting_program_error('Опция не найдена.')

	def print_phone_input_screen():
		bombshot.clear()
		print('Введите номер телефона (только российские номера),\nначиная с 7 или 8:')

		print(bombshot.go_back())
		print(bombshot.zero_to_exit())

		phone_n = bombshot.colored_input()

		if phone_n == '.':
			bombshot.print_full_main_screen()

		elif phone_n == '0':
			bombshot.exiting_program()

		else:

			if bombshot.to7(phone_n):
				# fixed phone
				fixed_phone = bombshot.to7(phone_n)

				bombshot.clear()
				print(bombshot.warning_output('Введите количество циклов:'))
				print(bombshot.go_back())
				print(bombshot.zero_to_exit())

				cycles_cnt = bombshot.colored_input()

				if cycles_cnt == '.':
					bombshot.print_phone_input_screen()
				elif cycles_cnt == '0':
					bombshot.exiting_program()
				elif cycles_cnt.isdigit():

					creds = bombshot.generate_credentials()

					name = creds[0]
					surname = creds[1]
					patronymic = creds[2]
					latin_name = creds[3]
					email = creds[4]
					password = creds[5]

					ua = UserAgent()
					useragent = ua.random
					proxy = ''

					cycles_cnt = int(cycles_cnt)

					bombshot.clear()
					print(bombshot.warning_output('С прокси или без?\n1 - с прокси\n2 - без прокси'))
					print(bombshot.go_back())
					print(bombshot.zero_to_exit())

					proxy_option = bombshot.colored_input()

					process_phrases = ['[БУМБАСИРУЕМ...]', '[ПЕРЕЕЗЖАЕМ БУМБАТРАКТОРОМ...]',
										'[ЗАСТАВЛЯЕМ ЖРАТЬ БУМБАСЯТИНУ...]', '[НАЧИНАЕМ БУМБАСИРОВКУ...]']	

					# with proxy
					if bombshot.is_non_zero_file(os.getcwd() + '/proxy_list.txt') and proxy_option == '1':
						lines = list(open('proxy_list.txt', 'r'))
						proxies = []

						for i in lines:
							proxies.append(i.replace('\n', ''))

						# proxies = {'http': "http://{}".format(proxy), 'https':"http://{}".format(proxy)}

						print(bcolors.WARNING + random.choice(process_phrases) 
							+ ': {} ({} циклов * {} прокси) раз на {}'.format(bcolors.FAIL + str(cycles_cnt * len(proxies)) + bcolors.WARNING,
							bcolors.FAIL + str(cycles_cnt) + bcolors.WARNING, bcolors.FAIL + str(len(proxies)) + bcolors.WARNING, 
							bcolors.FAIL + fixed_phone))
						print(bcolors.WARNING + '(может потребоваться время, чтобы смс начали приходить)')

						print(bcolors.WARNING + '[Ctrl + Z - Выход из программы]')

						for i in range(cycles_cnt):

							for z in proxies:
								proxies = {'http': "http://{}".format(z), 'https':"http://{}".format(z)}

								Thread(apis_services.send_sms(fixed_phone, name, surname, patronymic, latin_name, email, password, useragent, i, z, proxy)).start()
								time.sleep(5)

								if i == cycles_cnt and z == proxies:
									break
									bombshot.print_full_main_screen(bombshot.warning_output('[Отправлено {} циклов с {} прокси на телефон {}]').format(bcolors.FAIL + str(cycles_cnt * len(proxies)) + bcolors.WARNING, bcolors.FAIL + str(z) + bcolors.WARNING, bcolors.FAIL + fixed_phone + bcolors.WARNING))

					elif not bombshot.is_non_zero_file(os.getcwd() + '/proxy_list.txt') and proxy_option == '1':
						bombshot.clear()
						bombshot.print_full_main_screen()
						print(bombshot.exiting_program_error('Прокси отсутствуют в proxy_list.txt'))

					elif proxy_option == '2':

						print(bcolors.WARNING + random.choice(process_phrases) + ': {} циклов на {}'.format(bcolors.FAIL + str(cycles_cnt) + bcolors.WARNING, bcolors.FAIL + fixed_phone) + bcolors.WARNING + '\n(может потребоваться время, чтобы смс начали приходить)')
						print(bcolors.WARNING + '[Ctrl + Z - Выход из программы]')


						for i in range(cycles_cnt):

							Thread(apis_services.send_sms(fixed_phone, name, surname, patronymic, latin_name, email, password, useragent)).start()
							time.sleep(5)
							
							if i == cycles_cnt:
								break
								bombshot.print_full_main_screen(bombshot.warning_output('[Отправлено {} циклов на телефон {}]').format(bcolors.FAIL + str(cycles_cnt) + bcolors.WARNING, bcolors.FAIL + fixed_phone + bcolors.WARNING))

					elif proxy_option == '.':
						bombshot.print_phone_input_screen()

					elif proxy_option == '0':
						bombshot.exiting_program()

					# without proxy
					else:
						bombshot.print_full_main_screen()
						print(bombshot.error_output('[ОШИБКА]: Опция не найдена.'))
						

			else:				
				bombshot.clear()
				print(bombshot.error_output('[ОШИБКА]: Неверный формат номера.'))
				bombshot.print_full_main_screen()
						
	def print_full_main_screen(extra_message = None):
		bombshot.clear()
		bombshot.logo()
		bombshot.count_services()

		if extra_message is not None:
			print(extra_message)

		bombshot.main_screen()

	def clear_txt_file():

		if bombshot.is_non_zero_file(os.getcwd() + '/proxy_list.txt'):

			bombshot.clear()
			print(bombshot.warning_output('Вы уверены что хотите удалить содержимое proxy_list.txt?\nЭто действие необратимо.'))
			print(bcolors.FAIL + '1' + bcolors.WARNING + ' - Да')
			print(bcolors.FAIL + '2' + bcolors.WARNING + ' - Нет')

			print(bombshot.go_back())
			print(bombshot.zero_to_exit())

			user_option = bombshot.colored_input()

			if user_option == '.':
				bombshot.print_full_main_screen()

			elif user_option == '0':
				bombshot.exiting_program()

			elif user_option == '1' and bombshot.is_non_zero_file(os.getcwd() + '/proxy_list.txt'):

				proxies = []

				with open('proxy_list.txt', 'r') as infl:
					for i in infl:
						proxies.append(i.replace('\n', ''))

				proxies_cnt = len(proxies)
				proxies = []

				f = open('proxy_list.txt', 'w')
				bombshot.print_full_main_screen()

			elif user_option == '1' and not bombshot.is_non_zero_file(os.getcwd() + '/proxy_list.txt'):
				bombshot.print_full_main_screen(bcolors.FAIL + '[ОШИБКА]: proxy_list.txt уже пуст.')

			elif user_option == '2':
				bombshot.print_full_main_screen()

		else:
			bombshot.print_full_main_screen(bcolors.FAIL + '[ОШИБКА]: proxy_list.txt уже пуст.')



	def main_screen():
		print(bcolors.OKGREEN + 'Выберите опцию:\n' + bcolors.FAIL +
			'1 - Ввести номер телефона\n' + bcolors.WARNING +
			'2 - Сгенерировать случайные данные\n' +
			'3 - Парсинг прокси\n' +
			'4 - Перемешать прокси в списке\n' + bcolors.OKCYAN +
			'd - Очистить файл с прокси\n' + bcolors.FAIL + 
			'0 - Выход')
		
		if not bombshot.is_non_zero_file(os.getcwd() + '/proxy_list.txt'):
			print(bombshot.warning_output('[ПРЕДУПРЕЖДЕНИЕ]: Файл с прокси пуст, все запросы\nбудут происходить с вашего IP, что потенциально\nможет привести к его блокировке на некоторых сайтах.\nДля парсинга прокси введите ' + bcolors.FAIL + '5'))
		else:
			i = 0
			with open('proxy_list.txt', 'r') as infl:
				for line in infl:
					i += 1

			print(bcolors.WARNING +'[Загружено ' + bcolors.FAIL + f'{i}' + bcolors.WARNING + ' прокси в proxy_list.txt]')

		user_option = bombshot.colored_input()

		if user_option == '1':
			bombshot.print_phone_input_screen()

		elif user_option == '2':
			bombshot.random_name_generator()

		elif user_option == '3':
			bombshot.print_proxy_screen()

		elif user_option == '4':
			bombshot.shuffle_proxies()

		elif user_option == 'd':
			bombshot.clear_txt_file()

		elif user_option == '0':
			print(bombshot.exiting_program())
			exit()
		else:
			bombshot.exiting_program_error('Опция не найдена.')

if __name__ == '__main__':
	bombshot.print_full_main_screen()
