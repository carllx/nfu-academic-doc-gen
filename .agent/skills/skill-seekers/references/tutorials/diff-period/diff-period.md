# How To: Diff Period

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test diff period

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pi = date_range.to_period(...)

```python
pi = date_range('2016-01-01', periods=3).to_period('D')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': pi})
```

### Step 3: Assign result = df.diff(...)

```python
result = df.diff(1, axis=1)
```

### Step 4: Assign expected = unknown.astype(...)

```python
expected = (df - pd.NaT).astype(object)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
pi = date_range('2016-01-01', periods=3).to_period('D')
df = DataFrame({'A': pi})
result = df.diff(1, axis=1)
expected = (df - pd.NaT).astype(object)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_diff.py:189 | Complexity: Intermediate | Last updated: 2026-06-02*