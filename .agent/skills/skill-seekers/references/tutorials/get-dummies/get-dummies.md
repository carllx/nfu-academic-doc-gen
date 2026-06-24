# How To: Get Dummies

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test get dummies

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas`

**Setup Required:**
```python
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0, 1, 1], [0, 1, 0], [1, 0, 0]], columns=list('7ab'))
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
expected = DataFrame([[0, 1, 1], [0, 1, 0], [1, 0, 0]], columns=list('7ab'))
```

## Next Steps


---

*Source: test_get_dummies.py:20 | Complexity: Beginner | Last updated: 2026-06-02*