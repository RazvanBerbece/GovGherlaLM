# LLM Available Options Documentation

## Llama2 13B-Chat

### Notes on Llama2 13B-Chat integration
- Finetuned for conversation-like text generation
- Can be used with llama.cpp
    - In GGML format
    - Execute command `./main -t 10 -ngl 32 -m llama-2-13b-chat.ggmlv3.q4_0.bin --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "### Instruction: Write a story about llamas\n### Response:"` in the llama.cpp repo to run inference
    - If you want to have a chat-style conversation, replace the `-p` argument with `-i -ins`
- Maybe with alpaca-lora somehow