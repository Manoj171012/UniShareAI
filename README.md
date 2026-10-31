# UniShare AI

**Institutional Makerspace & Lab Equipment Platform**  
**Track:** Agentic AI  
**Team:** Manoj Marella · Rishi

> **Share equipment. Expand opportunity.** UniShare AI is an AI-assisted platform concept for helping universities and makerspaces share high-value equipment through structured booking, transparent allocation policies, condition records, and human-supervised decisions.

---

## Overview

Universities and makerspaces often own expensive, specialized equipment—such as 3D printers, oscilloscopes, cinema cameras, and laboratory instruments—that can be difficult for students and researchers to access. Owners may hesitate to share these assets because of qualification, misuse, damage, and accountability concerns. Informal booking can also allow frequent users to dominate limited slots.

**UniShare AI brings the equipment-sharing lifecycle into one governed workflow.** Users can discover equipment and submit requests. AI assists with requirement review, fairness insights, and incident summaries. The backend enforces configured policies, while human equipment managers retain final authority over access and incident decisions.

### Design principle

**AI assists. Backend rules enforce. Human managers authorize.**

---

## Core Features

### 1. AI Eligibility Reviewer
Reviews booking requests against equipment requirements using Google Gemini API, producing risk scores and safety recommendations.

### 2. AI Anti-Monopoly Agent
Supports fair access by identifying repeated booking concentration and enforcing weekly equipment allocation limits.

### 3. Condition and Transaction Records
Connects booking decisions with check-in, return details, and audit history.

---

## Architecture

```text
Frontend (HTML / Tailwind CSS) -> FastAPI Backend -> SQLite DB & Google Gemini API