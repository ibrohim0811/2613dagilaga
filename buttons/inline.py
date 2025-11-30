from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram_i18n import I18nContext


def change_lang_menu(i18n: I18nContext) -> InlineKeyboardMarkup:
    _ = i18n
    
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("uzbek"), callback_data="uzbek"),
                InlineKeyboardButton(text=_("rus"), callback_data="rus"),
                InlineKeyboardButton(text=_("en"), callback_data="en")
            ]
        ]
    )

def sorov_to_admin(i18n: I18nContext) -> InlineKeyboardMarkup:
    _ = i18n
    
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("ha"), callback_data="yes"),
                InlineKeyboardButton(text=_("yoq"), callback_data="no")
            ]
        ]
    )
    
def send_to_admin() -> InlineKeyboardMarkup:
    
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=("Accept ✅"), callback_data="accept"),
                InlineKeyboardButton(text=("Decline ❌"), callback_data="decline")
            ]
        ]
    )
    
