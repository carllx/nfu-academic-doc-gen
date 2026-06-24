# How To: Doc Examples

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test doc examples

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame([['a', 1], ['a', 2], ['a', 3], ['b', 4], ['b', 5]], columns=['A', 'B'])
```


## Complete Example

```python
# Workflow
df = pd.DataFrame([['a', 1], ['a', 2], ['a', 3], ['b', 4], ['b', 5]], columns=['A', 'B'])
```

## Next Steps


---

*Source: test_indexing.py:102 | Complexity: Beginner | Last updated: 2026-06-02*