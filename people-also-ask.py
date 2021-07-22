import requests
import json
from fake_useragent import UserAgent
from aitextgen import aitextgen #for ai text gen
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import pipeline

import streamlit as st

header = st.beta_container()
paa_blog = st.beta_container()
gpt_blog = st.beta_container()

menu = st.sidebar.radio("Choose your method:",("People Also Ask","Text Generation"))

with header:
    st.header("People also ask and Text Generation")

if menu == "People Also Ask":
    with paa_blog:
        input_keyword = st.text_input(label = "Enter your keyword...", value = "Scrum")
        keyword = input_keyword
        kw = keyword.replace(" ", "+")
        # st.text(kw)

        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + kw
        # st.write(url)

        ua = UserAgent()
        headers = {"user-agent": ua.chrome}
        response = requests.get(url, headers=headers, verify=False)
        # st.text(response.text)

        st.subheader("Suggestion keywords")
        suggestions = json.loads(response.text)
        for word in suggestions[1]:
            st.write(word)

        import people_also_ask

        paa = people_also_ask.get_related_questions(kw, 5)
        
        

        ans0 = people_also_ask.get_simple_answer(paa[0])
        ans1 = people_also_ask.get_simple_answer(paa[1])
        ans2 = people_also_ask.get_simple_answer(paa[2])
        ans3 = people_also_ask.get_simple_answer(paa[3])
        ans4 = people_also_ask.get_simple_answer(paa[4])

        st.write("---------")
        
        st.header("People also ask!")
        
        st.write(paa[0])
        st.write(ans0)
        st.write("")

        st.write(paa[1])
        st.write(ans1)
        st.write("")

        st.write(paa[2])
        st.write(ans2)
        st.write("")

        st.write(paa[3])
        st.write(ans3)
        st.write("")

        st.write(paa[4])
        st.write(ans4)
        st.write("")
else:
    with gpt_blog:
        st.header("Text Generation")
        
        method = st.sidebar.selectbox("Select methods",("aitextgen","gpt-2-large","gpt-neo", "pipeline"))
        max_word = st.sidebar.slider('Max words', min_value=50, max_value=500, step= 50)
        # st.write(max_word)

        # if method == 'aitextgen':
        #     st.subheader("aitextgen")
        # elif method == 'gpt-2-large':
        #     st.subheader("gpt-2-large")
        # else: 
        #     st.subheader('gpt-neo')
        
        prompt_text = st.text_input(label = "Enter your prompt text...", value = "What is your goal?")
        
        if method == 'aitextgen':
            st.title("Generate text from aitextgen")
            # instantiate the model / download 
            ai = aitextgen()
            gpt_text = ai.generate_one(prompt=prompt_text,max_length = max_word )
            
            st.write(gpt_text)
        elif method == 'gpt-2-large':
            st.title("Generate text from gpt2-large")
            #Load Model
            tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
            model = GPT2LMHeadModel.from_pretrained("gpt2-large", pad_token_id=tokenizer.eos_token_id)
            # Tokenize
            sentence = prompt_text
            input_ids = tokenizer.encode(sentence, return_tensors='pt')
            
            output = model.generate(input_ids, max_length=max_word, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
            tokenizer.decode(output[0], skip_special_tokens=True)

            text = tokenizer.decode(output[0], skip_special_tokens=True)
            print(text)

            st.write(text)
        elif method == 'gpt-neo-125M':
            st.title("gpt-neo-125M")
            generator = pipeline('text-generation', model= 'EleutherAI/gpt-neo-125M') 

            prompt = prompt_text
            res = generator(prompt, max_length=max_word, do_sample=True, temperature=0.9)

            st.write(res[0]['generated_text'])
        else:
            st.title('Pipeline: distilgpt2')
            generator = pipeline("text-generation", model="distilgpt2")

            prompt = prompt_text
            text_gen = generator(prompt, max_length=max_word,num_return_sequences=2,)
            st.write(text_gen[0]['generated_text'])


