# How To: Pivot List Like Columns

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate DataFrame: test pivot list like columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: input_index, input_columns, input_values, expected_values, expected_columns, expected_index
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'lev1': [1, 1, 1, 1, 2, 2, 2, 2], 'lev2': [1, 1, 2, 2, 1, 1, 2, 2], 'lev3': [1, 2, 1, 2, 1, 2, 1, 2], 'lev4': [1, 2, 3, 4, 5, 6, 7, 8], 'values': [0, 1, 2, 3, 4, 5, 6, 7]})
```


## Complete Example

```python
# Setup
# Fixtures: input_index, input_columns, input_values, expected_values, expected_columns, expected_index

# Workflow
df = pd.DataFrame({'lev1': [1, 1, 1, 1, 2, 2, 2, 2], 'lev2': [1, 1, 2, 2, 1, 1, 2, 2], 'lev3': [1, 2, 1, 2, 1, 2, 1, 2], 'lev4': [1, 2, 3, 4, 5, 6, 7, 8], 'values': [0, 1, 2, 3, 4, 5, 6, 7]})
```

## Next Steps


---

*Source: test_pivot_multilevel.py:183 | Complexity: Beginner | Last updated: 2026-06-02*