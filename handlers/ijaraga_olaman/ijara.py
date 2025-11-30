import os
from pathlib import Path
from aiogram import types, F
from aiogram_i18n import I18nContext
from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command  
from aiogram.utils.i18n import I18n
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ChatType


ij = Router()

GROUP_LINK = "https://t.me/+4LyURtBppBhlNzQy"

def inline_kb(i18n):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=i18n("join_to"), url=GROUP_LINK)]
        ]
    )

@ij.message(lambda message, i18n: message.text == i18n("ijara_o"))
async def throw(msg: types.Message, i18n: I18nContext):
    await msg.answer(i18n("offer"), reply_markup=inline_kb(i18n))
    
@ij.message(Command('clear'))
async def clear_chat_history(message: types.Message):
    # Bu chat guruh emas, balki shaxsiy chat ekanligini tekshirish muhim
    if message.chat.type != ChatType.PRIVATE:
        await message.reply("Bu buyruq faqat shaxsiy suhbatlarda ishlaydi.")
        return

    # 1. So'nggi 50 ta xabarni o'chirishga harakat qilish
    # Bot o'zi yuborgan va foydalanuvchi yuborgan xabarlarni o'chirishi mumkin
    for i in range(1, 51):
        try:
            # Xabar ID sini kamaytirib o'chiramiz
            await message.bot.delete_message(
                chat_id=message.chat.id, 
                message_id=message.message_id - i
            )
        except Exception:
            # Agar xabar allaqachon o'chirilgan bo'lsa yoki yuborilmagan bo'lsa, xato tashlaydi
            continue
            
    # 2. Tozalash tugaganini bildiruvchi xabar yuborish
    await message.answer("Suhbat muvaffaqiyatli tozalandi (so'nggi xabarlar o'chirildi).")

    # /clear buyrug'i yozilgan xabarni ham o'chiramiz
    try:
        await message.bot.delete_message(
            chat_id=message.chat.id, 
            message_id=message.message_id
        )
    except Exception:
        pass