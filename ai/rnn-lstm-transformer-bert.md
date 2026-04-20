# RNN / LSTM / Transformer / BERT

> 2026-03

## 배운 것

### NLP 모델 진화 흐름

```
RNN → LSTM → Seq2Seq + Attention → Transformer → BERT
```

### RNN

이전 시점 정보를 현재 학습에 반영하는 재귀 구조.

```
h_t = tanh(Φ_h × h_{t-1} + Φ_x × x_t + b)
```

- 파라미터 공유: 모든 시점에서 동일한 W 사용
- 한계: 문장이 길어지면 앞 정보가 소실 → **기울기 소실(Vanishing Gradient)**

### LSTM

RNN의 장기 기억 문제 해결. h(단기) + c(Cell State, 장기) 두 통로.

| 게이트 | 역할 |
|:---|:---|
| Forget Gate | 과거 정보 중 불필요한 것 삭제 |
| Input Gate | 현재 정보 중 저장할 것 선택 |
| Output Gate | 다음 단계로 내보낼 값 결정 |

### Transformer

RNN 없이 **Self-Attention만** 사용. 문장 전체를 한번에 병렬 처리.

**Self-Attention 계산 과정:**
```
1. Q, K, V 벡터 생성 (입력 × 학습 가능한 가중치 행렬)
2. Score = Q × K^T
3. Attention Weight = softmax(Score / √d_k)
4. Output = Attention Weight × V
```

- Q: 질문 (현재 찾는 주체)
- K: 인덱스 (비교 대상)
- V: 내용물 (실제 의미 정보)
- √d_k로 나누는 이유: 수치가 커지는 것 방지

### BERT

Transformer 인코더만 사용. 양방향(Bidirectional)으로 문맥 파악.

- **MLM (Masked Language Model)**: 단어를 가리고 주변 문맥으로 추론
- **NSP (Next Sentence Prediction)**: 두 문장이 이어지는지 맞히기
- `[CLS]` 토큰: 문장 전체 의미 대표

| 모델 | 핵심 | 현재 위치 |
|:---|:---|:---|
| RNN | 순환 구조 | 거의 안 씀 |
| LSTM | 게이트 시스템 | 가끔 시계열에 씀 |
| Transformer | Self-Attention, 병렬 | 현대 AI 표준 |
| BERT | 양방향 인코더 | 검색·분류 특화 |

## 막혔던 것 / 해결

Transformer에서 Positional Encoding이 왜 필요한지 몰랐음.  
RNN은 순서대로 처리해서 위치 정보가 자동으로 들어가지만, Transformer는 전체를 한번에 보기 때문에 단어 순서 정보를 따로 주입해야 함.
