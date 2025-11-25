from aiogram import types, F
from aiogram_i18n import I18nContext
from aiogram import Router
from aiogram.fsm.context import FSMContext

from keyboard.default import time_kv

from middlewares.i18n import i18n_middleware
from aiogram_i18n.context import I18nContext
from states.state import I_b_kvartira
from keyboard.default import ijaraga_beraman, make_regions_keyboard, fargona, namangan, navoi, andijon, buxoro, surxondaryo, sirdaryo, qoraqalpogiston, xorazm, toshkent_sh, toshkent_vil, jizzax, qashqadaryo, samarqand


dp = Router()

# @dp.message(lambda message, i18n: message.text == i18n("ijara_b"))
# async def ijaraga_b(msg: types.Message, i18n: I18nContext):
#     await msg.answer(i18n("select_section"), reply_markup=ijaraga_beraman(i18n))


@dp.message(lambda message, i18n: message.text == i18n("ijara_b"))
async def kv_start(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.set_state(I_b_kvartira.house_name)
    await msg.answer(i18n("bino_s"), reply_markup=ijaraga_beraman(i18n))
    
    
    
@dp.message(I_b_kvartira.house_name)
async def st_time(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(house_name = msg.text)
    await state.set_state(I_b_kvartira.time)
    await msg.answer(i18n("muddat"), reply_markup=time_kv(i18n))
    # 
    # 
    
@dp.message(I_b_kvartira.time)
async def region(msg: types.Message, i18n: I18nContext, state: FSMContext):
    time_h = msg.text
    await state.update_data(time = time_h)
    await state.set_state(I_b_kvartira.region)
    await msg.answer(i18n("viloyat"), reply_markup=make_regions_keyboard(i18n))
    
@dp.message(F.text == "Andijon")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=andijon())
    
@dp.message(F.text == "Buxoro")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=buxoro())

@dp.message(F.text == "Farg'ona")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=fargona())
    
@dp.message(F.text == "Jizzax")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=jizzax())

@dp.message(F.text == "Namangan")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=namangan())
    
@dp.message(F.text == "Navoiy")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=navoi())
    
@dp.message(F.text == "Qashqadaryo")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=qashqadaryo())
    
@dp.message(F.text == "Qoraqalpog'iston")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=qoraqalpogiston())
    
@dp.message(F.text == "Samarqand")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=samarqand())
    
@dp.message(F.text == "Sirdaryo")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=sirdaryo())
    
@dp.message(F.text == "Surxondaryo")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=surxondaryo())
    
@dp.message(F.text == "Toshkent vil.")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=toshkent_vil())
    
@dp.message(F.text == "Xorazm")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=xorazm())
    
@dp.message(F.text == "Toshkent sh.")
async def andj(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"), reply_markup=toshkent_sh())

@dp.message(I_b_kvartira.region)
async def reg(msg: types.Message, i18n: I18nContext, state: FSMContext):
    region_ = msg.text
    await state.update_data(tuman = region_)
    await state.set_state(I_b_kvartira.district)
    await msg.answer(i18n("tuman"))
    
# @dp.message(I_b_kvartira.district)
# async def tuman(msg: types.Message, state: FSMContext, i18n: I18nContext):
#     None
    

