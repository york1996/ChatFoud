from llm.qwen import generate_response

def get_foud_name(content):
    prompt = f'''
    请抽出以下句子中的基金名称：{content}\n
    请注意，仅返回基金名称，不要返回其他任何内容。\n
    若句子中没有基金名称，直接返回error。\n
    '''

    messages = [
        {"role": "system", "content": "你是一个抽取参数的机器人"},
        {"role": "user", "content": prompt}
    ]
    resp_str = generate_response(messages)
    print(f"get_foud_name = {resp_str}")
    return resp_str