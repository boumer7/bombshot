# BOMBSHOT v1.0 💣
— мощный, но работающий через раз СМС-бомбер с:

- Удобным интерфейсом
- Многопоточностью циклов
- Парсингом прокси и их сохранением
- Проверкой прокси на соединение

> Разработчик не несёт отвественность за урон, нанесённый этим ПО. Вы несёте полную отвественность за свои действия. Скачивая и используя ПО из этого репозитория, вы соглашаетесь с лицензией [Mozilla Public License 2.0](https://github.com/boumer7/bombshot/blob/main/LICENSE).

Проект был создан в целях пентеста (испытания на проникновение). Этот проект даёт возможность симуляции атаки СМС-флудинга, главным принципом которой является массовая рассылка спам-сообщений но номер жертвы при помощи ПО. В последнее время СМС-бомберы получили широкое распространение в хакерских кругах, что делает проблему защиты от подобных атак актуальной. Реалии текущего российского законадательства делают процесс поимки и обвинения подобных злоумышленников, рассылающих СМС-спам на номер жертвы, слишком сложным и затратным как по времени, так и материально. 

Единственным решением в данной ситуации остаётся защищаться от действий злоумышленника самостоятельно. В большинстве современных смартфонах присутствуют встроенные средства по предотвращению СМС-спама, однако они не всегда справляются со своей работой эффективно. Для повышения эффективности работы анти-спам фильтров требуется их применение на практике: в реальных условиях атаки или приближённых к реальным условиям атаки. BOMBSHOT v1.0 даёт возможность пользователю выступить в роли злоумышленника, отправляя сообщения при помощи ПО на номер жертвы, в его случае — на свой номер. Таким образом, пользователь, находясь в симуляции атаки, может настроить своё Анти-спам ПО наилучшим образом для предотвращения смс-рассылок в будущем.

# Установка
## Termux/Unix-подобные ОС:
<h3> 1. Для начала работы вам потребуется установить Python и Git: </h3>

```console
apt install python git
```
Это может занять некоторое время, если вас будут спрашивать разрешение на установку, то вводите **Y**.

<h3> 2. Далее вам нужно клонировать этот репозиторий. </h3>

```console
git clone https://github.com/boumer7/bombshot
```
Вас попросят авторизоваться через GitHub: вам нужно ввести свой логин, а потом пароль.

Переместитесь в папку bombshot два раза:
<br/>

```console
cd bombshot
```
```console
cd bombshot
```
Вы должны находится примерно в такой директории:<br/> <br/>
![lVc2C5DzDrQ](https://user-images.githubusercontent.com/33152397/109676757-13091e00-7b8a-11eb-8dcf-0867d5fbd33b.jpg)<br/> <br/>
(если вы не создавали каких-либо папок до этого).

Если вы не уверены, что находитесь в нужной директории, то напишите:
```console
ls
```
Это команда выведет список всех файлов в текущей директории, среди которых должен быть **bombshot.py** <br/> <br/>
![5kya1omYnbM](https://user-images.githubusercontent.com/33152397/109676923-359b3700-7b8a-11eb-99d8-dcae6fa4e9c0.jpg) <br/> <br/>
Если вы видите **bombshot.py**, то вы находитесь в правильной директории.

<h3> 3. Установите соответствующие библиотеки: </h3>

```console
pip install -r requirements.txt
```
Если команда не сработала, то попробуйте:
```console
pip3 install -r requirements.txt
```

<h3> 4. Запуск: </h3>

```console
python bombshot.py
```
Если скрипт не запустился, то попробуйте вызвать его с **python3**:
```console
python3 bombshot.py
```

## Если что-то пошло не так, то вы можете завершить процесс
Вывести список всех процессов в Termux:
```console
ps
```

Завершить процесс, где число — его PID:
```console
kill число
```
Либо вы можете завершить текущую сессию в Termux вверху экрана, нажав на **EXIT**
![CKSSZu6WLT4](https://user-images.githubusercontent.com/33152397/109675005-71350180-7b88-11eb-9347-0cdfc4010844.jpg)

## Windows:
Установите [Python 3](https://www.python.org/).
<br/>
Установите [Github](https://git-scm.com/download/win).
<br/><br/>
Приготовьте любую папку, в которую вы будете клонировать репозиторий:
<br/><br/>
![1](https://user-images.githubusercontent.com/77790965/110011218-3c63ae80-7d30-11eb-8551-9bedbab61ac6.jpg)
<br/><br/>
Откройте Windows Powershell либо cmd (для Windows 7 и ниже):
<br/><br/>
![2](https://user-images.githubusercontent.com/77790965/110011802-e2afb400-7d30-11eb-9be6-376eaeb17767.jpg)
<br/><br/>
При помощи команд cd <название папки>, зайдите в вашу подготовленную директорию:
<br/><br/>
![3](https://user-images.githubusercontent.com/77790965/110012164-4f2ab300-7d31-11eb-8bd9-278ea1fb6932.jpg)
<br/><br/>
Если у вас возникают трудности при нахождении папки при помощи консоли, то вы можете навестись на путь и нажать левой кнопкой мыши по нему:
<br/><br/>
![4](https://user-images.githubusercontent.com/77790965/110012361-826d4200-7d31-11eb-8729-6f08a95deeed.jpg)
<br/><br/>
Далее вписать в нём **powershell** и нажмите Enter, у вас откроется консоль в текущей директории:
<br/><br/>
![5](https://user-images.githubusercontent.com/77790965/110012502-a16bd400-7d31-11eb-9dce-207b7ff81979.jpg)
<br/><br/>
Убедившись, что консоль открыта в нужной директории, напишите:
```console
git clone https://github.com/boumer7/bombshot
```
Переместитесь в папку bombshot:
```console 
cd bombshot
```
Теперь переместитесь в подпапку bombshot.
<br/><br/>
Если вы не уверены, что находитесь в правильной директории, то напишите:
```console
dir
```
Среди файлов должен быть **bombshot.py**, если вы его видите, то вы в верной директории.
<br/><br/>
Установите все требуемые библиотеки:
```console
pip install -r requirements.txt
```
Если эта команда не сработала, то попробуйте:
```console
pip3 install -r requirements.txt
```
После установки, вы сможете запустить скрипт:
```console
python bombshot.py
```
Если это не сработало, то попробуйте запустить скрпит с **python3**:
```console
python3 bombshot.py
```
<br/><br/>
Поздравляем, теперь вы можете использовать BOMBSHOT v1.0.<br/>
Удачных пентестов!

