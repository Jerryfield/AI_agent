# Agent Engineering Learning Roadmap

> 学习目标：
>
> 从具有传统前后端开发经验的软件工程学习者，
> 逐步成长为能够独立设计、实现、评估和部署 Agent System 的 Agent Engineer。

---

# Learning Principle

整个学习过程遵循：

Learn
↓
Understand
↓
Implement
↓
Experiment
↓
Fail
↓
Debug
↓
Document
↓
Project

学习比例：

- 30% 理论与官方文档
- 50% Coding / Lab / Project
- 20% 笔记与复盘

核心原则：

> 不以掌握多少框架衡量进度，
> 而以是否能够脱离框架解释并实现核心机制衡量学习效果。

---

# Phase 0：学习环境初始化

目标：

建立长期 Agent Engineering 学习环境。

完成：

- [x] 创建 AgentEngineering Git Repository
- [x] 创建 docs/
- [x] 创建 labs/
- [x] 创建 projects/
- [x] 创建 experiments/
- [x] 创建 failures/
- [x] 创建 knowledge-map.md
- [x] 创建 learning-roadmap.md
- [x] 创建 progress.md
- [x] 创建笔记模板
- [x] 配置 .gitignore
- [x] 创建远程 Git Repository
- [x] 完成第一次 Commit

完成标准：

可以通过 Git 管理：

知识
+
代码
+
实验
+
项目
+
踩坑记录

---

# Phase 1：LLM Application Engineering

目标：

首先学会构建普通 LLM Application。

## Knowledge

学习：

- [ ] LLM 是什么
- [ ] Token
- [ ] Context Window
- [ ] Prompt
- [ ] System Instructions
- [ ] LLM API
- [ ] Streaming
- [ ] Structured Output
- [ ] JSON Schema
- [ ] Model Selection
- [ ] Token Cost
- [ ] Latency
- [ ] Error Handling

## Labs

完成：

### Lab 01

LLM API Hello World

### Lab 02

System Prompt

### Lab 03

Structured Output

### Lab 04

Streaming

### Lab 05

Error / Retry

## Mini Project

Document Analyzer

输入：

Document

输出：

Structured Result

例如：

{
  "summary": "",
  "keywords": [],
  "risks": []
}

## Completion Criteria

能够解释：

- LLM API 的基本调用流程
- Context 是什么
- Structured Output 为什么重要
- Token / Cost / Latency 的关系

能够不依赖 Agent Framework 完成一个 LLM Application。

---

# Phase 2：Agent Core

目标：

真正理解 Agent 为什么能够“行动”。

## Knowledge

学习：

- [ ] AI Agent 是什么
- [ ] Chatbot vs Workflow vs Agent
- [ ] Agent Core Components
- [ ] Agent Loop
- [ ] State
- [ ] Stop Condition
- [ ] Planning
- [ ] Reflection 基础认识

## Key Question

必须回答：

- Agent 和普通 Chatbot 有什么区别？
- Agent 为什么需要 Loop？
- Agent 怎么知道下一步做什么？
- Agent 怎么知道什么时候结束？

## Lab

手写 Minimal Agent Loop。

禁止：

第一版直接使用 LangChain / LangGraph。

目标流程：

User
↓
LLM
↓
Decision
↓
Tool
↓
Tool Result
↓
LLM
↓
Finish

## Mini Project

CLI Agent

能力：

- 接收用户目标
- 自主选择 Tool
- 执行 Tool
- 根据结果继续执行
- 最终返回 Answer

## Completion Criteria

能够自己实现一个 Agent Loop。

---

# Phase 3：Tool Engineering

目标：

掌握 Agent 与真实世界交互的核心能力。

## Knowledge

- [ ] Function Calling
- [ ] Tool Calling
- [ ] Tool Schema
- [ ] Tool Description
- [ ] Tool Arguments
- [ ] Tool Result
- [ ] Tool Error
- [ ] Timeout
- [ ] Retry
- [ ] Tool Permission
- [ ] Human Approval
- [ ] Tool Selection

## Labs

实现 Tool：

### weather

了解 Tool Call 基本流程。

### calculator

理解参数 Schema。

### file_reader

理解外部数据访问。

### search_code

理解复杂 Tool。

## Experiments

修改：

Tool Name
Tool Description
Tool Schema

观察：

Tool Selection Accuracy

## Mini Project

Research Agent

Tools：

- Search
- Read
- Calculate
- Save Result

## Completion Criteria

能够设计一个“适合模型使用”的 Tool，而不仅仅是 Python Function。

---

# Phase 4：Context Engineering

目标：

理解 Agent 的能力很大程度取决于：

模型在当前这一刻看到了什么。

## Knowledge

- [ ] Context Window
- [ ] Context Budget
- [ ] Context Selection
- [ ] Context Pollution
- [ ] Context Compression
- [ ] Context Summarization
- [ ] Tool Result Context

## Labs

实验：

同一个任务：

Context A
vs
Context B

比较输出。

## Completion Criteria

能够解释：

Prompt Engineering

和

Context Engineering

的区别。

---

# Phase 5：RAG

目标：

让 Agent 使用外部知识。

## Knowledge

- [ ] RAG
- [ ] Document Parsing
- [ ] Chunking
- [ ] Embedding
- [ ] Vector
- [ ] Similarity Search
- [ ] Vector Database
- [ ] Metadata
- [ ] Top-K
- [ ] Hybrid Search
- [ ] Rerank
- [ ] RAG Evaluation

## Labs

### Lab

Embedding Demo

### Lab

Vector Search

### Lab

Basic RAG

### Lab

Chunk Size Experiment

### Lab

Top-K Experiment

## Project

Personal Knowledge Base Assistant

Data：

当前 AgentEngineering/docs

实现：

docs/
↓
Parsing
↓
Chunking
↓
Embedding
↓
Vector Store
↓
Retrieval
↓
LLM

## Completion Criteria

能够解释：

为什么一个 RAG 系统回答错误。

而不是简单归因：

“模型不行”。

---

# Phase 6：Memory

目标：

理解长期 Agent 的记忆机制。

## Knowledge

- [ ] Short-term Memory
- [ ] Long-term Memory
- [ ] Session Memory
- [ ] Semantic Memory
- [ ] Memory Extraction
- [ ] Memory Retrieval
- [ ] Memory Update
- [ ] Memory Forgetting

## Key Question

能够区分：

Context
vs
State
vs
Memory
vs
RAG

## Lab

Personal Preference Agent

记录：

用户偏好

并在后续 Session 中使用。

---

# Phase 7：MCP

目标：

理解现代 Agent Tool Integration。

## Knowledge

- [ ] MCP 是什么
- [ ] MCP Host
- [ ] MCP Client
- [ ] MCP Server
- [ ] Tools
- [ ] Resources
- [ ] Prompts
- [ ] Transport
- [ ] MCP Security

## Key Question

必须回答：

- MCP 和 Function Calling 有什么区别？
- MCP 和 Tool Calling 是什么关系？
- MCP Server 是谁运行的？
- Agent 怎么发现 MCP Tools？

## Lab

实现：

Minimal MCP Server

提供：

- hello
- calculator

## Advanced Lab

Repository MCP Server

Tools：

- list_files
- read_file
- search_code
- git_log
- git_diff

## Project

Codebase Analysis Agent

Agent
↓
MCP Client
↓
Repository MCP Server
↓
Git Repository

## Completion Criteria

能够独立开发和调试 MCP Server。

---

# Phase 8：Agent Orchestration

目标：

从简单 Loop 进入复杂 Agent System。

## Knowledge

- [ ] Workflow
- [ ] State Machine
- [ ] Node
- [ ] Edge
- [ ] Conditional Edge
- [ ] Routing
- [ ] Checkpoint
- [ ] Persistence
- [ ] Interrupt
- [ ] Human-in-the-loop

## Framework

开始正式学习：

LangGraph

注意：

这里才开始系统学习 Agent Framework。

## Labs

### Workflow

A → B → C

### Conditional Workflow

A
↓
Condition
↙     ↘
B      C

### Loop

Analyze
↓
Execute
↓
Evaluate
↓
Retry

### Human Approval

Agent
↓
Plan
↓
Human Approval
↓
Execute

## Project

Development Workflow Agent

Requirement
↓
Analyze
↓
Plan
↓
Human Approval
↓
Execute
↓
Test
↓
Review

## Completion Criteria

能够设计一个 Stateful Agent Workflow。

---

# Phase 9：Multi-Agent

目标：

理解什么时候应该使用多个 Agent。

## Knowledge

- [ ] Supervisor
- [ ] Worker
- [ ] Routing
- [ ] Handoff
- [ ] Agent as Tool
- [ ] Shared Context
- [ ] Multi-Agent Failure

## Important

不要形成：

一个角色
=
一个 Agent

的错误设计习惯。

## Project

Software Engineering Team Agent

Supervisor
├── Requirement Agent
├── Coding Agent
├── Test Agent
└── Review Agent

重点：

分析 Multi-Agent 是否真的优于单 Agent。

---

# Phase 10：Evaluation

目标：

从 Agent Demo 进入 Agent Engineering。

## Knowledge

- [ ] Dataset
- [ ] Test Case
- [ ] Grader
- [ ] LLM-as-Judge
- [ ] Task Success Rate
- [ ] Tool Accuracy
- [ ] RAG Evaluation
- [ ] Regression Test

## Project

为前面的 Agent 创建：

50~100 个 Test Cases。

记录：

- Success Rate
- Tool Call Accuracy
- Latency
- Cost
- Failure Reason

## Completion Criteria

任何 Prompt / Model / Workflow 修改：

都能够通过 Eval 判断：

到底变好了还是变差了。

---

# Phase 11：Tracing & Observability

目标：

能够 Debug Agent。

## Knowledge

- [ ] Trace
- [ ] Span
- [ ] Logging
- [ ] Token Usage
- [ ] Tool Trace
- [ ] Error Trace
- [ ] Agent Handoff Trace

## Debug 思路

User
↓
Context
↓
Model
↓
Tool Selection
↓
Tool Result
↓
State
↓
Final Answer

逐层分析。

## Completion Criteria

Agent 出错时：

能够定位：

Prompt 问题
Context 问题
Tool 问题
Model 问题
Workflow 问题

而不是：

不断修改 Prompt 碰运气。

---

# Phase 12：Security

目标：

理解 Agent 比普通 LLM App 更大的安全风险。

## Knowledge

- [ ] Prompt Injection
- [ ] Indirect Prompt Injection
- [ ] Tool Permission
- [ ] Least Privilege
- [ ] Secret Management
- [ ] Human Approval
- [ ] Sandbox
- [ ] Data Leakage

## Lab

设计：

Read Tool

和

Write Tool

不同权限模型。

---

# Phase 13：Production Agent Engineering

目标：

让 Agent 真正成为软件系统。

## Knowledge

- [ ] FastAPI
- [ ] Async
- [ ] PostgreSQL
- [ ] Redis
- [ ] Queue
- [ ] Docker
- [ ] CI/CD
- [ ] Auth
- [ ] Rate Limit
- [ ] Retry
- [ ] Timeout
- [ ] Cache
- [ ] Cost Control
- [ ] Model Routing

## Project

Production Agent API

Frontend
↓
Backend API
↓
Agent Runtime
├── LLM
├── Tools
├── RAG
├── Memory
└── Workflow
↓
Database / Redis / Vector DB

---

# Phase 14：Capstone Project

最终作品：

AI Software Engineering Agent

## Architecture

User Requirement
↓
Requirement Analysis
↓
Repository Analysis
↓
Plan Generation
↓
Human Approval
↓
Code Modification
↓
Test
↓
Error Analysis
↓
Retry
↓
Code Review
↓
Final Report

## Required Capabilities

项目至少包含：

- LLM
- Tool Calling
- Agent Loop
- MCP
- RAG / Repository Context
- State
- Memory
- Human-in-the-loop
- Tracing
- Evals
- Security
- API
- Database
- Docker

---

# Phase 15：Interview & Job Preparation

整理：

## Concepts

Agent / RAG / MCP / Tool / Memory / State

## Engineering

Agent Debug
Agent Eval
Agent Security
Agent Architecture

## Projects

准备：

- Architecture Diagram
- README
- Demo
- Technical Decisions
- Problems Encountered
- Evaluation Result

目标：

面试时不仅描述：

“我用了 LangGraph。”

而是能够解释：

为什么需要它。

它解决什么问题。

不用它应该如何实现。

---

# Final Goal

最终达到：

I can build an Agent.

↓

I understand why it works.

↓

I can debug it.

↓

I can evaluate it.

↓

I can make it reliable.

↓

I can deploy it.

↓

Agent Engineer