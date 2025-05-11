from transformers import AutoModelForCausalLM, AutoTokenizer
import argparse
 from urllib.parse import unquote

# https://huggingface.co/arnir0/Tiny-LLM
if __name__ == '__main__':

    try:
        MODEL_NAME = "arnir0/Tiny-LLM"
        TOKENIZER = AutoTokenizer.from_pretrained(MODEL_NAME)
        MODEL = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

        def url_decode(prompt):
            decoded_string = unquote(prompt)
            return decoded_string

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
        
        def clean_text(generated_text):
            sp_arr = generated_text.split("\n")
            result = []

            for x in range(0, len(sp_arr), 1):
                if sp_arr[x] == "The attention mask and the pad token id were not set. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.":
                    continue
                if sp_arr[x] == "Setting `pad_token_id` to `eos_token_id`:2 for open-end generation.":
                    continue
                if sp_arr[x] == "The attention mask is not set and cannot be inferred from input because pad token is same as eos token. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.":
                    continue
                
                result.append(sp_arr[x])

            return result


        parser = argparse.ArgumentParser()
        parser.add_argument('--prompt')  
        args = parser.parse_args()
        PROMPT = args.prompt
        print("Arguments received python _tiny_llm.py --prompt " + str(PROMPT))
        print(clean_text(generate_text(url_decode(PROMPT), MODEL, TOKENIZER)))

    except Exception as ex:

        print('Exception: ' + str(ex))
