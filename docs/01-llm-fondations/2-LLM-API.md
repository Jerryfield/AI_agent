# 2.2 LLM API

## 1. 核心认识

作为 Agent Engineer，通常不是自己训练模型，而是通过 API 使用模型。

最基本的调用链路：

```text
Application
↓
Request
↓
LLM API
↓
Model Inference
↓
Response / Stream
↓
Application
```

生产环境还必须考虑：

```text
Async
Error Handling
Rate Limit
Timeout
Retry
Cost
Latency
```

核心认识：

> LLM API 本质上是一个昂贵、有延迟、可能失败、受到限流的远程服务。

---

## 2. Request / Response

### Request

Request 是一次完整的模型调用配置，通常包括：

```text
Request
├── Model
├── Input / Messages
├── Instructions
├── Generation Config
├── Tools
└── Output Config
```

因此：

```text
Prompt
= 提供给模型的输入内容

Request
= Prompt + Model + Parameters + Tools + Other Config
```

### Response

Response 不只是生成文本，还可能包括：

```text
Response
├── Generated Content
├── Tool Call
├── Structured Output
├── Token Usage
├── Finish Reason
└── Metadata
```

所以：

```text
Response ≠ Text
```

Agent 中的 Response 可能直接是一个 Tool Call。

---

## 3. Streaming

普通模式：

```text
Request
↓
等待完整生成
↓
完整 Response
```

Streaming：

```text
Request
↓
LLM
↓
Chunk
↓
Chunk
↓
Chunk
↓
Complete
```

Streaming 的主要作用：

> 降低用户感知延迟（Perceived Latency）。

它通常不会显著减少完整响应的总生成时间。

---

## 4. Async

同步调用：

```text
Call LLM
↓
等待
↓
Response
↓
继续执行
```

异步调用：

> 在等待 LLM、Tool、Database 等 I/O 时，程序可以继续处理其他任务。

Agent Backend 中常见等待对象：

```text
LLM API
Search API
Database
MCP Server
External Tools
```

### Streaming vs Async

```text
Streaming
= 结果如何返回

Async
= 等待期间程序如何执行
```

两者可以组合使用：

```text
Async Streaming
```

---

## 5. Error Handling

常见错误：

```text
LLM API Error
├── Authentication Error
├── Invalid Request
├── Rate Limit
├── Timeout
├── Network Error
└── Server Error
```

不能对所有错误都直接 Retry。

### Retryable

通常是临时错误：

```text
Network Error
Timeout
Rate Limit
部分 5xx Server Error
```

### Non-Retryable

通常是请求本身存在问题：

```text
Invalid API Key
Malformed Request
Unsupported Parameter
Invalid Schema
```

标准处理思路：

```text
Error
↓
Classify
↓
Retryable?
├── Yes → Retry Policy
└── No  → Fail Fast
```

---

## 6. Rate Limit

模型服务通常会限制：

```text
Requests Per Minute
Tokens Per Minute
Concurrent Requests
```

Agent 更容易触发 Rate Limit，因为一次用户任务可能产生多次模型调用：

```text
User
↓
LLM
↓
Tool
↓
LLM
↓
Tool
↓
LLM
```

如果再加入：

```text
Multi-Agent
Parallel Tool Calls
Evaluation
Reflection
```

调用量会进一步增加。

---

## 7. Timeout

Timeout 用于限制一次外部调用最多等待多久。

```text
Request
↓
Wait
↓
Timeout Reached
↓
Abort / Handle Error
```

Agent 特别需要 Timeout，因为它可能同时依赖：

```text
LLM
Search
Database
Browser
MCP
External API
```

任何一个外部服务无限等待，都可能阻塞整个 Agent Loop。

---

## 8. Retry

Retry 用于处理临时性失败。

```text
Request
↓
Failure
↓
Retryable?
↓
Backoff
↓
Retry
```

不能无限 Retry，因此通常需要：

```text
Timeout
Max Retries
Backoff
```

### Exponential Backoff

常见等待策略：

```text
1s → 2s → 4s → 8s
```

通常还会加入 Jitter，避免大量请求同时再次冲击服务。

---

## 9. Cost

LLM API 成本通常与以下因素相关：

```text
Input Tokens
+
Output Tokens
+
Model
+
Number of Calls
```

Agent 更容易发生 Cost Explosion：

```text
更多 Agent Loop
+
更长 Context
+
更多 Tool Results
+
更多 LLM Calls
=
更高 Cost
```

因此：

> Stop Condition 不只是控制 Agent 行为，也是 Cost Control Mechanism。

---

## 10. Latency

Latency 是从请求发出到获得结果所花费的时间。

### TTFT

Time To First Token：

> 从 Request 发出到第一个 Token 返回的时间。

### Total Latency

> 从 Request 发出到完整 Response 结束的总时间。

```text
Request
↓
TTFT
↓
First Token
↓
Generating
↓
Complete
```

### Agent Latency

Agent 总延迟通常是多次调用累积：

```text
LLM
↓
Tool
↓
LLM
↓
Tool
↓
LLM
```

因此：

```text
Total Latency
≈
LLM Latency
+ Tool Latency
+ LLM Latency
+ ...
```

---

## 11. Agent Engineering 的核心 Trade-off

Agent 系统不能只关注模型能力，还需要同时权衡：

```text
Quality
Cost
Latency
Reliability
```

Agent Loop 同时会放大：

```text
Cost
Latency
Rate Limit Risk
Failure Probability
```

---

## 12. LLM Application Runtime

生产级调用流程可以理解为：

```text
Application
↓
Build Request
↓
LLM Client
↓
LLM API
↓
Success / Error
↓
Retry / Fail
↓
Response / Streaming
↓
Parse / Validate
↓
Application Logic
```

同时记录：

```text
Latency
Tokens
Cost
Errors
Retries
Request ID
```

因此生产级调用不应该只是：

```text
response = call_llm()
```

而应该逐渐具备：

```text
Request
↓
Timeout
↓
Retry
↓
Rate Limit Handling
↓
Response
↓
Validation
↓
Logging
↓
Metrics
```

---

## 13. 容易混淆的概念

```text
Streaming
= 结果如何返回

Async
= 等待期间程序如何执行
```

```text
Timeout
= 最多等多久

Retry
= 失败后是否再试
```

```text
Rate Limit
= 服务端限制调用频率或资源使用

Timeout
= 客户端等待超过设定时间
```

```text
Latency
= 花多少时间

Cost
= 花多少钱
```

---

## 14. 一句话总结

> LLM API 是 Agent 与模型交互的运行基础。生产级 Agent 必须在模型调用之外处理 Streaming、Async、Timeout、Retry、Rate Limit、Error Handling、Cost 和 Latency，才能把一个可能失败的远程模型服务包装成可靠的软件系统。

---

## 15. Interview Questions & Answers

### 1. LLM API 的 Request 和 Prompt 有什么区别？

Prompt 是提供给模型的输入内容；Request 是完整 API 调用，通常还包含 Model、Parameters、Tools 等配置。

### 2. Streaming 的作用是什么？

Streaming 让模型边生成边返回结果，主要降低用户感知延迟，但不一定减少完整生成时间。

### 3. Streaming 和 Async 有什么区别？

```text
Streaming = 结果如何返回
Async = 等待期间程序如何执行
```

两者可以同时使用。

### 4. 哪些 LLM API Error 适合 Retry？

Timeout、Network Error、Rate Limit、部分 5xx 等临时错误通常可以 Retry；认证错误、参数错误通常不应 Retry。

### 5. 为什么 Retry 需要 Exponential Backoff？

避免失败后立即重复请求，进一步加重服务器压力或 Rate Limit。

### 6. Timeout 的作用是什么？

给外部调用设置最大等待时间，防止某个 LLM 或 Tool 请求无限阻塞整个系统。

### 7. 为什么 Agent 更容易触发 Rate Limit？

因为一次 Agent 任务往往包含多次 LLM 和 Tool 调用，单次用户请求会被放大成多次 API Request。

### 8. 为什么 Agent 容易出现 Cost Explosion？

因为 Agent Loop 会增加模型调用次数、Context Tokens、Tool Results 和 Output Tokens。

### 9. TTFT 和 Total Latency 有什么区别？

TTFT 是到第一个 Token 返回的时间；Total Latency 是到完整响应结束的总时间。

### 10. 生产级 LLM 调用需要考虑哪些核心问题？

至少包括 Timeout、Retry、Rate Limit、Error Handling、Latency、Cost、Logging 和 Observability。

---

## 16. 核心速记

```text
Request ≠ Prompt

Streaming = 如何返回
Async = 如何等待

Timeout = 最多等多久
Retry = 失败后是否再试

Agent Loop
= 决策机制
+ Cost 放大器
+ Latency 放大器

LLM API
= Remote
+ Expensive
+ Fallible
+ Rate-Limited
```
