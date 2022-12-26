
# 프로젝트명
2022 SKKU 산학 협력 프로젝트 / 웅진씽크빅 / Talking NPC / WikiChatbot

2022년도 웅진씽크빅 기업과 함께한 산학 협력 프로젝트

<br>

> 아이들이 궁금한 것이 있을 때 백과사전처럼 이용할 수 있는 챗봇입니다.

> QA Task처럼 Context와 qeustion이 주어지면, 그에 맞는 정답을 도출하는 챗봇입니다.

> BERT 모델을 사용하여 QA Task를 진행하도록 하였고, Wikipedia API를 이용하여 질문에 대한 context를 불러왔습니다.


<br>
<br>
<br>
<br>

## 프로젝트 소개

### 프로젝트 개요/동기
<p align="justify">

기업의 니즈에 맞춰 아이가 웅진 메타버스 플랫폼 안에서 지루함을 느끼지 않도록 도와주는 AI Agent를 만들고자 하였습니다.

따라서 아이가 궁금한 것이 있다면, 언제든 물어볼 수 있는 QA chatbot을 만들어 아이들의 궁금증을 해소해주고자 하였습니다.

<br>
정답에 대한 문맥(Context)은 위키피디아 API를 이용하여 찾도록 하였고, BERT 모델을 통해 정답을 도출하도록 하였습니다.
</p>

<p align="center">

</p>

<br>
<br>
<br>

## 기술 스택

| Python |
| :--------: |

<br>
<br>
<br>

## Framework
Flask / AWS EC2

(Python 버전은 3.8을 사용하였습니다.)

<br>
<br>
<br>

## 설치 방법

### Clone Repository

```sh
git clone https://github.com/Taerogrammer/WikiChatbot.git
```

### Prerequisites

```sh
pip install -r requirements.txt
```

<br>
<br>
<br>

## 파일 구조

📦wiki_chatbot

 ┣ 📂dataset
 
 ┃ ┣ 📜KorQuAD_v1.0_dev.json
 
 ┃ ┣ 📜KorQuAD_v1.0_train.json
 
 ┃ ┗ 📜ko_wiki_v1_squad.json
 
 ┣ 📂result_v2
 
 ┃ ┣ 📜config.json
 
 ┃ ┣ 📜pytorch_model.bin
 
 ┃ ┣ 📜special_tokens_map.json
 
 ┃ ┣ 📜tokenizer_config.json
 
 ┃ ┣ 📜training_args.bin
 
 ┃ ┗ 📜vocab.txt
 
 ┣ 📂static
 
 ┃ ┣ 📜funct.js
 
 ┃ ┗ 📜mystyle.css
 
 ┣ 📂templates
 
 ┃ ┗ 📜index.html
 
 ┣ 📜app.py
 
 ┣ 📜app2.py
 
 ┗ 📜requirements.txt

<br>
<br>
- app.py : 유니티와 연동할 때  파일입니다.

- app2.py : 데모사이트로 확인을 하고자 할 때 연결하는 파일입니다.

- dataset : KorQuAD v 1.0과 AiHub의 질의응답 데이터셋을 이용하였습니다.

- model : 위에 언급된 dataset을 훈련시켜 만들었습니다. (epoch : 4, batch size : 32) <br>         
        만약 custom한 모델을 이용해보고 싶다면 result_v2 파일에 개인 model을 추가하시면 됩니다. 


<br>
<br>
<br>

## 사용 예제

유저가 챗봇에게 다가가 질문을 하면, 그에 맞는 답변을 제공해줍니다.

만약 질문에 대한 답변을 찾지 못하거나, 질문을 이해하지 못하였을 때에는 질문을 이해하지 못하였다는 메세지를 전달합니다.



### Process


1. 질문을 하게 되면, 질문 속 단어를 선정하여 그 단어와 관련된 wikipedia 페이지를 불러옵니다.
2. 불러온 페이지를 BERT max sequence length (512 token)을 기반으로 문단을 만듭니다.
3. 나눈 문단과 질문을 TF-IDF를 통해 질문의 내용과 가장 유사한 문단을 불러옵니다.
4. 불러온 문단을 context, 질문을 question으로 지정한 뒤, wiki chatbot 실행합니다.
5. question 중 grad_fn 값이 양수인 경우에만 답을 출력합니다.
6. grad_fn 값이 음수인 경우 “제가 잘 이해하지 못했어요” 등의 답변 출력합니다.


<br>
<br>
<br>

## API 설명

### /answer [POST]

- 유니티 내부에서 해당 챗봇에게 질문을 하면, 질문에 대한 답변을 해줍니다. 

Request
```
{ "question' : "티라노의 먹이는?" }
```

Response 
```
{ "answer" : "조각류, 갑각류" }
```

- 예시

![unityWiki](https://user-images.githubusercontent.com/104834390/209521725-4b2b6580-1801-4eec-8b68-1bc1b66f0071.png)


### /answer_2 [POST]

- 데모 사이트에서 답변을 확인하기 위해 제작하였습니다.

- 질문을 작성하고 request를 보내주면 answer, 정답에 대한 tensor값(정수), 정답을 찾아온 위키피디아 페이지와 정답에 대한 하이라이트 페이지를 불러옵니다.

- AWS ubuntu 22.04 LTS 버전을 사용하였습니다.

- 데모 사이트

![wikibot](https://user-images.githubusercontent.com/104834390/209521405-b427c031-974b-425b-ab5e-d77197b71890.png)

- 참조 위키피디아 페이지

![wikipage](https://user-images.githubusercontent.com/104834390/209521457-244198ea-c5fb-41e2-a6ce-5e1b70da7490.png)
