from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command('start'))
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.\n'
                         'для расчета калорий введите /calories')


@dp.message(Command('calories'))
async def set_age(message:types.Message, state:FSMContext):
    await message.answer('введите свой возраст')
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message:types.Message, state:FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('введите свой рост')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('введите свой вес')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    res=str(data['weight']*10+6.25*data['growth']+5*data['age']+5)
    await message.answer(text=f'ваша норма калорий {res}ККал')
    await state.clear()


@dp.message()
async def all_message(message: types.Message):
    await message.answer('чтобы начать общение, введите /start')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
