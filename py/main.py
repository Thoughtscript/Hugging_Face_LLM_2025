from transformers import AutoModelForCausalLM, AutoTokenizer

# https://huggingface.co/arnir0/Tiny-LLM
if __name__ == '__main__':

    try:
        MODEL_NAME = "arnir0/Tiny-LLM"
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

        def generate_text(prompt, model, tokenizer, max_length=512, temperature=1, top_k=50, top_p=0.95):
            inputs = tokenizer.encode(prompt, return_tensors="pt")

            outputs = model.generate(
                inputs,
                max_length=max_length,
                temperature=temperature,
                top_k=top_k,
                top_p=top_p,
                do_sample=True
            )

            generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            return generated_text
        
        prompt = "According to all known laws of aviation, there is no way a bee should be able to fly."
        generated_text = generate_text(prompt, model, tokenizer)
        print(generated_text)

    except Exception as ex:

        print('Exception: ' + str(ex))
