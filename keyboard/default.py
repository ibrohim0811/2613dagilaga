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

ANDIJON_DISTRICTS = ["Andijon sh.", "Asaka", "Baliqchi", "Bo‘z", "Jalaquduq", "Izboskan"]
BUXORO_DISTRICTS = ["Buxoro sh.", "G‘ijduvon", "Jondor", "Kogon", "Peshku", "Romitan"]
FARGONA_DISTRICTS = ["Farg‘ona sh.", "Qo‘qon", "Marg‘ilon", "Bag‘dod", "Beshariq"]
JIZZAX_DISTRICTS = ["Jizzax sh.", "Arnasoy", "Baxmal", "Zarbdor", "Zomin", "Do‘stlik"]
NAMANGAN_DISTRICTS = ["Namangan sh.", "Chortoq", "Kosonsoy", "Mingbuloq", "Norin", "Pop"]
NAVOIY_DISTRICTS = ["Navoiy sh.", "Karmana", "Konimex", "Navbahor", "Tomdi", "Uchquduq"]
QASHQADARYO_DISTRICTS = ["Qarshi sh.", "G‘uzor", "Dehqonobod", "Chiroqchi", "Koson", "Nishon"]
QORAQALPOGISTON_DISTRICTS = ["Nukus sh.", "Amudaryo", "Beruniy", "Chimboy", "Ellikqal’a"]
SAMARQAND_DISTRICTS = ["Samarqand sh.", "Bulung‘ur", "Ishtixon", "Jomboy", "Kattaqo‘rg‘on"]
SIRDARYO_DISTRICTS = ["Guliston sh.", "Boyovut", "Sayxunobod", "Sardoba", "Shirin"]
SURXONDARYO_DISTRICTS = ["Termiz sh.", "Angor", "Boysun", "Denov", "Jarqo‘rg‘on"]
TOSHKENT_VIL_DISTRICTS = ["Toshkent vil.", "Bekobod", "Chinoz", "Qibray", "Olmaliq", "Zangiota"]
TOSHKENT_SH_DISTRICTS = ["Toshkent sh."]  # Toshkent shahri alohida
XORAZM_DISTRICTS = ["Urganch sh.", "Xiva", "Shovot", "Yangiariq", "Yangibozor"]

# =================================
# Yordamchi funksiya: 2 ustunli keyboard
# =================================
def make_keyboard(items: list, row_width: int = 2, i18n: I18nContext = None, add_back=True):
    rows = []

    # Tarjima funksiyasi
    _ = i18n.gettext if i18n else (lambda x: x)

    # Asosiy tugmalar
    buttons = [KeyboardButton(text=_(item)) for item in items]

    # Ustunlarga bo‘lish
    for i in range(0, len(buttons), row_width):
        rows.append(buttons[i:i+row_width])

    # Orqaga tugmasi (ixtiyoriy)
    if add_back:
        rows.append([KeyboardButton(text=_("back"))])
        rows.append([KeyboardButton(text=_("back_main"))])

    return ReplyKeyboardMarkup(
        keyboard=rows,
        resize_keyboard=True
    )

# =================================
# Har bir viloyat uchun alohida funksiya
# =================================
def andijon():
    kb = make_keyboard(ANDIJON_DISTRICTS)
    return kb

def buxoro():
    kb = make_keyboard(BUXORO_DISTRICTS)
    return kb

def fargona():
    kb = make_keyboard(FARGONA_DISTRICTS)
    return kb

def jizzax():
    kb = make_keyboard(JIZZAX_DISTRICTS)
    return kb

def namangan():
    kb = make_keyboard(NAMANGAN_DISTRICTS)
    return kb

def navoi():
    kb = make_keyboard(NAVOIY_DISTRICTS)
    return kb

def qashqadaryo():
    kb = make_keyboard(QASHQADARYO_DISTRICTS)
    return kb

def qoraqalpogiston():
    kb = make_keyboard(QORAQALPOGISTON_DISTRICTS)
    return kb

def samarqand():
    kb = make_keyboard(SAMARQAND_DISTRICTS)
    return kb

def sirdaryo():
    kb = make_keyboard(SIRDARYO_DISTRICTS)
    return kb

def surxondaryo():
    kb = make_keyboard(SURXONDARYO_DISTRICTS)
    return kb

def toshkent_vil():
    kb = make_keyboard(TOSHKENT_VIL_DISTRICTS)
    return kb

def toshkent_sh():
    kb = make_keyboard(TOSHKENT_SH_DISTRICTS)
    return kb
def xorazm():
    kb = make_keyboard(XORAZM_DISTRICTS)
    return kb
