# Project — {{Project Name}}

> **Status:** Planning / Developing / Evaluating / Completed
>
> **一句话描述：**
>
> 用一句话说明这个项目要解决什么问题。

---

## 1. 项目目标

这个项目最终要解决什么问题？

> 

项目完成后，用户应该能够：

- 
- 
- 

---

## 2. 为什么做这个项目？

这个项目主要用于练习哪些能力？

- [ ] LLM Application
- [ ] Structured Output
- [ ] Tool Calling
- [ ] Agent Loop
- [ ] Context Engineering
- [ ] RAG
- [ ] Memory
- [ ] MCP
- [ ] Workflow
- [ ] Multi-Agent
- [ ] Human-in-the-loop
- [ ] Evals
- [ ] Security
- [ ] Production Engineering

---

## 3. User Story

### User

谁会使用这个系统？

> 

### Problem

用户当前遇到什么问题？

> 

### Goal

希望 Agent 帮用户完成什么？

> 

---

## 4. Scope

### V1 必须实现

- [ ] 
- [ ] 
- [ ] 

### 暂时不实现

- [ ] 
- [ ] 

### 为什么暂时不实现？

> 

用于防止项目无限膨胀。

---

## 5. System Architecture

```text
User
 ↓
Frontend / Client
 ↓
Backend API
 ↓
Agent Runtime
 ├── Model
 ├── Instructions
 ├── Context
 ├── Tools
 ├── RAG
 ├── Memory
 └── State
 ↓
External Systems
```

根据实际项目修改。

---

## 6. Agent Workflow

```text
User Request
     ↓
Analyze
     ↓
Plan
     ↓
Act / Tool
     ↓
Observe
     ↓
Evaluate
     ↓
Finish / Retry
```

描述关键分支：

- 什么情况下继续执行？
- 什么情况下调用 Tool？
- 什么情况下需要 Human Approval？
- 什么情况下停止？

---

## 7. Components

### 7.1 Agent

职责：

> 

---

### 7.2 Model

选择：

> 

原因：

- 
- 

---

### 7.3 Tools

| Tool | Purpose | Read / Write | Risk |
|---|---|---|---|
|  |  |  |  |

---

### 7.4 RAG

是否使用：

Yes / No

用途：

> 

---

### 7.5 Memory

是否使用：

Yes / No

用途：

> 

---

### 7.6 Storage

| Storage | Purpose |
|---|---|
|  |  |

---

### 7.7 External Systems

- 
- 

---

## 8. State Design

Agent 运行过程中需要维护哪些 State？

```text
user_request
plan
current_step
tool_results
retrieved_context
error
final_answer
```

根据实际项目调整。

### State 生命周期

哪些 State：

- 仅当前 Turn 使用？
- 当前 Session 使用？
- 需要持久化？

---

## 9. Context Design

模型每一步需要看到什么？

### 必须 Context

- 
- 

### 可选 Context

- 
- 

### 不应该进入 Context

- 
- 

---

## 10. Technical Decisions

只记录真正影响系统设计的重要决定。

### Decision 01 — {{Decision Title}}

**问题**

为什么需要做这个决定？

> 

**选择**

最终选择：

> 

**原因**

- 
- 

**Alternative**

还考虑过：

- 

**为什么没有选择**

> 

**Trade-off**

这个选择带来的代价：

> 

---

## 11. Security

### Tool Permission

- 

### Human Approval

哪些操作必须人工确认？

- 

### Prompt Injection

防护：

- 

### Secret Management

- 

### File / Network Access

- 

---

## 12. Error Handling

需要考虑：

- [ ] Tool Timeout
- [ ] Tool Error
- [ ] Model Error
- [ ] Invalid Structured Output
- [ ] Retry Limit
- [ ] Agent Infinite Loop
- [ ] External API Failure

处理策略：

> 

---

## 13. Evaluation

### Test Dataset

Test Cases:

> 

### Metrics

| Metric | Target | Actual |
|---|---:|---:|
| Task Success Rate |  |  |
| Tool Selection Accuracy |  |  |
| Tool Argument Accuracy |  |  |
| Avg Latency |  |  |
| Avg Tool Calls |  |  |
| Avg Cost |  |  |

---

## 14. Problems & Failures

重要问题不要在这里展开，创建 Failure Note。

- [[]]
- [[]]

---

## 15. Project Evolution

### V0.1

实现：

- 

主要问题：

- 

---

### V0.2

修改：

- 

为什么修改：

> 

结果：

> 

---

## 16. 最终结果

项目是否达到最初目标？

> 

### Demo

- Screenshot:
- Video:
- Repository:
- API:

---

## 17. Lessons Learned

通过这个项目，我真正理解了：

1. 
2. 
3. 

如果重新设计一次，我会：

1. 
2. 

---

## 18. Related Knowledge

- [[]]
- [[]]

---

## 19. Next

下一步：

- [ ] 
- [ ] 
