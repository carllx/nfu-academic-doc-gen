# How To: Value Counts Object Inference Deprecated

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test value counts object inference deprecated

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.base.common`


## Step-by-Step Guide

### Step 1: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2016-01-01', periods=3, tz='UTC')
```

### Step 2: Assign idx = dti.astype(...)

```python
idx = dti.astype(object)
```

### Step 3: Assign msg = 'The behavior of value_counts with object-dtype is deprecated'

```python
msg = 'The behavior of value_counts with object-dtype is deprecated'
```

### Step 4: Assign exp = dti.value_counts(...)

```python
exp = dti.value_counts()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 6: Assign res = idx.value_counts(...)

```python
res = idx.value_counts()
```


## Complete Example

```python
# Workflow
dti = pd.date_range('2016-01-01', periods=3, tz='UTC')
idx = dti.astype(object)
msg = 'The behavior of value_counts with object-dtype is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = idx.value_counts()
exp = dti.value_counts()
tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_value_counts.py:346 | Complexity: Intermediate | Last updated: 2026-06-02*