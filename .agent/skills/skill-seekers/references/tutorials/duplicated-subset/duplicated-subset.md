# How To: Duplicated Subset

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test duplicated subset

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
# Fixtures: subset, keep
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [0, 1, 1, 2, 0], 'B': ['a', 'b', 'b', 'c', 'a'], 'C': [np.nan, 3, 3, None, np.nan]})
```

### Step 2: Assign expected = unknown.duplicated(...)

```python
expected = df[subset].duplicated(keep=keep)
```

### Step 3: Assign result = df.duplicated(...)

```python
result = df.duplicated(keep=keep, subset=subset)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign subset = list(...)

```python
subset = list(df.columns)
```

### Step 6: Assign subset = value

```python
subset = [subset]
```


## Complete Example

```python
# Setup
# Fixtures: subset, keep

# Workflow
df = DataFrame({'A': [0, 1, 1, 2, 0], 'B': ['a', 'b', 'b', 'c', 'a'], 'C': [np.nan, 3, 3, None, np.nan]})
if subset is None:
    subset = list(df.columns)
elif isinstance(subset, str):
    subset = [subset]
expected = df[subset].duplicated(keep=keep)
result = df.duplicated(keep=keep, subset=subset)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_duplicated.py:76 | Complexity: Intermediate | Last updated: 2026-06-02*