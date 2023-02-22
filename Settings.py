from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = '-'
"""@transport_innovations_bot"""
kb_mm = ['Заполнить заявку', 'Справка']
MainMenu = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*kb_mm)
kb_mam = ['Список вопросов', 'Добавить вопрос', 'Изменить вопрос', 'Удалить вопрос', 'Добавить/Удалить админа', 'Список админов', 'Главное меню']
MainAdminMenu = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*kb_mam)
kb_am = ['Список вопросов', 'Добавить вопрос', 'Изменить вопрос', 'Удалить вопрос', 'Главное меню']
AdminMenu = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*kb_am)
GoToQuestions = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data="Yes"), InlineKeyboardButton(text="Нет", callback_data="No")
        ]
    ])
MainAdmin = ["843356160"]
kb_sa = ['Отменить действие']
AdminStopKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*kb_sa)
