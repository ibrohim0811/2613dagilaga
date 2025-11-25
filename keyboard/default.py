from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram_i18n import I18nContext
from aiogram import types


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
    
def time_kv(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("long_time")),
                KeyboardButton(text=_("daily"))
            ],
            [
                KeyboardButton(text=_("back")),
                KeyboardButton(text=_("back_main"))
            ]
        ],
        resize_keyboard=True
    )

# Viloyatlar ro'yxati
REGIONS = [
    "Andijon", "Buxoro",
    "Farg'ona", "Jizzax",
    "Namangan", "Navoiy",
    "Qashqadaryo", "Qoraqalpog'iston",
    "Samarqand", "Sirdaryo",
    "Surxondaryo", "Toshkent vil.",
    "Xorazm", "Toshkent sh."
]

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def make_regions_keyboard(i18n: I18nContext):
    _ = i18n

    # Keyboard tugmalarini list sifatida yaratamiz
    keyboard = []
    row = []
    for region in REGIONS:
        row.append(KeyboardButton(text=region))
        if len(row) == 2:  # 2 ustun
            keyboard.append(row)
            row = []

    if row:  # oxirgi qator 1 ta tugma bo‘lsa
        keyboard.append(row)

    # Pastga default tugmalar
    keyboard.append([KeyboardButton(text=_("back_main"))])
    keyboard.append([KeyboardButton(text=_("back"))])

    # ReplyKeyboardMarkup yaratish
    kb = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )

    return kb



# =================================
# Yordamchi funksiya: 2 ustunli keyboard
# =================================

# def make_keyboard(i18n: I18nContext):
#     markup = ReplyKeyboardMarkup(
#     keyboard=[], 
#     resize_keyboard=True
# )


#     keyboard = []
#     row = []

#     for name in districts:
#         row.append(KeyboardButton(text=name))
#         if len(row) == 2:  # 2 ustunli
#             keyboard.append(row)
#             row = []

#     if row:  # oxirgi qolgan bo‘lsa
#         keyboard.append(row)

#     # Orqaga tugmalar
#     keyboard.append([KeyboardButton(text=_("back"))])
#     keyboard.append([KeyboardButton(text=_("back_main"))])

#     return ReplyKeyboardMarkup(
#         keyboard=keyboard,
#         resize_keyboard=True
#     )

# =================================
# Har bir viloyat uchun alohida funksiya
# =================================
def andijon():
    # kb = make_keyboard(ANDIJON_DISTRICTS)
    # return kb


