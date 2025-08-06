from scripts.api import call_chatgpt


def get_fun_fact():
    text = call_chatgpt("你是一個冷知識生成器，請給我一個有趣的冷知識。", "請給我一個有趣的冷知識。")
    return text
