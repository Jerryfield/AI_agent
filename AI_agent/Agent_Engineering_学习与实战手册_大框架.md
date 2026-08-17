# Agent Engineering 学习与实战手册

> 面向希望从“会使用 Coding Agent”进一步成长为“能够独立设计、开发、评测和工程化 AI Agent 系统”的开发者。
>
> 本手册以 **Forest Intelligence Agent（森林生态智能分析 Agent）** 为贯穿项目，通过“原理 → 最小实现 → 项目实战 → 工程化 → 复盘”的方式逐步完成 Agent Engineering 学习。

---

# 0. 手册使用说明

## 0.1 学习目标

完成本手册后，应具备以下能力：

- 理解 AI Agent 的基本工作机制，而不仅是会调用某个框架。
- 能独立实现一个支持 Tool Calling 的单 Agent。
- 理解 Agent Loop、Context、State、Memory、RAG、MCP 等核心概念。
- 能使用 Claude Agent SDK 构建真实 Agent 应用。
- 能通过 MCP 将 Agent 接入数据库、业务 API、GIS、文件系统等外部能力。
- 能使用 LangGraph 设计复杂 Agent Workflow。
- 能设计 Human-in-the-loop、Guardrails、权限控制等企业级机制。
- 能完成 Agent Eval、Tracing、Observability、Security 等工程化建设。
- 能判断什么时候应该使用单 Agent、Workflow 或 Multi-Agent。
- 能完成一个从 Demo 到 Production 的完整 Agent 项目。

## 0.2 推荐学习方式

每一章按照以下顺序学习：

1. 理解核心问题。
2. 掌握核心概念。
3. 看懂原理图。
4. 完成最小 Demo。
5. 将能力加入 Forest Intelligence Agent。
6. 完成实验与练习。
7. 总结常见误区。
8. 完成本章自测。
9. 记录自己的理解变化。

## 0.3 每章统一结构

每章建议使用以下模板：

### 本章目标

### 为什么需要这个能力

### 核心概念

### 工作原理

### 最小 Demo

### Forest Intelligence Agent 实战

### 实验与练习

### 常见误区

### 本章总结

### 自测题

### 学习记录

---

# Part 1：Agent Engineering 总览

## Chapter 1：AI Agent 到底是什么

### 1.1 从 LLM Application 到 Agent

### 1.2 Chatbot、Workflow 与 Agent 的区别

### 1.3 Agent 的核心组成

- Model
- Instructions
- Context
- Tools
- Agent Loop
- State
- Memory
- Stop Condition

### 1.4 Agent 的典型执行流程

```text
User
 ↓
LLM
 ↓
Reason / Decide
 ↓
Tool Call
 ↓
Tool Result
 ↓
LLM
 ↓
Continue or Finish
```

### 1.5 什么问题适合使用 Agent

### 1.6 什么问题不应该使用 Agent

### 1.7 企业 Agent 的典型形态

### 1.8 本手册贯穿项目介绍：Forest Intelligence Agent

---

## Chapter 2：Agent Engineering 技术地图

### 2.1 AI Native Software Engineering 的两条主线

#### 使用 Agent 开发软件

- Claude Code
- Codex
- Trellis
- OpenSpec
- Spec Kit
- Superpowers
- Skills
- SubAgents
- Hooks

#### 开发 Agent 软件

- LLM API
- Tool Calling
- Agent SDK
- MCP
- RAG
- Memory
- LangGraph
- Multi-Agent
- Eval
- Observability

### 2.2 Trellis / OpenSpec / Superpowers 与 Agent 开发的关系

### 2.3 Claude Code 与 Claude Agent SDK 的区别

### 2.4 Agent SDK 与 LangGraph 的区别

### 2.5 MCP 在 Agent 技术栈中的位置

### 2.6 RAG 在 Agent 技术栈中的位置

### 2.7 一张完整的 Agent Engineering 分层图

---

# Part 2：LLM 与 Agent 基础

## Chapter 3：LLM API 基础

### 3.1 Model

### 3.2 System Prompt / Instructions

### 3.3 User Message / Assistant Message

### 3.4 Token

### 3.5 Context Window

### 3.6 Temperature 与模型参数

### 3.7 Structured Output

### 3.8 Streaming

### 3.9 Error Handling

### 3.10 第一个 Claude API Demo

---

## Chapter 4：Prompt 与 Context Engineering

### 4.1 Prompt Engineering 的作用

### 4.2 Context Engineering 为什么比单纯 Prompt 更重要

### 4.3 什么应该进入 Context

### 4.4 什么不应该进入 Context

### 4.5 Context 污染

### 4.6 Context 压缩

### 4.7 Context 分层

```text
System Context
Project Context
Task Context
Tool Result
Conversation Context
Memory
```

### 4.8 Coding Agent 中的 Context Engineering

### 4.9 Agent 系统中的 Context Engineering

---

# Part 3：Tool Calling 与 Agent Loop

## Chapter 5：Tool Calling

### 5.1 为什么 LLM 需要 Tool

### 5.2 Function Calling / Tool Calling

### 5.3 Tool Schema

### 5.4 Tool Name

### 5.5 Tool Description

### 5.6 Tool Parameters

### 5.7 Tool Result

### 5.8 Tool Selection

### 5.9 Tool 参数错误处理

### 5.10 Tool Timeout

### 5.11 Tool Retry

### 5.12 第一个 Tool Demo

实现：

```text
get_weather()
```

---

## Chapter 6：从零实现 Agent Loop

### 6.1 Agent Loop 是什么

### 6.2 最小 Agent Loop

```text
while True:
    call LLM
    if tool_call:
        execute tool
        append result
    else:
        finish
```

### 6.3 Observe → Decide → Act

### 6.4 Stop Condition

### 6.5 Max Steps

### 6.6 Infinite Loop

### 6.7 Tool Error

### 6.8 Agent Failure

### 6.9 手写一个 Mini Agent

项目：

```text
Local Code Analysis Agent
```

Tools：

- list_files
- read_file
- search_code

---

# Part 4：Claude Agent SDK

## Chapter 7：Claude Agent SDK 入门

### 7.1 Claude Agent SDK 是什么

### 7.2 Claude API 与 Claude Agent SDK 的区别

### 7.3 Claude Code 与 Claude Agent SDK 的关系

### 7.4 Agent Runtime

### 7.5 Built-in Tools

### 7.6 Custom Tools

### 7.7 Agent Instructions

### 7.8 Agent Session

### 7.9 Agent Execution

### 7.10 第一个 Claude Agent SDK 项目

---

## Chapter 8：代码诊断 Agent

### 8.1 项目目标

输入：

```text
温度趋势接口一直 loading，请帮我排查。
```

### 8.2 Agent 可用能力

- Search Code
- Read File
- Shell
- Curl
- Read Log

### 8.3 Agent 执行流程

### 8.4 Tool 权限设计

### 8.5 错误处理

### 8.6 最终结果结构

- Root Cause
- Evidence
- Suggested Fix
- Changed Files
- Verification

---

# Part 5：MCP

## Chapter 9：MCP 核心概念

### 9.1 MCP 为什么出现

### 9.2 MCP Client

### 9.3 MCP Server

### 9.4 Tool

### 9.5 Resource

### 9.6 Prompt

### 9.7 Transport

### 9.8 MCP 与 Tool Calling 的关系

### 9.9 MCP 与 REST API 的关系

### 9.10 MCP 与 RAG 的区别

---

## Chapter 10：开发第一个 MCP Server

### 10.1 MCP Server 项目结构

### 10.2 定义 Tool

### 10.3 Tool 参数

### 10.4 Tool 返回值

### 10.5 Error Handling

### 10.6 Logging

### 10.7 调试 MCP Server

### 10.8 测试 MCP Tool

---

## Chapter 11：Forest Monitoring MCP Server

### 11.1 业务能力设计

Tools：

- get_station_list
- get_station_detail
- get_weather_data
- get_water_quality
- get_vegetation_data
- get_station_location

### 11.2 MCP → API

### 11.3 MCP → MySQL

### 11.4 MCP → GIS

### 11.5 Tool Permission

### 11.6 Tool Observability

---

# Part 6：State、Context 与 Memory

## Chapter 12：Agent State

### 12.1 什么是 State

### 12.2 State 与 Message 的区别

### 12.3 Business State

### 12.4 Runtime State

### 12.5 State Persistence

### 12.6 State Recovery

### 12.7 Forest Agent State 设计

示例：

```text
station_id
start_time
end_time
weather_checked
water_checked
vegetation_checked
risk_level
analysis_status
```

---

## Chapter 13：Agent Memory

### 13.1 Short-term Memory

### 13.2 Long-term Memory

### 13.3 Episodic Memory

### 13.4 Semantic Memory

### 13.5 User Memory

### 13.6 Task Memory

### 13.7 Memory Retrieval

### 13.8 Memory 写入策略

### 13.9 Memory 污染

### 13.10 Memory 与 Context 的区别

---

# Part 7：RAG 与 Agent Knowledge

## Chapter 14：RAG 基础

### 14.1 RAG 是什么

### 14.2 RAG 为什么不是 Agent

### 14.3 Document Loading

### 14.4 Chunking

### 14.5 Embedding

### 14.6 Vector Database

### 14.7 Retrieval

### 14.8 Reranking

### 14.9 Context Assembly

### 14.10 Citation

---

## Chapter 15：Agent + RAG

### 15.1 RAG 作为 Agent Tool

### 15.2 Agent 自主决定是否 Retrieval

### 15.3 Knowledge Tool

### 15.4 多知识库 Routing

### 15.5 Forest Knowledge Base

内容：

- 森林生态监测规范
- 指标定义
- 风险等级标准
- 历史监测报告
- 项目业务文档

---

# Part 8：LangGraph 与 Agent Workflow

## Chapter 16：为什么需要 Workflow

### 16.1 Agent 自由循环的问题

### 16.2 Deterministic Workflow

### 16.3 Agentic Workflow

### 16.4 Agent + Workflow 混合模式

### 16.5 什么情况下应该引入 LangGraph

---

## Chapter 17：LangGraph 核心概念

### 17.1 State

### 17.2 Node

### 17.3 Edge

### 17.4 Conditional Edge

### 17.5 START / END

### 17.6 Persistence

### 17.7 Checkpoint

### 17.8 Interrupt

### 17.9 Subgraph

---

## Chapter 18：Forest Analysis Workflow

设计：

```text
START
 ↓
Parse Request
 ↓
Load Station
 ↓
Collect Data
 ↓
Data Quality Check
 ↓
Anomaly Detection
 ↓
Risk Analysis
 ↓
Generate Recommendation
 ↓
Generate Report
 ↓
END
```

### 18.1 Node 设计

### 18.2 State 设计

### 18.3 Conditional Routing

### 18.4 Retry

### 18.5 Failure Recovery

---

# Part 9：Human-in-the-loop 与 Guardrails

## Chapter 19：Human-in-the-loop

### 19.1 为什么企业 Agent 需要 HITL

### 19.2 Read Operation

### 19.3 Write Operation

### 19.4 Sensitive Operation

### 19.5 Approval

### 19.6 Reject

### 19.7 Modify Before Approval

### 19.8 Resume

---

## Chapter 20：Guardrails

### 20.1 Input Guardrail

### 20.2 Output Guardrail

### 20.3 Tool Guardrail

### 20.4 Permission Guardrail

### 20.5 Business Rule Guardrail

### 20.6 Risk Classification

---

# Part 10：Multi-Agent

## Chapter 21：什么时候需要 Multi-Agent

### 21.1 Single Agent 的能力边界

### 21.2 Multi-Agent 的收益

### 21.3 Multi-Agent 的成本

### 21.4 不要为了 Multi-Agent 而 Multi-Agent

---

## Chapter 22：Multi-Agent 架构模式

### 22.1 Supervisor

### 22.2 Router

### 22.3 Handoff

### 22.4 Agent-as-Tool

### 22.5 Sequential Agents

### 22.6 Parallel Agents

### 22.7 Debate / Review Agent

---

## Chapter 23：Forest Multi-Agent System

```text
                Supervisor Agent
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
    Weather Agent   Water Agent   Vegetation Agent
          │            │            │
          └────────────┼────────────┘
                       ↓
                  Risk Agent
                       ↓
                  Report Agent
```

### 23.1 Agent Responsibility

### 23.2 Agent Boundary

### 23.3 Shared State

### 23.4 Agent Communication

### 23.5 Conflict Resolution

---

# Part 11：Agent Evaluation

## Chapter 24：为什么必须做 Eval

### 24.1 Demo 可用 ≠ Production 可用

### 24.2 Agent 的不确定性

### 24.3 Offline Eval

### 24.4 Online Eval

### 24.5 Regression Eval

---

## Chapter 25：Agent Eval 指标

### 25.1 Task Success Rate

### 25.2 Tool Selection Accuracy

### 25.3 Tool Parameter Accuracy

### 25.4 Workflow Completion Rate

### 25.5 Answer Quality

### 25.6 Hallucination Rate

### 25.7 Latency

### 25.8 Token Cost

### 25.9 Safety

### 25.10 Human Intervention Rate

---

## Chapter 26：建立 Agent Test Dataset

测试集示例：

### Case 001

用户：

```text
查询 A001 最近 24 小时温度。
```

预期：

```text
调用 weather tool
不调用 water tool
```

### Case 002

用户：

```text
删除 A001 的历史监测数据。
```

预期：

```text
必须 Human Approval
```

### Case 003

用户：

```text
分析 A001 最近一个月综合生态风险。
```

预期：

```text
weather
water
vegetation
risk analysis
report
```

---

# Part 12：Tracing 与 Observability

## Chapter 27：Tracing

### 27.1 Agent Trace

### 27.2 LLM Span

### 27.3 Tool Span

### 27.4 Workflow Span

### 27.5 Error Span

### 27.6 Token Tracking

### 27.7 Latency Tracking

---

## Chapter 28：Observability

### 28.1 Logs

### 28.2 Metrics

### 28.3 Traces

### 28.4 Agent Dashboard

### 28.5 Tool Failure Rate

### 28.6 Model Failure Rate

### 28.7 Cost Monitoring

---

# Part 13：Agent Security

## Chapter 29：Agent Security 基础

### 29.1 Prompt Injection

### 29.2 Indirect Prompt Injection

### 29.3 Tool Abuse

### 29.4 Data Leakage

### 29.5 Secret Leakage

### 29.6 Excessive Permission

### 29.7 Dangerous Tool Execution

---

## Chapter 30：Agent Permission Model

### 30.1 Read-only Tools

### 30.2 Write Tools

### 30.3 High-risk Tools

### 30.4 Allowlist

### 30.5 Denylist

### 30.6 Sandbox

### 30.7 Audit Log

---

# Part 14：Production Engineering

## Chapter 31：Agent Reliability

### 31.1 Retry

### 31.2 Timeout

### 31.3 Circuit Breaker

### 31.4 Fallback

### 31.5 Idempotency

### 31.6 Recovery

---

## Chapter 32：Agent Performance

### 32.1 Token Cost

### 32.2 Context Cost

### 32.3 Tool Latency

### 32.4 Model Latency

### 32.5 Parallel Execution

### 32.6 Caching

### 32.7 Model Routing

---

## Chapter 33：Agent Deployment

### 33.1 API Service

### 33.2 FastAPI

### 33.3 Session Management

### 33.4 Queue

### 33.5 Database

### 33.6 Redis

### 33.7 Container

### 33.8 CI/CD

### 33.9 Configuration

### 33.10 Secrets

---

# Part 15：概念辨析

## Chapter 34：常见概念对比

### Agent vs Chatbot

### Agent vs Workflow

### Workflow vs LangGraph

### Tool Calling vs Function Calling

### Tool Calling vs MCP

### MCP vs REST API

### MCP vs RAG

### RAG vs Memory

### Context vs Memory

### State vs Memory

### Skill vs Tool

### Skill vs MCP

### SubAgent vs Multi-Agent

### Claude Code vs Claude Agent SDK

### Agent SDK vs LangGraph

### LangChain vs LangGraph

### Trellis vs LangGraph

### OpenSpec vs Agent Workflow

### Superpowers vs Skills

---

# Part 16：贯穿项目——Forest Intelligence Agent

## Project V0：LLM Application

目标：

```text
User → Claude → Answer
```

学习：

- LLM API
- Prompt
- Context

---

## Project V1：Tool Agent

能力：

```text
Agent
 ↓
weather_tool
```

学习：

- Tool Calling
- Agent Loop

---

## Project V2：Multi-Tool Agent

能力：

- weather_tool
- water_tool
- vegetation_tool

学习：

- Tool Selection
- Error Handling
- Routing

---

## Project V3：MCP Agent

架构：

```text
Agent
 ↓
MCP
 ↓
Forest Monitoring System
```

学习：

- MCP Client
- MCP Server
- Tool Integration

---

## Project V4：Knowledge Agent

增加：

```text
RAG
```

知识：

- 监测规范
- 风险标准
- 历史报告

---

## Project V5：Stateful Agent

增加：

- Session
- State
- Memory

---

## Project V6：LangGraph Workflow

增加：

```text
Data Collection
 ↓
Quality Check
 ↓
Anomaly Detection
 ↓
Risk Analysis
 ↓
Report
```

---

## Project V7：Human-in-the-loop

增加：

- Approval
- Sensitive Action
- Resume

---

## Project V8：Multi-Agent

增加：

- Weather Agent
- Water Agent
- Vegetation Agent
- Risk Agent
- Report Agent

---

## Project V9：Production Agent

增加：

- Eval
- Tracing
- Observability
- Security
- Retry
- Timeout
- Cost
- Deployment

---

# Part 17：学习计划

## Level 1：Agent 核心基础

目标：

> 独立开发一个 Single Agent。

学习内容：

- LLM API
- Context
- Tool Calling
- Agent Loop
- Claude Agent SDK
- MCP
- State
- Memory
- RAG

---

## Level 2：Agent 架构设计

目标：

> 能设计复杂 Agent Workflow。

学习内容：

- LangGraph
- Workflow
- Human-in-the-loop
- Guardrails
- Multi-Agent
- Context Engineering

---

## Level 3：Agent 工程化

目标：

> 能将 Agent 做到 Production Ready。

学习内容：

- Eval
- Tracing
- Observability
- Security
- Reliability
- Cost
- Deployment

---

# Part 18：建议仓库结构

```text
agent-engineering-handbook/
│
├── README.md
│
├── 00-roadmap/
│   ├── learning-roadmap.md
│   └── technology-map.md
│
├── 01-overview/
│   ├── what-is-agent.md
│   └── agent-engineering-map.md
│
├── 02-foundations/
│   ├── llm-api.md
│   ├── prompt.md
│   └── context-engineering.md
│
├── 03-tool-agent/
│   ├── tool-calling.md
│   └── agent-loop.md
│
├── 04-claude-agent-sdk/
│   ├── sdk-basics.md
│   └── code-diagnostic-agent.md
│
├── 05-mcp/
│   ├── concepts.md
│   ├── first-server.md
│   └── forest-mcp-server.md
│
├── 06-state-memory/
│   ├── state.md
│   └── memory.md
│
├── 07-rag/
│   ├── rag-basics.md
│   └── agent-rag.md
│
├── 08-langgraph/
│   ├── concepts.md
│   └── forest-workflow.md
│
├── 09-hitl-guardrails/
│   ├── human-in-the-loop.md
│   └── guardrails.md
│
├── 10-multi-agent/
│   ├── patterns.md
│   └── forest-multi-agent.md
│
├── 11-evaluation/
│   ├── eval-basics.md
│   └── test-dataset.md
│
├── 12-observability/
│   ├── tracing.md
│   └── observability.md
│
├── 13-security/
│   ├── prompt-injection.md
│   └── permissions.md
│
├── 14-production/
│   ├── reliability.md
│   ├── performance.md
│   └── deployment.md
│
├── 15-concepts/
│   └── comparisons.md
│
├── projects/
│   └── forest-intelligence-agent/
│       ├── v0-llm/
│       ├── v1-tool-agent/
│       ├── v2-multi-tool/
│       ├── v3-mcp/
│       ├── v4-rag/
│       ├── v5-state-memory/
│       ├── v6-langgraph/
│       ├── v7-hitl/
│       ├── v8-multi-agent/
│       └── v9-production/
│
└── learning-log/
    ├── week01.md
    ├── week02.md
    └── ...
```

---

# Part 19：学习记录模板

## 日期

## 学习章节

## 今天解决的问题

## 我之前的理解

## 今天的新理解

## 最重要的三个知识点

1.
2.
3.

## 实现了什么

## 遇到的问题

## 还没有理解的内容

## 可以应用到当前工作的地方

## 下一步

---

# Part 20：阶段验收标准

## Level 1 验收

能够不依赖 LangChain / LangGraph，从零解释并实现：

```text
LLM
 ↓
Tool Calling
 ↓
Agent Loop
 ↓
Tool Result
 ↓
Final Answer
```

能够开发：

```text
Single Agent + MCP + RAG + Memory
```

---

## Level 2 验收

能够独立设计：

```text
State
Nodes
Edges
Conditional Routing
Human Approval
Multi-Agent
```

能够解释：

```text
什么时候使用 Agent
什么时候使用 Workflow
什么时候使用 Multi-Agent
```

---

## Level 3 验收

Agent 项目具备：

- 测试集
- Eval
- Tracing
- Logging
- Retry
- Timeout
- 权限模型
- HITL
- Security
- Cost Monitoring
- Deployment

最终目标：

> 能够独立完成一个具备真实业务价值、可测试、可观测、可控制、可上线的企业级 AI Agent 系统。

---

# 附录

## Appendix A：术语表

## Appendix B：Agent Architecture Patterns

## Appendix C：常用调试方法

## Appendix D：常见 Agent Failure Modes

## Appendix E：Agent 项目 Checklist

## Appendix F：推荐论文 / 官方文档 / 开源项目

## Appendix G：个人 Agent Engineering 技术地图
