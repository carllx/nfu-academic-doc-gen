# How To: Fillna Tzaware Different Column

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna tzaware different column

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
df = DataFrame({'A': date_range('20130101', periods=4, tz='US/Eastern'), 'B': [1, 2, np.nan, np.nan]})
```

### Step 2: Assign msg = "DataFrame.fillna with 'method' is deprecated"

```python
msg = "DataFrame.fillna with 'method' is deprecated"
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': date_range('20130101', periods=4, tz='US/Eastern'), 'B': [1.0, 2.0, 2.0, 2.0]})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.fillna(...)

```python
result = df.fillna(method='pad')
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': date_range('20130101', periods=4, tz='US/Eastern'), 'B': [1, 2, np.nan, np.nan]})
msg = "DataFrame.fillna with 'method' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.fillna(method='pad')
expected = DataFrame({'A': date_range('20130101', periods=4, tz='US/Eastern'), 'B': [1.0, 2.0, 2.0, 2.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_fillna.py:205 | Complexity: Intermediate | Last updated: 2026-06-02*