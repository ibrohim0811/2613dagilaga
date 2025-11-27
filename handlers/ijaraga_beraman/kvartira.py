from aiogram import types, F
from aiogram_i18n import I18nContext
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import I18n

from keyboard.default import time_kv

from middlewares.i18n import i18n_middleware
from aiogram_i18n.context import I18nContext
from states.state import I_b_kvartira
from keyboard.default import ijaraga_beraman, tuman, persons,  generate_size_keyboard, tamir, make_jihozlar, make_szz_keyboard


dp = Router()


# @dp.message(lambda message, i18n: message.text == i18n("ijara_b"))
# async def ijaraga_b(msg: types.Message, i18n: I18nContext):
#     await msg.answer(i18n("select_section"), reply_markup=ijaraga_beraman(i18n))

@dp.message(lambda message, i18n: message.text == i18n("back"))
async def back(msg: types.Message, i18n: I18nContext):
    await msg.answer(i18n("back_1"), reply_markup=ijaraga_beraman(i18n))

@dp.message(lambda message, i18n: message.text == i18n("ijara_b"))
async def kv_start(msg: types.Message, i18n: I18nContext, state: FSMContext):    
    await state.set_state(I_b_kvartira.house_name)
    await msg.answer(i18n("bino_s"), reply_markup=ijaraga_beraman(i18n))


@dp.message(I_b_kvartira.house_name)
async def st_time(msg: types.Message, i18n: I18nContext, state: FSMContext):
    buttons = [
        i18n("flat"),
        i18n("house"),
        i18n("dacha"),
        i18n("office"),
        i18n("back_main")
    ]
    if msg.text in buttons:
        await state.update_data(house_name = msg.text)
        await state.set_state(I_b_kvartira.time)
        await msg.answer(i18n("muddat"), reply_markup=time_kv(i18n))
    else:
        await msg.answer(i18n("err_button"))
        await state.set_state(I_b_kvartira.house_name)
        await msg.answer(i18n("bino_s"), reply_markup=ijaraga_beraman(i18n))

 
@dp.message(I_b_kvartira.time)
async def time(msg: types.Message, i18n: I18nContext, state: FSMContext):
    check_btn = [
        i18n("long_time"),
        i18n("daily")
    ]
    if msg.text in check_btn:
        await state.update_data(time = msg.text)
        await state.set_state(I_b_kvartira.district)
        await msg.answer(i18n("tuman"), reply_markup=tuman(i18n))
    else:
        await msg.answer(i18n("err_button"))
        await state.set_state(I_b_kvartira.time)
        await msg.answer(i18n("muddat"), reply_markup=time_kv(i18n))
        
@dp.message(I_b_kvartira.district)
async def disrict(msg: types.Message, i18n: I18nContext, state: FSMContext):
    check = [
    i18n("bektemir"),
    i18n("chilonzor"),
    i18n("yashnobod"),
    i18n("mirzo"),
    i18n("mirobod"),
    i18n("olmazor"),
    i18n("sergeli"),
    i18n("shayxon"),
    i18n("uchtepa"),
    i18n("yakkasaroy"),
    i18n("yunus"),
    i18n("yangihayot")
]
    if msg.text in check:
        await state.update_data(tuman_ = msg.text)
        await state.set_state(I_b_kvartira.who)
        await msg.answer(i18n("who"), reply_markup=persons(i18n))
    else:
        await msg.answer(i18n("err_button"))
        await state.set_state(I_b_kvartira.district)
        await msg.answer(i18n("tuman"), reply_markup=tuman(i18n))
        
@dp.message(I_b_kvartira.who)
async def room(msg: types.Message, i18n: I18nContext, state: FSMContext):
    humans = [
        i18n("students"),
        i18n("workers"),
        i18n("travels"),
        i18n("family"),
        i18n("friend"),
        i18n("all")
    ]
    if msg.text in humans:
        await state.update_data(kimga = msg.text)
        await state.set_state(I_b_kvartira.size)
        await msg.answer(i18n("olcham"), reply_markup=make_szz_keyboard(i18n))
    else:
        await msg.answer(i18n("err_button"))
        await state.set_state(I_b_kvartira.who)
        await msg.answer(i18n("who"), reply_markup=persons(i18n))
        
@dp.message(I_b_kvartira.size)
async def room_size(msg: types.Message, i18n: I18nContext, state: FSMContext):
    
    sizes = [20, 22, 25, 28, 30, 33, 36, 38, 41, 44, 46, 49, 52, 54, 57, 60, 62, 65, 68, 70, 73, 76, 78, 81, 84, 86, 89, 92, 94, 97, 100, 102, 105, 108, 110, 113, 116, 118, 121, 124, 126, 129, 132, 134, 137, 140, 142, 145, 148, 150, 153, 156, 158, 161, 164, 166, 169, 172, 174, 177, 180, 182, 185, 188, 190, 193, 196, 198, 201, 204, 206, 209, 212, 214, 217, 220, 222, 225, 228, 230, 233, 236, 238, 241, 244, 246, 249, 252, 254, 257, 260, 262, 265, 268, 270, 273, 276, 278, 281, 284, 286, 289, 292, 294, 297, 300, 302, 305, 308, 310, 313, 316, 318, 321, 324, 326, 329, 332, 334, 337, 340, 342, 345, 348, 350, 353, 356, 358, 361, 364, 366, 369, 372, 374, 377, 380, 382, 385, 388, 390, 393, 396, 398, 401, 404, 406, 409, 412, 414, 417, 420, 422, 425, 428, 430, 433, 436, 438, 441, 444, 446, 449, 452, 454, 457, 460, 462, 465, 468, 470, 473, 476, 478, 481, 484, 486, 489, 492, 494, 497, 500, 502, 505, 508, 510, 513, 516, 518, 521, 524, 526, 529, 532, 534, 537, 540, 542, 545, 548, 550, 553, 556, 558, 561, 564, 566, 569, 572, 574, 577, 580, 582, 585, 588, 590, 593, 596, 598, 601, 604, 606, 609, 612, 614, 617, 620, 622, 625, 628, 630, 633, 636, 638, 641, 644, 646, 649, 652, 654, 657, 660, 662, 665, 668, 670, 673, 676, 678, 681, 684, 686, 689, 692, 694, 697, 700, 702, 705, 708, 710, 713, 716, 718, 721, 724, 726, 729, 732, 734, 737, 740, 742, 745, 748, 750, 753, 756, 758, 761, 764, 766, 769, 772, 774, 777, 780, 782, 785, 788, 790, 793, 796, 798, 801, 804, 806, 809, 812, 814, 817, 820, 822, 825, 828, 830, 833, 836, 838, 841, 844, 846, 849, 852, 854, 857, 860, 862, 865, 868, 870, 873, 876, 878, 881, 884, 886, 889, 892, 894, 897, 900, 902, 905, 908, 910, 913, 916, 918, 921, 924, 926, 929, 932, 934, 937, 940, 942, 945, 948, 950, 953, 956, 958, 961, 964, 966, 969, 972, 974, 977, 980, 982, 985, 988, 990, 993, 996, 998, 1498, 1998, 2498, 2998, 3498, 3998, 4498, 4998]       
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
    if msg.text in szz:
        await state.update_data(mkv = msg.text)
        await state.set_state(I_b_kvartira.tamir)
        await msg.answer(i18n("tamir"), reply_markup=tamir(i18n))
    else:
        await msg.answer(i18n("err_button"))
        await state.set_state(I_b_kvartira.size)
        await msg.answer(i18n("olcham"))
        
@dp.message(I_b_kvartira.tamir)
async def building(msg: types.Message, i18n: I18nContext, state: FSMContext):
    buttons = [
        i18n("euro"),
        i18n("normal"),
        i18n("without"),
        i18n("back_building")
    ]
    
    if msg.text in buttons:
        await state.update_data(building_ = msg.text)
        await state.set_state(I_b_kvartira.image)
        await msg.answer(i18n("send_img"))
    else:
        await msg.answer(i18n("err_button"))
        await state.set_state(I_b_kvartira.tamir)
        await msg.answer(i18n("tamir"), reply_markup=tamir(i18n))
        
@dp.message(I_b_kvartira.image, F.photo)
async def get_img(msg: types.Message, i18n: I18nContext, state: FSMContext):
    image = msg.photo[-1].file_id
    xabar = msg.text
    await state.update_data(img = image)
    await state.set_state(I_b_kvartira.price)
    await msg.answer(i18n("things"), reply_markup=make_jihozlar(i18n, xabar))
    
@dp.message(I_b_kvartira.image)
async def check_img(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("err_image"))
    await state.set_state(I_b_kvartira.image)
    await msg.answer(i18n("send_img"))
    
# @dp.message(I_b_kvartira.price)
# async def narx(msg: types.Message, i18n: I18nContext, state: FSMContext):
    
    
    
    
    
        
# @dp.message(I_b_kvartira.time)
# async def region(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     time_h = msg.text
#     await state.update_data(time = time_h)
#     await state.set_state(I_b_kvartira.region)
#     await msg.answer(i18n("viloyat"), reply_markup=make_regions_keyboard(i18n))
    


# @dp.message(I_b_kvartira.region)
# async def reg(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     region_ = msg.text
#     await state.update_data(tuman = region_)
#     await state.set_state(I_b_kvartira.district)
#     await msg.answer(i18n("tuman"))
    
# @dp.message(I_b_kvartira.district)
# async def tuman(msg: types.Message, state: FSMContext, i18n: I18nContext):
#     None
    

#i18n qilish oxirgacha bitirish kerak