# LLM 디코딩 / 평가 / RLHF / Hallucination

> 2025-04-16

## 배운 것

### 디코딩 알고리즘

| 방법 | 설명 |
|:---|:---|
| Greedy Search | 매 시점 확률 최고인 단어 1개만 선택. 빠르지만 반복적일 수 있음. |
| Beam Search | 상위 k개 조합 유지하며 탐색. 번역 등에 자주 사용. |
| Temperature Scaling | 높으면 창의적, 낮으면 보수적. |
| Top-K / Top-p Sampling | 상위 K개 or 누적 확률 p까지만 후보로 제한. |

### LLM 평가

**벤치마크**

| 벤치마크 | 측정 대상 |
|:---|:---|
| MMLU | 다양한 전문 지식 (수학, 법, 의학 등) |
| GSM8K | 초등 수준 수학 논리력 |
| HumanEval | Python 코드 작성 능력 |

한계: **Data Contamination** — 학습 데이터에 평가 문제가 포함되면 점수가 왜곡됨.

**LLM-as-a-Judge**: 더 강력한 LLM이 다른 LLM 출력을 평가.  
편향 주의: 위치 편향, 길이 편향, 자기 선호 편향.

### RLHF (선호 학습)

```
SFT (사람이 쓴 고품질 답변으로 학습)
    ↓
보상 모델 학습 (사람이 응답 순위 매김 → RM 학습)
    ↓
PPO 강화학습 (보상 높은 방향으로 모델 업데이트)
```

**DPO**: 복잡한 RL 없이 선호 데이터로 직접 최적화. 최근 PPO보다 많이 쓰임.

### Hallucination & Alignment

- **Hallucination**: 사실이 아닌 내용을 그럴듯하게 지어내는 현상 → **RAG**로 완화.
- **Alignment**: 모델 목표를 인간의 가치·윤리와 일치시키는 과정. RLHF가 핵심 도구.

## 막혔던 것 / 해결

Temperature를 낮추면 왜 보수적이 되는지 이해 안 됐음.  
확률 분포를 Temperature로 나누면 큰 값은 더 커지고 작은 값은 더 작아짐.  
→ Temperature 낮을수록 최고 확률 단어에 쏠림 → 항상 비슷한 답변.
