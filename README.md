# AI-Driven Identity Risk Scoring

## Problem
Static access control systems fail to adapt to changing user behavior, causing security risks.

## Solution
This project uses AI to dynamically evaluate identity risk and apply adaptive access control.

## Features
- Anomaly detection using Isolation Forest
- Risk scoring (0–100)
- Adaptive decisions (ALLOW / MFA / BLOCK)
- Explainable AI (reason for decisions)
- Privacy-preserving hashing

## How to Run
pip install -r requirements.txt  
python Python.py

## Output
- High-risk users detection
- Risk summary distribution
- Explainable access decisions

## Impact
- Reduces insider threats  
- Improves compliance  
- Minimizes false access denial  