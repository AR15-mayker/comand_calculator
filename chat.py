import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    user_name = message.from_user.first_name
    welcome_text = (
        f"🔢 Привет, {user_name}! Я — бот-калькулятор. 🧮\n\n"
        "Просто напиши мне математическое выражение (например, '2+2', '5*3' или '10/2'), "
        "и я мгновенно решу его! 😊\n\n"
    )
    await message.answer(welcome_text)


@dp.message()
async def calculate(message: Message):
    try:
        expression = message.text
        expression = expression.replace("^", "**")  # Поддержка степеней
        result = eval(expression)  # Вычисление (опасно без валидации!)
        await message.answer(f"✅ Результат: {result}")
    except ZeroDivisionError:
        await message.answer("❌ Ошибка: деление на ноль!")
    except Exception:
        await message.answer("❌ Ошибка: некорректный ввод. Пример: '2+2' или '5*3'")
