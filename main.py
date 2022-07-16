import logging
import time
import os

from misstake import extract_link
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from screen import take_screen, driver, TimeoutException, WebDriverException

bot = Bot(token=TOKEN)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=open('photo/photo.jpg', 'rb')
                         )
    await message.answer("Hi🖐️\n"
                         "This is the Event Horizon project.\n"
                         "Send me a link to the .onion site and I'll send you a screenshot of that site.\n"
                         "If you have questions, press /help.\n\n"
                         "Community <a href='https://t.me/darkn3t_prison'>Горизонт Событий</a>\n"
                         "Developed by <a href='https://t.me/b3_pati3nt'>Abanazar</a>\n\n", parse_mode:='HTML'
                         "Designed by <a href='https://t.me/zireaellll'>Zireael</a>\n\n", parse_mode:='HTML'
                         )

@dp.message_handler(content_types=['text'])
async def hadle_urls(message: types.Message):
    link = extract_link(message.text)
    if link != 0: # link exist in message
       start_time = time.time()
       try:
           msg_request = await message.answer('Request has been sent.\n'
                                              'Please wait'
                                              )
           screen_site = take_screen(link[0])
           await msg_request.delete()
           await bot.send_photo(chat_id=message.chat.id,
                                photo=open(screen_site, 'rb'),
                                caption="According to your request: {0}\nRequest time: {1} sec."
                                .format(link[0],round(time.time() - start_time))
                                )
           if os.path.exists(screen_site):
               os.remove(screen_site)
               
       except TimeoutException:
           await msg_request.delete()
           await message.answer('Timed out waiting for a response from the resource.')
           await message.answer_sticker(r'CAACAgIAAxkBAAEE9exio5aFSonquBgqJPOyiXrQIKCz0AACEAADcPcaMRgljWVLMdIYJAQ')
       
       except WebDriverException:
           await msg_request.delete()
           await message.answer('No access to resource.')
           await message.answer_sticker(r'CAACAgIAAxkBAAEE9exio5aFSonquBgqJPOyiXrQIKCz0AACEAADcPcaMRgljWVLMdIYJAQ')
       
       except:
           await msg_request.delete()
           await message.answer('An unexpected error occurred, please try again later.')
           await message.answer_sticker(r'CAACAgIAAxkBAAEE9e5io5aKhuAAAb-06NcvyF765gZdNQsAAo0MAAKp9tBLixqlJA7vLZckBA')

if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    finally:
        driver.close()
        driver.quit()
