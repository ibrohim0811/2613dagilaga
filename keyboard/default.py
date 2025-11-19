from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram_i18n import I18nContext


def main_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    
    return ReplyKeyboardMarkup(
        keyboard=[
            [   KeyboardButton(text=_("ijara_o")),
                KeyboardButton(text=_("ijara_b"))
            ],
            [
                KeyboardButton(text=_("language_button")),
                KeyboardButton(text=_("about"))
            ]
        ],
        resize_keyboard=True
    )
    
def ijaraga_beraman(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("flat")),
                KeyboardButton(text=_("house"))
            ],
            [
                KeyboardButton(text=_("dacha")),
                KeyboardButton(text=_("office"))
            ],
            [
                KeyboardButton(text=_("back_main"))
            ]
        ],
        resize_keyboard=True
    )