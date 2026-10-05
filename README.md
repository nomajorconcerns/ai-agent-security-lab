# AI Agent Security Lab

A hands-on cybersecurity project exploring how AI agents can securely use tools, access data, and enforce permissions.

## Overview

This object is a controlled environment for learning and demonstrating AI agent security concepts. The agent can interact with simulated resources while enforcing access controls based on tokens and permissions. 

A small Python project that explores how to secure AI agents, built step by step as a learning portfolio.

## What it demonstrates

- **Authorization:** each agent has its own list of allowed tools, and unknown agents get nothing (least privilege)
- **Audit logging:** every ALLOWED, BLOCKED, and ALERT decision is recorded with a timestamp
- **Attack detection:** a scanner normalizes text (spacing, punctuation, look-alike characters like 1gn0re) and quarantines prompt injection phrases
- **Authentication:** agents must present a valid token before any permission check runs
- **Tests:** automated checks (pytest) prove the security rules work

## Run it

    python agent.py
    python -m pytest

## Limitations

- The scanner only matches known phrases. It will not catch paraphrases, synonyms, other languages, or instructions hidden inside long documents.
- Tokens are hard-coded demo values. Real systems keep secrets outside the code.
- Real defenses are layered: permissions, logging, and human review matter as much as input filtering.

## Roadmap

- Load tokens from environment variables instead of code
- Detect suspicious tool-use patterns, not just suspicious text
