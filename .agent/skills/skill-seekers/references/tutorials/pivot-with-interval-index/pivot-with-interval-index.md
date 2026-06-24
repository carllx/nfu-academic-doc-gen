# How To: Pivot With Interval Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pivot with interval index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape`
- `pandas.core.reshape.pivot`

**Setup Required:**
```python
# Fixtures: interval_values, dropna
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': interval_values, 'B': 1})
```

### Step 2: Assign msg = 'The default value of observed=False is deprecated'

```python
msg = 'The default value of observed=False is deprecated'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'B': 1.0}, index=Index(interval_values.unique(), name='A'))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.pivot_table(...)

```python
result = df.pivot_table(index='A', values='B', dropna=dropna)
```

### Step 6: Assign expected = expected.astype(...)

```python
expected = expected.astype(float)
```


## Complete Example

```python
# Setup
# Fixtures: interval_values, dropna

# Workflow
df = DataFrame({'A': interval_values, 'B': 1})
msg = 'The default value of observed=False is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.pivot_table(index='A', values='B', dropna=dropna)
expected = DataFrame({'B': 1.0}, index=Index(interval_values.unique(), name='A'))
if not dropna:
    expected = expected.astype(float)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_pivot.py:311 | Complexity: Intermediate | Last updated: 2026-06-02*