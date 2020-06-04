from glob import glob
from random import choice
import ephem

from my_utils import main_keyboard, get_smile, play_random_numbers

def greet_user(update, context):
    smile = get_smile(context.user_data)
    user_name = update.message.from_user.first_name
    my_keyboard = ReplyKeyboardMarkup([['Прислать котика']])
    print(f'Greetings, my dear little {user_name}! {smile} You push /start')
    update.message.reply_text(f'Greetings, my dear little {user_name}! {smile} You push /start',
                              reply_markup=main_keyboard())

def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except(TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите целое число"
    update.message.reply_text(message)

def planet(update, context):
    user_text = update.message.text 
    l = user_text.split()
    current_time = datetime.datetime.now() 
    plnt = eval('ephem.'+l[1])(f'{current_time.year}/{current_time.day}/{current_time.month}')
    constellation = ephem.constellation(plnt)
    print(constellation)
    update.message.reply_text(constellation)

def send_cat_picture(update, context):
    cat_photos_list = glob('images/cat*')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'), reply_markup=main_keyboard())

def talk_to_me(update, context):
    smile = get_smile(context.user_data)
    user_text = update.message.text 
    username = update.effective_user.first_name
    text = update.message.text
    update.message.reply_text(f"Hi there, {username} {smile}! Ты написал: {text}")

def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )

def error_callback(update, error):
    try:
        raise error
    except:
        print("Telegram Error")
        print(f'Error with {update.message.text}')
        update.message.reply_text(f'Error with {update.message.text}. Try again')
        print(error)

