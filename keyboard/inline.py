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
