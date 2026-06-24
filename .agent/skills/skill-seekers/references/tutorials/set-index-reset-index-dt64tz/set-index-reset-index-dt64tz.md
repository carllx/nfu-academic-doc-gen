# How To: Set Index Reset Index Dt64Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set index reset index dt64tz

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index(date_range('20130101', periods=3, tz='US/Eastern'), name='foo')
```

**Verification:**
```python
assert result['foo'].dtype == 'datetime64[ns, US/Eastern]'
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [0, 1, 2]}, index=idx)
```

### Step 3: Assign result = df.reset_index(...)

```python
result = df.reset_index()
```

**Verification:**
```python
assert result['foo'].dtype == 'datetime64[ns, US/Eastern]'
```

### Step 4: Assign df = result.set_index(...)

```python
df = result.set_index('foo')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, idx)
```


## Complete Example

```python
# Workflow
idx = Index(date_range('20130101', periods=3, tz='US/Eastern'), name='foo')
df = DataFrame({'A': [0, 1, 2]}, index=idx)
result = df.reset_index()
assert result['foo'].dtype == 'datetime64[ns, US/Eastern]'
df = result.set_index('foo')
tm.assert_index_equal(df.index, idx)
```

## Next Steps


---

*Source: test_reset_index.py:59 | Complexity: Intermediate | Last updated: 2026-06-02*