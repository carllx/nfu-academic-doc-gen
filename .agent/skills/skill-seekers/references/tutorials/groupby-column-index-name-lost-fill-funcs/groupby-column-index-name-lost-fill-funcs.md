# How To: Groupby Column Index Name Lost Fill Funcs

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate DataFrame: test groupby column index name lost fill funcs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: func
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 1.0, -1.0], [1, np.nan, np.nan], [1, 2.0, -2.0]], columns=Index(['type', 'a', 'b'], name='idx'))
```


## Complete Example

```python
# Setup
# Fixtures: func

# Workflow
df = DataFrame([[1, 1.0, -1.0], [1, np.nan, np.nan], [1, 2.0, -2.0]], columns=Index(['type', 'a', 'b'], name='idx'))
```

## Next Steps


---

*Source: test_missing.py:16 | Complexity: Beginner | Last updated: 2026-06-02*