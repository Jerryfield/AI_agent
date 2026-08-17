# Failure — {{Problem Name}}

> **Status:** Investigating / Solved
>
> **一句话描述：**
>
> 用一句话描述问题的核心现象。

---

## 1. 问题现象

发生了什么？

尽量描述可观察到的事实，不要在这里直接写原因。

例如：

> Agent 在执行 `search_code` 后持续重复调用同一个 Tool，无法进入 Final Answer。

---

## 2. 预期行为

原本应该发生什么？

```text
Expected Flow
  ↓
...
```

---

## 3. 实际行为

实际发生了什么？

```text
Actual Flow
  ↓
...
```

---

## 4. 影响

这个问题造成了什么影响？

例如：

- Task 失败
- Tool Call 次数异常
- Token 成本增加
- Latency 增加
- 重复写入数据
- Agent 无法停止

---

## 5. 复现方式

### Input

```text

```

### Environment

- Model:
- Prompt Version:
- Code Version / Commit:
- SDK / Framework:
- OS:
- Other:

### Steps

1. 
2. 
3. 

---

## 6. Trace / Log / Evidence

只保留和问题有关的证据。

```text

```

如果涉及 Agent：

重点关注：

```text
User Input
↓
Context
↓
Model Output
↓
Tool Call
↓
Tool Result
↓
Next Model Call
```

---

## 7. 排查过程

不要只记录最终答案。

记录真正有价值的排查思路。

### Hypothesis 1

**怀疑：**

> 

**如何验证：**

> 

**结果：**

> 

**结论：**

Confirmed / Rejected

---

### Hypothesis 2

**怀疑：**

> 

**如何验证：**

> 

**结果：**

> 

**结论：**

Confirmed / Rejected

---

## 8. Root Cause

最终根因：

> 

为什么这个原因会导致当前问题：

> 

---

## 9. Solution

采取了什么修改？

### Change

- 
- 

### Key Code / Config

```python
# key fix
```

---

## 10. Verification

怎么确认问题真的解决了？

### Before

```text
Task Result:
Tool Calls:
Latency:
Cost:
Other:
```

### After

```text
Task Result:
Tool Calls:
Latency:
Cost:
Other:
```

---

## 11. Engineering Lesson

这次问题让我真正理解了什么？

> 

以后遇到类似问题，我会优先检查：

1. 
2. 
3. 

---

## 12. Prevention

未来如何避免同类问题？

- [ ] 
- [ ] 

例如：

- 添加 Stop Condition
- 增加 Eval Case
- 增加参数校验
- 增加 Tool Permission
- 增加 Timeout / Retry 限制

---

## 13. Related Knowledge

- [[]]
- [[]]

---

## 14. Related Lab / Project

### Lab

- [[]]

### Project

- [[]]
