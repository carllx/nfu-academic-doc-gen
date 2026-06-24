# How To: Degree Sequences

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test degree sequences

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign seq = nx.utils.powerlaw_sequence(...)

```python
seq = nx.utils.powerlaw_sequence(10, seed=1)
```

**Verification:**
```python
assert len(seq) == 10
```

### Step 2: Assign seq = nx.utils.powerlaw_sequence(...)

```python
seq = nx.utils.powerlaw_sequence(10)
```

**Verification:**
```python
assert len(seq) == 10
```


## Complete Example

```python
# Workflow
seq = nx.utils.powerlaw_sequence(10, seed=1)
seq = nx.utils.powerlaw_sequence(10)
assert len(seq) == 10
```

## Next Steps


---

*Source: test_random_sequence.py:6 | Complexity: Beginner | Last updated: 2026-06-02*