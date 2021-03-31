# BOMBSHOT v3.0-beta 💣
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square)](https://python.org)
[![Qiwi](https://img.shields.io/badge/Qiwi-Поддержать-orange?style=flat-square&logo=qiwi&cacheSeconds=3600)](https://qiwi.com/n/BOUMER7)

— кроссплатформенный пентест-инструмент для симуляции атаки СМС-рассылок с:

- Удобным интерфейсом
- Парсингом прокси и их сохранением
- Проверкой прокси на соединение

### Установка: [Android/Linux](#termux-linux) | [Windows](#windows) | [IOS](#ios)

### [Рекомендации](#recom) | [Лицензия](https://github.com/boumer7/bombshot/blob/main/LICENSE) | [Положение об использовании ПО](https://github.com/boumer7/bombshot/blob/main/REGULATIONS.md)

<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/33152397/113221271-5e981000-928d-11eb-892c-2295d4f8cf34.png"/></kbd>
<p>Скриншот из консольной версии BOMBSHOT v3.0-beta</p>

## Дисклеймер / Письменный отказ от ответственности

Разработчик не несёт отвественности за урон, нанесённый этим ПО. Вы несёте полную отвественность за свои действия. Скачивая и используя ПО из этого репозитория, вы соглашаетесь с лицензией [Mozilla Public License 2.0](https://github.com/boumer7/bombshot/blob/main/LICENSE) и с [положением об использовании ПО](https://github.com/boumer7/bombshot/blob/main/REGULATIONS.md).

## Цель проекта

Проект был создан в целях пентеста (испытания на проникновение). Этот проект даёт возможность симуляции атаки СМС-флудинга, главным принципом которой является массовая рассылка спам-сообщений на номер жертвы при помощи ПО. В последнее время СМС-бомберы получили широкое распространение в хакерских кругах, что делает проблему защиты от подобных атак актуальной. Реалии текущего российского законадательства делают процесс поимки и обвинения подобных злоумышленников, рассылающих СМС-спам на номер жертвы, слишком сложным и затратным как по времени, так и материально. 

Единственным решением в данной ситуации остаётся защищаться от действий злоумышленника самостоятельно. В большинстве современных смартфонах присутствуют встроенные средства по предотвращению СМС-спама, однако они не всегда справляются со своей работой эффективно. Для повышения эффективности работы анти-спам фильтров требуется их применение на практике: в реальных условиях атаки или приближённых к реальным условиям атаки. BOMBSHOT даёт возможность пользователю выступить в роли злоумышленника, отправляя сообщения при помощи ПО на номер жертвы, в его случае — на свой номер. Таким образом, пользователь, находясь в симуляции атаки, может настроить своё Анти-спам ПО наилучшим образом для предотвращения смс-рассылок в будущем.

# Установка

<h2> <a name="termux-linux">Android (Termux) / Unix-подобные ОС:</a> </h2>

<h3> 1. Подготовка </h3>

### Android

Для начала вам понадобится установить приложение **Termux** в [Google Play](https://play.google.com/store/apps/details?id=com.termux&hl=en&gl=US). Root-права не требуются. Откройте его и перед вам появится консоль.

## [Termux в Google Play](https://play.google.com/store/apps/details?id=com.termux&hl=en&gl=US)

<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/33152397/110842898-beb41b80-82b8-11eb-96ce-19a92f7c229e.png"/></kbd>

### Linux

Откройте консоль комбинацией клавиш **Ctrl + Alt + T** либо мануально.

<h3> 2. Установка Python и Git: </h3>

В консоли введите следующие команды для установки **Python** и **Git**:

```console
apt install python git
```
Это может занять некоторое время, если вас будут спрашивать разрешение на установку, то вводите **Y**.

<h3> 3. Далее вам нужно клонировать этот репозиторий: </h3>

```console
git clone https://github.com/boumer7/bombshot
```
Вас попросят авторизоваться через GitHub: вам нужно ввести свой логин, а потом пароль.

Переместитесь в папку **bombshot** два раза:
<br/>

```console
cd bombshot
```
```console
cd bombshot
```
Вы должны находится примерно в такой директории:<br/> <br/>
<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/33152397/109676757-13091e00-7b8a-11eb-8dcf-0867d5fbd33b.jpg"/></kbd>
  <br/> <br/>
(если вы не создавали каких-либо папок до этого).

Если вы не уверены, что находитесь в нужной директории, то напишите:
```console
ls
```
Это команда выведет список всех файлов в текущей директории, среди которых должен быть **bombshot.py** <br/> <br/>
<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/33152397/109676923-359b3700-7b8a-11eb-99d8-dcae6fa4e9c0.jpg"/></kbd><br/> <br/>
Если вы видите **bombshot.py**, то вы находитесь в правильной директории.

<h3> 4. Установите соответствующие библиотеки: </h3>

```console
pip install -r requirements.txt
```
Если команда не сработала, то попробуйте:
```console
pip3 install -r requirements.txt
```
Примечание: Если на этом этапе библиотеки не установятся из-за остутствия pip, то отдельно установите менеджер пакетов **pip3**:
```console
apt install py3-pip
```
<h3> 5. Запуск: </h3>

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

Завершить процесс, где число — его **PID**:

```console
kill -9 число
```
<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/33152397/110849021-ca571080-82bf-11eb-9464-373f19436f14.png"/></kbd>

Либо вы можете завершить текущую сессию в **Termux** вверху экрана, нажав на **EXIT**:
<br/><br/>
<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/33152397/110862421-84567880-82d0-11eb-85c1-ddffdfde886e.png"/></kbd>

## Windows:
<h3> 1. Для начала работы вам потребуется установить Python и Git: </h3>

### Установите [Python 3](https://www.python.org/)

**[ВАЖНО]: При установке Python не забудьте поставить галочку на последний пункт**:
<br/><br/>
<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/33152397/110019165-2d352e80-7d39-11eb-98f5-4cf7614c577d.png"/></kbd>


### Установите [Github](https://git-scm.com/download/win)

(32/64-bit Git for Windows Setup). <br/>
При установке нажимайте далее со всеми рекомендуемыми галочками, если вы не желаете иного.
<br/>

<h3> 2. Подготовка директории: </h3>
Приготовьте любую папку, в которую вы будете клонировать репозиторий:
<br/><br/>

<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/77790965/110011218-3c63ae80-7d30-11eb-8551-9bedbab61ac6.jpg"/></kbd>
<br/><br/>

<h3> 3. Открытие консоли в нужной директории: </h3>

Рекомендуем использовать терминал [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701) для работы с ПО. Вы можете использовать любой другой терминал, но следует учесть, что некоторые символы могут отображаться некорректно.

<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/33152397/111032719-a9f19800-841e-11eb-8b80-9cf0289c9e2e.png"/></kbd>

Откройте **Windows Terminal**, **Windows Powershell** или **cmd**:

<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/77790965/110011802-e2afb400-7d30-11eb-9be6-376eaeb17767.jpg"/></kbd>
<br/><br/>

При помощи команд **cd *название папки***, перейдите в вашу подготовленную директорию:

<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/77790965/110012164-4f2ab300-7d31-11eb-8bd9-278ea1fb6932.jpg"/></kbd>
<br/><br/>

Если у вас возникают трудности при нахождении папки при помощи консоли, то вы можете навестись на путь и нажать левой кнопкой мыши по нему:
<br/>

<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/77790965/110012361-826d4200-7d31-11eb-8729-6f08a95deeed.jpg"/></kbd>
<br/><br/>

Далее вписать в нём **powershell** и нажать Enter. У вас откроется консоль в текущей директории:

<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/77790965/110012502-a16bd400-7d31-11eb-9dce-207b7ff81979.jpg"/></kbd>
<br/>

<h3> 4. Клонирование репозитории: </h3>

Убедившись, что консоль открыта в нужной директории, напишите:

```console
git clone https://github.com/boumer7/bombshot
```

Переместитесь в папку bombshot:
```console 
cd bombshot
```
Теперь переместитесь в подпапку bombshot:

```console 
cd bombshot
```

Если вы не уверены, что находитесь в правильной директории, то напишите:

```console
dir
```

Среди файлов должен быть **bombshot.py**, если вы его видите, то вы в верной директории.
<br/>
<h3> 5. Установка библиотек и запуск </h3>

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
Если это не сработало, то попробуйте запустить скрипт с **python3**:

```console
python3 bombshot.py
```

Поздравляем, теперь вы можете использовать BOMBSHOT.<br/>
**Удачных пентестов!**

## IOS
<h3> 1. Для начала работы вам потребуется установить iSH (>=IOS 11): </h3>

## [iSH в App Store](https://apps.apple.com/us/app/ish-shell/id1436902243)

<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/33152397/110845298-84984900-82bb-11eb-81a6-f11e6e7c8cd1.png"/></kbd>


<h3> 2. Откройте iSH и напиишите следующие команды: </h3>

Проверьте, установлен ли у вас менеджер пакетов **apk**:

```console
apk
```

Если после ввода этой команды у вас выводит ошибку, то напишите следующую команду для установки **apk**:

```console
wget -qO- http://dl-cdn.alpinelinux.org/alpine/v3.12/main/x86/apk-tools-static-2.10.5-r1.apk | tar -xz sbin/apk.static && ./sbin/apk.static add apk-tools && rm sbin/apk.static
```

Обновите и установите список устаревших модулей:

```console
apk update && apk upgrade 
```

Установите **Python**:

```console

apk add python3
```
Установите менеджер пакетов **pip3**:
```console
apk add py3-pip
```
Установите **Git**:
```console

apk add git
```
<h3> 3. Клонирование репозитория: </h3>

Далее вам нужно клонировать этот репозиторий:

```console
git clone https://github.com/boumer7/bombshot
```

Вас попросят авторизоваться через GitHub: вам нужно ввести свой логин, а потом пароль.

Переместитесь в папку **bombshot** два раза:

```console
cd bombshot
```

```console
cd bombshot
```

Вы должны находится примерно в такой директории:<br/> <br/>
<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/77790965/110965550-5707da00-8365-11eb-955a-220768028dca.jpg"/></kbd><br/>
(если вы не создавали каких-либо папок до этого).

Если вы не уверены, что находитесь в нужной директории, то напишите:
```console
ls
```

Это команда выведет список всех файлов в текущей директории, среди которых должен быть **bombshot.py** <br/> <br/>
<kbd><image style="border-radius:50%" src="https://user-images.githubusercontent.com/77790965/110965651-71da4e80-8365-11eb-921a-ceee8d25600b.jpg"/></kbd>
<br/> <br/>
Если вы видите **bombshot.py**, то вы находитесь в правильной директории.

<h3> 4. Установка библиотек: </h3>

```console
pip3 install -r requirements.txt
```

<h3> 5. Запуск: </h3>

```console
python3 bombshot.py
```

Поздравляем, теперь вы можете использовать BOMBSHOT.<br/>
**Удачных пентестов!**

## <a name="recom"> Рекомендации и примечания </a>

- Используйте безлимитный интернет. Данное ПО потребляет большое количество интернет-трафика.
- Используйте прокси для достижения максимального результата.
- Очищайте кэш после использования при помощи соответствующего софта (например, [CCleaner](https://play.google.com/store/apps/details?id=com.piriform.ccleaner&hl=en&gl=US)).
- Загрузите как можно больше прокси перед использованием.
- Рассчитайте мощность: количество циклов умножается на количество прокси при отправке, большинство сайтов просто поставят временный запрет на рассылку сообщений ввиду ограничений, наложенных из-за частоты запросов и вам перестанут приходить сообщения. Если у вас много прокси, то отправьте меньше циклов, если у вас мало прокси, то отправьте больше циклов.
- Перед отправкой сообщений на свой номер убедитесь в том, что вы сохранили важные для себя сообщения, в противном случае они могут потерятся среди спама.


