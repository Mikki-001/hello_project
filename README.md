# Chinese Learning Telegram Bot

Простой Telegram-бот для изучения китайских слов уровня HSK1.

## 1) Создание бота через BotFather

1. Открой Telegram и найди `@BotFather`.
2. Отправь команду `/newbot`.
3. Укажи имя бота и уникальный username (должен оканчиваться на `bot`).
4. Скопируй выданный токен.

## 2) Настройка окружения

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Открой `.env` и подставь настоящий токен в `TELEGRAM_BOT_TOKEN`.

## 3) Запуск

```bash
python -m bot.main
```

## Команды бота

- `/start` — приветствие и меню
- `/word` — случайное китайское слово
- `/quiz` — мини-викторина
- `/help` — список команд

## Тесты

```bash
pytest
```
