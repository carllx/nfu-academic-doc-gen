# How To: Full Matches

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test full matches

## Prerequisites

**Required Modules:**
- `unittest`
- `numpy`
- `nltk.data`
- `nltk.translate.bleu_score`


## Step-by-Step Guide

### Step 1: Assign references = value

```python
references = ['John loves Mary'.split()]
```

**Verification:**
```python
assert sentence_bleu(references, hypothesis, weights) == 1.0
```

### Step 2: Assign hypothesis = unknown.split(...)

```python
hypothesis = 'John loves Mary'.split()
```

### Step 3: Assign weights = value

```python
weights = (1.0 / n,) * n
```

**Verification:**
```python
assert sentence_bleu(references, hypothesis, weights) == 1.0
```


## Complete Example

```python
# Workflow
references = ['John loves Mary'.split()]
hypothesis = 'John loves Mary'.split()
for n in range(1, len(hypothesis)):
    weights = (1.0 / n,) * n
    assert sentence_bleu(references, hypothesis, weights) == 1.0
```

## Next Steps


---

*Source: test_bleu.py:127 | Complexity: Beginner | Last updated: 2026-06-02*