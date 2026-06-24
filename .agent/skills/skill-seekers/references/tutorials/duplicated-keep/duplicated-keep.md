# How To: Duplicated Keep

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate DataFrame: test duplicated keep

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `sys`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: keep, expected
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [0, 1, 1, 2, 0], 'B': ['a', 'b', 'b', 'c', 'a']})
```


## Complete Example

```python
# Setup
# Fixtures: keep, expected

# Workflow
df = DataFrame({'A': [0, 1, 1, 2, 0], 'B': ['a', 'b', 'b', 'c', 'a']})
```

## Next Steps


---

*Source: test_duplicated.py:53 | Complexity: Beginner | Last updated: 2026-06-02*