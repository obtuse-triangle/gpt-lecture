# gpt-lecture
gpt api를 활용한 flask 기반 웹 서비스

---

# 개발 환경
1. PyCharm 으로 수업 진행함
2. 본 레파지토리 clone | fork
3. PyCharm에서 가상 공간 설정 
   1. file > setting > Project > Python interpreter > Add interpreter > Add Local interpreter > Virtualenv Environment 설정 화면에서 3.12 선택
4. `pip install -r requirements.txt`
5. `main.py` 우클릭 &rarr; Modify Run Configuration &rarr; Choose target to run 에서 Script Path 대신 Module Name 을 선택 &rarr; uvicorn 모듈을 선택 &rarr; `main:app --reload` 추가 &rarr; 저장 후 실행
6. 실행 후 확인

# branch
자신의 학번으로 생성 후 수업 끝날때 pr
