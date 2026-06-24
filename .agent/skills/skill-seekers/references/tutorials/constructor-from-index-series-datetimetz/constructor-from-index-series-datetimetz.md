# How To: Constructor From Index Series Datetimetz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor from index series datetimetz

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('2015-01-01 10:00', freq='D', periods=3, tz='US/Eastern')
```

### Step 2: Assign idx = idx._with_freq(...)

```python
idx = idx._with_freq(None)
```

### Step 3: Assign result = Categorical(...)

```python
result = Categorical(idx)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.categories, idx)
```

### Step 5: Assign result = Categorical(...)

```python
result = Categorical(Series(idx))
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.categories, idx)
```


## Complete Example

```python
# Workflow
idx = date_range('2015-01-01 10:00', freq='D', periods=3, tz='US/Eastern')
idx = idx._with_freq(None)
result = Categorical(idx)
tm.assert_index_equal(result.categories, idx)
result = Categorical(Series(idx))
tm.assert_index_equal(result.categories, idx)
```

## Next Steps


---

*Source: test_constructors.py:363 | Complexity: Intermediate | Last updated: 2026-06-02*