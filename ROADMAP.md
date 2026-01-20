# Project Roadmap

This document outlines the planned evolution of the Personal Agent System.  
It serves as a strategic guide for future development, ensuring the project grows in a structured, intentional way.

---

## Vision

Build a personal AI agent that acts as an extension of Bryan’s thinking — capable of storing ideas, tracking goals, reasoning about inputs, generating opportunities, and supporting long-term financial and personal growth.

The system should remain:
- Modular
- Extensible
- Transparent
- Safe
- Locally runnable
- Easy to maintain and evolve

---

## Current Version: 1.0.0

The agent currently supports:
- Persistent JSON memory
- Idea CRUD
- Goal CRUD + completion
- Command routing
- LLM fallback for natural language
- Clean architecture under `src/`

This foundation enables the next major capabilities.

---

## Phase 1 — Intelligence Upgrade (Tool-Aware Agent)

### 1. Automatic Tool Selection
Enable the LLM to:
- Parse user intent
- Decide which tool to call
- Format arguments correctly
- Execute tools autonomously

This moves the agent from command-driven to intelligent behavior.

### 2. Multi-Step Reasoning
Add a planning layer so the agent can:
- Break tasks into steps
- Execute them sequentially
- Reflect and adjust

### 3. Reflection Loop
Allow the agent to:
- Review past actions
- Improve responses
- Learn preferences over time

---

## Phase 2 — Memory Upgrade (Semantic + Structured)

### 1. Vector Memory
Add embeddings to support:
- Semantic search
- Idea clustering
- Long-term recall

### 2. Memory Consolidation
Periodic summarization of:
- Ideas
- Goals
- Conversations
- Progress

### 3. Profile Expansion
Store:
- Preferences
- Skills
- Constraints
- Long-term objectives

---

## Phase 3 — External Capabilities

### 1. Web Search Integration
Allow the agent to:
- Research topics
- Validate information
- Pull real-time data

### 2. Calendar + Scheduling
Add tools for:
- Event creation
- Reminders
- Daily planning

### 3. Financial Analysis Tools
Support:
- Budgeting
- Cash flow modeling
- Opportunity evaluation
- Risk assessment

---

## Phase 4 — Opportunity Engine

### 1. Idea Ranking
Score ideas based on:
- Feasibility
- ROI
- Time cost
- Alignment with goals

### 2. Opportunity Generation
Use the LLM to:
- Propose new ideas
- Expand existing ones
- Identify patterns

### 3. Project Builder
Generate:
- Plans
- Milestones
- Requirements
- First steps

---

## Phase 5 — Autonomy & Workflow Automation

### 1. Task Queue
Allow the agent to:
- Queue tasks
- Execute them over time
- Track progress

### 2. Background Processes
Enable:
- Daily summaries
- Weekly reviews
- Goal progress checks

### 3. Agent Extensions
Support plugins for:
- Email parsing
- File analysis
- API integrations

---

## Long-Term Goals

- A fully autonomous personal operating system
- A trusted advisor for financial and personal growth
- A system that compounds value over years
- A durable asset for Bryan’s family and legacy

---

## Notes

This roadmap is iterative.  
As the agent evolves, new opportunities will emerge and priorities may shift.  
Each phase builds on the last, ensuring stability and clarity throughout development.