from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram_i18n import I18nContext
from aiogram.utils.i18n import I18n 
from aiogram import types

i18n = I18n(path="locales", default_locale="uz")

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



def tuman(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("bektemir")),
                KeyboardButton(text=_("chilonzor"))
            ],
            [
                KeyboardButton(text=_("yashnobod")),
                KeyboardButton(text=_("mirzo"))
            ],
            [
                KeyboardButton(text=_("mirobod")),
                KeyboardButton(text=_("olmazor"))
            ],
            [
                KeyboardButton(text=_("sergeli")),
                KeyboardButton(text=_("shayxon"))
            ],
            [
                KeyboardButton(text=_("uchtepa")),
                KeyboardButton(text=_("yakkasaroy"))
            ],
            [
                KeyboardButton(text=_("yunus")),
                KeyboardButton(text=_("yangihayot"))
            ]
        ],
        resize_keyboard=True
    )

def persons(i18n: I18nContext) ->  ReplyKeyboardMarkup:
    _ = i18n
    
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("students")),
                KeyboardButton(text=_("workers"))
            ],
            [
                KeyboardButton(text=_("travels")),
                KeyboardButton(text=_("family"))
            ],
            [
                KeyboardButton(text=_("friend")),
                KeyboardButton(text=_("all"))
            ],
            [
                KeyboardButton(text=_("back_to")),
                KeyboardButton(text=_("back_main"))
            ]
        ],
        resize_keyboard=True
    )

    


def make_szz_keyboard(i18n: I18nContext):
    _ = i18n
    szz = ['20 m²', '22 m²', '25 m²', '28 m²', '30 m²', '33 m²', '36 m²', '38 m²', '41 m²', '44 m²', '46 m²', '49 m²',
           '52 m²', '54 m²', '57 m²', '60 m²', '62 m²', '65 m²', '68 m²', '70 m²', '73 m²', '76 m²', '78 m²', '81 m²',
           '84 m²', '86 m²', '89 m²', '92 m²', '94 m²', '97 m²', '100 m²', '102 m²', '105 m²', '108 m²', '110 m²',
           '113 m²', '116 m²', '118 m²', '121 m²', '124 m²', '126 m²', '129 m²', '132 m²', '134 m²', '137 m²',
           '140 m²', '142 m²', '145 m²', '148 m²', '150 m²', '153 m²', '156 m²', '158 m²', '161 m²', '164 m²',
           '166 m²', '169 m²', '172 m²', '174 m²', '177 m²', '180 m²', '182 m²', '185 m²', '188 m²', '190 m²',
           '193 m²', '196 m²', '198 m²', '201 m²', '204 m²', '206 m²', '209 m²', '212 m²', '214 m²', '217 m²',
           '220 m²', '222 m²', '225 m²', '228 m²', '230 m²', '233 m²', '236 m²', '238 m²', '241 m²', '244 m²',
           '246 m²', '249 m²', '252 m²', '254 m²', '257 m²', '260 m²', '262 m²', '265 m²', '268 m²', '270 m²',
           '273 m²', '276 m²', '278 m²', '281 m²', '284 m²', '286 m²', '289 m²', '292 m²', '294 m²', '297 m²',
           '300 m²', '302 m²', '305 m²', '308 m²', '310 m²', '313 m²', '316 m²', '318 m²', '321 m²', '324 m²',
           '326 m²', '329 m²', '332 m²', '334 m²', '337 m²', '340 m²', '342 m²', '345 m²', '348 m²', '350 m²',
           '353 m²', '356 m²', '358 m²', '361 m²', '364 m²', '366 m²', '369 m²', '372 m²', '374 m²', '377 m²',
           '380 m²', '382 m²', '385 m²', '388 m²', '390 m²', '393 m²', '396 m²', '398 m²', '401 m²', '404 m²',
           '406 m²', '409 m²', '412 m²', '414 m²', '417 m²', '420 m²', '422 m²', '425 m²', '428 m²', '430 m²',
           '433 m²', '436 m²', '438 m²', '441 m²', '444 m²', '446 m²', '449 m²', '452 m²', '454 m²', '457 m²',
           '460 m²', '462 m²', '465 m²', '468 m²', '470 m²', '473 m²', '476 m²', '478 m²', '481 m²', '484 m²',
           '486 m²', '489 m²', '492 m²', '494 m²', '497 m²', '500 m²', '502 m²', '505 m²', '508 m²', '510 m²',
           '513 m²', '516 m²', '518 m²', '521 m²', '524 m²', '526 m²', '529 m²', '532 m²', '534 m²', '537 m²',
           '540 m²', '542 m²', '545 m²', '548 m²', '550 m²', '553 m²', '556 m²', '558 m²', '561 m²', '564 m²',
           '566 m²', '569 m²', '572 m²', '574 m²', '577 m²', '580 m²', '582 m²', '585 m²', '588 m²', '590 m²',
           '593 m²', '596 m²', '598 m²', '601 m²', '604 m²', '606 m²', '609 m²', '612 m²', '614 m²', '617 m²',
           '620 m²', '622 m²', '625 m²', '628 m²', '630 m²', '633 m²', '636 m²', '638 m²', '641 m²', '644 m²',
           '646 m²', '649 m²', '652 m²', '654 m²', '657 m²', '660 m²', '662 m²', '665 m²', '668 m²', '670 m²',
           '673 m²', '676 m²', '678 m²', '681 m²', '684 m²', '686 m²', '689 m²', '692 m²', '694 m²', '697 m²',
           '700 m²', '702 m²', '705 m²', '708 m²', '710 m²', '713 m²', '716 m²', '718 m²', '721 m²', '724 m²',
           '726 m²', '729 m²', '732 m²', '734 m²', '737 m²', '740 m²', '742 m²', '745 m²', '748 m²', '750 m²',
           '753 m²', '756 m²', '758 m²', '761 m²', '764 m²', '766 m²', '769 m²', '772 m²', '774 m²', '777 m²',
           '780 m²', '782 m²', '785 m²', '788 m²', '790 m²', '793 m²', '796 m²', '798 m²', '801 m²', '804 m²',
           '806 m²', '809 m²', '812 m²', '814 m²', '817 m²', '820 m²', '822 m²', '825 m²', '828 m²', '830 m²',
           '833 m²', '836 m²', '838 m²', '841 m²', '844 m²', '846 m²', '849 m²', '852 m²', '854 m²', '857 m²',
           '860 m²', '862 m²', '865 m²', '868 m²', '870 m²', '873 m²', '876 m²', '878 m²', '881 m²', '884 m²',
           '886 m²', '889 m²', '892 m²', '894 m²', '897 m²', '900 m²', '902 m²', '905 m²', '908 m²', '910 m²',
           '913 m²', '916 m²', '918 m²', '921 m²', '924 m²', '926 m²', '929 m²', '932 m²', '934 m²', '937 m²',
           '940 m²', '942 m²', '945 m²', '948 m²', '950 m²', '953 m²', '956 m²', '958 m²', '961 m²', '964 m²',
           '966 m²', '969 m²', '972 m²', '974 m²', '977 m²', '980 m²', '982 m²', '985 m²', '988 m²', '990 m²',
           '993 m²', '996 m²', '998 m²', '1498 m²', '1998 m²', '2498 m²', '2998 m²', '3498 m²', '3998 m²', '4498 m²', '4998 m²']

    keyboard = []
    row = []

    for idx, item in enumerate(szz, start=1):
        row.append(KeyboardButton(text=item))

        # Har 4 ta bo‘lsa qatorga qo‘shamiz
        if idx % 4 == 0:
            keyboard.append(row)
            row = []

    # Qolganlari bo‘lsa — qo‘shamiz
    if row:
        keyboard.append(row)
        keyboard.append([
        KeyboardButton(text=_("back_rooms")),
        KeyboardButton(text=_("back_main"))
    ])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )


def generate_size_keyboard(i18n: I18nContext):
    keyboard = []
    row = []
    szz = ['20 m²', '22 m²', '25 m²', '28 m²', '30 m²', '33 m²', '36 m²', '38 m²', '41 m²', '44 m²', '46 m²', '49 m²',
           '52 m²', '54 m²', '57 m²', '60 m²', '62 m²', '65 m²', '68 m²', '70 m²', '73 m²', '76 m²', '78 m²', '81 m²',
           '84 m²', '86 m²', '89 m²', '92 m²', '94 m²', '97 m²', '100 m²', '102 m²', '105 m²', '108 m²', '110 m²',
           '113 m²', '116 m²', '118 m²', '121 m²', '124 m²', '126 m²', '129 m²', '132 m²', '134 m²', '137 m²',
           '140 m²', '142 m²', '145 m²', '148 m²', '150 m²', '153 m²', '156 m²', '158 m²', '161 m²', '164 m²',
           '166 m²', '169 m²', '172 m²', '174 m²', '177 m²', '180 m²', '182 m²', '185 m²', '188 m²', '190 m²',
           '193 m²', '196 m²', '198 m²', '201 m²', '204 m²', '206 m²', '209 m²', '212 m²', '214 m²', '217 m²',
           '220 m²', '222 m²', '225 m²', '228 m²', '230 m²', '233 m²', '236 m²', '238 m²', '241 m²', '244 m²',
           '246 m²', '249 m²', '252 m²', '254 m²', '257 m²', '260 m²', '262 m²', '265 m²', '268 m²', '270 m²',
           '273 m²', '276 m²', '278 m²', '281 m²', '284 m²', '286 m²', '289 m²', '292 m²', '294 m²', '297 m²',
           '300 m²', '302 m²', '305 m²', '308 m²', '310 m²', '313 m²', '316 m²', '318 m²', '321 m²', '324 m²',
           '326 m²', '329 m²', '332 m²', '334 m²', '337 m²', '340 m²', '342 m²', '345 m²', '348 m²', '350 m²',
           '353 m²', '356 m²', '358 m²', '361 m²', '364 m²', '366 m²', '369 m²', '372 m²', '374 m²', '377 m²',
           '380 m²', '382 m²', '385 m²', '388 m²', '390 m²', '393 m²', '396 m²', '398 m²', '401 m²', '404 m²',
           '406 m²', '409 m²', '412 m²', '414 m²', '417 m²', '420 m²', '422 m²', '425 m²', '428 m²', '430 m²',
           '433 m²', '436 m²', '438 m²', '441 m²', '444 m²', '446 m²', '449 m²', '452 m²', '454 m²', '457 m²',
           '460 m²', '462 m²', '465 m²', '468 m²', '470 m²', '473 m²', '476 m²', '478 m²', '481 m²', '484 m²',
           '486 m²', '489 m²', '492 m²', '494 m²', '497 m²', '500 m²', '502 m²', '505 m²', '508 m²', '510 m²',
           '513 m²', '516 m²', '518 m²', '521 m²', '524 m²', '526 m²', '529 m²', '532 m²', '534 m²', '537 m²',
           '540 m²', '542 m²', '545 m²', '548 m²', '550 m²', '553 m²', '556 m²', '558 m²', '561 m²', '564 m²',
           '566 m²', '569 m²', '572 m²', '574 m²', '577 m²', '580 m²', '582 m²', '585 m²', '588 m²', '590 m²',
           '593 m²', '596 m²', '598 m²', '601 m²', '604 m²', '606 m²', '609 m²', '612 m²', '614 m²', '617 m²',
           '620 m²', '622 m²', '625 m²', '628 m²', '630 m²', '633 m²', '636 m²', '638 m²', '641 m²', '644 m²',
           '646 m²', '649 m²', '652 m²', '654 m²', '657 m²', '660 m²', '662 m²', '665 m²', '668 m²', '670 m²',
           '673 m²', '676 m²', '678 m²', '681 m²', '684 m²', '686 m²', '689 m²', '692 m²', '694 m²', '697 m²',
           '700 m²', '702 m²', '705 m²', '708 m²', '710 m²', '713 m²', '716 m²', '718 m²', '721 m²', '724 m²',
           '726 m²', '729 m²', '732 m²', '734 m²', '737 m²', '740 m²', '742 m²', '745 m²', '748 m²', '750 m²',
           '753 m²', '756 m²', '758 m²', '761 m²', '764 m²', '766 m²', '769 m²', '772 m²', '774 m²', '777 m²',
           '780 m²', '782 m²', '785 m²', '788 m²', '790 m²', '793 m²', '796 m²', '798 m²', '801 m²', '804 m²',
           '806 m²', '809 m²', '812 m²', '814 m²', '817 m²', '820 m²', '822 m²', '825 m²', '828 m²', '830 m²',
           '833 m²', '836 m²', '838 m²', '841 m²', '844 m²', '846 m²', '849 m²', '852 m²', '854 m²', '857 m²',
           '860 m²', '862 m²', '865 m²', '868 m²', '870 m²', '873 m²', '876 m²', '878 m²', '881 m²', '884 m²',
           '886 m²', '889 m²', '892 m²', '894 m²', '897 m²', '900 m²', '902 m²', '905 m²', '908 m²', '910 m²',
           '913 m²', '916 m²', '918 m²', '921 m²', '924 m²', '926 m²', '929 m²', '932 m²', '934 m²', '937 m²',
           '940 m²', '942 m²', '945 m²', '948 m²', '950 m²', '953 m²', '956 m²', '958 m²', '961 m²', '964 m²',
           '966 m²', '969 m²', '972 m²', '974 m²', '977 m²', '980 m²', '982 m²', '985 m²', '988 m²', '990 m²',
           '993 m²', '996 m²', '998 m²', '1498 m²', '1998 m²', '2498 m²', '2998 m²', '3498 m²', '3998 m²', '4498 m²', '4998 m²']

    _ = i18n
    for i, size in enumerate(szz, 1):
        row.append(KeyboardButton(text=f"{szz}"))

        # Har 4 ta tugmadan keyin yangi qatorga o'tamiz
        if i % 4 == 0:
            keyboard.append(row)
            row = []

    # Qolgan tugmalarni ham qo'shamiz
    if row:
        keyboard.append(row)
        
    keyboard.append([
        KeyboardButton(text=_("back_rooms")),
        KeyboardButton(text=_("back_main"))
    ])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    
   
def tamir(i18n: I18nContext):
    
    _ = i18n
    
    return ReplyKeyboardMarkup(
        keyboard=[
        [   
            KeyboardButton(text=i18n("euro")),
            KeyboardButton(text=i18n("normal"))
        ],
        [
            KeyboardButton(text=i18n("without")),
            KeyboardButton(text=i18n("back_building"))
        ]
        ],
        resize_keyboard=True
    )
    
def make_jihozlar(i18n: I18nContext, msg):
    _ = i18n
    # Bosilgan tugmaning matni
    pressed = msg.text.strip() if msg and msg.text else None

    # Jihozlar ro‘yxati
    jihozlar = [
        i18n("quvur"),
        i18n("video"),
        i18n("internet"),
        i18n("wifi"),
        i18n("gaz"),
        i18n("suv"),
        i18n("air"),
        i18n("pech"),
        i18n("police"),
        i18n("child"),
        i18n("mebel"),
        i18n("vanna"),
        i18n("wash"),
        i18n("lift"),
        i18n("parking"),
    ]

    # Bosilgan tugmani ro‘yxatdan olib tashlash
    if pressed in jihozlar:
        jihozlar.remove(pressed)

    # 4 ustunli keyboard yasash
    keyboard = []
    row = []

    for idx, item in enumerate(jihozlar, start=1):
        row.append(KeyboardButton(text=item))

        if idx % 4 == 0:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    # Oxiriga Back tugmalarini qo‘shish
    keyboard.append([
        KeyboardButton(text=_("back_rooms")),
        KeyboardButton(text=_("back_main")),
    ])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )


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

    # kb = make_keyboard(ANDIJON_DISTRICTS)
    # return kb


