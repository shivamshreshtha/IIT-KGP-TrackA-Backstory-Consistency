# 📘 Backstory–Narrative Consistency Verification System  
### Track A: Systems Reasoning with NLP & Generative AI

> **Goal:** Verify whether a hypothetical backstory for a character is consistent with the full narrative of a long-form novel (100k+ words).

---

## 🚀 What Problem Are We Solving?

Given:
- A **full-length novel** (100k+ words)
- A **hypothetical backstory** for a central character  

We determine whether the backstory:
- Remains **consistent over time**
- Preserves **causal coherence**
- Respects **narrative constraints**
- Is supported by **evidence across the text**

This goes beyond simple contradiction checks and focuses on **deep narrative reasoning**.

---

## 🧠 Core Idea

We frame the task as **hypothesis verification**:

- **Novel** → Ground Truth  
- **Backstory** → Hypothesis  

The system retrieves relevant evidence from the novel and evaluates each backstory claim before producing a **binary verdict**.

---

## 🗺️ System Architecture

```mermaid
flowchart LR

    subgraph Novel["📚 Novel Processing"]
        A["Full Novel (100k+ words)"] --> B["Chunking"]
        B --> C["Text Chunks"]
        C --> D["Pathway Semantic Index"]
    end

    subgraph Backstory["🧬 Backstory Processing"]
        E["Hypothetical Backstory"] --> F["Claim Decomposition"]
        F --> H["Atomic Claims (core / non-core)"]
    end

    subgraph Reasoning["🤖 Reasoning"]
        D -->|Semantic Retrieval| G["Relevant Narrative Chunks"]
        H --> I["LLM Claim Evaluation"]
        G --> I
        I --> J["Claim Scores"]
    end

    subgraph Output["🧮 Aggregation & Output"]
        J --> K["Deterministic Aggregation"]
        K --> L["Final Decision"]
        L --> M["results.csv"]
    end
