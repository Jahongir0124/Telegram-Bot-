from aiogram.types import *     

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ℹ️ Biz haqimizda")],
        [KeyboardButton(text="📝 So‘rovnoma")]
    ],
    resize_keyboard=True
)


back_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='⬅️Bosh menyuga')]
    ],
    resize_keyboard=True
)


request_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅️Orqaga")],
        [KeyboardButton(text="Bekor qilish!")]
    ],
    resize_keyboard=True
)


accept_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Ha",
                callback_data="yes"
            ),
            InlineKeyboardButton(
                text="❌ Yo'q",
                callback_data="no"
            )
        ]
    ]
)


phone_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📱 Telefon raqamni yuborish",
                request_contact=True
            )
        ],
        [KeyboardButton(text="⬅️Orqaga")],
        [KeyboardButton(text="Bekor qilish!")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)