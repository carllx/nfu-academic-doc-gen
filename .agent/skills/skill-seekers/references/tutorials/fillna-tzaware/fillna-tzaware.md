# How To: Fillna Tzaware

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna tzaware

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
df = DataFrame({'A': [Timestamp('2012-11-11 00:00:00+01:00'), NaT]})
```

### Step 2: Assign exp = DataFrame(...)

```python
exp = DataFrame({'A': [Timestamp('2012-11-11 00:00:00+01:00'), Timestamp('2012-11-11 00:00:00+01:00')]})
```

### Step 3: Assign msg = "DataFrame.fillna with 'method' is deprecated"

```python
msg = "DataFrame.fillna with 'method' is deprecated"
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [NaT, Timestamp('2012-11-11 00:00:00+01:00')]})
```

### Step 6: Assign exp = DataFrame(...)

```python
exp = DataFrame({'A': [Timestamp('2012-11-11 00:00:00+01:00'), Timestamp('2012-11-11 00:00:00+01:00')]})
```

### Step 7: Assign msg = "DataFrame.fillna with 'method' is deprecated"

```python
msg = "DataFrame.fillna with 'method' is deprecated"
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```

### Step 9: Assign res = df.fillna(...)

```python
res = df.fillna(method='pad')
```

### Step 10: Assign res = df.fillna(...)

```python
res = df.fillna(method='bfill')
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [Timestamp('2012-11-11 00:00:00+01:00'), NaT]})
exp = DataFrame({'A': [Timestamp('2012-11-11 00:00:00+01:00'), Timestamp('2012-11-11 00:00:00+01:00')]})
msg = "DataFrame.fillna with 'method' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = df.fillna(method='pad')
tm.assert_frame_equal(res, exp)
df = DataFrame({'A': [NaT, Timestamp('2012-11-11 00:00:00+01:00')]})
exp = DataFrame({'A': [Timestamp('2012-11-11 00:00:00+01:00'), Timestamp('2012-11-11 00:00:00+01:00')]})
msg = "DataFrame.fillna with 'method' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = df.fillna(method='bfill')
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_fillna.py:174 | Complexity: Advanced | Last updated: 2026-06-02*