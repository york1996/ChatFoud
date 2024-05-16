from llm.qwen import generate_response

def is_foud_question(content):
    messages = [
        {"role": "system", "content": "你是一个智能助手"},
        {"role": "user", "content": f"请判断以下句子是否与金融或基金领域有关，请注意，内容与金融有关返回true，无关返回false，不要返回其他任意内容，回答只能是true/false：\n{content} \n"}
    ]
    resp_str = generate_response(messages)
    print(f"is_foud_question = {resp_str}")
    return "true" in resp_str.lower()