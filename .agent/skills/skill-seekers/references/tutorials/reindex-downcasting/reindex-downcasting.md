# How To: Reindex Downcasting

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex downcasting

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
s = Series(False, index=range(5))
```

### Step 2: Assign msg = 'Downcasting object dtype arrays on'

```python
msg = 'Downcasting object dtype arrays on'
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(False, index=range(5))
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = s.shift.bfill(...)

```python
result = s.shift(1).bfill()
```


## Complete Example

```python
# Workflow
s = Series(False, index=range(5))
msg = 'Downcasting object dtype arrays on'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = s.shift(1).bfill()
expected = Series(False, index=range(5))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reindex.py:162 | Complexity: Intermediate | Last updated: 2026-06-02*