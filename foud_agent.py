import argparse

from core.check_foud_content import is_foud_question
from core.gen_final_resp_content import gen_answer
from core.get_foud_info import get_foud_info
from core.get_foud_name import get_foud_name
from llm.qwen import generate_response

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--content", type=str, help="输入你要咨询的问题")
    args = parser.parse_args()
    resp_str = predict_resp(args.content)
    print(resp_str)

def predict_resp(content):
    # 判断是否为金融类问题 TODO
    # 使用Qwen
    if not is_foud_question(content):
    
    # 使用微调文本二分类模型 ~121MB
    # if not is_foud_question_fast(content):
        return "问题与金融领域无关，请重新输入"
    
    
    # 抽取问题中的基金名称
    foud_name = get_foud_name(content)
    if foud_name.lower() == "error":
        return "请在问题中带入您要咨询的基金名称"
    
    # 根据基金名称获取基金信息 TODO
    foud_info = get_foud_info(content) 

    # LLM结合基金信息获取回答
    return gen_answer(foud_info, content)
if __name__=='__main__':
    main()