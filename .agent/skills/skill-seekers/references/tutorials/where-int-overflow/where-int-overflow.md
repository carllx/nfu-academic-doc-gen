# How To: Where Int Overflow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test where int overflow

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`

**Setup Required:**
```python
# Fixtures: replacement
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1.0, 2e+25, 'nine'], [np.nan, 0.1, None]])
```

### Step 2: Assign result = df.where(...)

```python
result = df.where(pd.notnull(df), replacement)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.0, 2e+25, 'nine'], [replacement, 0.1, replacement]])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: replacement

# Workflow
df = DataFrame([[1.0, 2e+25, 'nine'], [np.nan, 0.1, None]])
result = df.where(pd.notnull(df), replacement)
expected = DataFrame([[1.0, 2e+25, 'nine'], [replacement, 0.1, replacement]])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_where.py:1089 | Complexity: Intermediate | Last updated: 2026-06-02*