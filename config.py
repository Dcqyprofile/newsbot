
if LLM_PROVIDER == "openai":
    call_openai_api(prompt)
elif LLM_PROVIDER == "ollama":
    call_ollama_local_model(prompt)