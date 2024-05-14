from llm.qwen import generate_response
from transformers import pipeline

def is_foud_question(content):
    messages = [
        {"role": "system", "content": "请判断以下内容是否与金融有关，如果是返回true，如果不是返回 false，请不要返回true/false以外的任何内容。"},
        {"role": "user", "content": content}
    ]
    resp_str = generate_response(messages)
    return resp_str.lower() == "true"

def is_foud_question_faster(content):
    # https://huggingface.co/WhichPath/gte-small-zh-foud-cls
    classifier = pipeline("text-classification", model="WhichPath/gte-small-zh-foud-cls")
    result = classifier(content)
    return result[0]['label'] == 'TRUE'
