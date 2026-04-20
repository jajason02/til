# ML 기초 / 회귀 / 분류 평가지표

> 2026-03

## 배운 것

### AI / ML / DL 포함 관계

```
AI ⊃ ML ⊃ DL
```

- AI: 환경·데이터를 인지·학습하여 목표 달성하는 시스템
- ML: 규칙을 직접 코딩하는 대신 **데이터에서 규칙을 학습**
- DL: ML 안에서 신경망(Neural Network)을 사용하는 방법론

### 데이터 구성

- **Feature(x)**: 모델이 예측에 사용하는 입력. 예측의 근거.
- **Label(y)**: 모델이 맞춰야 하는 정답값.
- **Train / Validation / Test** 분할: Test는 학습에 전혀 사용되지 않은 데이터로 최종 일반화 성능 확인.

### 회귀 평가지표

```
MSE = (1/n) × Σ(yi - ŷi)²       ← 작을수록 좋음
R²  = 1 - MSE모델 / Variance데이터  ← 1에 가까울수록 좋음
```

- R² = 0: 평균으로만 예측하는 수준
- R² < 0: 평균보다 못한 성능

### 혼동 행렬 & 분류 평가지표

|  | 예측 P | 예측 N |
|:---|:---|:---|
| 실제 P | TP | FN |
| 실제 N | FP | TN |

```
Accuracy  = (TP + TN) / 전체
Precision = TP / (TP + FP)   ← 소심하게 예측, FP 적음
Recall    = TP / (TP + FN)   ← 놓치지 않음, FN 적음
F1        = 2 × (Precision × Recall) / (Precision + Recall)
```

불균형 데이터에서 Accuracy만 믿으면 안 됨. 모든 샘플을 정상으로 예측해도 99% 나올 수 있음.

## 막혔던 것 / 해결

Precision과 Recall 중 어떤 걸 올려야 하는지 헷갈렸음.  
암 진단처럼 환자를 놓치면 안 되는 경우 → Recall 중요.  
스팸 필터처럼 정상 메일을 스팸으로 잘못 분류하면 안 되는 경우 → Precision 중요.
