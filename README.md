
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
:::: Chatbot Game 이미지 넣기 ::::
</p>

<br>
<br>
<br>

## 기술 스택

| Python |
| :--------: |
|   Python Button   |

::::   아니면 좀 다른 형식의 버튼 구해보기   ::::

<br>
<br>
<br>

## Framework
Flask

<br>
<br>
<br>

## 설치 방법

### Clone Repository

```sh
깃 주소 작성하기
```

### Prerequisites

```sh
prerequistes 작성
```

<br>
<br>
<br>

## 파일 구조

파일 구조 작성



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



