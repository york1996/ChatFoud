from core.foud_info import FoudInfo
from llm.qwen import generate_response

def gen_answer(foud_info: FoudInfo, content: str):
    messages = [
        {"role": "system", "content": "你是一个基金领域的专家。"},
        {"role": "user", "content": f'''
         请结合以下信息，回答用户的问题。
         基金全称：{foud_info.full_name};
         基金代码：{foud_info.code};
         基金简称：{foud_info.code};
         基金类型：{foud_info.type};
         管理人：{foud_info.manager};
         托管人：{foud_info.custodian};
         管理费率：{foud_info.manager_fee_rate};
         托管费率：{foud_info.custodian_fee_rate};
         用户问题：{content}
         '''
        }
    ]
    return generate_response(messages)