from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher()

kb = [[types.KeyboardButton(text='Рассчитать'), types.KeyboardButton(text='Информация')], ]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, )

ikb = [[types.InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
        types.InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]]
inlinekeyboard = types.InlineKeyboardMarkup(inline_keyboard=ikb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command('start'))
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup=keyboard)


@dp.message(F.text == 'Рассчитать')
async def main_menu(message):
    await message.answer('выберите опцию', reply_markup=inlinekeyboard)


@dp.callback_query(F.data == 'formulas')
async def get_formulas(callback: types.CallbackQuery):
    await callback.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


@dp.callback_query(F.data == 'calories')
async def set_age(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('введите свой возраст', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
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
    await state.update_data(weight=float(message.text))
    data = await state.get_data()
    res = str(data['weight'] * 10 + 6.25 * data['growth'] + 5 * data['age'] + 5)
    await message.answer(text=f'ваша норма калорий {res}ККал')
    await state.clear()


@dp.message()
async def all_message(message: types.Message):
    await message.answer('чтобы начать общение, введите /start')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
