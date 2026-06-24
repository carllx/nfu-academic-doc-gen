# How To: Partial Slice Doesnt Require Monotonicity

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partial slice doesnt require monotonicity

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2014-01-01', periods=30, freq='30D')
```

**Verification:**
```python
assert (nidx[indexer_2014].year == 2014).all()
```

### Step 2: Assign pi = dti.to_period(...)

```python
pi = dti.to_period('D')
```

**Verification:**
```python
assert not (nidx[~indexer_2014].year == 2014).any()
```

### Step 3: Assign ser_montonic = Series(...)

```python
ser_montonic = Series(np.arange(30), index=pi)
```

**Verification:**
```python
assert nidx[23].year == 2015 and nidx[23].month == 5
```

### Step 4: Assign shuffler = value

```python
shuffler = list(range(0, 30, 2)) + list(range(1, 31, 2))
```

### Step 5: Assign ser = value

```python
ser = ser_montonic.iloc[shuffler]
```

### Step 6: Assign nidx = value

```python
nidx = ser.index
```

### Step 7: Assign indexer_2014 = np.array(...)

```python
indexer_2014 = np.array([0, 1, 2, 3, 4, 5, 6, 15, 16, 17, 18, 19, 20], dtype=np.intp)
```

**Verification:**
```python
assert (nidx[indexer_2014].year == 2014).all()
```

### Step 8: Assign result = nidx.get_loc(...)

```python
result = nidx.get_loc('2014')
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, indexer_2014)
```

### Step 10: Assign expected = value

```python
expected = ser.iloc[indexer_2014]
```

### Step 11: Assign result = value

```python
result = ser.loc['2014']
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 13: Assign result = value

```python
result = ser['2014']
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 15: Assign indexer_may2015 = np.array(...)

```python
indexer_may2015 = np.array([23], dtype=np.intp)
```

**Verification:**
```python
assert nidx[23].year == 2015 and nidx[23].month == 5
```

### Step 16: Assign result = nidx.get_loc(...)

```python
result = nidx.get_loc('May 2015')
```

### Step 17: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, indexer_may2015)
```

### Step 18: Assign expected = value

```python
expected = ser.iloc[indexer_may2015]
```

### Step 19: Assign result = value

```python
result = ser.loc['May 2015']
```

### Step 20: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 21: Assign result = value

```python
result = ser['May 2015']
```

### Step 22: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('2014-01-01', periods=30, freq='30D')
pi = dti.to_period('D')
ser_montonic = Series(np.arange(30), index=pi)
shuffler = list(range(0, 30, 2)) + list(range(1, 31, 2))
ser = ser_montonic.iloc[shuffler]
nidx = ser.index
indexer_2014 = np.array([0, 1, 2, 3, 4, 5, 6, 15, 16, 17, 18, 19, 20], dtype=np.intp)
assert (nidx[indexer_2014].year == 2014).all()
assert not (nidx[~indexer_2014].year == 2014).any()
result = nidx.get_loc('2014')
tm.assert_numpy_array_equal(result, indexer_2014)
expected = ser.iloc[indexer_2014]
result = ser.loc['2014']
tm.assert_series_equal(result, expected)
result = ser['2014']
tm.assert_series_equal(result, expected)
indexer_may2015 = np.array([23], dtype=np.intp)
assert nidx[23].year == 2015 and nidx[23].month == 5
result = nidx.get_loc('May 2015')
tm.assert_numpy_array_equal(result, indexer_may2015)
expected = ser.iloc[indexer_may2015]
result = ser.loc['May 2015']
tm.assert_series_equal(result, expected)
result = ser['May 2015']
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_partial_slicing.py:158 | Complexity: Advanced | Last updated: 2026-06-02*