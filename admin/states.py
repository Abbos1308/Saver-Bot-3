from aiogram.fsm.state import State, StatesGroup

class AdminState(StatesGroup):
    base = State()
    add_channel = State()
    statistika = State()
    reklama = State()
    confirm = State()