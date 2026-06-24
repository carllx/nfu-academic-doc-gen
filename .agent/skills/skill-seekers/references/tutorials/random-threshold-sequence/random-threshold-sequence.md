# How To: Random Threshold Sequence

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random threshold sequence

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.threshold`


## Step-by-Step Guide

### Step 1: Call pytest.raises()

```python
pytest.raises(ValueError, nxt.random_threshold_sequence, 10, 1.5)
```

**Verification:**
```python
assert len(nxt.random_threshold_sequence(10, 0.5)) == 10
```


## Complete Example

```python
# Workflow
assert len(nxt.random_threshold_sequence(10, 0.5)) == 10
assert nxt.random_threshold_sequence(10, 0.5, seed=42) == ['d', 'i', 'd', 'd', 'd', 'i', 'i', 'i', 'd', 'd']
pytest.raises(ValueError, nxt.random_threshold_sequence, 10, 1.5)
```

## Next Steps


---

*Source: test_threshold.py:147 | Complexity: Beginner | Last updated: 2026-06-02*