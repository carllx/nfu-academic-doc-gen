# How To: Fillna Limit And Value

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna limit and value

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 3)))
```

### Step 2: Assign unknown = value

```python
df.iloc[2:7, 0] = np.nan
```

### Step 3: Assign unknown = value

```python
df.iloc[3:5, 2] = np.nan
```

### Step 4: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 5: Assign unknown = 999

```python
expected.iloc[2, 0] = 999
```

### Step 6: Assign unknown = 999

```python
expected.iloc[3, 2] = 999
```

### Step 7: Assign result = df.fillna(...)

```python
result = df.fillna(999, limit=1)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 3)))
df.iloc[2:7, 0] = np.nan
df.iloc[3:5, 2] = np.nan
expected = df.copy()
expected.iloc[2, 0] = 999
expected.iloc[3, 2] = 999
result = df.fillna(999, limit=1)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_fillna.py:147 | Complexity: Advanced | Last updated: 2026-06-02*