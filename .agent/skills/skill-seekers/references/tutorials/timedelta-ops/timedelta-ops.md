# How To: Timedelta Ops

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timedelta ops

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays.string_arrow`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([Timestamp('20130101') + timedelta(seconds=i * i) for i in range(10)])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign td = s.diff(...)

```python
td = s.diff()
```

**Verification:**
```python
assert result[0] == expected
```

### Step 3: Assign result = td.mean(...)

```python
result = td.mean()
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign expected = to_timedelta(...)

```python
expected = to_timedelta(timedelta(seconds=9))
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = td.to_frame.mean(...)

```python
result = td.to_frame().mean()
```

**Verification:**
```python
assert result[0] == expected
```

### Step 6: Assign result = td.quantile(...)

```python
result = td.quantile(0.1)
```

**Verification:**
```python
assert result == expected
```

### Step 7: Assign expected = Timedelta(...)

```python
expected = Timedelta(np.timedelta64(2600, 'ms'))
```

**Verification:**
```python
assert result[0] == expected
```

### Step 8: Assign result = td.median(...)

```python
result = td.median()
```

**Verification:**
```python
assert result == expected
```

### Step 9: Assign expected = to_timedelta(...)

```python
expected = to_timedelta('00:00:09')
```

**Verification:**
```python
assert result[0] == expected
```

### Step 10: Assign result = td.to_frame.median(...)

```python
result = td.to_frame().median()
```

**Verification:**
```python
assert s.diff().median() == timedelta(days=4)
```

### Step 11: Assign result = td.sum(...)

```python
result = td.sum()
```

**Verification:**
```python
assert s.diff().median() == timedelta(days=6)
```

### Step 12: Assign expected = to_timedelta(...)

```python
expected = to_timedelta('00:01:21')
```

**Verification:**
```python
assert result == expected
```

### Step 13: Assign result = td.to_frame.sum(...)

```python
result = td.to_frame().sum()
```

**Verification:**
```python
assert result[0] == expected
```

### Step 14: Assign result = td.std(...)

```python
result = td.std()
```

### Step 15: Assign expected = to_timedelta(...)

```python
expected = to_timedelta(Series(td.dropna().values).std())
```

**Verification:**
```python
assert result == expected
```

### Step 16: Assign result = td.to_frame.std(...)

```python
result = td.to_frame().std()
```

**Verification:**
```python
assert result[0] == expected
```

### Step 17: Assign s = Series(...)

```python
s = Series([Timestamp('2015-02-03'), Timestamp('2015-02-07')])
```

**Verification:**
```python
assert s.diff().median() == timedelta(days=4)
```

### Step 18: Assign s = Series(...)

```python
s = Series([Timestamp('2015-02-03'), Timestamp('2015-02-07'), Timestamp('2015-02-15')])
```

**Verification:**
```python
assert s.diff().median() == timedelta(days=6)
```


## Complete Example

```python
# Workflow
s = Series([Timestamp('20130101') + timedelta(seconds=i * i) for i in range(10)])
td = s.diff()
result = td.mean()
expected = to_timedelta(timedelta(seconds=9))
assert result == expected
result = td.to_frame().mean()
assert result[0] == expected
result = td.quantile(0.1)
expected = Timedelta(np.timedelta64(2600, 'ms'))
assert result == expected
result = td.median()
expected = to_timedelta('00:00:09')
assert result == expected
result = td.to_frame().median()
assert result[0] == expected
result = td.sum()
expected = to_timedelta('00:01:21')
assert result == expected
result = td.to_frame().sum()
assert result[0] == expected
result = td.std()
expected = to_timedelta(Series(td.dropna().values).std())
assert result == expected
result = td.to_frame().std()
assert result[0] == expected
s = Series([Timestamp('2015-02-03'), Timestamp('2015-02-07')])
assert s.diff().median() == timedelta(days=4)
s = Series([Timestamp('2015-02-03'), Timestamp('2015-02-07'), Timestamp('2015-02-15')])
assert s.diff().median() == timedelta(days=6)
```

## Next Steps


---

*Source: test_reductions.py:333 | Complexity: Advanced | Last updated: 2026-06-02*