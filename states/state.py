from aiogram.fsm.state import State, StatesGroup

class I_b_kvartira(StatesGroup):
    house_name = State()
    time = State()
    region = State()
    district = State()
    who = State()
    room = State()
    size = State()
    tamir = State()
    image = State()
    price = State()
    makler = State()
    phone = State()
    description = State()
    sorov = State()
    