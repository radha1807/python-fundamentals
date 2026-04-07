def  call_llm(prompt, model='gpt-4o-mini', temperature=0, max_tokens=500):
    print(f"prompt={prompt}, model={model}, temp={temperature}, tokens={max_tokens}")
    
call_llm('Hello',  temperature=0.9)  