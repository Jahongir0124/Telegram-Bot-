from aiogram.fsm.state import State, StatesGroup


class RegisterState(StatesGroup):

    full_name = State()
    phone_number = State()
    about_project = State()
    active_time = State()
    income = State()
    partner = State()
    need_invest = State()
    spend = State()
    return_time = State()
    multiply_income = State()
    privilege_time = State()
    can_suggest = State()
    is_accept = State()
    


state_titles = {
    "full_name": "To'liq ismingizni kiriting:",
    "phone_number": "Telefon raqamingizni kiriting:",
    "about_project": "Loyihangiz haqida ma'lumot bering:",
    "active_time": "Qancha vaqtda beri faoliyat yuritasiz?",
    "income": "Daromadingiz oylik yoki yillik?",
    "partner": "Sherikchilikda ishlab kop'rganmisiz?",
    "need_invest": "Nima sababdan investitsiyaga muhtojsiz?",
    "spend": "Investitsiya olgan mablagini qayerga sarflamoqchisiz?",
    "return_time": "Qancha vaqtda bu mablag'ni qaytara olasiz?",
    "multiply_income": "Investitsiya olgandan keyn daromadi nechi barobarga kopayadi?",
    "privilege_time": "Investor sizga qancha vaqt imtiyozli davr qilib berishini xoxlaysiz?",
    "can_suggest": "Investorga qanaqa qulay takliflar bera oladi?",
    
}


