# How To: At Time Datetimeindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test at time datetimeindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = date_range(...)

```python
index = date_range('2012-01-01', '2012-01-05', freq='30min')
```

**Verification:**
```python
assert len(result) == 4
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((len(index), 5)), index=index)
```

### Step 3: Assign akey = time(...)

```python
akey = time(12, 0, 0)
```

### Step 4: Assign ainds = value

```python
ainds = [24, 72, 120, 168]
```

### Step 5: Assign result = df.at_time(...)

```python
result = df.at_time(akey)
```

### Step 6: Assign expected = value

```python
expected = df.loc[akey]
```

### Step 7: Assign expected2 = value

```python
expected2 = df.iloc[ainds]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected2)
```

**Verification:**
```python
assert len(result) == 4
```


## Complete Example

```python
# Workflow
index = date_range('2012-01-01', '2012-01-05', freq='30min')
df = DataFrame(np.random.default_rng(2).standard_normal((len(index), 5)), index=index)
akey = time(12, 0, 0)
ainds = [24, 72, 120, 168]
result = df.at_time(akey)
expected = df.loc[akey]
expected2 = df.iloc[ainds]
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result, expected2)
assert len(result) == 4
```

## Next Steps


---

*Source: test_at_time.py:119 | Complexity: Advanced | Last updated: 2026-06-02*