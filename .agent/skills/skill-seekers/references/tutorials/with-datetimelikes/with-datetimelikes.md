# How To: With Datetimelikes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test with datetimelikes

## Prerequisites

**Required Modules:**
- `copy`
- `inspect`
- `pydoc`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._config.config`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `IPython.core.completer`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': date_range('20130101', periods=10), 'B': timedelta_range('1 day', periods=10)})
```

### Step 2: Assign t = value

```python
t = df.T
```

### Step 3: Assign result = t.dtypes.value_counts(...)

```python
result = t.dtypes.value_counts()
```

### Step 4: Assign expected = Series(...)

```python
expected = Series({np.dtype('object'): 10}, name='count')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': date_range('20130101', periods=10), 'B': timedelta_range('1 day', periods=10)})
t = df.T
result = t.dtypes.value_counts()
expected = Series({np.dtype('object'): 10}, name='count')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_api.py:211 | Complexity: Intermediate | Last updated: 2026-06-02*