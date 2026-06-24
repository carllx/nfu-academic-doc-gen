# How To: Copy Deep False Retains Id

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate MultiIndex: test copy deep false retains id

## Prerequisites

**Required Modules:**
- `copy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex(...)

```python
idx = MultiIndex(levels=[['foo', 'bar'], ['fizz', 'buzz']], codes=[[0, 0, 0, 1], [0, 0, 1, 1]], names=['first', 'second'])
```


## Complete Example

```python
# Workflow
idx = MultiIndex(levels=[['foo', 'bar'], ['fizz', 'buzz']], codes=[[0, 0, 0, 1], [0, 0, 1, 1]], names=['first', 'second'])
```

## Next Steps


---

*Source: test_copy.py:89 | Complexity: Beginner | Last updated: 2026-06-02*