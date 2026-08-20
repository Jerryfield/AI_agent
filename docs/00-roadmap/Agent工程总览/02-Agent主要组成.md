# Agent核心组件

> 记录 Agent 的核心组成及关键边界，避免展开到具体框架实现。

---

## 1. Core Components

一个典型 Agent 可以抽象为：

```text
                         User Goal
                            │
                            ▼
                    ┌───────────────┐
                    │ Instructions  │
                    └───────┬───────┘
                            │
             ┌──────────────▼──────────────┐
             │           Context           │
             │                             │
             │ User Input                  │
             │ State                       │
             │ Memory                      │
             │ Retrieved Knowledge         │
             │ Tool Results                │
             └──────────────┬──────────────┘
                            │
                            ▼
                     ┌────────────┐
                     │   Model    │
                     └─────┬──────┘
                           │
                     Decide Next
                           │
             ┌─────────────┴─────────────┐
             │                           │
         Tool Call                   Final Answer
             │                           │
             ▼                           ▼
       Guardrails / HITL           Output Guardrail
             │                           │
             ▼                           ▼
           Tool                    Stop Condition
             │
             ▼
        Tool Result
             │
             ▼
        Update State
             │
             ▼
       Agent Loop Again
```

常见核心组件：

- Model
- Instructions
- Context
- Tools
- Agent Loop
- State
- Memory
- Stop Condition
- Guardrails
- Human-in-the-loop

---

## 2. Model

Model 是 Agent 的决策组件，主要负责：

- 理解任务
- 分析 Context
- 判断下一步
- 选择 Tool 或生成最终回答

核心理解：

> Model ≠ Agent

---

## 3. Instructions

Instructions 定义 Agent：

- 是谁
- 要完成什么
- 应该如何工作
- 有哪些行为约束

例如：

```text
You are a software engineering agent.

- Read before editing.
- Run tests after changes.
- Never push without approval.
```

核心理解：

> Instructions 是行为指导，不应该承担全部安全控制。

---

## 4. Context

Context 是：

> 当前这一次 Model Call 能看到的信息。

可能包括：

- User Goal
- Instructions
- Conversation History
- Relevant State
- Tool Results
- Retrieved Knowledge
- Memory

核心：

```text
Context = Model sees
```

---

## 5. Tools

Tools 是 Agent 与外部环境交互的能力，例如：

```text
read_file
edit_file
search_code
run_test
database_query
send_email
```

Tools 决定 Agent 的：

> Action Space

Tool 权限越大，能力越强，同时风险也越高。

---

## 6. Agent Loop

Agent Loop 是 Agent 的核心运行机制：

```text
Model
 ↓
Decision
 ↓
Tool
 ↓
Observation
 ↓
Model
 ↓
...
```

简化：

```text
Observe
→ Decide
→ Act
→ Observe
→ Repeat
```

---

## 7. State

State 表示：

> 当前任务现在处于什么状态。

例如：

```json
{
  "task": "fix failing tests",
  "step": 5,
  "tests_failed": 2,
  "modified_files": ["UserService.java"]
}
```

核心：

```text
State = System knows now
```

---

## 8. Memory

Memory 保存：

> 过去的信息中，未来仍值得再次使用的内容。

例如：

```text
用户偏好：
- Python 项目使用 uv
- 不允许自动 git push
```

核心：

```text
Memory = System remembers
```

---

## 9. Context vs State vs Memory

这是最重要的边界之一：

```text
Context = Model sees

State = System knows now

Memory = System remembers
```

关系：

```text
State ──┐
        ├─ select / retrieve → Context → Model
Memory ─┘
```

---

## 10. Stop Condition

Stop Condition 决定：

> Agent 什么时候必须结束。

常见条件：

- Final Answer
- Goal 已验证完成
- Max Steps
- Timeout
- Token / Cost Budget
- Unrecoverable Error

工程上最好不要只依赖：

> “模型说任务完成了。”

而应该配合外部 Verification。

---

## 11. Guardrails

Guardrails 是：

> 系统自动执行的检查与约束。

常见位置：

```text
Input Guardrail
Tool Guardrail
Output Guardrail
```

核心区别：

```text
Instructions
= 告诉模型不要做

Guardrails
= 系统不允许模型做
```

---

## 12. Human-in-the-loop

HITL 是：

> 在关键操作前暂停 Agent，把决定交给人。

例如：

```text
Agent proposes git push
        ↓
Pause
        ↓
Human Approve / Reject
        ↓
Resume
```

常用于：

- Production Deploy
- Delete
- Payment
- Database Write
- External Communication

---

## 13. Guardrails vs HITL

```text
Guardrail
= Machine-enforced boundary

HITL
= Human decision boundary
```

例如：

```text
金额 > 50000
→ 自动拒绝
```

是 Guardrail。

```text
金额 > 50000
→ 暂停等待人工审批
```

是 HITL。

---

## 14. Minimal Mental Model

```text
Model      = decide
Tools      = act
Context    = see
State      = track
Memory     = remember
Loop       = repeat
Stop       = finish
Guardrails = constrain
HITL       = escalate to human
```

---

## 15. Three Important Boundaries

### Model ≠ Agent

Model 只是 Agent 的决策组件。

### Context ≠ State ≠ Memory

```text
Context = Model sees
State   = System knows now
Memory  = System remembers
```

### Instructions ≠ Guardrails ≠ HITL

```text
Instructions
“应该怎么做”

Guardrails
“系统允许怎么做”

HITL
“这个决定交给人”
```

---

## 16. Interview Questions

1. **Agent 通常由哪些核心组件组成？**

   Agent 是一个由 Model 决策、Tools 行动、Context/State/Memory 提供信息，并通过 Loop 持续运行，同时由 Stop Condition、Guardrails 和 HITL 控制边界的系统。

2. **Model 和 Agent 有什么区别？**

​	Model 负责“思考和决策”，Agent 负责“围绕目标持续运行并完成任务”。

3. **Context、State、Memory 有什么区别？**

```
State ──┐
        ├── select / retrieve ──→ Context ──→ Model
Memory ─┘
```

4. **Tool 在 Agent 中承担什么作用？**

​	Tool 让 Agent 从“只能生成文本”变成“可以与外部环境交互”。

5. **Agent Loop 是什么？**

​	Agent Loop 让模型能够根据真实执行结果不断调整下一步行动。

6. **为什么需要 Stop Condition？**

​	避免死循环，不可控制行为

7. **Instructions 和 Guardrails 有什么区别？**

​	Instructions 是“告诉模型不要做”，Guardrails 是“系统不允许它做”。

8. **Guardrails 和 HITL 有什么区别？**

​	Guardrails系统自动判断，HITL由人来决定

9. **为什么高风险 Tool 通常需要 HITL？**

​	因为 LLM 的决策并不是绝对可靠的，而某些 Tool 一旦执行会产生真实、不可逆或高成本影响。把高影响决策的最终责任和控制权保留在人类或业务系统手中。

---

## 17. One-Sentence Summary

> Agent 本质上是一个由 Model 做决策、通过 Tools 行动、依赖 Context / State / Memory 保持连续性，并由 Loop、Stop Condition、Guardrails 和 HITL 控制运行边界的系统。
