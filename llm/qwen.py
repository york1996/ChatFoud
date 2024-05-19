from transformers import AutoModelForCausalLM, AutoTokenizer
import  torch

device = "mps"
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen1.5-4B-Chat",torch_dtype=torch.float16,device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-4B-Chat")

def generate_response(messages):
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=1024
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return response

def generate_response_single(content):
    messages = [
        {"role": "system", "content": "你是一个智能助理。"},
        {"role": "user", "content": content}
    ]
    resp = generate_response(messages)
    return resp