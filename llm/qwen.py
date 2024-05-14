from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda"
model = AutoModelForCausalLM.from_pretrained("Qwen/CodeQwen1.5-7B-Chat",torch_dtype="auto",device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("Qwen/CodeQwen1.5-7B-Chat")

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
    generated_texts = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return generated_texts[0]