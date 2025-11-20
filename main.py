import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from pathlib import Path
from aiogram import types
from aiogram_i18n import I18nContext

from dotenv import load_dotenv
from middlewares.i18n import i18n_middleware
from aiogram_i18n.context import I18nContext
from keyboard.default import main_menu, ijaraga_beraman
from keyboard.inline import change_lang_menu
from models.users import User
from database import SessionLocal


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


dp = Dispatcher()
i18n_middleware.setup(dispatcher=dp)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "uz")
SUPPORTED_LANGUAGES = ["uz", "ru", "en"]
# DATABASE_URL = os.getenv("")



@dp.message(Command('start'))
async def start(message: types.Message, i18n: I18nContext):
    await i18n.set_locale(DEFAULT_LANGUAGE)
    try:
        db = SessionLocal()
        db_user = User(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        language_code=message.from_user.language_code,
        is_active=True
    )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        pass
    await message.answer(i18n("start_text"), reply_markup=main_menu(i18n))
    
@dp.message(lambda message, i18n: message.text == i18n("ijara_b"))
async def ijaraga_b(msg: types.Message, i18n: I18nContext):
    await msg.answer(i18n("select_section"), reply_markup=ijaraga_beraman(i18n))
    
@dp.message(lambda message, i18n: message.text == i18n("back_main"))
async def back_main(msg: types.Message, i18n: I18nContext):
    await msg.answer(i18n("main_menu_text"), reply_markup=main_menu(i18n))
    
# @dp.message(F.photo)
# async def photo(msg: types.Message):
#     url = msg.photo[-1]
#     await msg.answer(f"{url}")
    

#language row
@dp.message(lambda message, i18n: message.text == i18n("language_button"))
async def change_lang(msg: types.Message, i18n: I18nContext):
    await msg.answer(i18n("select_lang"), reply_markup=change_lang_menu(i18n))


#change to uzbek
@dp.callback_query(lambda c: c.data == "uzbek")
async def uzbek(callback: types.CallbackQuery, i18n: I18nContext):
    await i18n.set_locale("uz")
    await callback.message.answer(i18n("sucsess_lang"), reply_markup=main_menu(i18n))
    await callback.answer()
#rus 
@dp.callback_query(lambda c: c.data == "rus")
async def rus(callback: types.CallbackQuery, i18n: I18nContext):
    await i18n.set_locale("ru")
    await callback.message.answer(i18n("sucsess_lang"), reply_markup=main_menu(i18n))
    await callback.answer()

#ingliz
   
@dp.callback_query(lambda c: c.data == "en")
async def english(callback: types.CallbackQuery, i18n: I18nContext):
    await i18n.set_locale("en")
    await callback.message.answer(i18n("sucsess_lang"), reply_markup=main_menu(i18n))
    await callback.answer()

#about
@dp.message(lambda message, i18n: message.text == i18n("about"))
async def about_bot(msg: types.Message, i18n: I18nContext):
    image_id = 'AgACAgIAAxkBAAMZaR3hxfOWFcG_2-h0_iP_6BvPr_UAArgSaxudV_BIZXaO87VI__wBAAMCAAN5AAM2BA'
    await msg.answer_photo(image_id, caption=i18n("about_text"))

async def main():
    bot = Bot(token=BOT_TOKEN)
    # i18n_middleware.setup(dispatcher=dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
    
#chala qoldi i18n qilish  default buttonlarni qoyish