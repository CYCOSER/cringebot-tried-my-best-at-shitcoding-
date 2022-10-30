import logging
from itertools import count
import datetime
import calendar
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types

import aiogram
from aiogram.dispatcher import FSMContext

API_TOKEN = '5746797527:AAGdSqgTCuFIkncAAPinoyTV0i4vAlO1C-I'
swish = False
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)
switch = False
Time = False
arr = [0, 0, 0, 0, 0, 0]
kbs = []
zalarr = 'Зал Бочки Большой зал Малый танцевальный Большой танцевальный зал Ститцевая'
arrus = 'Стулья' 'TB LG со стойками СтолыВешалка для одежды Журнальные столы Диван Стул барный Колонки Базов станция радио микрофона Микшер'
x = 0
items = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

kb = [['Стулья', 'TB LG со стойками'],
      ['Столы', 'Вешалка для одежды'],
      ['Журнальные столы', 'Диван'],
      ['Стул барный', 'Колонки'],
      ['Базов. станция радио микрофона'],
      ['Микшер', 'Все!']]
keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.full_name
    kb2 = [['Форум', 'Собеседование'],
           ['Развлечение', 'Конкурс']]
    keyboard_x = types.ReplyKeyboardMarkup(
        keyboard=kb2,
        resize_keyboard=True
    )
    await message.answer(f"Здравствуйте {user_name}!\nХотели бы забронировать зал в Доме Молодежи?")
    await message.answer("Какова цель мироприятия?", reply_markup=keyboard_x)


@dp.message_handler(lambda message: message.text == "Форум" or message.text == "Собеседование" or message.text ==
                                    "Развлечение" or message.text == "Конкурс")
async def appnd(message: types.Message):
    arr[0] = message.text
    print(arr)
    kb = [
        [
            types.KeyboardButton(text="0-35"),
            types.KeyboardButton(text="35-50"),
            types.KeyboardButton(text="50-150")
        ],
    ]
    keyboard_p = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )

    global switch
    switch = True
    await message.answer("Сколько человек прийдут на мероприятие?", reply_markup=keyboard_p)


@dp.message_handler(lambda message: message.text == "0-35")
async def zero_to_thityfive(message: types.Message):
    chat_id = message.chat.id
    print(chat_id)
    global switch
    if switch == True:
        await message.answer("Вам подходят залы:", reply_markup=types.ReplyKeyboardRemove())
        kb = [['Малый танцевальный'],
              ['Ститцевая'],
              ['Большой танцевальный зал']]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
        )
        await message.answer("Mалый танцевальный зал\n15-20 человек", reply_markup=keyboard)
        await bot.send_photo(chat_id, open("pics/maly_zal.jpg", 'rb'))
        await message.answer("Ститцевая\n20-25 человек")
        await bot.send_photo(chat_id, open("pics/stytsevaya.jpg", 'rb'))
        await message.answer("Большой танцевальный зал\n25-35 человек")
        await bot.send_photo(chat_id, open("pics/bolsh_tantz_zal.jpg", 'rb'))
        switch = False
        await message.answer("Выберите зал")
        await message.answer("Выбрете оборудование", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "35-50")
async def thityfive_to_fifty(message: types.Message):
    chat_id = message.chat.id
    global switch
    if switch == True:
        kb = [['Зал Бочки'],
              ['Большой зал']]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
        )
        await message.answer("Вам подходят залы:", reply_markup=types.ReplyKeyboardRemove())
        await message.answer("Зал Бочки\n35-50 человек", reply_markup=keyboard)
        await bot.send_photo(chat_id, open("pics/zal_bochki.jpg", 'rb'))
        await message.answer("Большой зал\n50-150 человек")
        await bot.send_photo(chat_id, open("pics/bolshoy_zal.jpg", 'rb'))
        switch = False
        await message.answer("Выберите зал")
        await message.answer("Выбрете оборудование", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in zalarr)
async def asdfgdfsg(message: types.Message):
    arr[1] = (message.text)
    await message.answer("Выбрете оборудование", reply_markup=keyboard)
    print(arr)

@dp.message_handler(lambda message: message.text == "50-150")
async def fifty_to_hundrednfifty(message: types.Message):
    chat_id = message.chat.id
    global switch
    if switch == True:
        await message.answer("Вам подходит зал:", reply_markup=types.ReplyKeyboardRemove())
        await message.answer("Большой зал\n50-150 человек")
        await bot.send_photo(chat_id, open("pics/bolshoy_zal.jpg", 'rb'))
        switch = False
        arr[2] = ("Большой зал")
        print(arr)
        await message.answer("Выбрете оборудование", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Стулья")
async def stylya(message: types.Message):
    global x
    x = 1
    await message.answer("Выберите количество до 100 штук", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text == "TB LG со стойками")
async def TB_LG(message: types.Message):
    global x
    x = 2
    await message.answer("Выберите количество до 2х штук", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text == "Столы")
async def Stoly(message: types.Message):
    global x
    x = 3
    await message.answer("Выберите количество до 45 штук", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text == "Вешалка для одежды")
async def Vesh(message: types.Message):
    global x
    x = 4
    await message.answer("Выберите количество до 6 штук", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text == "Журнальный столик")
async def Jstol(message: types.Message):
    global x
    items[4] = message.text
    print(items)
    x = 5
    await message.answer("Выберите количество до 2 штук", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text  == "Диван")
async def Dvan(message: types.Message):
    await message.answer("У нас есть только один диван")
    items[5] = 1
    print(items)
    await message.answer("Отлично! Еще что-то?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Стул барный")
async def Bar(message: types.Message):
    await message.answer("У нас есть только один барный стул")
    items[6] = 1
    print(items)
    await message.answer("Отлично! Еще что-то?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Колонки")
async def Kolonk(message: types.Message):
    global x
    x = 6
    await message.answer("Выберите количество до 2 штук", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text == "Базов. станция радио микрофона")
async def Radio(message: types.Message):
    await message.answer("У нас есть только одна станция")
    items[8] = 1
    print(items)
    await message.answer("Отлично! Еще что-то?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Микшер")
async def Miksh(message: types.Message):
    await message.answer("У нас есть только один микшер")
    items[9] = 1
    print(items)
    await message.answer("Отлично! Еще что-то?", reply_markup=keyboard)

@dp.message_handler(lambda message: x == 1)
async def stuly(message: types.Message):
    global x
    items[0] = message.text
    print(items)
    x = 0
    await message.answer("Отлично! Еще что-то?", reply_markup=keyboard)

@dp.message_handler(lambda message: x == 2)
async def asdfdasf(message: types.Message):
    global x
    items[1] = message.text
    print(items)
    x = 0
    await message.answer("Отлично! Еще что-то?", reply_markup=keyboard)

@dp.message_handler(lambda message: x == 3)
async def asdasdafsf(message: types.Message):
    global x
    items[2] = message.text
    print(items)
    x = 0
    await message.answer("Отлично! Еще что-то?", reply_markup=keyboard)

@dp.message_handler(lambda message: x == 4)
async def asdasafsf(message: types.Message):
    global x
    items[3] = message.text
    print(items)
    x = 0
    await message.answer("Отлично! Еще что-то?", reply_markup=keyboard)


@dp.message_handler(lambda message: x == 5)
async def asdasafsf(message: types.Message):
    global x
    items[4] = message.text
    print(items)
    x = 0
    await message.answer("Отлично! Еще что-то?", reply_markup=keyboard)


@dp.message_handler(lambda message: x == 6)
async def asdasafsf(message: types.Message):
    global x
    items[7] = message.text
    print(items)
    x = 0
    await message.answer("Отлично! Еще что-то?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Все!")
async def Aleuo(message: types.Message):
    date = datetime.date.today() + datetime.timedelta(days=4)
    xo = 4
    i = 0
    while xo != 0:
        fodate = date + datetime.timedelta(days=i)
        weekday = calendar.day_name[fodate.weekday()]
        i += 1
        if weekday != 'Sunday' and weekday != 'Saturday':
            kbs.append(weekday)
            xo -= 1
        print(kbs)
    for k in range(len(kbs)):
        if kbs[k] == "Monday":
            kbs[k] = "Понедельник"
        if kbs[k] == "Tuesday":
            kbs[k] = "Вторник"
        if kbs[k] == "Wednesday":
            kbs[k] = "Среда"
        if kbs[k] == "Thursday":
            kbs[k] = "Четверг"
        if kbs[k] == "Friday":
            kbs[k] = "Пятница"
    kb = [[f'{kbs[0]}', f'{kbs[1]}'],
          [f'{kbs[2]}', f'{kbs[3]}']]
    keyboard_p = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    global swish
    swish = True
    await message.answer("Выберите день или введите дату (формат xx.xx.xxxx)", reply_markup=keyboard_p)


@dp.message_handler(lambda message: message.text in kbs)
async def asdfw(message: types.Message):
    if message.text == "Понедельник" or message.text == "Вторник" or message.text == "Четверг":
        arr[2] = (f"На ближайший {message.text}")
    else:
        arr[2] = (f"На следущую {message.text[:-1]}у")
    print(arr)
    await message.answer("Выберите время с 9 утра до 9 вечера(в формате xx:xx-xx:xx)", reply_markup=types.ReplyKeyboardRemove())
    global swish
    swish = True


@dp.message_handler()
async def cringe(message: types.Message):
    global swish
    if swish == True:
        global Time
        arr[3] = message.text
        print(arr)
        swish = False
        await message.answer("Расскажите подробности о мероприятии")
        return
    if swish == False and Time == False:
        arr[4] = message.text
        print(arr)
        Time = True
        await message.answer("Введите контактные данные")
        return
    if Time == True:
        arr[5] = message.text
        print(arr)
    await bot.send_message(960831479, f"Цель мероприятия: {arr[0]}\n\n"
                                      f"Описание события: {arr[4]}\n\n"
                                      f"Желаемый зал: {arr[1]}\n\n"
                                      f"Желаемое оборудование:\n"
                                      f"{items[0]} стульев\n"
                                      f"{items[1]} TB LG\n"
                                      f"{items[2]} столов\n"
                                      f"{items[3]} вешалок\n"
                                      f"{items[4]} журнальных столиков\n"
                                      f"{items[5]} диван\n"
                                      f"{items[6]} стул барный\n"
                                      f"{items[7]} колонки со стойками\n"
                                      f"{items[8]} базовая станция радио микрофона\n"
                                      f"{items[9]} микшер\n\n"
                                      f"Дата: {arr[2]}\n\n"
                                      f"Время: {arr[3]}\n\n"
                                      f"Контактные данные: {arr[5]}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
