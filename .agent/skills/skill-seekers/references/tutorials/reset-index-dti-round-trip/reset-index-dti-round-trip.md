# How To: Reset Index Dti Round Trip

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset index dti round trip

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range._with_freq(...)

```python
dti = date_range(start='1/1/2001', end='6/1/2001', freq='D')._with_freq(None)
```

**Verification:**
```python
assert d2.dtypes.iloc[0] == np.dtype('M8[ns]')
```

### Step 2: Assign d1 = DataFrame(...)

```python
d1 = DataFrame({'v': np.random.default_rng(2).random(len(dti))}, index=dti)
```

**Verification:**
```python
assert df.index[0] == stamp
```

### Step 3: Assign d2 = d1.reset_index(...)

```python
d2 = d1.reset_index()
```

**Verification:**
```python
assert df.reset_index()['Date'].iloc[0] == stamp
```

### Step 4: Assign d3 = d2.set_index(...)

```python
d3 = d2.set_index('index')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(d1, d3, check_names=False)
```

### Step 6: Assign stamp = datetime(...)

```python
stamp = datetime(2012, 11, 22)
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame([[stamp, 12.1]], columns=['Date', 'Value'])
```

### Step 8: Assign df = df.set_index(...)

```python
df = df.set_index('Date')
```

**Verification:**
```python
assert df.index[0] == stamp
```


## Complete Example

```python
# Workflow
dti = date_range(start='1/1/2001', end='6/1/2001', freq='D')._with_freq(None)
d1 = DataFrame({'v': np.random.default_rng(2).random(len(dti))}, index=dti)
d2 = d1.reset_index()
assert d2.dtypes.iloc[0] == np.dtype('M8[ns]')
d3 = d2.set_index('index')
tm.assert_frame_equal(d1, d3, check_names=False)
stamp = datetime(2012, 11, 22)
df = DataFrame([[stamp, 12.1]], columns=['Date', 'Value'])
df = df.set_index('Date')
assert df.index[0] == stamp
assert df.reset_index()['Date'].iloc[0] == stamp
```

## Next Steps


---

*Source: test_reset_index.py:20 | Complexity: Advanced | Last updated: 2026-06-02*