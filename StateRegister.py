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
   
    
}


