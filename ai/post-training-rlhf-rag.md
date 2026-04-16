# Post-Training / RLHF / RAG / Information Retrieval

> 2025-04-16

## 배운 것

### Post-Training 흐름

```
Pre-training (대규모 데이터로 기본 능력 학습)
    ↓
Instruction Tuning (지시 따르기 학습)
    ↓
RLHF (인간 피드백 기반 강화학습)
    ↓
배포 (Deploy)
```

---

### Instruction Tuning

모델이 사람의 지시를 잘 따르도록 파인튜닝. Pre-training과의 차이:
- Pre-training: 다음 토큰 예측
- Instruction Tuning: 지시 수행

데이터 형식: `(instruction, input, output)` 트리플렛

```
Instruction: 다음 문장을 영어로 번역해줘
Input: 오늘 날씨가 좋다
Output: The weather is nice today
```

특징: 적은 데이터로도 효과적. 학습 안 한 새 지시에도 어느 정도 대응 가능(Zero-shot).

---

### RLHF (Reinforcement Learning from Human Feedback)

**3단계 파이프라인**

1. **SFT** — 사람이 작성한 고품질 응답으로 파인튜닝
2. **보상 모델 학습** — 동일 질문에 여러 응답 생성 → 사람이 순위 매김 → 보상 모델(RM) 학습
3. **RL 최적화 (PPO)** — 보상 모델 기준으로 강화학습, PPO 알고리즘 주로 사용

한계: 사람 피드백 수집 비용 높음, 보상 해킹(reward hacking) 발생 가능.

---

### RAG (Retrieval-Augmented Generation)

외부 지식 베이스에서 정보를 검색해 LLM 생성에 활용하는 기법.

| 문제 | RAG로 해결 |
|:---|:---|
| LLM 지식 컷오프 | 최신 정보 검색 |
| 환각(Hallucination) | 실제 문서 기반 답변 |
| 기업 내부 데이터 | 외부 DB 연결 |

```
질문 → 쿼리 임베딩 → 벡터 DB 유사 문서 검색 → LLM에 문서+질문 입력 → 답변 생성
```

---

### Information Retrieval 종류

**Sparse Retrieval (키워드 기반)**
- TF-IDF: 단어 빈도 × 역문서 빈도
- BM25: TF-IDF 개선판, 현재도 강력한 베이스라인
- 장점: 빠르고 해석 가능 / 단점: 동의어·문맥 파악 어려움

**Dense Retrieval (임베딩 기반)**
- DPR: 질문/문서 각각 인코딩 후 유사도 계산
- Bi-Encoder: 쿼리·문서 독립 인코딩 (빠름)
- Cross-Encoder: 쿼리+문서 함께 인코딩 (정확하지만 느림)
- 장점: 의미적 유사성 파악 / 단점: 계산 비용 높음

**Hybrid Retrieval**: Sparse + Dense 결합 → 재랭킹(Reranking) → 최종 선택

---

### Tool Usage & MCP

**Tool Usage**: LLM이 외부 도구(API, 계산기, 검색엔진 등)를 호출해 능력을 확장하는 기법.

**MCP (Model Context Protocol)**: LLM이 외부 도구와 표준화된 방식으로 소통하기 위한 프로토콜. Anthropic이 2024년 말 제안한 오픈 표준.

| 항목 | Tool Usage | MCP |
|:---|:---|:---|
| 개념 | LLM이 도구를 사용하는 능력 | 도구 연결 표준 규약 |
| 비유 | "전화 통화 능력" | "전화기 표준 규격" |

## 막혔던 것 / 해결

RLHF에서 보상 해킹이 왜 생기는지 헷갈렸음.  
보상 모델이 완벽하지 않기 때문에 LLM이 실제로 좋은 답변을 하는 게 아니라 보상 모델을 속이는 방향으로 최적화될 수 있음.
