# BOMBSHOT CLI v3.0
# Licensed under Mozilla Public License 2.0

# by boumer7

import os

import time
import random
import json

# for multithreaded cycles
import threading
from threading import Thread

# transliteration module with a lot of transliteration standards
import iuliia
# module for getting proxies
import proxyscrape
import urllib.request

from fake_useragent import UserAgent
from pathlib import Path

# file with services' APIs
import apis_services
from configparser import ConfigParser

# for colorful text in terminal
from colorama import init
from colorama import Fore, Back, Style

# reset string color specs prior to the new string
init(autoreset=True)

# I prefer not using self.

# settings class
class sets:

	def settings_screen():
		bs.clear()

		print(
			bs.warning_o(bsl["SETTINGS"]["MAIN"]) + 
			bs.warning_o(bsl["SETTINGS"]["CHANGE_LANGUAGE"]) +
			bs.warning_o(bsl["SETTINGS"]["CHANGE_REGION"])
		)

		print(bs.go_back())
		print(bs.zero_to_exit())

		next_input = bs.colored_i()

		if next_input == '.':
			bs.print_full_main_screen()

		elif next_input == '0':
			bs.exiting_program_on_purpose()

		elif next_input == '1':
			sets.change_language()

		elif next_input == '2':
			sets.change_phone_region()

		else:
			bs.print_full_main_screen(bs.exiting_program())

	def change_phone_region():
		bs.clear()
		print(bs.warning_o(bsl["SETTINGS"]["REGION"]["MAIN"]) +
		bs.warning_o(bsl["SETTINGS"]["REGION"]["RU"]) +
		bs.warning_o(bsl["SETTINGS"]["REGION"]["UA"])
		)

		print(bs.go_back())
		print(bs.zero_to_exit())

		next_input = bs.colored_i()

		cfg_lang = ''

		if next_input == '.':
			sets.settings_screen()

		elif next_input == '0':
			bs.exiting_program_on_purpose()

		else:
			bs.print_full_main_screen(bs.warning_ob(bsl["SETTINGS"]["REGION"]["WARN"]))

	def change_language():

		bs.clear()
		print(bs.warning_o(bsl["GENERAL"]["CHANGE_LANGUAGE"]))
		print(bs.go_back())
		print(bs.zero_to_exit())

		next_input = bs.colored_i()

		cfg_lang = ''

		if next_input == '.':
			sets.settings_screen()

		elif next_input == '0':
			bs.exiting_program_on_purpose()

		elif next_input.lower() in ('ru', 'ua', 'en'):
			cfg_lang = next_input
			bs.load_lang(cfg_lang.lower())

		else:
			cfg_lang = 'EN'
			bs.load_lang(cfg_lang.lower(), True)


class bs:

	def load_lang(lang_remember = None, default = False):

		if not lang_remember:
			cwd = os.getcwd()
			cfg_path = cwd + '/cfg.ini'
			cfg_path = Path(cfg_path)

			if not os.path.exists(cfg_path):

				config_object = ConfigParser()

				config_object["USER"] = {
				"LANGUAGE": "EN"
				}

				with open('cfg.ini', 'w') as conf:
					config_object.write(conf)

			else:

				try:
					config = ConfigParser()
					config.read('cfg.ini')
				except Exception as e:
					bs.print_full_main_screen(e + ': ERROR READING CONFIG')

			cfg_lang = config['USER']['LANGUAGE']

			global bsl

			if cfg_lang == "RU":

				with open('lang/ru_lang.json', encoding='utf-8') as f:
					bsl = json.load(f)

			elif cfg_lang == "UA":

				with open('lang/ua_lang.json', encoding='utf-8') as f:
					bsl = json.load(f)

			else:

				with open('lang/en_lang.json', encoding='utf-8') as f:
					bsl = json.load(f)

		else:

			if not default:

				with open(f'lang/{lang_remember}_lang.json', encoding='utf-8') as f:
					bsl = json.load(f)

				cwd = os.getcwd()
				cfg_path = cwd + '/cfg.ini'
				cfg_path = Path(cfg_path)

				parser = ConfigParser()
				parser.read(cfg_path)
				parser.set('USER', 'language', lang_remember.upper())

				with open(cfg_path, "w") as f:
					parser.write(f)

				bs.print_full_main_screen(bs.success_o(bsl["GENERAL"]["CHANGED_LANG"]))

			else:

				with open(f'lang/en_lang.json') as f:
					bsl = json.load(f, encoding='utf-8')

				cwd = os.getcwd()
				cfg_path = cwd + '/cfg.ini'
				cfg_path = Path(cfg_path)

				parser = ConfigParser()
				parser.read(cfg_path)
				parser.set('USER', 'language', lang_remember.upper())

				with open(cfg_path, "w") as f:
					parser.write(f)

				bs.print_full_main_screen(bs.error_o(bsl["ERRORS"]["LANGUAGE_NOT_FOUND"]))

		return bsl

	# Functions for easy colorful outputs

	def colored_i():
		u_input = input(bs.okcyan_o(bsl["GENERAL"]["INPUT"] + ' >> '))
		return u_input

	def error_o(text = None):
		return Fore.WHITE + Back.RED  + text

	def red_o(text = None):
		return Fore.RED + text

	def warning_o(text = None):
		return Fore.YELLOW + text

	def warning_ob(text = None):
		return Back.YELLOW + Fore.BLACK + text

	def okcyan_o(text = None):
		return Fore.CYAN + text

	def okgreen_o(text = None):
		return Fore.GREEN + text

	def success_o(text = None):
		return Back.GREEN + Fore.WHITE + text

	def exiting_program_on_purpose():
		bs.clear()
		print(bs.warning_o(bsl["GENERAL"]["EXIT_PRG_WARN"]))
		exit()

	def exiting_program(text = None):
		bs.clear()
		print(bs.warning_o(bsl["GENERAL"]["EXITING_OPT_NOT_FOUND"]))
		exit()

	def exiting_program_error(text = None):
		print(bs.error_o(bsl["GENERAL"]["ERROR"] + str(text) + bsl["GENERAL"]["EXITING_PRG"]))
		exit()

	def clear():
		os.system('cls' if os.name == 'nt' else 'clear')

	def logo():
		logo = (bs.red_o('BOMBSHOT v3.0-beta 💣 ') 
			+ bs.okcyan_o('| BY BOUMER7\n'))
		print(logo, end='')
		print(bs.okgreen_o(bsl["GENERAL"]["PENTEST_TOOL"]))

	# Checks whether a file has content (True) and not (False)
	# https://stackoverflow.com/a/15924160
	def is_non_zero_file(fpath):
		fpath = Path(fpath)
		try:
			return os.path.isfile(fpath) and os.path.getsize(fpath) > 0
		except OSError as e:
			return e

	# Checks proxy for connection with provided timeout
	# https://stackoverflow.com/a/765436
	def is_bad_proxy(proxy, proxy_timeout = 0.5):
		ua = UserAgent() 

		try:
			proxy_handler = urllib.request.ProxyHandler({'http': proxy})
			opener = urllib.request.build_opener(proxy_handler)
			opener.addheaders = [('User-Agent', ua.random)]
			urllib.request.install_opener(opener)
			req = urllib.request.Request('http://proxyjudge.us/azenv.php')
			urllib.request.urlopen(req, timeout = proxy_timeout)

		except urllib.error.HTTPError:
			return True

		except Exception as detail:
			return True

		return False

	# Gets HTTP-proxies with proxyscrape library
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

		print(bs.warning_o(bsl["PROXY"]["FOUND"]), bs.red_o(str(len(proxies))), 
			bs.warning_o(bsl["PROXY"]["HTTP_PROXIES"]))

		print(bs.warning_o(bsl["PROXY"]["PERFORMANCE_CHECK"]))
		print(bs.warning_o(bsl["GENERAL"]["CTRL_Z_EXIT"]))


		time.sleep(1)
		bs.clear()
		start_time = time.time()

		cnt = 0

		print(bs.warning_o(bsl["PROXY"]["CHECKED"]) + bs.red_o(' 0 ') 
			+ bs.warning_o(bsl["PROXY"]["OUT_OF"]), 
			bs.red_o(str(len(proxies))), bs.warning_o(bsl["PROXY"]["PROXIES_WITH_TIMEOUT"]), 
			bs.red_o(str(proxy_timeout)), bs.warning_o(bsl["PROXY"]["SECONDS_3"]))

		print(bs.warning_o(bsl["PROXY"]["CHOSEN"]), bs.red_o(str(cnt)),
			bs.warning_o(bsl["PROXY"]["OUT_OF"]), 
			bs.red_o(str(desired_amount)), bs.warning_o(bsl["PROXY"]["PROXIES_WITH_TIMEOUT"]), 
			bs.red_o(str(proxy_timeout)), bs.warning_o(bsl["PROXY"]["SECONDS_3"]))

		print(bs.warning_o(bsl["GENERAL"]["CTRL_Z_EXIT"]))

		checked_proxy = []
		
		for ind, item in enumerate(proxies, start = 1):

			if cnt < desired_amount:

				if bs.is_bad_proxy(item, proxy_timeout):
					print('[BAD PROXY]')
				else:
					checked_proxy.append(item) 
					cnt += 1
			else:
				break


			bs.clear()

			print(bs.warning_o(bsl["PROXY"]["CHECKED"]), bs.red_o(str(ind)),
			bs.warning_o(bsl["PROXY"]["OUT_OF"]), 
			bs.red_o(str(len(proxies))), bs.warning_o(bsl["PROXY"]["PROXIES_WITH_TIMEOUT"]), 
			bs.red_o(str(proxy_timeout)), bs.warning_o(bsl["PROXY"]["SECONDS_3"]))

			print(bs.warning_o(bsl["PROXY"]["CHOSEN"]), bs.okgreen_o(str(cnt)),
			bs.warning_o(bsl["PROXY"]["OUT_OF"]), 
			bs.red_o(str(desired_amount)), bs.warning_o(bsl["PROXY"]["PROXIES_WITH_TIMEOUT"]), 
			bs.red_o(str(proxy_timeout)), bs.warning_o(bsl["PROXY"]["SECONDS_3"]))

			print(bs.warning_o(bsl["PROXY"]["EXIT_WARN"]))
			print(bs.warning_o(bsl["GENERAL"]["CTRL_Z_EXIT"]))


		end_time = time.time()

		extra_message = (bsl["PROXY"]["APPENDED"], str(cnt), 
			bsl["PROXY"]["PROXIES_WITH_TIMEOUT"], str(proxy_timeout), 
			bsl["PROXY"]["SECONDS_1"], bsl["PROXY"]["TO_THE_PROXY_LIST"], bsl["PROXY"]["IN"],
			str(round(end_time - start_time, 2)), bsl["PROXY"]["SECONDS_1"] + ']')

		extra_message = bs.success_o(' '.join(x for x in extra_message))

		with open('proxy_list.txt', 'a') as infl:
			for item in checked_proxy:
				infl.write(''.join(item) + '\n')

		bs.print_full_main_screen(extra_message)

	# Standartizes phone format to 7 (RU)
	def to7(phone):
		phone = str(phone)

		# RU phone standartization
		if len(phone) == 11:
			if phone[0] in ('7', '8'):
				if phone[0] == '8':
					phone = '7' + phone[1:]
				return phone
		else:
			return False

	# Generates random credentials for automated requests (CIS region vocabularies)
	def generate_credentials():

		vocabulary = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

		name_vocabulary = [
		'Павел', 'Михаил', 'Иван', 'Матвей', 'Игорь', 'Владимир',
		'Михаил', 'Георгий', 'Савелий', 'Никита', 'Александр', 
		'Алексей', 'Роман', 'Марк', 'Макар', 'Егор', 'Тихон',
		'Андрей', 'Родион', 'Максим', 'Даниил', 'Кирилл', 'Лев', 
		'Тимофей', 'Степан'
		]

		surname_vocabulary = [
		'Смирнов', 'Яковлев', 'Воробьев', 'Фомин', 'Миронов',
		'Капустин', 'Соболев', 'Захаров', 'Акимов', 'Кравцов',
		'Алексеев', 'Александров', 'Романов', 'Бочаров', 'Павлов',
		'Новиков', 'Афанасьев', 'Колосов', 'Антонов', 'Денисов',
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

		# using yandex maps transliteration schema as default
		yandex_maps = iuliia.Schemas.get("yandex_maps")

		name = random.choice(name_vocabulary)
		latin_name = iuliia.translate(name, schema = yandex_maps)

		surname = random.choice(surname_vocabulary)
		latin_surname = iuliia.translate(surname, schema = yandex_maps)

		patronymic = random.choice(patronymic_vocabulary)

		email_value = latin_name.lower() + rand_sep + latin_surname.lower() + str(rand_end)

		email = "{}@{}".format(email_value, random.choice(email_vocabulary))

		return name, surname, patronymic, latin_name, email, password

	# Functions that return most common phrases
	def update_value():
		return bs.okcyan_o(bsl["GENERAL"]["UPDATE_VALUES"])

	def zero_to_exit():
		return bs.red_o(bsl["GENERAL"]["ZERO_TO_EXIT"])

	def go_back():
		return bs.okgreen_o(bsl["GENERAL"]["GO_BACK"])

	# Main menu section for credentials randomization
	def random_name_generator():
		bs.clear()
		creds = bs.generate_credentials()
		name_in_cyrllic = (bsl["RND_GEN"]["NAME_IN_CYRILLIC"], creds[1], creds[0], creds[2])
		name_in_cyrllic = ' '.join(x for x in name_in_cyrllic)
		name_in_cyrllic = bs.warning_o(name_in_cyrllic)

		latin_full_name = creds[1] + ' ' + creds[0] + ' ' + creds[2]

		yandex_maps = iuliia.Schemas.get("yandex_maps")

		print(bs.warning_o(bsl["RND_GEN"]["NAME_IN_LATIN"]), 
			bs.warning_o(iuliia.translate(latin_full_name, schema = yandex_maps)))

		print(bs.warning_o(bsl["RND_GEN"]["E-MAIL"]), bs.warning_o(creds[4]))
		print(bs.warning_o(bsl["RND_GEN"]["PASSWORD"]), bs.warning_o(creds[5]))

		print(bs.go_back())
		print(bs.update_value())
		print(bs.zero_to_exit())

		next_input = bs.colored_i()

		if next_input == '.':
			bs.clear()
			bs.print_full_main_screen()

		elif next_input == '0':
			print(bs.option_not_found())
			exit()

		elif next_input == ',':
			bs.random_name_generator()

		else:
			bs.exiting_program()

	# Shuffles proxies in the proxy_list.txt
	def shuffle_proxies():

		colors = [
			Back.RED, Back.YELLOW, 
			Back.BLUE, Back.CYAN, 
			Back.WHITE
		]

		random.shuffle(colors)

		c1 = random.choice(colors)
		c2 = random.choice(colors)
		c3 = random.choice(colors)

		while c2 == c1 or c1 == c3 or c2 == c3:
			c1 = random.choice(colors)
			c2 = random.choice(colors)
			c3 = random.choice(colors)

		if bs.is_non_zero_file(os.getcwd() + '/proxy_list.txt'):

			proxies = []
			with open('proxy_list.txt', 'r') as infl:
				for i in infl:
					proxies.append(i.replace('\n', ''))

			random.shuffle(proxies)

			with open('proxy_list.txt', 'w') as infl:
				for i in proxies:
					infl.write(i + '\n')

			prx_len = str(len(proxies))

			bs.print_full_main_screen(

				bs.success_o(bsl["PROXY"]["SHUFFLE_SUCCESS"].format(prx_len))
				+ f'{c1}  {c2}  {c3}  '

			)
		else:
			bs.print_full_main_screen(bs.error_o(bsl["ERRORS"]["PROXY_LIST_EMPTY_ERR"])
				+ f'{c1}  {c2}  {c3}  '
				)

	def count_services():
		apis_file = open('apis_services.py', encoding='utf-8')
		apis_content = apis_file.read()

		services_count = apis_content.count('requests.post') + apis_content.count('requests.get')
		print(bs.warning_o(bsl["GENERAL"]["SERVICES"]), str(bs.red_o(str(services_count))))

	# Main menu proxy screen
	def print_proxy_screen():
		bs.clear()
		print(bs.warning_o(bsl["PROXY"]["PROXY_AMNT_INPUT"]))
		print(bs.go_back())
		print(bs.zero_to_exit())

		next_input = bs.colored_i()

		if next_input == '.':
			bs.print_full_main_screen()

		elif next_input == '0':
			bs.exiting_program_on_purpose()

		elif next_input.isdigit():

			if 1 <= int(next_input) <= 1000:
				bs.clear()
				print(bs.warning_o(bsl["PROXY"]["PROXY_TIMEOUT_INPUT"]))
				print(bs.go_back())
				print(bs.zero_to_exit())
				print(bs.warning_o(bsl["PROXY"]["PROXY_TIMEOUT_DEFAULT_INPUT"]))

				proxy_timeout = bs.colored_i()

				if proxy_timeout == '.':
					bs.print_full_main_screen()

				elif proxy_timeout == '0':
					bs.exiting_program_on_purpose()

				elif proxy_timeout == 'N' or proxy_timeout == 'n':
					bs.get_proxies(int(next_input), 0.5)

				elif isinstance(float(proxy_timeout), float) or isinstance(int(proxy_timeout), int):

					if 0.1 <= float(proxy_timeout) <= 10.0:

						bs.get_proxies(int(next_input), float(proxy_timeout))
					else:
						bs.print_full_main_screen()
						print(bs.error_o(bsl["ERRORS"]["PROXY_TIMEOUT_INPUT_ERR"]))

				else:
					bs.exiting_program_error(bsl["GENERAL"]["EXITING_OPT_NOT_FOUND"])
			else:
				bs.print_full_main_screen()
				print(bs.error_o(bsl["ERRORS"]["PROXY_AMNT_INPUT_ERR"]))

		else:
			bs.exiting_program()

	# Main menu phone input screen
	def print_phone_input_screen():
		bs.clear()

		print(bs.warning_o(bsl["SEND_SMS_PROMPT"]["PHONE_NUM_INPUT"]))

		print(bs.go_back())
		print(bs.zero_to_exit())

		phone_n = bs.colored_i()

		if phone_n == '.':
			bs.print_full_main_screen()

		elif phone_n == '0':
			bs.exiting_program_on_purpose()

		else:

			if bs.to7(phone_n):
				# fixed phone
				fixed_phone = bs.to7(phone_n)

				bs.clear()
				print(bs.warning_o(bsl["SEND_SMS_PROMPT"]["SMS_TIMES_INPUT"]))
				print(bs.go_back())
				print(bs.zero_to_exit())

				cycles_cnt = bs.colored_i()

				if cycles_cnt == '.':
					bs.print_phone_input_screen()
				elif cycles_cnt == '0':
					bs.exiting_program_on_purpose()
				elif cycles_cnt.isdigit():

					creds = bs.generate_credentials()

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

					bs.clear()
					print(bs.warning_o(bsl["SEND_SMS_PROMPT"]["WHETHER_PROXY_INPUT"]))
					print(bs.go_back())
					print(bs.zero_to_exit())

					proxy_option = bs.colored_i()

					# with proxy
					if bs.is_non_zero_file(os.getcwd() + '/proxy_list.txt') and proxy_option == '1':
						lines = list(open('proxy_list.txt', 'r'))
						proxies = []

						for i in lines:
							proxies.append(i.replace('\n', ''))

						# proxies = {'http': "http://{}".format(proxy), 'https':"http://{}".format(proxy)}

						print(bs.warning_o(bsl["SEND_SMS_PROMPT"]["SMS_SENDING"]),
							bs.warning_o(bsl["SEND_SMS_PROMPT"]["SMS_TIMES_AND_TO"]).format(
								bs.red_o(str(cycles_cnt)), bs.red_o(fixed_phone)))

						print(bs.warning_o(bsl["SEND_SMS_PROMPT"]["SMS_TIME_WARN"]))

						print(bs.warning_o(bsl["GENERAL"]["CTRL_Z_EXIT"]))

						for i in range(cycles_cnt):

							for z in proxies:
								proxies = {'http': "http://{}".format(z), 'https':"http://{}".format(z)}

								apis_services.send_sms(fixed_phone, name, surname, patronymic, latin_name, email, password, useragent, i, z, proxy)
								time.sleep(2)

								if i == cycles_cnt and z == proxies:
									break
									bs.print_full_main_screen(bs.success_o(bsl["SEND_SMS_PROMPT"]["PROXY_SMS_TIMES_SENT"]).format(str(cycles_cnt), str(z), fixed_phone))

					elif not bs.is_non_zero_file(os.getcwd() + '/proxy_list.txt') and proxy_option == '1':
						bs.clear()
						bs.print_full_main_screen()
						print(bs.print_full_main_screen(bs.red_o(bsl["ERRORS"]["PROXY_LIST_EMPTY_ERR"])))

					elif proxy_option == '2':

						print(bs.warning_o(bsl["SEND_SMS_PROMPT"]["SMS_SENDING"] + ':'),
							bs.warning_o(bsl["SEND_SMS_PROMPT"]["SMS_TIMES_AND_TO"]).format(
								bs.red_o(str(cycles_cnt)), bs.red_o(fixed_phone)))

						print(bs.warning_o(bsl["SEND_SMS_PROMPT"]["SMS_TIME_WARN"]))

						print(bs.warning_o(bsl["GENERAL"]["CTRL_Z_EXIT"]))


						for i in range(cycles_cnt):

							apis_services.send_sms(fixed_phone, name, surname, patronymic, latin_name, email, password, useragent)
							time.sleep(5)
							
							if i == cycles_cnt:
								break
								bs.print_full_main_screen(bs.warning_o(bsl["SEND_SMS_PROMPT"]["SMS_TIMES_SENT"]).format(str(cycles_cnt), fixed_phone))

					elif proxy_option == '.':
						bs.print_phone_input_screen()

					elif proxy_option == '0':
						bs.exiting_program_on_purpose()

					# without proxy
					else:
						bs.print_full_main_screen()
						print(bs.exiting_program())
						

			else:				
				bs.clear()
				bs.print_full_main_screen(
				bs.error_o(bsl["ERRORS"]["PHONE_FORMAT_ERR"]))
	
	# Glues all functions for main menu display						
	def print_full_main_screen(extra_message = None):
		bs.clear()
		bs.logo()
		bs.count_services()

		if extra_message:
			print(extra_message)

		bs.main_screen()

	# Clears the proxy_list.txt
	def clear_txt_file():

		if bs.is_non_zero_file(os.getcwd() + '/proxy_list.txt'):

			bs.clear()
			print(bs.warning_o(bsl["PROXY_LIST_CLEAR_PROMPT"]["PROXY_LIST_CLEAR_WARN"]))
			print(bs.warning_o(bsl["PROXY_LIST_CLEAR_PROMPT"]["1_TO_YES"]))
			print(bs.warning_o(bsl["PROXY_LIST_CLEAR_PROMPT"]["2_TO_NO"]))

			print(bs.go_back())
			print(bs.zero_to_exit())

			user_option = bs.colored_i()

			if user_option == '.':
				bs.print_full_main_screen()

			elif user_option == '0':
				bs.exiting_program_on_purpose()

			elif user_option == '1' and bs.is_non_zero_file(os.getcwd() + '/proxy_list.txt'):

				proxies = []

				with open('proxy_list.txt', 'r') as infl:
					for i in infl:
						proxies.append(i.replace('\n', ''))

				proxies_cnt = len(proxies)
				proxies = []

				f = open('proxy_list.txt', 'w')
				bs.print_full_main_screen()

			elif user_option == '1' and not bs.is_non_zero_file(os.getcwd() + '/proxy_list.txt'):
				bs.print_full_main_screen(bs.error_o(bsl["ERRORS"]["PROXY_LIST_ALRDY_EMPTY_ERR"]))

			elif user_option == '2':
				bs.print_full_main_screen()

		else:
			bs.print_full_main_screen(bs.error_o(bsl["ERRORS"]["PROXY_LIST_ALRDY_EMPTY_ERR"]))


	# Main menu
	def main_screen():
		print(
			bs.red_o(bsl["MAIN_MENU"]["1_TO_PHONE_NUM"]) + 
			bs.warning_o(bsl["MAIN_MENU"]["2_TO_GENERATE_RANDOM_DATA"]) +
			bs.warning_o(bsl["MAIN_MENU"]["3_TO_PARSE_PROXIES"]) +
			bs.warning_o(bsl["MAIN_MENU"]["4_TO_SHUFFLE_PROXY_LIST"]) +
			bs.okcyan_o(bsl["MAIN_MENU"]["5_TO_ENTER_SETTINGS"]) +
			bs.warning_o(bsl["MAIN_MENU"]["D_TO_CLEAR_PROXY_LIST"]) +
			bs.red_o(bsl["MAIN_MENU"]["0_TO_EXIT"])
			)
		
		if not bs.is_non_zero_file(os.getcwd() + '/proxy_list.txt'):
			print(bs.warning_o(bsl["MAIN_MENU"]["PROXY_LIST_EMPTY_WARN"]))
		else:
			i = 0
			with open('proxy_list.txt', 'r') as infl:
				for line in infl:
					i += 1

			print(bs.okgreen_o(bsl["PROXY"]["LOADED_PROXIES"].format(str(i))))
			
		user_option = bs.colored_i()

		if user_option == '1':
			bs.print_phone_input_screen()

		elif user_option == '2':
			bs.random_name_generator()

		elif user_option == '3':
			bs.print_proxy_screen()

		elif user_option == '4':
			bs.shuffle_proxies()

		elif user_option == '5':
			sets.settings_screen()

		elif user_option == 'd' or user_option == 'D':
			bs.clear_txt_file()

		elif user_option == '0':
			print(bs.exiting_program_on_purpose())
			exit()
		else:
			bs.exiting_program_error(bs.exiting_program())

if __name__ == '__main__':
	# loads lang !IMPORTANT
	bs.load_lang()
	# loads main screen !IMPORTANT
	bs.print_full_main_screen()
