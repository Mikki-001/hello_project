"""Bot handlers for commands and message responses."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from bot.services.chinese import build_quiz_question, check_answer, get_random_word


@dataclass
class QuizState:
    correct_answer: str
    total: int = 0
    score: int = 0


QUIZ_STORAGE: Dict[int, QuizState] = {}


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [["/word", "/quiz"], ["/help"]]
    await update.message.reply_text(
        "Привет! Я бот для изучения китайского (HSK1).\n"
        "Выбери формат обучения:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start — приветствие и меню\n"
        "/word — случайное слово\n"
        "/quiz — мини-викторина\n"
        "/help — список команд"
    )


async def word_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    word = get_random_word()
    await update.message.reply_text(
        f"🀄 Слово дня:\n{word['hanzi']}\nPinyin: {word['pinyin']}\nПеревод: {word['translation']}"
    )


async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    question = build_quiz_question()
    state = QUIZ_STORAGE.get(user_id)
    if state is None:
        state = QuizState(correct_answer=question["correct_answer"])
        QUIZ_STORAGE[user_id] = state
    else:
        state.correct_answer = question["correct_answer"]

    options_keyboard = [[option] for option in question["options"]]
    await update.message.reply_text(
        question["question"],
        reply_markup=ReplyKeyboardMarkup(options_keyboard, resize_keyboard=True, one_time_keyboard=True),
    )


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    user_text = update.message.text
    state = QUIZ_STORAGE.get(user_id)

    if state is None:
        await update.message.reply_text("Используй /word или /quiz, чтобы начать обучение.")
        return

    state.total += 1
    if check_answer(user_text, state.correct_answer):
        state.score += 1
        await update.message.reply_text(
            f"✅ Верно! Твой счет: {state.score}/{state.total}.\nНапиши /quiz для следующего вопроса."
        )
    else:
        await update.message.reply_text(
            "❌ Неверно. "
            f"Правильный ответ: {state.correct_answer}.\n"
            f"Твой счет: {state.score}/{state.total}.\n"
            "Напиши /quiz для следующего вопроса."
        )
