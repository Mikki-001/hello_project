from bot.services.chinese import build_quiz_question, check_answer, get_random_word


def test_random_word_card_format() -> None:
    word = get_random_word()
    assert set(word.keys()) == {"hanzi", "pinyin", "translation"}
    assert word["hanzi"]
    assert word["pinyin"]
    assert word["translation"]


def test_quiz_question_generation() -> None:
    quiz = build_quiz_question()
    assert "question" in quiz
    assert "options" in quiz
    assert "correct_answer" in quiz
    assert isinstance(quiz["options"], list)
    assert len(quiz["options"]) == 4
    assert quiz["correct_answer"] in quiz["options"]


def test_answer_validation() -> None:
    assert check_answer("Привет", "привет") is True
    assert check_answer("  привет  ", "привет") is True
    assert check_answer("пока", "привет") is False
