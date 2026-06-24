# How To: Mixed Frame With Integer Sum

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mixed frame with integer sum

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([['a', 1]], columns=list('ab'))
```

### Step 2: Assign df = df.astype(...)

```python
df = df.astype({'b': 'Int64'})
```

### Step 3: Assign result = df.sum(...)

```python
result = df.sum()
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(['a', 1], index=['a', 'b'])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([['a', 1]], columns=list('ab'))
df = df.astype({'b': 'Int64'})
result = df.sum()
expected = Series(['a', 1], index=['a', 'b'])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:1940 | Complexity: Intermediate | Last updated: 2026-06-02*