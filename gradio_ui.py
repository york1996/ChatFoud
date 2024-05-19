from foud_agent import predict_resp
import gradio as gr

# Gradio 接口函数
def answer_question(question):
    return predict_resp(question)


# 创建 Gradio 接口
iface = gr.Interface(
    fn=answer_question,          # 接口函数
    inputs=gr.Textbox(lines=2, placeholder="请输入你的问题..."),  # 输入文本框
    outputs=gr.Textbox(),        # 输出文本框
    title="ChatFoud",            # 标题
    description="请输入一个问题，并获得答案。",  # 描述
)

if __name__=='__main__':
    # 启动 Gradio 接口
    iface.launch()