# How To: Between Time Datetimeindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test between time datetimeindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = date_range(...)

```python
index = date_range('2012-01-01', '2012-01-05', freq='30min')
```

**Verification:**
```python
assert len(result) == 12
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((len(index), 5)), index=index)
```

### Step 3: Assign bkey = slice(...)

```python
bkey = slice(time(13, 0, 0), time(14, 0, 0))
```

### Step 4: Assign binds = value

```python
binds = [26, 27, 28, 74, 75, 76, 122, 123, 124, 170, 171, 172]
```

### Step 5: Assign result = df.between_time(...)

```python
result = df.between_time(bkey.start, bkey.stop)
```

### Step 6: Assign expected = value

```python
expected = df.loc[bkey]
```

### Step 7: Assign expected2 = value

```python
expected2 = df.iloc[binds]
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
assert len(result) == 12
```


## Complete Example

```python
# Workflow
index = date_range('2012-01-01', '2012-01-05', freq='30min')
df = DataFrame(np.random.default_rng(2).standard_normal((len(index), 5)), index=index)
bkey = slice(time(13, 0, 0), time(14, 0, 0))
binds = [26, 27, 28, 74, 75, 76, 122, 123, 124, 170, 171, 172]
result = df.between_time(bkey.start, bkey.stop)
expected = df.loc[bkey]
expected2 = df.iloc[binds]
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result, expected2)
assert len(result) == 12
```

## Next Steps


---

*Source: test_between_time.py:200 | Complexity: Advanced | Last updated: 2026-06-02*