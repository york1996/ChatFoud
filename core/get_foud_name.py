from llm.qwen import generate_response

def get_foud_name(content):
    messages = [
        {"role": "system", "content": "请抽出user提问中的基金名称，请仅返回基金名称，不要返回任何额外内容，如果没有基金名称，返回 error。"},
        {"role": "user", "content": content}
    ]
    resp_str = generate_response(messages)
    return resp_str