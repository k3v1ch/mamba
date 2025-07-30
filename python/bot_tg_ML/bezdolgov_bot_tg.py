from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import joblib
import numpy as np
import logging

API_TOKEN = '7500425339:AAHYezqRBvd1wJyH27J02Xp5QuRvGZZw3wE'

# Загрузка модели
model = joblib.load('C:/Users/viplu/OneDrive/Desktop/GitHub/mamba/python/bot_tg_ML/model.pkl')

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Словарь для хранения данных пользователей
user_data = {}

# Очерёдность признаков
features_order = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                  'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# Подсказки
prompts = {
    'sex': "Выберите пол:",
    'age': "Введите ваш возраст:",
    'cp': "Выберите тип боли в груди:",
    'trestbps': "Введите артериальное давление в покое (мм рт.ст):",
    'chol': "Введите уровень холестерина (мг/дл):",
    'fbs': "Уровень сахара натощак > 120 мг/дл?",
    'restecg': "Выберите результат ЭКГ в покое:",
    'thalach': "Введите максимальную достигнутую ЧСС:",
    'exang': "Была ли стенокардия при нагрузке?",
    'oldpeak': "Введите показатель ST-понижения:",
    'slope': "Выберите форму кривой ST:",
    'ca': "Введите количество сосудов (0–3):",
    'thal': "Выберите тип талассемии:"
}

# Клавиатуры
def get_binary_kb(feature, yes="Да", no="Нет"):
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(yes, callback_data=f"{feature}_1"),
        InlineKeyboardButton(no, callback_data=f"{feature}_0")
    )

def get_cp_kb():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Типичная стенокардия", callback_data="cp_0"),
        InlineKeyboardButton("Атипичная стенокардия", callback_data="cp_1"),
        InlineKeyboardButton("Неангинальная боль", callback_data="cp_2"),
        InlineKeyboardButton("Асимптоматично", callback_data="cp_3")
    )

def get_restecg_kb():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Норма", callback_data="restecg_0"),
        InlineKeyboardButton("Отклонения ST-T", callback_data="restecg_1"),
        InlineKeyboardButton("Гипертрофия ЛЖ", callback_data="restecg_2")
    )

def get_slope_kb():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Восходящий", callback_data="slope_0"),
        InlineKeyboardButton("Горизонтальный", callback_data="slope_1"),
        InlineKeyboardButton("Нисходящий", callback_data="slope_2")
    )

def get_thal_kb():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Норма", callback_data="thal_1"),
        InlineKeyboardButton("Фиксированный дефект", callback_data="thal_2"),
        InlineKeyboardButton("Обратимый дефект", callback_data="thal_3")
    )

# Опрашиваем следующую недостающую характеристику
async def ask_next_question(user_id):
    user_features = user_data[user_id]
    for feature in features_order:
        if feature not in user_features:
            if feature == 'sex':
                return prompts[feature], get_binary_kb('sex', 'Мужчина', 'Женщина')
            elif feature == 'cp':
                return prompts[feature], get_cp_kb()
            elif feature == 'fbs':
                return prompts[feature], get_binary_kb('fbs')
            elif feature == 'restecg':
                return prompts[feature], get_restecg_kb()
            elif feature == 'exang':
                return prompts[feature], get_binary_kb('exang')
            elif feature == 'slope':
                return prompts[feature], get_slope_kb()
            elif feature == 'thal':
                return prompts[feature], get_thal_kb()
            else:
                return prompts[feature], None
    return None, None

# Проверка — все ли признаки собраны
def is_all_data_collected(user_id):
    return len(user_data.get(user_id, {})) == len(features_order)

# Выдача предсказания
async def send_prediction(user_id):
    features = [user_data[user_id][f] for f in features_order]
    prediction = model.predict([features])[0]
    if prediction == 1:
        await bot.send_message(user_id, "⚠️ Есть риск сердечного заболевания.")
    else:
        await bot.send_message(user_id, "✅ Вероятно, ваше сердце в порядке.")

# Старт
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_data[message.from_user.id] = {}
    text, kb = await ask_next_question(message.from_user.id)
    await message.answer(text, reply_markup=kb)

# Обработка кнопок
@dp.callback_query_handler(lambda c: '_' in c.data)
async def callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {}

    key, value = callback_query.data.split('_')
    user_data[user_id][key] = int(value)

    await bot.answer_callback_query(callback_query.id)

    if is_all_data_collected(user_id):
        await send_prediction(user_id)
    else:
        text, kb = await ask_next_question(user_id)
        await bot.send_message(user_id, text, reply_markup=kb)

# Обработка числовых текстовых ответов
@dp.message_handler()
async def message_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        await message.answer("Введите /start для начала.")
        return

    for feature in features_order:
        if feature not in user_data[user_id] and feature not in ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']:
            try:
                value = float(message.text)
                user_data[user_id][feature] = value
                if is_all_data_collected(user_id):
                    await send_prediction(user_id)
                else:
                    text, kb = await ask_next_question(user_id)
                    await message.answer(text, reply_markup=kb)
            except ValueError:
                await message.answer("Пожалуйста, введите корректное число.")
            break
        # Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

