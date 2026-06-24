# How To: Agg Cast Results Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg cast results dtypes

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.printing`
- `pandas.tests.extension.decimal.array`


## Step-by-Step Guide

### Step 1: Assign u = value

```python
u = [dt.datetime(2015, x + 1, 1) for x in range(12)]
```

### Step 2: Assign v = list(...)

```python
v = list('aaabbbbbbccd')
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'X': v, 'Y': u})
```

### Step 4: Assign result = unknown.agg(...)

```python
result = df.groupby('X')['Y'].agg(len)
```

### Step 5: Assign expected = unknown.count(...)

```python
expected = df.groupby('X')['Y'].count()
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
u = [dt.datetime(2015, x + 1, 1) for x in range(12)]
v = list('aaabbbbbbccd')
df = DataFrame({'X': v, 'Y': u})
result = df.groupby('X')['Y'].agg(len)
expected = df.groupby('X')['Y'].count()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_other.py:141 | Complexity: Intermediate | Last updated: 2026-06-02*