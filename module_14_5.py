from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
import crud_functions

api = ''
bot = Bot(token=api)
dp = Dispatcher()

kb = [[types.KeyboardButton(text='Рассчитать'), types.KeyboardButton(text='Информация')],
      [types.KeyboardButton(text='Купить'), types.KeyboardButton(text='Регистрация')]]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, )

ikb = [[types.InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
        types.InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]]
inlinekeyboard = types.InlineKeyboardMarkup(inline_keyboard=ikb)

buyikb = [[types.InlineKeyboardButton(text='product1',callback_data='product_buying'),
           types.InlineKeyboardButton(text='product2',callback_data='product_buying'),
           types.InlineKeyboardButton(text='product3',callback_data='product_buying'),
           types.InlineKeyboardButton(text='product4',callback_data='product_buying')]]
inline_buy_kb = types.InlineKeyboardMarkup(inline_keyboard=buyikb)

products = crud_functions.get_all_products()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

@dp.message(Command('start'))
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup=keyboard)


@dp.message(F.text == 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=inlinekeyboard)


@dp.callback_query(F.data == 'formulas')
async def get_formulas(callback: types.CallbackQuery):
    await callback.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


@dp.callback_query(F.data == 'calories')
async def set_age(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите свой возраст', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=float(message.text))
    data = await state.get_data()
    res = str(data['weight'] * 10 + 6.25 * data['growth'] + 5 * data['age'] + 5)
    await message.answer(text=f'Ваша норма калорий {res}ККал',reply_markup=keyboard)
    await state.clear()

@dp.message(F.text == 'Купить')
async def get_buying_list(message):
    for product in products:
        img = types.FSInputFile(product[4])
        result = await message.answer_photo(
            img,
            caption=f'Название:{product[1]}|Описание:{product[2]}|Цена:{product[3]} '
        )
    await message.answer(text='Выберите товар',reply_markup=inline_buy_kb)

@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(callback: types.CallbackQuery):
    await callback.message.answer('Вы успешно приобрели продукт!')

@dp.message(F.text == "Регистрация")
async def register_username(message:types.Message,state:FSMContext):
    await message.answer('Введите имя пользователя',reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(RegistrationState.username)

@dp.message(RegistrationState.username)
async def register_email(message:types.Message,state:FSMContext):
    if crud_functions.is_included(message.text):
        await message.answer('Такой пользователь уже существует. Введите другое имя')
    else:
        await state.update_data(username = message.text)
        await message.answer('Введите свой адрес электронной почты')
        await state.set_state(RegistrationState.email)

@dp.message(RegistrationState.email)
async def register_age(message:types.Message,state:FSMContext):
    await state.update_data(email = message.text)
    await message.answer('Введите свой возраст')
    await state.set_state(RegistrationState.age)

@dp.message(RegistrationState.age)
async def register_balance(message:types.Message,state:FSMContext):
    await state.update_data(age = message.text)
    await state.update_data(balance = 1000)
    userdata = await state.get_data()
    crud_functions.add_user(userdata['username'],userdata['email'],userdata['age'],userdata['balance'])
    await message.answer(f'Поздравляем,{userdata['username']}! Регистрация завершена. Ваш баланс "1000"',
                         reply_markup=keyboard)
    await state.clear()


@dp.message()
async def all_message(message: types.Message):
    await message.answer('Чтобы начать общение, введите /start')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
