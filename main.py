import asyncio
import logging
import sys
from os import getenv
from button import *
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv
from texts import *
from StateRegister import *
from aiogram.fsm.context import FSMContext
from database import *



load_dotenv()

TOKEN = getenv('BOT_TOKEN')

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    
    await message.answer(f"Assalomu aleykum, {html.bold(message.from_user.full_name)}!\nBotga xush kelibsiz", reply_markup=menu)
@dp.message(F.text == 'ℹ️ Biz haqimizda')
async def select_button(message: Message):

    await message.answer(about_us, reply_markup=back_btn)
async def set_state_with_history(state: FSMContext, new_state, name_state):
    data = await state.get_data()

    history = data.get("history", [])
    current_state = await state.get_state()

    if current_state:
        history.append(current_state)

    await state.update_data(history=history)
    await state.set_state(new_state)
@dp.message(F.text == "⬅️Orqaga")
async def go_back(message: Message, state: FSMContext):

    data = await state.get_data()
    history = data.get("history", [])

    if not history:
        await message.answer("Iltimos kerakli bo'limni tanlang: ", reply_markup=menu)
        return

    prev_state = history.pop()

    await state.update_data(history=history)
    await state.set_state(prev_state)
    state_name = await state.get_state()
    key_state = state_name.split(":")[-1]
    if (key_state == "phone_number"):
        await message.answer(f"Oldingi bosqichga qaytdik: {state_titles[key_state]}", reply_markup=phone_kb)
    elif (key_state == "partner"):
        await message.answer(f"Oldingi bosqichga qaytdik: {state_titles[key_state]}", reply_markup=accept_keyboard)
    else:
        await message.answer(f"Oldingi bosqichga qaytdik: {state_titles[key_state]}")
@dp.message((F.text == '⬅️Bosh menyuga') | (F.text == "Bekor qilish!"))
async def back_button(message: Message):

    await message.answer("Iltimos kerakli bo'limni tanlang: ", reply_markup=menu)
@dp.message(F.text == "📝 So‘rovnoma")
async def start_register(message: Message, state: FSMContext):
    
    await message.answer("\nTo'liq ismingizni kiriting:")
    
    await state.set_state(RegisterState.full_name)

#Full name get function
@dp.message(RegisterState.full_name)
async def get_fullName(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)

    await message.answer("Telefon raqamingizni kiriting:", reply_markup=phone_kb)

    await state.set_state(RegisterState.phone_number)

#Phone number get function

@dp.message(RegisterState.phone_number)
async def get_phoneNumber(message: Message, state: FSMContext):

    await state.update_data(phone_number=message.text)
    await message.answer("Loyihangiz haqida ma'lumot bering: ", reply_markup=request_buttons)
    await set_state_with_history(state, RegisterState.about_project, "Telefon nomerni kiritish")

@dp.message(RegisterState.about_project)
async def get_about_project(message: Message, state: FSMContext):

    
    await state.update_data(about_project=message.text)
    await message.answer("Qancha vaqtda beri faoliyat yuritasiz? ", reply_markup=request_buttons)
    await set_state_with_history(state, RegisterState.active_time, "Telefon nomerni kiritish")

@dp.message(RegisterState.active_time)
async def get_active_time(message: Message, state: FSMContext):

    await state.update_data(active_time=message.text)
    await message.answer("Daromadingiz oylik yoki yillik?", reply_markup=request_buttons)
    await set_state_with_history(state, RegisterState.income, "Telefon nomerni kiritish")
@dp.message(RegisterState.income)
async def get_income(message: Message, state: FSMContext):

    await state.update_data(income=message.text)
    await message.answer("Sherikchilikda ishlab kop'rganmisiz?", reply_markup=accept_keyboard)
    await set_state_with_history(state, RegisterState.partner, "Telefon nomerni kiritish")

@dp.callback_query(RegisterState.partner)
async def get_partner(callback: CallbackQuery, state: FSMContext):

    await state.update_data(partner=callback.data)
    await callback.message.answer("Nima sababdan investitsiyaga muhtojsiz?", reply_markup=request_buttons)
    await set_state_with_history(state, RegisterState.need_invest, "Telefon nomerni kiritish")

@dp.message(RegisterState.need_invest)
async def get_need_invest(message: Message, state: FSMContext):

    await state.update_data(need_invest=message.text)
    await message.answer("Investitsiya olgan mablagini qayerga sarflamoqchisiz?", reply_markup=request_buttons)
    await set_state_with_history(state, RegisterState.spend, "Telefon nomerni kiritish")

@dp.message(RegisterState.spend)
async def get_spend(message: Message, state: FSMContext):

    await state.update_data(spend=message.text)
    await message.answer("Qancha vaqtda bu mablag'ni qaytara olasiz?", reply_markup=request_buttons)
    await set_state_with_history(state, RegisterState.return_time, "Telefon nomerni kiritish")

@dp.message(RegisterState.return_time)
async def get_return_time(message: Message, state: FSMContext):

    await state.update_data(return_time=message.text)
    await message.answer("Investitsiya olgandan keyn daromadi nechi barobarga kopayadi?", reply_markup=request_buttons)
    await set_state_with_history(state, RegisterState.multiply_income, "Telefon nomerni kiritish")


@dp.message(RegisterState.multiply_income)
async def get_multiply_income(message: Message, state: State):

    await state.update_data(multiply_income=message.text)
    await message.answer("Investor sizga qancha vaqt imtiyozli davr qilib berishini xoxlaysiz?", reply_markup=request_buttons)
    await set_state_with_history(state, RegisterState.privilege_time, "Telefon nomerni kiritish")

@dp.message(RegisterState.privilege_time)
async def get_privilege_time(message: Message, state: State):

    await state.update_data(privilege_time=message.text)
    await message.answer("Investorga qanaqa qulay takliflar bera oladi?", reply_markup=request_buttons)
    await set_state_with_history(state, RegisterState.can_suggest, "Telefon nomerni kiritish")


@dp.message(RegisterState.can_suggest)
async def get_Can_suggest(message: Message, state: FSMContext):

    await state.update_data(can_suggest=message.text)
    await message.answer(accept_text, reply_markup=accept_keyboard)
    await set_state_with_history(state, RegisterState.is_accept, "Telefon nomerni kiritish")

@dp.callback_query(RegisterState.is_accept)
async def get_is_accept(callback: CallbackQuery, state: FSMContext):
    
    await state.update_data(is_accept=callback.data)
    data = await state.get_data()
    data['user_id'] = callback.from_user.id

    if (data['is_accept'] == 'yes'):
        save_user(data)
    
    await callback.message.answer("So'rovnomamizda qatnashganingizdan minnatdormiz!", reply_markup=back_btn)

async def main() -> None:
    
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())