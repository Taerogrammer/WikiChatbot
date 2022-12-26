import sys
from konlpy.tag import Hannanum
import pandas as pd # 데이터프레임 사용을 위해
from math import log # IDF 계산을 위해







#----------------------------------------------------------
import wikipediaapi

wiki=wikipediaapi.Wikipedia('ko')

wiki = wikipediaapi.Wikipedia(
        language='ko',
        extract_format=wikipediaapi.ExtractFormat.WIKI)

#----------------------------------------------------------


from transformers import BertModel, BertConfig, BertTokenizer, BertForQuestionAnswering
import torch
import json

tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")
model = BertForQuestionAnswering.from_pretrained('bert-base-multilingual-cased')
model.load_state_dict(torch.load("result_v2/pytorch_model.bin",  map_location=torch.device("cpu")))


question = "치타의 속력은?"  

hannanum = Hannanum()

x = hannanum.nouns(question)

if "공룡" not in x:

        print(x)
else:
        x[0] = "공룡"
        print(x[0])


p_wiki = wiki.page(x[0])






global answer
answer = ""


global contexts
contexts=""


#------------------------------------------------------------




encoding = tokenizer.encode_plus(question)              
input_ids, token_type_ids = encoding["input_ids"], encoding["token_type_ids"]

q_token = len(encoding["input_ids"])

encoding = tokenizer.encode_plus(question, p_wiki.text)
input_ids, token_type_ids = encoding["input_ids"], encoding["token_type_ids"]

para_tmp = list()
para = list()


sum_sentence = ""

sentence = p_wiki.text.split('.')    # '.'을 단위로 split했음 왜냐하면 그냥 문장으로 split 했을 때 그 특징 같은거를 같이 담지 못할 수도 있음 



max_token = 512 - q_token


sentence_len = len(sentence)

cnt_token = 0
t_id = 0
cnt = 0
n = 0

while t_id < max_token:             # 질문 + context가 들어가야 함
        
        if cnt == sentence_len-2:

                encoding = tokenizer.encode_plus(sentence[cnt-2])   #문장으로 자르기는 성공 및 token 개수도 구함
                input_ids = encoding["input_ids"]
                t_id =  t_id + len(input_ids)
                cnt_token = cnt_token + len(input_ids)

                sum_sentence += "".join(sentence[cnt-2])

                if t_id > max_token:

                        para.append(sum_sentence)
                        t_id = 0
                        sum_sentence = ""
        
                break

        else:
                encoding = tokenizer.encode_plus(sentence[cnt])   #문장으로 자르기는 성공 및 token 개수도 구함
                input_ids = encoding["input_ids"]
                t_id =  t_id + len(input_ids)

                cnt_token = cnt_token + len(input_ids)


                        
                sum_sentence += "".join(sentence[cnt])
                cnt = cnt + 1 

                if t_id > max_token:

                        para.append(sum_sentence)
                        t_id = 0
                        sum_sentence = ""


import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


percent = list()

tfidf_vectorizer = TfidfVectorizer()

# 벡터화
for i in range(len(para)):
        
        tfidf_matrix = tfidf_vectorizer.fit_transform([question, para[i]]).todense()
        tfidf1 = tfidf_matrix[0]
        tfidf2 = tfidf_matrix[1]
        percent.append(cosine_similarity(tfidf1, tfidf2))

maxindex = numpy.argmax(percent)

encoding = tokenizer.encode_plus(question, para[maxindex])
input_ids, token_type_ids = encoding["input_ids"], encoding["token_type_ids"]

if len(input_ids) > 512:
        encoding = tokenizer.encode_plus(question, para[maxindex][:720])
        input_ids, token_type_ids = encoding["input_ids"], encoding["token_type_ids"]









start_scores, end_scores = model(torch.tensor([input_ids]), token_type_ids=torch.tensor([token_type_ids]))

all_tokens = tokenizer.convert_ids_to_tokens(input_ids)

answer = ' '.join(all_tokens[torch.argmax(start_scores) : torch.argmax(end_scores)+1])


answer = answer.replace('#', '').strip()
answer = answer.replace('[UNK]', '').strip()   

if answer =="[CLS]" or answer =="":
        answer = "질문에 대해 이해하지 못한 것 같아요"

elif start_scores[0][torch.argmax(start_scores)] < 0 or end_scores[0][torch.argmax(end_scores)] < 0:
        answer = "제가 대답할 수 없는 질문인 것 같아요"



contexts=p_wiki.text


from flask import Flask, render_template, request, jsonify, send_from_directory, flash
import sys, os
app = Flask(__name__)


global total





@app.route('/', methods = ['GET', 'POST'])
def hello():
    
    return render_template("index.html")


@app.route("/answer", methods=['POST'])
def update_name():
        
    
    
    try:
                
        content = request.get_json(silent=True)
        content = content["question"]
        
        hannanum = Hannanum()

        x = hannanum.nouns(content)

        if "공룡" not in x:

                print(x)
        else:
                x[0] = "공룡"
                print(x)


        p_wiki = wiki.page(x[0])

        encoding = tokenizer.encode_plus(content)              
        input_ids, token_type_ids = encoding["input_ids"], encoding["token_type_ids"]

        q_token = len(encoding["input_ids"])

        encoding = tokenizer.encode_plus(content, p_wiki.text)
        input_ids, token_type_ids = encoding["input_ids"], encoding["token_type_ids"]

        para_tmp = list()
        para = list()


        sum_sentence = ""
             
        sentence = p_wiki.text.replace('다.', '다.*');

        sentence = sentence.split('*')

        max_token = 512 - q_token


        sentence_len = len(sentence)

        cnt_token = 0
        t_id = 0
        cnt = 0
        n = 0


        while t_id < max_token:             # 질문 + context가 들어가야 함
                
                if cnt == sentence_len-2:

                        encoding = tokenizer.encode_plus(sentence[cnt-2])   #문장으로 자르기는 성공 및 token 개수도 구함
                        input_ids = encoding["input_ids"]
                        t_id =  t_id + len(input_ids)
                        cnt_token = cnt_token + len(input_ids)

                        sum_sentence += "".join(sentence[cnt-2])

                        if t_id > max_token:
                                para.append(sum_sentence)
                                t_id = 0
                                sum_sentence = ""
                
                        break

                else:

                        encoding = tokenizer.encode_plus(sentence[cnt])   #문장으로 자르기는 성공 및 token 개수도 구함
                        input_ids = encoding["input_ids"]
                        t_id =  t_id + len(input_ids)

                        cnt_token = cnt_token + len(input_ids)


                                
                        sum_sentence += "".join(sentence[cnt])
                        cnt = cnt + 1 

                        if t_id > max_token:
                                para.append(sum_sentence)
                                t_id = 0
                                sum_sentence = ""
        
        percent = list()

        tfidf_vectorizer = TfidfVectorizer()

        # 벡터화
        for i in range(len(para)):
                
                tfidf_matrix = tfidf_vectorizer.fit_transform([content, para[i]]).todense()
                tfidf1 = tfidf_matrix[0]
                tfidf2 = tfidf_matrix[1]
                percent.append(cosine_similarity(tfidf1, tfidf2))


        maxindex = numpy.argmax(percent)

        encoding = tokenizer.encode_plus(content, para[maxindex])
        input_ids, token_type_ids = encoding["input_ids"], encoding["token_type_ids"]

        if len(input_ids) > 512:
                encoding = tokenizer.encode_plus(content, para[maxindex][:720])
                input_ids, token_type_ids = encoding["input_ids"], encoding["token_type_ids"]









        start_scores, end_scores = model(torch.tensor([input_ids]), token_type_ids=torch.tensor([token_type_ids]))

        answer=input_ids[torch.argmax(start_scores) : torch.argmax(end_scores)+1]
        answer=tokenizer.decode(answer)

        answer = answer.replace('[UNK]', '').strip()   

        if answer =="[CLS]" or answer =="":
                answer = "질문에 대해 이해하지 못한 것 같아요"
                contexts=" "
                   
        elif start_scores[0][torch.argmax(start_scores)] < 0 or end_scores[0][torch.argmax(end_scores)] < 0:
                answer = "제가 대답할 수 없는 질문인 것 같아요"
                contexts=" "

        total = start_scores[0][torch.argmax(start_scores)].item() + end_scores[0][torch.argmax(end_scores)].item()




    except:
            answer = "질문을 받을 수 없을 것 같아요. 다른 질문을 해주세요."
            total = "None"
            contexts=" "


    contexts=p_wiki.text

    total = "정답 관련 유사값(단위: Tensor) : " +  str(total)

    answer_start = answer.split(" ")[0]
    answer_end = answer.split(" ")[-1]

    index_start = contexts.find(answer_start)
    
    prac = contexts[:index_start] + " <<<<< " + contexts[index_start:]

    end_len = len(answer_end)

    index_end = prac.find(answer_end)

    prac_2 = prac[:index_end+end_len] + " >>>>> " + prac[index_end+end_len:]

 
    contexts = prac_2

    wiki_url = p_wiki.fullurl

    return answer +" ( " +  str(total) + " )" + "**" +  contexts + "**" + wiki_url


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
