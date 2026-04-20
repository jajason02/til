# LLM 평가 / AI Agent / Memory / Tool / Deep Research

> 2026-03

## 배운 것

### LLM 평가

LLM 출력은 정답이 하나가 아니라 전통적인 정확도 측정이 어려움.

**자동 평가 지표**
- BLEU: n-gram 겹침 측정 (의미적 유사성 반영 못함)
- ROUGE: 요약 평가, 재현율 기반
- Perplexity: 낮을수록 좋음. 다음 토큰을 얼마나 확신하는지의 역수 개념.

**벤치마크**

| 벤치마크 | 측정 대상 |
|:---|:---|
| MMLU | 57개 분야 지식 |
| HumanEval | 코딩 능력 |
| GSM8K | 초등 수준 수학 |
| TruthfulQA | 사실 정확성·환각 측정 |

벤치마크 오염(Contamination): 학습 데이터에 벤치마크 문제가 포함되어 점수가 부풀려지는 문제.

**LLM-as-a-Judge**: 강력한 LLM이 다른 LLM 출력을 평가. 자기 편향(Self-bias) 주의.

---

### AI Agent

LLM이 목표를 받아 스스로 계획하고, 도구를 사용하며, 행동을 실행하는 시스템.

| 항목 | 일반 LLM | AI Agent |
|:---|:---|:---|
| 동작 | 질문 → 답변 (1회) | 목표 → 계획 → 실행 → 반복 |
| 자율성 | 낮음 | 높음 |
| 메모리 | 단일 컨텍스트 | 장기 메모리 활용 가능 |

**ReAct 패턴 (Reasoning + Acting)**

```
Thought: 뭘 해야 할지 추론
    ↓
Action: Tool 호출
    ↓
Observation: 결과 확인
    ↓
Thought: 다시 추론
    ↓
... 반복 ...
    ↓
Final Answer
```

**Multi-Agent**: Orchestrator가 Research/Writing/Review Agent에 역할 분담.

---

### Memory 4종류

| 종류 | 설명 | 인간 비유 |
|:---|:---|:---|
| Sensory | 현재 입력 (컨텍스트 윈도우의 현재 값) | 감각 기억 |
| In-Context | 컨텍스트 윈도우 내 대화 히스토리 | 단기 기억 |
| External | 벡터 DB 등 외부 저장소 (RAG와 연결) | 메모장·책 |
| In-Weights | 모델 파라미터에 내재화된 지식 | 장기 기억 |

---

### Tool & Function Calling

```python
tools = [
    {
        "name": "get_weather",
        "description": "특정 도시의 날씨를 가져옴",
        "parameters": {"city": "string"}
    }
]
# LLM이 필요 시 → {"name": "get_weather", "parameters": {"city": "서울"}}
# → 실제 함수 실행 → 결과 전달 → 최종 답변
```

주의: Tool 결과를 무시하고 자체 답변하는 경우, 적절하지 않은 Tool 호출, 보안 이슈.

---

### Deep Research

AI Agent가 복잡한 질문에 자율적으로 여러 단계의 검색·추론을 반복해 심층 보고서를 생성.

| 항목 | 일반 RAG | Deep Research |
|:---|:---|:---|
| 검색 횟수 | 1~2회 | 수십 회 반복 |
| 자율성 | 낮음 | 높음 |
| 출력물 | 짧은 답변 | 구조화된 보고서 |

```
질문 분해 → 각 sub-question 검색 → 새로운 질문 생성 → 반복 → 종합 → 보고서
```

## 막혔던 것 / 해결

Memory 4종류 중 Sensory와 In-Context 차이가 헷갈렸음.  
Sensory는 지금 이 순간 들어오는 raw 입력(이미지, 텍스트), In-Context는 대화 히스토리 포함 컨텍스트 전체.
