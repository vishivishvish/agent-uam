# 🚀 Agent-UAM

## Proof of Concept for Agentic Workflow Automation

Welcome to Agent-UAM 🎯

This project is a Proof of Concept that demonstrates how traditional enterprise workflows can be reimagined using Agentic AI.

Instead of rigid RPA scripts and static rule engines, this system uses a structured state machine, tool abstraction, and agent orchestration to automate complex User Access Management workflows.

The goal is simple:

Prove that any structured workflow can be automated in the age of Agentic AI.

## 🔥 What This POC Demonstrates

This system simulates a real enterprise scenario:

- 📥 Pulling ServiceNow request data
- 🔎 Extracting and normalizing request details
- 👤 Resolving approvers via mapping logic
- 🧠 Executing deterministic workflow steps
- ⚙️ Provisioning logic via modular tools
- 📤 Returning structured results through an API

All driven through a configurable state machine.

- No hardcoded flow logic.
- No brittle RPA click automation.
- No static scripts that break when requirements evolve.

## 🧠 Architecture Overview

This system is built with clean separation of concerns:

FastAPI as the API boundary

LangGraph for strict state machine orchestration

Tool abstraction layer for workflow operations

Config driven workflow definitions

Local Git version control for deterministic evolution

The orchestration layer is modular, meaning it can be swapped if enterprise requirements demand a different agent framework.

The design principle:

- Keep orchestration flexible
- Keep tools deterministic
- Keep state explicit

## ⚙️ Why This Matters

Traditional RPA bots:

- Break when UI changes
- Handle only happy paths
- Struggle with dynamic decision logic
- Require heavy rework for change requests

Agentic systems on the other hand:

- Operate on structured state
- Use tool calls instead of screen scraping
- Adapt to new logic via configuration
- Scale across workflows

This POC is a first step toward building a reusable Agentic workflow engine capable of handling:

- Account creation
- Modification
- Reactivation
- Deactivation
- Multi-step approval flows
- Conditional branching
- Human-in-the-loop decisions

## 🧩 Current Scope

This repository currently implements:

Structured request ingestion

Deterministic graph execution

Configurable workflow steps

Git based iterative development

Future evolution includes:

LLM powered decision nodes

Dynamic tool selection

Conditional graph branching

Enterprise API integrations

Multi-workflow support

## 🛠 Tech Stack

Python 🐍

FastAPI ⚡

LangGraph 🔗

Git version control 🧭

Config driven orchestration 📄

## 🎯 Vision

The long term vision is to build a flexible Agentic system where:

Adding a new workflow requires only config changes

New modules can be integrated without rewriting orchestration

Enterprise automation becomes adaptive instead of brittle

This is not just automation.

This is workflow intelligence.

## 👨‍💻 About

Built as a hands-on exploration into enterprise grade Agentic systems and state driven AI orchestration.

If you are exploring next generation automation systems, feel free to fork, experiment, and push the boundaries 🚀
