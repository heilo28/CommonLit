# CommonLit
(https://www.kaggle.com/competitions/commonlit-evaluate-student-summaries)

1. kaggle data 
 - summaries_train.csv - Summaries in the training set.
   - student_id - The ID of the student writer.
   - prompt_id - The ID of the prompt which links to the prompt file.
   - text - The full text of the student's summary.
   - content - The content score for the summary. The first target.
   - wording - The wording score for the summary. The second target.
 - summaries_test.csv - Summaries in the test set. Contains all fields above except content and wording.

2. 문제 정의 
- target이 두개인 문제
- Text Data를 가지고 numeric data를 prediction 필요
- 평가 지표인 RMSE를 최소화 하는 방향으로 학습
- Transformer를 활용
  - 해당 문제를 해결하기 위해 적합한 모델 서치 필요

3. pacakges
   - tensorflow 2.10
   - python 3.11
   - nltk
