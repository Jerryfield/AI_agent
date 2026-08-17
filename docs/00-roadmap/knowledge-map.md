Agent Engineering
│
├── LLM
├── Agent
├── Tool
├── Context
├── RAG
├── MCP
├── Memory
├── Workflow
├── Multi-Agent
├── Evals
├── Security
└── Production

# Agent Engineering Knowledge Map

> 本文档用于维护个人 Agent Engineering 知识地图。
>
> 它回答的问题不是“现在学什么”，而是：
>
> **成为一名 Agent Engineer，需要建立怎样的完整知识体系？**

---

# 1. Agent Engineering 总览

## 1.1 AI Application 演进

- Traditional Application
- AI Application
- LLM Application
- AI Workflow
- AI Agent
- Agentic System

## 1.2 Agent 基本概念

- Agent 是什么
- Agent 与 Chatbot 的区别
- Agent 与 Workflow 的区别
- Agent 与传统自动化程序的区别
- Single Agent
- Multi-Agent
- Agentic Workflow

## 1.3 Agent 核心组成

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

# 2. LLM Foundations

## 2.1 LLM 基础概念

- Token
- Tokenization
- Context Window
- Prompt
- System Instructions
- User Message
- Assistant Message
- Temperature
- Sampling
- Reasoning Model
- Multimodal Model

## 2.2 LLM API

- Request / Response
- Streaming
- Async
- Error Handling
- Rate Limit
- Timeout
- Retry
- Cost
- Latency

## 2.3 Structured Output

- JSON Output
- JSON Schema
- Schema Validation
- Pydantic
- Structured Response

## 2.4 Prompt Engineering

- System Prompt
- Few-shot Prompt
- Role Prompt
- Chain-of-Thought 的基本认识
- Prompt Template
- Prompt Versioning

## 2.5 Model Selection

- Model Capability
- Context Length
- Reasoning Ability
- Latency
- Cost
- Model Routing

---

# 3. Agent Core

## 3.1 Agent Loop

理解基本循环：

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
Continue / Finish

需要掌握：

- Agent Loop 为什么存在
- Loop 如何驱动
- Tool Result 如何重新进入 Context
- Loop 如何终止
- 无限循环问题

## 3.2 Agent State

- Stateless
- Stateful
- Conversation State
- Runtime State
- Workflow State
- Persistent State

## 3.3 Stop Condition

- Final Answer
- Maximum Turns
- Timeout
- Tool Result Condition
- Explicit Termination

## 3.4 Planning

- Task Decomposition
- Plan-and-Execute
- Dynamic Planning
- Replanning

## 3.5 Reflection

- Self Review
- Critique
- Retry
- Reflection Loop

---

# 4. Tool Engineering

## 4.1 Tool Calling

- Function Calling
- Tool Calling
- Tool Schema
- Tool Description
- Tool Arguments
- Tool Result

## 4.2 Tool Execution

需要理解：

模型并不真正执行 Tool。

典型流程：

LLM
↓
生成 Tool Call
↓
Application
↓
执行 Function / API
↓
Tool Result
↓
返回 LLM

## 4.3 Tool Design

- Tool Granularity
- Tool Naming
- Tool Description
- Parameter Design
- Return Structure

## 4.4 Tool Reliability

- Timeout
- Retry
- Exception Handling
- Validation
- Idempotency
- Fallback

## 4.5 Tool Security

- Permission
- Read / Write Separation
- Dangerous Operation
- Human Approval
- Sandbox

## 4.6 Tool Selection

- Tool Routing
- Tool Discovery
- Tool Confusion
- Tool Priority
- Tool Composition

---

# 5. Context Engineering

## 5.1 Context 基础

- Context 是什么
- Context Window
- Context Budget
- Relevant Context
- Context Pollution

## 5.2 Context 来源

- User Input
- System Instructions
- Conversation
- Tool Result
- Retrieved Documents
- Memory
- Runtime State

## 5.3 Context Management

- Context Selection
- Context Filtering
- Context Compression
- Context Summarization
- Context Prioritization

## 5.4 Context Engineering

需要理解：

Prompt Engineering
↓
如何写好指令

Context Engineering
↓
在正确时间给模型正确的信息

---

# 6. RAG

## 6.1 RAG 基础

- RAG 是什么
- 为什么需要 RAG
- RAG 与 Agent 的关系

## 6.2 Document Processing

- Document Loader
- Parsing
- Cleaning
- Chunking
- Metadata

## 6.3 Embedding

- Embedding
- Vector
- Similarity
- Cosine Similarity

## 6.4 Vector Database

- Vector Store
- Index
- Insert
- Search
- Metadata Filter

## 6.5 Retrieval

- Semantic Search
- Keyword Search
- Hybrid Search
- Top-K
- Query Rewrite
- Rerank

## 6.6 Advanced RAG

- Multi Query
- Parent-Child Retrieval
- Contextual Retrieval
- Agentic RAG
- Graph RAG 基础认识

## 6.7 RAG Evaluation

- Retrieval Accuracy
- Recall
- Precision
- Context Relevance
- Answer Faithfulness

---

# 7. Memory

## 7.1 Memory 基础

- Memory 是什么
- Memory 与 Context 的区别
- Memory 与 RAG 的区别
- Memory 与 State 的区别

## 7.2 Short-term Memory

- Conversation History
- Session Memory
- Working Memory

## 7.3 Long-term Memory

- User Preference
- Historical Facts
- Experience
- Semantic Memory

## 7.4 Memory Pipeline

- Memory Extraction
- Memory Storage
- Memory Retrieval
- Memory Update
- Memory Forgetting

---

# 8. MCP

## 8.1 MCP 基础

- MCP 是什么
- MCP 为什么出现
- MCP 与 Tool Calling 的关系
- MCP 与 Function Calling 的区别

## 8.2 MCP Architecture

- MCP Host
- MCP Client
- MCP Server

## 8.3 MCP Server Capabilities

- Tools
- Resources
- Prompts

## 8.4 MCP Transport

- Local Transport
- Remote Transport
- Connection Lifecycle

## 8.5 MCP Server Development

- Tool Registration
- Resource Exposure
- Error Handling
- Logging
- Authentication

## 8.6 MCP Client

- Server Discovery
- Tool Discovery
- Tool Invocation
- Resource Access

## 8.7 MCP Security

- Trust Boundary
- Permission
- Authentication
- Prompt Injection
- Tool Injection
- Sensitive Data

---

# 9. Agent Orchestration

## 9.1 Workflow

- Sequential Workflow
- Parallel Workflow
- Conditional Workflow
- Loop Workflow

## 9.2 State Machine

- State
- Node
- Edge
- Conditional Edge
- Transition

## 9.3 Routing

- Intent Routing
- Model Routing
- Tool Routing
- Agent Routing

## 9.4 Persistence

- Checkpoint
- Resume
- Recovery
- Durable Execution

## 9.5 Human-in-the-loop

- Approval
- Review
- Edit
- Interrupt
- Resume

## 9.6 Multi-Agent

- Supervisor
- Worker
- Router
- Handoff
- Agent as Tool

## 9.7 Multi-Agent 问题

- Coordination Cost
- Context Sharing
- Infinite Delegation
- Responsibility Boundary
- Debugging Difficulty

---

# 10. Agent Evaluation

## 10.1 为什么需要 Evals

不能仅通过：

“我测试了几个问题，感觉还不错”

判断 Agent 质量。

## 10.2 Eval Dataset

- Test Case
- Golden Dataset
- Regression Dataset

## 10.3 Agent Metrics

- Task Success Rate
- Tool Selection Accuracy
- Tool Argument Accuracy
- Retrieval Accuracy
- Hallucination Rate
- Latency
- Cost

## 10.4 Grader

- Rule-based Grader
- LLM-as-Judge
- Human Evaluation

## 10.5 Regression Testing

Agent 修改：

Prompt
Model
Tool
Workflow

之后重新执行 Eval。

---

# 11. Observability

## 11.1 Trace

记录：

- User Input
- Model Call
- Tool Call
- Tool Result
- Agent Handoff
- Error
- Final Output

## 11.2 Logging

- Application Log
- Agent Log
- Tool Log
- Error Log

## 11.3 Metrics

- Token Usage
- Latency
- Cost
- Error Rate
- Tool Calls
- Success Rate

## 11.4 Debugging

- Prompt Debugging
- Context Debugging
- Tool Debugging
- Workflow Debugging

---

# 12. Agent Security

## 12.1 Prompt Injection

- Direct Prompt Injection
- Indirect Prompt Injection

## 12.2 Tool Security

- Tool Permission
- Least Privilege
- Dangerous Tool
- Human Approval

## 12.3 Data Security

- Sensitive Data
- Secret Management
- Data Leakage

## 12.4 Sandbox

- File System Isolation
- Code Execution Isolation
- Network Isolation

## 12.5 Agent Authorization

- User Permission
- Agent Permission
- Tool Permission
- Resource Permission

---

# 13. Production Engineering

## 13.1 Backend

- Python
- FastAPI
- AsyncIO
- REST API
- WebSocket / Streaming

## 13.2 Storage

- PostgreSQL
- Redis
- Vector Database
- Object Storage

## 13.3 Infrastructure

- Docker
- Linux
- CI/CD
- Cloud Deployment

## 13.4 Reliability

- Retry
- Timeout
- Circuit Breaker
- Rate Limit
- Queue
- Idempotency

## 13.5 Performance

- Token Optimization
- Context Optimization
- Caching
- Parallel Tool Calls
- Model Routing

## 13.6 Cost

- Token Cost
- Model Cost
- Retrieval Cost
- Tool Cost
- Infrastructure Cost

---

# 14. Agent Frameworks

原则：

先理解原理，再学习框架。

## 14.1 OpenAI Agents SDK

关注：

- Agent
- Runner
- Tool
- Handoff
- Guardrail
- Tracing

## 14.2 LangGraph

关注：

- State
- Node
- Edge
- Conditional Edge
- Checkpoint
- Interrupt
- Persistence

## 14.3 其他框架

只做横向了解：

- LangChain
- AutoGen
- CrewAI
- PydanticAI
- Semantic Kernel

核心目标不是掌握所有框架。

而是：

理解框架解决了 Agent Engineering 中的什么问题。

---

# 15. Agent Design Patterns

需要逐渐掌握：

- Tool-Using Agent
- Router Pattern
- Sequential Workflow
- Parallel Workflow
- Evaluator-Optimizer
- Planner-Executor
- Supervisor-Worker
- Agent-as-Tool
- Human Approval
- Retry / Reflection
- RAG Agent
- Coding Agent

---

# 16. AI Coding Agent

重点研究对象：

- Code Search
- Repository Context
- Planning
- File Editing
- Test Execution
- Error Analysis
- Code Review
- Git Integration
- Sandbox
- MCP
- Long-running Task

可以结合：

- Claude Code
- Codex
- OpenSpec
- Superpowers

观察真实 Coding Agent 如何工作。

---

# 17. Software Engineering Foundations

已有基础持续加强：

- Git
- Linux
- HTTP
- REST API
- Database
- Redis
- Message Queue
- Docker
- Testing
- Design Pattern
- Clean Architecture
- Distributed System

Agent Engineering 本质仍然是 Software Engineering。

---

# 18. Papers & Research

逐步阅读：

- Transformer
- ReAct
- RAG
- Toolformer
- Reflexion
- Agent Benchmarks
- Memory
- Multi-Agent

原则：

工程实践优先。

Paper 用于解释：

为什么某些 Agent Pattern 有效。

---

# 19. Interview Knowledge

最终应该能够回答：

## Agent

- 什么是 AI Agent？
- Workflow 和 Agent 有什么区别？
- Agent Loop 是什么？
- Agent 如何停止？

## Tool

- Function Calling 是什么？
- Tool Calling 是怎么工作的？
- 模型真的调用了 API 吗？

## RAG

- RAG Pipeline 是什么？
- Chunk 如何设计？
- RAG 和 Memory 有什么区别？

## MCP

- MCP 是什么？
- MCP 和 Function Calling 有什么区别？
- MCP Server 是什么？

## Agent Engineering

- 如何防止 Agent 无限循环？
- 如何评估 Agent？
- 如何 Debug Agent？
- 如何设计 Tool？
- 如何降低 Agent 成本？
- 如何保证 Agent 安全？

---

# 20. 最终能力模型

目标：

Agent Engineer
│
├── Software Engineering
│
├── LLM Engineering
│
├── Context Engineering
│
├── Tool Engineering
│
├── Agent Orchestration
│
├── RAG / Memory
│
├── MCP
│
├── Evaluation
│
├── Observability
│
├── Security
│
└── Production Engineering

最终要求：

不仅能够：

“调用一个 Agent Framework”

而是能够：

设计、实现、调试、评估和部署一个可靠的 Agent System。