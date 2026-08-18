# Agent Basic Concepts

> 本笔记只记录 Agent 的核心边界与架构概念，不重复 AI Application 的演进过程。

---

## 1. Agent 是什么

可以把 Agent 暂时理解为：

> 围绕一个目标运行，由模型根据当前 Context、State 和 Observation 动态决定下一步行动，并通过 Tools 与环境交互，持续执行直到任务完成或满足停止条件的 AI 系统。

核心结构：

```text
Goal
 ↓
Observe
 ↓
Decide
 ↓
Act
 ↓
Observe
 ↓
...
 ↓
Finish
```

Agent 的关键不在于“用了 LLM”或“调用了 Tool”，而在于：

> **模型是否参与运行时决策。**

---

## 2. Agent 的核心特征

一个典型 Agent 通常包含：

- Goal：需要完成的任务
- Model：负责理解、推理和决策
- Context：当前模型可见的信息
- Tools：可执行的外部能力
- State：当前任务执行状态
- Loop：持续 Observe → Decide → Act
- Stop Condition：决定何时结束

简化理解：

```text
Agent
=
Goal
+
Runtime Decision
+
Action
+
Feedback Loop
```

---

## 3. Agent vs Chatbot

### Chatbot

核心目标：

```text
User Message
 ↓
Response
```

重点是：

> Conversation

### Agent

核心目标：

```text
User Goal
 ↓
Actions
 ↓
Environment Change
 ↓
Outcome
```

重点是：

> Task Completion

因此：

> Chat 是交互形式，Agent 是执行架构。

一个 Agent 完全可以使用 Chat UI。

---

## 4. Agent vs Workflow

这是最重要的边界之一。

### Workflow

```text
Step A
 ↓
Step B
 ↓
Step C
```

主要执行路径由开发者提前定义。

核心：

> **Code owns the control flow.**

### Agent

```text
Goal
 ↓
Model
 ↓
Decide Next Action
 ↓
Tool
 ↓
Observation
 ↓
Decide Again
```

执行路径会根据运行时结果动态变化。

核心：

> **Model dynamically participates in control flow.**

判断一个系统是不是 Agent，不应该只看有没有 Tool，而应该问：

> 下一步行动是代码写死的，还是模型根据当前状态动态决定的？

---

## 5. Agent vs Traditional Automation

### Traditional Automation

特点：

```text
Trigger
+
Predefined Procedure
```

例如：

```text
Login
 ↓
Download
 ↓
Send Email
```

属于：

> Procedure-driven

### Agent

特点：

```text
Goal
 ↓
Observe
 ↓
Decide
 ↓
Act
 ↓
Adapt
```

属于：

> Goal-driven

区别在于：

> 传统自动化主要执行预定义步骤，Agent 可以根据 Observation 调整执行策略。

---

## 6. Tool Calling ≠ Agent

下面这个系统：

```text
LLM
 ↓
Search
 ↓
LLM
 ↓
Database
```

不一定是 Agent。

如果代码已经固定：

```text
Generate Query
 ↓
Search
 ↓
Summarize
 ↓
Save
```

它更接近 Workflow。

因此：

> Tool Calling 是 Agent 的基础能力之一，但不是判断 Agent 的充分条件。

---

## 7. Single Agent

Single Agent 指系统中只有一个主要决策主体。

例如：

```text
            Coding Agent
          /     |      \
         ↓      ↓       ↓
      Files   Shell   Tests
```

一个 Single Agent 也可以拥有：

- 多个 Tools
- RAG
- Memory
- State
- MCP
- HITL
- Planning

所以：

> Single Agent 不等于 Simple Agent。

工程上通常应该先建立 Single Agent Baseline，再判断是否真的需要拆分。

---

## 8. Multi-Agent

Multi-Agent 指系统中存在多个具有独立角色、Instructions、Context 或 Tools 的 Agent，并通过某种机制协作。

例如：

```text
          Manager Agent
          /     |      \
         ↓      ↓       ↓
     Planner   Coder   Reviewer
```

常见协作方式：

### Manager / Agent as Tool

```text
Manager
   ↓
调用 Specialist Agent
   ↓
结果返回 Manager
```

Manager 始终保留总体控制权。

### Handoff

```text
Agent A
   ↓
移交任务控制权
   ↓
Agent B
```

当前任务由新的 Agent 接管。

---

## 9. Multi-Agent 不是目标

Multi-Agent 会增加：

- Context 管理复杂度
- 通信成本
- Latency
- Token Cost
- Debug 难度
- Failure Modes

因此：

> Multi-Agent 是架构选择，不是 Single Agent 的升级版。

优先顺序：

```text
Single Agent
 ↓
建立 Baseline
 ↓
发现明确瓶颈
 ↓
再考虑 Multi-Agent
```

---

## 10. Agentic Workflow

Agentic Workflow 可以理解为：

> 高层流程由代码控制，但部分节点交给 Agent 动态决策的混合架构。

例如：

```text
Permission Check
      ↓
┌───────────────────┐
│   Agent Process   │
│ Observe → Decide  │
│    → Tool → ...   │
└───────────────────┘
      ↓
Human Approval
      ↓
Database Write
      ↓
Audit Log
```

特点：

```text
Deterministic Workflow
        +
Local Agent Autonomy
```

这种模式通常更适合企业生产系统，因为：

- 关键业务边界可控
- Agent 仍能处理开放问题
- 高风险操作可以保留人工审批
- 更容易审计和 Debug

---

## 11. Core Boundary

判断 Agent 最重要的问题：

> **Who owns the control flow?**

如果：

```text
Developer
 ↓
Predefined Flow
```

更接近：

> Workflow / Automation

如果：

```text
Model
 ↓
根据 Observation
动态决定下一步
```

更接近：

> Agent

---

## 12. Quick Comparison

| 类型 | 核心关注点 | Control Flow |
|---|---|---|
| Chatbot | Conversation | 通常较简单 |
| Automation | 执行固定过程 | Code |
| Workflow | 编排多个步骤 | Code |
| Agent | 完成目标 | Model 参与动态决策 |
| Single Agent | 单一主要决策主体 | 一个 Agent |
| Multi-Agent | 多 Agent 协作 | 多个 Agent |
| Agentic Workflow | Workflow + 局部 Agent | Code + Model |

---

## 13. My Current Mental Model

我目前判断 Agent 时，优先看四件事：

```text
Goal
 ↓
Runtime Decision
 ↓
Action
 ↓
Feedback Loop
```

最重要的判断不是：

> 有没有 LLM？  
> 有没有 Tool？  
> 有没有很多步骤？

而是：

> **系统是否允许模型根据运行时 Observation 动态决定下一步行动。**

---

## 14. Interview Questions

1. 什么是 AI Agent？
2. Agent 和 Chatbot 有什么区别？
3. Agent 和 Workflow 最核心的区别是什么？
4. 为什么 Tool Calling 不等于 Agent？
5. Agent 和传统自动化有什么区别？
6. Single Agent 和 Multi-Agent 如何选择？
7. 什么情况下应该考虑 Multi-Agent？
8. 什么是 Agentic Workflow？
9. 为什么企业 Agent 通常不会让模型控制所有业务流程？

---

## 15. One-Sentence Summary

> Agent 的核心不是“调用了多少 AI 能力”，而是模型是否围绕目标，在受控边界内根据运行时反馈持续决定并执行下一步行动。
