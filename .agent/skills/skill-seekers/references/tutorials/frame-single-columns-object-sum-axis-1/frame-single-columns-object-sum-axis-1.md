# How To: Frame Single Columns Object Sum Axis 1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame single columns object sum axis 1

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `enum`
- `functools`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation`
- `pandas.tests.frame.common`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {'One': Series(['A', 1.2, np.nan])}
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data)
```

### Step 3: Assign result = df.sum(...)

```python
result = df.sum(axis=1)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(['A', 1.2, 0])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = {'One': Series(['A', 1.2, np.nan])}
df = DataFrame(data)
result = df.sum(axis=1)
expected = Series(['A', 1.2, 0])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:1196 | Complexity: Intermediate | Last updated: 2026-06-02*