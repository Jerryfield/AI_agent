# 2.1 LLM 是什么

## 1. 核心定义

LLM（Large Language Model）可以理解为：

> 根据已有 Token，预测下一个 Token 的概率生成模型。

简化表示：

```text
Previous Tokens
↓
LLM
↓
Next Token Probability
↓
Select Token
↓
Repeat
```

即：

```text
P(next_token | previous_tokens)
```

---

## 2. Token

Token 是模型处理文本的基本单位，不完全等于“字”或“单词”。

```text
Text
↓
Tokenizer
↓
Tokens
↓
Model
```

因此：

```text
Context Window
Token Usage
Token Budget
```

都是基于 Token 计算的。

---

## 3. Next Token Prediction

LLM 的训练目标虽然是预测下一个 Token，但为了做好预测，模型会从大规模数据中学习：

- 语言结构
- 世界知识
- 代码模式
- 概念关系
- 任务结构
- 推理模式

核心认识：

> Simple training objective ≠ Simple capability.

因此，“LLM 只是自动补全”虽然描述了生成机制，但不足以描述模型最终表现出的能力。

---

## 4. Foundation Model

Foundation Model 是在大规模、广泛数据上训练得到的通用基础模型，可以支持多种下游任务：

```text
Foundation Model
├── Chatbot
├── Coding Assistant
├── RAG
├── Agent
└── Vertical Application
```

---

## 5. Pretraining 与 Instruction Tuning

### Pretraining

通过大规模数据进行 Token Prediction，获得基础语言、知识和代码能力。

```text
Large-scale Data
↓
Pretraining
↓
Pretrained / Foundation Model
```

### Instruction Tuning

通过“指令 → 理想回答”形式的数据，让模型学习遵循用户指令。

```text
Pretrained Model
↓
Instruction Tuning
↓
Instruction-Tuned Model
```

可以简单理解为：

```text
Pretraining
= 学习语言、知识和模式

Instruction Tuning
= 学习如何按照指令完成任务
```

---

## 6. Chat Model 与 Reasoning Model

### Chat Model

针对对话和指令交互优化，通常支持：

```text
System
Developer
User
Assistant
Tool
```

等消息角色。

### Reasoning Model

针对复杂问题求解、Coding、Planning、多步骤推理等任务进一步优化。

两者底层仍然属于生成式语言模型。

---

## 7. 从 LLM 到 Agent

整体关系：

```text
Large-scale Data
↓
Pretraining
↓
Foundation Model
↓
Instruction Tuning / Alignment
↓
Chat Model / Reasoning Model
↓
LLM Application
↓
Chatbot / RAG / Agent
```

在 Agent 中：

```text
LLM
= 理解 Context + 生成决策

Agent Runtime
= 执行决策
```

例如：

```text
Context
↓
LLM
↓
Tool Call
↓
Agent Runtime
↓
Tool
↓
Observation
↓
LLM
↓
Final Answer
```

LLM 本身不会真正调用 API，它只是生成 Tool Call；真正执行工具的是 Agent Runtime。

---

## 8. Agent Engineering 的关键理解

LLM 本质上是：

```text
Probabilistic Generator
```

而传统软件更强调：

```text
Deterministic Execution
```

因此 Agent Engineering 的重要任务之一是：

> 将概率模型包装成尽可能可靠的软件系统。

常见工程手段：

- Structured Output
- Schema
- Validation
- Tool Calling
- Retry
- Guardrails
- Evaluation
- Tracing
- External Verification

核心模型：

```text
Probabilistic World
        ↓
       LLM
        ↓
Structured Interface
        ↓
Schema / Validation / Tool Call
        ↓
Deterministic Software
```

---

## 9. 常见误区

```text
LLM ≠ Database
LLM ≠ Search Engine
LLM ≠ Agent
```

更准确地说：

```text
Model = decide / generate

Agent
= Model
+ Tools
+ Context
+ State
+ Loop
+ Runtime
+ Control
```

---

## 10. 一句话总结

> LLM 的核心生成机制是 Next Token Prediction；经过大规模预训练和指令优化后，它能够表现出语言理解、代码生成、推理和任务决策能力。在 Agent 系统中，LLM 通常负责生成决策，而 Agent Runtime 负责真正执行这些决策。

---

## 11. Interview Questions

1. LLM 的核心生成机制是什么？

​	自回归预测：根据已有 Token，预测下一个 Token 的概率分布，并不断重复生成。

2. Token 与单词有什么区别？

Token 是模型处理文本的基本单位，**不等于单词**。一个单词可能由一个或多个 Token 组成，中文字符、标点、代码片段等也可能被拆成不同 Token。

3. 为什么 Next Token Prediction 可以产生复杂能力？

模型学习了更深层次的模式

4. Pretraining 和 Instruction Tuning 有什么区别？

**Pretraining** 主要让模型学习语言、知识、代码和数据中的各种模式。**Instruction Tuning** 则进一步让模型学会：根据用户指令完成任务。

5. Foundation Model、Chat Model、Reasoning Model 有什么关系？

Foundation Model 是通用基础模型。在此基础上经过指令训练和对齐，可以形成适合对话的 **Chat Model**，也可以进一步针对复杂问题求解进行优化，形成 **Reasoning Model**。

6. 为什么 LLM 可以生成 Tool Call，但真正执行 Tool 的不是 LLM？

LLM 负责决定调用什么，Runtime 负责真正执行。

7. 为什么 Agent 系统需要 Structured Output、Validation 和 Evaluation？

因为 LLM 是概率模型，输出并不能保证每次都正确、合法、稳定。本质上是在解决：**Probabilistic LLM 与 Reliable Software System 之间的可靠性问题。**
