from scripts.api import call_chatgpt


def get_life_tip():
    text = call_chatgpt("你是一個人生建議生成器，請給我一個有用的建議。", "請給我一個有用的建議。")
    return text
