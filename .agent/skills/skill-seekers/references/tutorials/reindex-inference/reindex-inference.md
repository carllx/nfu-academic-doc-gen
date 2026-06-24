# How To: Reindex Inference

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex inference

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([True, False, False, True], index=list('abcd'))
```

### Step 2: Assign new_index = 'agc'

```python
new_index = 'agc'
```

### Step 3: Assign msg = 'Downcasting object dtype arrays on'

```python
msg = 'Downcasting object dtype arrays on'
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([True, True, False], index=list(new_index))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = s.reindex.ffill(...)

```python
result = s.reindex(list(new_index)).ffill()
```


## Complete Example

```python
# Workflow
s = Series([True, False, False, True], index=list('abcd'))
new_index = 'agc'
msg = 'Downcasting object dtype arrays on'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = s.reindex(list(new_index)).ffill()
expected = Series([True, True, False], index=list(new_index))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reindex.py:151 | Complexity: Intermediate | Last updated: 2026-06-02*