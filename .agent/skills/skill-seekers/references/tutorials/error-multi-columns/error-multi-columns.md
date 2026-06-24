# How To: Error Multi Columns

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate DataFrame: test error multi columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: input_subset, error_message
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': [[0, 1, 2], np.nan, [], (3, 4)], 'B': 1, 'C': [['a', 'b', 'c'], 'foo', [], ['d', 'e', 'f']]}, index=list('abcd'))
```


## Complete Example

```python
# Setup
# Fixtures: input_subset, error_message

# Workflow
df = pd.DataFrame({'A': [[0, 1, 2], np.nan, [], (3, 4)], 'B': 1, 'C': [['a', 'b', 'c'], 'foo', [], ['d', 'e', 'f']]}, index=list('abcd'))
```

## Next Steps


---

*Source: test_explode.py:49 | Complexity: Beginner | Last updated: 2026-06-02*