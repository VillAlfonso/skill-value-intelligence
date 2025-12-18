# Skill Value Intelligence System

## Overview

People invest significant time learning technical skills with limited visibility
into their **economic value** or how that value changes over time.
Common advice such as *“just trust the process”* often ignores a real risk:
**skills can depreciate faster than individuals can reskill**.

This project builds a **data-driven decision support system** that estimates the
**relative economic value of technical skills** using publicly observable market signals.

The goal is not to predict the future with certainty, but to **reduce uncertainty**
around skill investment decisions.

---

## Problem Statement

Choosing which skills to learn has become increasingly risky due to:
- rapid technological change
- shifting labor market demand
- misalignment between hype and compensation
- lack of transparent, quantitative guidance

This system treats skills as **economic assets** whose value can be approximated
using market-derived signals rather than intuition or trend-following.

---

## What This Project Does

This repository implements a modular data science pipeline that:

1. **Ingests job market data**  
   Structured job postings containing role descriptions and salary ranges.

2. **Extracts technical skills**  
   Skills are identified from job descriptions using explainable text matching
   as a baseline approach.

3. **Computes market signals**
   - **Demand Signal**: frequency of skill mentions in job postings
   - **Compensation Signal**: average salary midpoint associated with roles
     mentioning the skill

4. **Builds a Skill Value Index (SVI)**  
   A normalized composite score combining demand and compensation to estimate
   the **relative economic attractiveness** of skills.

The output is a ranked list of skills based on current observable market signals.

---

## Skill Value Index (SVI)

The Skill Value Index combines two normalized components:

- **Demand** (posting frequency)
- **Compensation** (salary midpoint)

Each signal is normalized using min–max scaling and combined with equal weighting:

SVI = 0.5 × Demand_norm + 0.5 × Compensation_norm



This design prioritizes:
- interpretability
- transparency
- defensible assumptions
- ease of adjustment as the system evolves

---

## How to Interpret Results

- The Skill Value Index is **relative**, not absolute
- Rankings compare skills *within the dataset*, not across all markets
- High SVI skills are both **widely requested and better compensated**
- Low SVI skills may be:
  - common but low-paying
  - niche and high-paying
  - emerging but underrepresented

This system supports **decision-making**, not guarantees.

---

## Limitations and Assumptions

This project explicitly acknowledges its constraints:

- Small, manually seeded dataset (early-stage validation)
- Job postings reflect employer intent, not confirmed hires
- Salary ranges may be noisy or inflated
- Skill mentions may correlate with seniority or role type
- Correlation does not imply causation

These limitations are documented intentionally and guide future improvements.

---

## Project Structure


<img width="325" height="213" alt="image" src="https://github.com/user-attachments/assets/961eae6f-83fc-4420-aa6f-f18db7706de3" />



---

## Intended Use

This project is intended for:
- individuals evaluating skill investment decisions
- analysts studying labor market dynamics
- educators and curriculum designers
- exploratory research into human capital economics

It is not intended for automated hiring, individual evaluation,
or deterministic career prediction.

---

## Status

This is an **active, iterative research project**.
Accuracy is treated as a process rather than a claim,
with emphasis on transparency and signal validity.
