
# 프로젝트명
2022 SKKU 산학 협력 프로젝트 / 웅진씽크빅 / Talking NPC / WikiChatbot

2022년도 웅진씽크빅 기업과 함께한 산학 협력 프로젝트

<br>

> 아이들이 궁금한 것이 있을 때 백과사전처럼 이용할 수 있는 챗봇입니다.

> QA Task처럼 Context와 qeustion이 주어지면, 그에 맞는 정답을 도출하는 챗봇입니다.

> BERT 모델을 사용하여 QA Task를 진행하도록 하였고, Wikipedia API를 이용하여 질문에 대한 context를 불러왔습니다.

<br>
<br>

※  https://github.com/JoungheeKim/korean-question-answer-system 에서 프로젝트 진행 방법에 대한 도움을 받았습니다.  ※


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

- dataset : 학습에 사용된 데이터셋. KorQuAD v 1.0과 AiHub의 질의응답 데이터셋을 이용하였습니다.

- result_v2 : output_dir 이름

<br>
<br>

## 모델 학습 및 평가방법

[BERT](https://github.com/JoungheeKim/korean-question-answer-system), [KoBERT](https://github.com/monologg/KoBERT-KorQuAD) 학습 방법을 참고하였습니다.

<br>

1. 학습 방법

```sh
python run_korquad.py --model_type hanbert --model_name_or_path HanBert-54kN-torch --output_dir result/ --do_train --train_dir resource/korquad2/train/ --gradient_accumulation_steps 4 --max_seq_length 512 --logging_steps 5000 --save_steps 5000 --num_train_epochs 1 --dataset_type korquad2 --version_2_with_negative
```
<br>

2. 평가 명령어

```sh
python run_korquad.py --model_type hanbert --model_name_or_path aihub/ --output_dir result/ --do_eval --predict_dir resource/korquad2/dev/ --max_seq_length 512 --dataset_type korquad2 --version_2_with_negative
```

<br>

- options

  - model_type : 모델타입(bert, kobert, hanbert) 선택

  - model_name_or_path : 모델타입에 따라 선택(bert : bert-base-multilingual-cased, kobert : monologg/kobert, habert : HanBert-54kN-torch)하거나 모델이 있는 폴더 설정

  - output_dir : 학습 또는 평가 결과를 저장할 폴더

  - do_train : 학습 할 때 설정하는 옵션(true/false)

  - train_dir : 학습에 필요한 파일(.json)이 있는 폴더

  - do_eval : 평가 할 때 설정하는 옵션(true/false)

  - predict_dir : 평가에 필요한 파일(.json)이 있는 폴더

  - dataset_type : korquad1.0 또는 aibhub 데이터(.json)을 학습할 때는 korquad1, korquad2.0 을 학습할 때는 korquad2로 설정
  
  <br>
  
- 프로젝트 파라미터
  
   - model_type : bert
  
   - model_name_or_path : bert-base-multilingual-cased
  
   - output_dir : {본인이 원하는 디렉토리 경로}
  
   - do_train : true
  
   - train_dir : {train시킬 데이터셋 경로}
  
   - do_eval : true
  
   - predict_dir : {평가할 때 사용할 데이터셋 경로}
  
   - dataset_type : korquad1
 <br>
 
[korean-question-answer-system](https://github.com/JoungheeKim/korean-question-answer-system) 페이지를 git clone하여 위의 훈련 방법을 진행하면 output_dir에 훈련된 model이 생성됩니다.

- 만약 본인이 custom한 model을 통해 프로젝트를 진행하고 싶으면, app.py과 app2.py에서 file_dir를 본인의 model이 있는 경로로 설정해주면 됩니다.
  
  (현재 result_v2로 설정되어 있습니다)


 
 <br>
 <br>

### 모델 다운로드

만약 모델을 학습시킬 수 없는 환경이라면 해당 드라이브에서 모델을 다운받을 수 있습니다.

다운을 받은 후 output_dir의 경로를 맞춰주시면 정상적으로 작동함을 알 수 있습니다.

:::: [모델 다운로드] 모델 링크 걸어놓기 ::::

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




### /answer_2 [POST]

- 데모 사이트에서 답변을 확인하기 위해 제작하였습니다.

- 질문을 작성하고 request를 보내주면 answer, 정답에 대한 tensor값(정수), 정답을 찾아온 위키피디아 페이지와 정답에 대한 하이라이트 페이지를 불러옵니다.

- AWS ubuntu 22.04 LTS 버전을 사용하였습니다.

- 데모 사이트

![wikibot](https://user-images.githubusercontent.com/104834390/209521405-b427c031-974b-425b-ab5e-d77197b71890.png)

- 참조 위키피디아 페이지

![wikipage](https://user-images.githubusercontent.com/104834390/209521457-244198ea-c5fb-41e2-a6ce-5e1b70da7490.png)
