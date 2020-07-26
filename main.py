import telebot 
import config
import helps
import requests
import re
from SqlLiteDatabase import SQLighter




from telebot import types 

TEXT = "🥳Бота обновили😇\nТеперь поиск работает по новому, для поиска фильма просто пишите названия фильма😅\nНаслаждайтесь ботом всего доброго😋"

message = False
url1 = {}
url2 = {}
urls = {}


def new_list(db, table, text):
	sqlite = SQLighter(db,table)
	for a in sqlite.count_id_chat_name():
		bot.send_message(a[0],"С празником {0}!!!\n".format(a[1])+text)
	sqlite.close()


def ParsFilm(bot, message, url):
	response = requests.get(url)
	global  url1
	global  url2
	url1[message.chat.id] = re.findall(r'(?:<a.href=")(.*?)(?:"><span class="navnext">Вперед</span></a>)', response.content.decode('utf-8'))
	url2[message.chat.id] = re.findall(r'(?:<a.href=")(.*?)(?:"><span class="navprev">Назад</span></a>)', response.content.decode('utf-8'))
	markup = types.InlineKeyboardMarkup(row_width=3)
	text = re.findall(r'(?:<div.class="navcent">.*<span>)(.*?)(?:</span>)', response.content.decode('utf-8'))
	texts = re.findall(r'(?:<a.href=".*">)(.*?)(?:</a></div>)', response.content.decode('utf-8'))

	test = str(text[0]) + "/" +  str(texts[0])
	
	urlss = re.findall(r'(?:<h2><a.href=")(.*?)(?:">.*</a></h2>)', response.content.decode('utf-8'))
	messeges(message.chat.id,urlss)
	i = 0

	for film in re.findall(r'(?:<h2><a.href=".*">)(.*?)(?:</a></h2>)', response.content.decode('utf-8')):
		item = types.InlineKeyboardButton(film, callback_data='film'+str(i))
		markup.add(item)
		i = i+1
	
	item1 = types.InlineKeyboardButton("<", callback_data='back') 
	item2 = types.InlineKeyboardButton(test, callback_data='test')
	item3 = types.InlineKeyboardButton(">", callback_data='next')  
	markup.add(item1,item2,item3)
	bot.send_message(message.chat.id, message.text,reply_markup=markup, parse_mode='html')


def ParsTestFilm(bot, call, url):
	global url1
	global url2
	response = requests.get(url)
	url1[call.message.chat.id] = re.findall(r'(?:<a.href=")(.*?)(?:"><span class="navnext">Вперед</span></a>)', response.content.decode('utf-8'))
	url2[call.message.chat.id] = re.findall(r'(?:<a.href=")(.*?)(?:"><span class="navprev">Назад</span></a>)', response.content.decode('utf-8'))
	markup = types.InlineKeyboardMarkup()
	text = re.findall(r'(?:<div.class="navcent">.*<span>)(.*?)(?:</span>)', response.content.decode('utf-8'))
	texts = re.findall(r'(?:<a.href=".*">)(.*?)(?:</a></div>)', response.content.decode('utf-8'))

	test = str(text[0]) + "/" +  str(texts[0])

	urlss = re.findall(r'(?:<h2><a.href=")(.*?)(?:">.*</a></h2>)', response.content.decode('utf-8'))
	messeges(call.message.chat.id,urlss)
	i = 0

	for film in re.findall(r'(?:<h2><a.href=".*">)(.*?)(?:</a></h2>)', response.content.decode('utf-8')):
		item = types.InlineKeyboardButton(film, callback_data='film' + str(i))
		markup.add(item)
		i = i+1

	

	item1 = types.InlineKeyboardButton("<", callback_data='back') 
	item2 = types.InlineKeyboardButton(test, callback_data='test')
	item3 = types.InlineKeyboardButton(">", callback_data='next')  
	markup.add(item1,item2,item3)
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text,reply_markup=markup)


def BottumFilm(bot, call, url):
	global url1
	global url2
	response = requests.get(url)
	url1[call.message.chat.id] = re.findall(r'(?:<a.href=")(.*?)(?:"><span class="navnext">Вперед</span></a>)', response.content.decode('utf-8'))
	url2[call.message.chat.id] = re.findall(r'(?:<a.href=")(.*?)(?:"><span class="navprev">Назад</span></a>)', response.content.decode('utf-8'))
	markup = types.InlineKeyboardMarkup()
	text = re.findall(r'(?:<div.class="navcent">.*<span>)(.*?)(?:</span>)', response.content.decode('utf-8'))
	texts = re.findall(r'(?:<a.href=".*">)(.*?)(?:</a></div>)', response.content.decode('utf-8'))
	test = str(text[0]) + "/" +  str(texts[0])
	
	
	urlss = re.findall(r'(?:<h2><a.href=")(.*?)(?:">.*</a></h2>)', response.content.decode('utf-8'))
	messeges(call.message.chat.id,urlss)
	i = 0

	for film in re.findall(r'(?:<h2><a.href=".*">)(.*?)(?:</a></h2>)', response.content.decode('utf-8')):
		item = types.InlineKeyboardButton(film, callback_data='film' + str(i))
		markup.add(item)
		i = i+1


	item1 = types.InlineKeyboardButton("<", callback_data='back')
	item2 = types.InlineKeyboardButton(test, callback_data='test')
	item3 = types.InlineKeyboardButton(">", callback_data='next')
	markup.add(item1,item2,item3)
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text,reply_markup=markup)

def BottumOldFilm(bot, call, url):
	global url1
	global url2
	response = requests.get(url)
	url1[call.message.chat.id] = re.findall(r'(?:<a.href=")(.*?)(?:"><span class="navnext">Вперед</span></a>)', response.content.decode('utf-8'))
	url2[call.message.chat.id] = re.findall(r'(?:<a.href=")(.*?)(?:"><span class="navprev">Назад</span></a>)', response.content.decode('utf-8'))
	markup = types.InlineKeyboardMarkup(row_width=3)
	text = re.findall(r'(?:<div.class="navcent">.*<span>)(.*?)(?:</span>)', response.content.decode('utf-8'))
	texts = re.findall(r'(?:<a.href=".*">)(.*?)(?:</a></div>)', response.content.decode('utf-8'))
	test = str(text[0]) + "/" +  str(texts[0])
	

	urlss = re.findall(r'(?:<h2><a.href=")(.*?)(?:">.*</a></h2>)', response.content.decode('utf-8'))
	messeges(call.message.chat.id,urlss)
	i = 0
	for film in re.findall(r'(?:<h2><a.href=".*">)(.*?)(?:</a></h2>)', response.content.decode('utf-8')):
		item = types.InlineKeyboardButton(film, callback_data='film' + str(i))
		markup.add(item)
		i = i+1

	
	item1 = types.InlineKeyboardButton("<", callback_data='back')
	item2 = types.InlineKeyboardButton(test, callback_data='test')
	item3 = types.InlineKeyboardButton(">", callback_data='next')
	markup.add(item1,item2,item3)
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text,reply_markup=markup)



def ParsFilmWan(bot, call,url):
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=url)


def messeges(chat_id, mas):
	global urls
	urls[chat_id] = mas 











bot = telebot.TeleBot(config.TOKEN)
if message:
	new_list(config.DATABASE, config.TABLES, TEXT)



@bot.message_handler(commands=['start'])
def welcome(message):
	sqlite = SQLighter(config.DATABASE, config.TABLES)
	if message.from_user.username:
		if message.from_user.first_name:
			sqlite.add_new(message.chat.id, message.from_user.username,message.from_user.first_name)
		else:
			sqlite.add_new(message.chat.id, message.from_user.username,"None")
	elif message.from_user.first_name:
		sqlite.add_new(message.chat.id, "None",message.from_user.first_name)
	else:
		sqlite.add_new(message.chat.id, "None","None")

	sqlite.close()
	

	sti = open("./index.webp", "rb")
	bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, "Добро пожаловать, {}!\nЯ - <b>{}</b>, отличный подборник фильмов!!!".format(message.from_user.first_name, bot.get_me().username), parse_mode='html')
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("😇 Новинка")
	item2 = types.KeyboardButton("🧑‍💻 Популярное")
	item3 = types.KeyboardButton("👍 Топ 100")
	item4 = types.KeyboardButton("👅 Категории")
	item5 = types.KeyboardButton("🤔 Год")
	markup.add(item1, item2, item3, item4, item5)
	bot.send_message(message.chat.id, helps.HELP,reply_markup=markup)


@bot.message_handler(commands=['info'])
def info(message):
	bot.send_message(message.chat.id, helps.INFO, parse_mode='html');



@bot.message_handler(commands=['exit'])
def exit(message):
	sti = open("./index1.webp", "rb")
	bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, "Прощай, {}!\nХорошего дня!!!".format(message.from_user.first_name), parse_mode='html')





@bot.message_handler(content_types=['text'])
def lalala(message):
	global urls
	if message.chat.type == 'private':
		if message.text == "😇 Новинка":
			url = "https://kinokrad.co/6-filmy-2020-novinki/"
			ParsFilm(bot, message, url)

		elif message.text == "🧑‍💻 Популярное":
			
			url = "https://kinokrad.co/views-films/"
			response = requests.get(url)
			markup = types.InlineKeyboardMarkup()


			test = re.findall(r'(?:<b><a.href=")(.*?)(?:">.*</a></b>)', response.content.decode('utf-8'))
			urls[message.chat.id] = test
			i = 0

			for film in re.findall(r'(?:<b><a.href=".*">)(.*?)(?:</a>)', response.content.decode('utf-8')):
				item = types.InlineKeyboardButton( film,callback_data='film' + str(i))
				markup.add(item)
				i = i +1


			bot.send_message(message.chat.id,message.text,reply_markup=markup)
		
		
		elif message.text == "👍 Топ 100":

			url = "https://kinokrad.co/rating-films-online/"
			response = requests.get(url)
			markup = types.InlineKeyboardMarkup()
			test = re.findall(r'(?:<b><a.href=")(.*?)(?:">.*</a></b>)', response.content.decode('utf-8'))
			urls[message.chat.id] = test
			i = 0

			for film in re.findall(r'(?:<b><a.href=".*">)(.*?)(?:</a>)', response.content.decode('utf-8')):
				item = types.InlineKeyboardButton( film,callback_data='film' + str(i))
				markup.add(item)
				i = i +1

			bot.send_message(message.chat.id,message.text,reply_markup=markup)
		
		elif message.text == "🤔 Год":
			markup = types.InlineKeyboardMarkup(row_width=1)
			item1 = types.InlineKeyboardButton("Фильми за 2020", callback_data='2020') 
			item2 = types.InlineKeyboardButton("Фильми за 2019", callback_data='2019')
			item3 = types.InlineKeyboardButton("Фильми за 2018", callback_data='2018')
			markup.add(item1,item2,item3)
			bot.send_message(message.chat.id, "🤔 Год",reply_markup=markup)

		elif message.text == "👅 Категории":
			markup = types.InlineKeyboardMarkup(row_width=1)
			item1 = types.InlineKeyboardButton("Аниме", callback_data='1') 
			item2 = types.InlineKeyboardButton("Мультфильмы", callback_data='2')
			item3 = types.InlineKeyboardButton("Драмы", callback_data='3')
			item4 = types.InlineKeyboardButton("Детективы", callback_data='4')
			item5 = types.InlineKeyboardButton("Биография", callback_data='5')
			item6 = types.InlineKeyboardButton("Мелодрамы", callback_data='6')
			item7 = types.InlineKeyboardButton("Военные", callback_data='7')
			item8 = types.InlineKeyboardButton("Боевики", callback_data='8')
			item9 = types.InlineKeyboardButton("Комедии", callback_data='9')
			item10 = types.InlineKeyboardButton("Криминальные", callback_data='10')
			item11 = types.InlineKeyboardButton("Триллеры", callback_data='11')
			item12 = types.InlineKeyboardButton("Исторические", callback_data='12')
			item13 = types.InlineKeyboardButton("Документальные", callback_data='13')
			item14 = types.InlineKeyboardButton("Приключения", callback_data='14')
			item15 = types.InlineKeyboardButton("Мистические", callback_data='15')
			item16 = types.InlineKeyboardButton("Ужасы", callback_data='16')
			item17 = types.InlineKeyboardButton("Семейные", callback_data='17')
			item18 = types.InlineKeyboardButton("Спортивные", callback_data='18')
			item19 = types.InlineKeyboardButton("Фантастика", callback_data='19')
			item20 = types.InlineKeyboardButton("Фэнтези", callback_data='20')
			markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20)
			bot.send_message(message.chat.id, "👅 Категории",reply_markup=markup)
		
		else:
			url = "https://kinokrad.co/"
			data_dict = {
			'story':message.text,
			'do':'search',
			'subaction':'search',
			}

			response = requests.post(url, data=data_dict)
			names = re.findall(r'(?:<h3><a href=".*".>)(.*?)(?:</a></h3>)', response.content.decode('utf-8'))
			if names:
				markup = types.InlineKeyboardMarkup()
				test = re.findall(r'(?:<h3><a href=")(.*?)(?:".>.*</a></h3>)', response.content.decode('utf-8'))
				messeges(message.chat.id,test)
				i = 0
				for name in names:
					item = types.InlineKeyboardButton(name, callback_data="film"+str(i))
					markup.add(item)
					i = i + 1
				bot.send_message(message.chat.id, message.text, parse_mode='html', reply_markup=markup)
			else:
				sti = open("./index2.webp", "rb")
				bot.send_sticker(message.chat.id, sti)
				bot.send_message(message.chat.id, "Нет фильмов в поиску🤷‍♂️🤷‍♀️")











@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	try:
		if call.message:
			global url1
			global url2
			if call.data == 'back':
				if url2[call.message.chat.id]:
					BottumFilm(bot, call,url2[call.message.chat.id][0])
				else:
					bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="Это первая страница!!!") 
					
			elif call.data == 'next':
				if url1[call.message.chat.id]:
					BottumFilm(bot, call, url1[call.message.chat.id][0])
				else:
					bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="Это последняя страница!!!")
			

			
			elif 'film' in call.data:
				global urls
				i = int(call.data.replace('film',''))
				if urls:
					url = urls[call.message.chat.id][i]
					ParsFilmWan(bot, call, url)
				else:
					bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="Обновите поиск😘")

			elif call.data == 'test':
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="Пустая кнопка")
			
			elif call.data == '1':
				url = "https://kinokrad.co/anime2/"
				ParsTestFilm(bot, call, url)
			
			elif call.data == '2':
				url = "https://kinokrad.co/multfilm-online7/"
				ParsTestFilm(bot, call, url)
			
			elif call.data == '3':
				url = "https://kinokrad.co/drama-films/"
				ParsTestFilm(bot, call, url)
			
			elif call.data == '4':
				url = "https://kinokrad.co/detektiv-online/"
				ParsTestFilm(bot, call, url)
			
			elif call.data == '5':
				url = "https://kinokrad.co/biografiya2/"
				ParsTestFilm(bot, call, url)
			
			elif call.data == '6':
				url = "https://kinokrad.co/melodrama/"
				ParsTestFilm(bot, call, url)

			elif call.data == '7':
				url = "https://kinokrad.co/voennyy4/"
				ParsTestFilm(bot, call, url)

			elif call.data == '8':
				url = "https://kinokrad.co/boevik3/"
				ParsTestFilm(bot, call, url)

			elif call.data == '9':
				url = "https://kinokrad.co/komediya-3/"
				ParsTestFilm(bot, call, url)

			elif call.data == '10':
				url = "https://kinokrad.co/kriminal2/"
				ParsTestFilm(bot, call, url)
			
			elif call.data == '11':
				url = "https://kinokrad.co/trillers2/"
				ParsTestFilm(bot, call, url)

			elif call.data == '12':
				url = "https://kinokrad.co/istoriya/"
				ParsTestFilm(bot, call, url)

			elif call.data == '13':
				url = "https://kinokrad.co/dokumentalny2/"
				ParsTestFilm(bot, call, url)

			elif call.data == '14':
				url = "https://kinokrad.co/priklyucheniya-onlin/"
				ParsTestFilm(bot, call, url)

			elif call.data == '15':
				url = "https://kinokrad.co/mistika2/"
				ParsTestFilm(bot, call, url)

			elif call.data == '16':
				url = "https://kinokrad.co/uzhasy-online-3/"
				ParsTestFilm(bot, call, url)

			elif call.data == '17':
				url = "https://kinokrad.co/semeynyy2/"
				ParsTestFilm(bot, call, url)

			elif call.data == '18':
				url = "https://kinokrad.co/sport2/"
				ParsTestFilm(bot, call, url)

			elif call.data == '19':
				url = "https://kinokrad.co/fantastika4/"
				ParsTestFilm(bot, call, url)
			
			elif call.data == '20':
				url = "https://kinokrad.co/fentezi2/"
				ParsTestFilm(bot, call, url)

			elif call.data == '2020':
				url = "https://kinokrad.co/7-filmy-2020-novinki/"
				BottumOldFilm(bot, call, url)

			elif call.data == '2019':
				url = "https://kinokrad.co/10-filmy-novinki-2019/"
				BottumOldFilm(bot, call, url)
			
			elif call.data == '2018':
				url = "https://kinokrad.co/2-filmy-novinki-2018/"
				BottumOldFilm(bot, call, url)

	except IndexError  as e:
   		print(repr(e))	
   		bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="Обновите запрос")


	except Exception as e:
		print(repr(e))	




#RUN
if __name__ == '__main__':
	try:
		bot.polling(none_stop=True)
	except:
		pass