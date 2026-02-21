"""Chinese learning content and quiz logic."""

from __future__ import annotations

import random
from typing import Dict, List

Word = Dict[str, str]

HSK1_WORDS: List[Word] = [
    {"hanzi": "你好", "pinyin": "nǐ hǎo", "translation": "привет"},
    {"hanzi": "谢谢", "pinyin": "xièxie", "translation": "спасибо"},
    {"hanzi": "再见", "pinyin": "zàijiàn", "translation": "до свидания"},
    {"hanzi": "是", "pinyin": "shì", "translation": "быть"},
    {"hanzi": "不", "pinyin": "bù", "translation": "не"},
    {"hanzi": "我", "pinyin": "wǒ", "translation": "я"},
    {"hanzi": "你", "pinyin": "nǐ", "translation": "ты"},
    {"hanzi": "他", "pinyin": "tā", "translation": "он"},
    {"hanzi": "她", "pinyin": "tā", "translation": "она"},
    {"hanzi": "我们", "pinyin": "wǒmen", "translation": "мы"},
    {"hanzi": "他们", "pinyin": "tāmen", "translation": "они"},
    {"hanzi": "这", "pinyin": "zhè", "translation": "это"},
    {"hanzi": "那", "pinyin": "nà", "translation": "то"},
    {"hanzi": "哪", "pinyin": "nǎ", "translation": "какой/где"},
    {"hanzi": "谁", "pinyin": "shéi", "translation": "кто"},
    {"hanzi": "什么", "pinyin": "shénme", "translation": "что"},
    {"hanzi": "哪儿", "pinyin": "nǎr", "translation": "где"},
    {"hanzi": "几", "pinyin": "jǐ", "translation": "сколько"},
    {"hanzi": "多少", "pinyin": "duōshao", "translation": "сколько (много)"},
    {"hanzi": "人", "pinyin": "rén", "translation": "человек"},
    {"hanzi": "中国", "pinyin": "Zhōngguó", "translation": "Китай"},
    {"hanzi": "学生", "pinyin": "xuésheng", "translation": "студент"},
    {"hanzi": "老师", "pinyin": "lǎoshī", "translation": "учитель"},
    {"hanzi": "朋友", "pinyin": "péngyou", "translation": "друг"},
    {"hanzi": "家", "pinyin": "jiā", "translation": "дом, семья"},
    {"hanzi": "学校", "pinyin": "xuéxiào", "translation": "школа"},
    {"hanzi": "工作", "pinyin": "gōngzuò", "translation": "работа"},
    {"hanzi": "吃", "pinyin": "chī", "translation": "есть"},
    {"hanzi": "喝", "pinyin": "hē", "translation": "пить"},
    {"hanzi": "看", "pinyin": "kàn", "translation": "смотреть"},
    {"hanzi": "听", "pinyin": "tīng", "translation": "слушать"},
    {"hanzi": "说", "pinyin": "shuō", "translation": "говорить"},
    {"hanzi": "读", "pinyin": "dú", "translation": "читать"},
    {"hanzi": "写", "pinyin": "xiě", "translation": "писать"},
    {"hanzi": "买", "pinyin": "mǎi", "translation": "покупать"},
    {"hanzi": "爱", "pinyin": "ài", "translation": "любить"},
    {"hanzi": "喜欢", "pinyin": "xǐhuan", "translation": "нравиться"},
    {"hanzi": "有", "pinyin": "yǒu", "translation": "иметь"},
    {"hanzi": "没有", "pinyin": "méiyǒu", "translation": "не иметь"},
    {"hanzi": "会", "pinyin": "huì", "translation": "уметь"},
    {"hanzi": "可以", "pinyin": "kěyǐ", "translation": "можно"},
    {"hanzi": "好", "pinyin": "hǎo", "translation": "хороший"},
    {"hanzi": "大", "pinyin": "dà", "translation": "большой"},
    {"hanzi": "小", "pinyin": "xiǎo", "translation": "маленький"},
    {"hanzi": "多", "pinyin": "duō", "translation": "много"},
    {"hanzi": "少", "pinyin": "shǎo", "translation": "мало"},
    {"hanzi": "今天", "pinyin": "jīntiān", "translation": "сегодня"},
    {"hanzi": "明天", "pinyin": "míngtiān", "translation": "завтра"},
    {"hanzi": "昨天", "pinyin": "zuótiān", "translation": "вчера"},
    {"hanzi": "现在", "pinyin": "xiànzài", "translation": "сейчас"},
]


def get_random_word() -> Word:
    """Return random word card from HSK1 list."""
    return random.choice(HSK1_WORDS)


def build_quiz_question() -> dict:
    """Build a multiple choice question from the dictionary."""
    correct_word = random.choice(HSK1_WORDS)
    wrong_words = random.sample(
        [w for w in HSK1_WORDS if w["hanzi"] != correct_word["hanzi"]],
        k=3,
    )
    options = [correct_word["translation"], *(w["translation"] for w in wrong_words)]
    random.shuffle(options)

    return {
        "question": f"Что означает слово: {correct_word['hanzi']} ({correct_word['pinyin']})?",
        "options": options,
        "correct_answer": correct_word["translation"],
    }


def check_answer(user_answer: str, correct_answer: str) -> bool:
    """Check user answer ignoring spaces/case."""
    return user_answer.strip().lower() == correct_answer.strip().lower()
