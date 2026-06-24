# How To: Where Invalid Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where invalid dtypes

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.frequencies`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('20130101', periods=3, tz='US/Eastern')
```

**Verification:**
```python
assert isinstance(expected[0], np.timedelta64)
```

### Step 2: Assign tail = unknown.tolist(...)

```python
tail = dti[2:].tolist()
```

**Verification:**
```python
assert isinstance(expected[0], int)
```

### Step 3: Assign i2 = Index(...)

```python
i2 = Index([pd.NaT, pd.NaT] + tail)
```

**Verification:**
```python
assert expected[0] is td
```

### Step 4: Assign mask = notna(...)

```python
mask = notna(i2)
```

### Step 5: Assign result = dti.where(...)

```python
result = dti.where(mask, i2.values)
```

### Step 6: Assign expected = Index(...)

```python
expected = Index([pd.NaT.asm8, pd.NaT.asm8] + tail, dtype=object)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign naive = dti.tz_localize(...)

```python
naive = dti.tz_localize(None)
```

### Step 9: Assign result = naive.where(...)

```python
result = naive.where(mask, i2)
```

### Step 10: Assign expected = Index(...)

```python
expected = Index([i2[0], i2[1]] + naive[2:].tolist(), dtype=object)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 12: Assign pi = i2.tz_localize.to_period(...)

```python
pi = i2.tz_localize(None).to_period('D')
```

### Step 13: Assign result = dti.where(...)

```python
result = dti.where(mask, pi)
```

### Step 14: Assign expected = Index(...)

```python
expected = Index([pi[0], pi[1]] + tail, dtype=object)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 16: Assign tda = i2.asi8.view(...)

```python
tda = i2.asi8.view('timedelta64[ns]')
```

### Step 17: Assign result = dti.where(...)

```python
result = dti.where(mask, tda)
```

### Step 18: Assign expected = Index(...)

```python
expected = Index([tda[0], tda[1]] + tail, dtype=object)
```

**Verification:**
```python
assert isinstance(expected[0], np.timedelta64)
```

### Step 19: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 20: Assign result = dti.where(...)

```python
result = dti.where(mask, i2.asi8)
```

### Step 21: Assign expected = Index(...)

```python
expected = Index([pd.NaT._value, pd.NaT._value] + tail, dtype=object)
```

**Verification:**
```python
assert isinstance(expected[0], int)
```

### Step 22: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 23: Assign td = pd.Timedelta(...)

```python
td = pd.Timedelta(days=4)
```

### Step 24: Assign result = dti.where(...)

```python
result = dti.where(mask, td)
```

### Step 25: Assign expected = Index(...)

```python
expected = Index([td, td] + tail, dtype=object)
```

**Verification:**
```python
assert expected[0] is td
```

### Step 26: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('20130101', periods=3, tz='US/Eastern')
tail = dti[2:].tolist()
i2 = Index([pd.NaT, pd.NaT] + tail)
mask = notna(i2)
result = dti.where(mask, i2.values)
expected = Index([pd.NaT.asm8, pd.NaT.asm8] + tail, dtype=object)
tm.assert_index_equal(result, expected)
naive = dti.tz_localize(None)
result = naive.where(mask, i2)
expected = Index([i2[0], i2[1]] + naive[2:].tolist(), dtype=object)
tm.assert_index_equal(result, expected)
pi = i2.tz_localize(None).to_period('D')
result = dti.where(mask, pi)
expected = Index([pi[0], pi[1]] + tail, dtype=object)
tm.assert_index_equal(result, expected)
tda = i2.asi8.view('timedelta64[ns]')
result = dti.where(mask, tda)
expected = Index([tda[0], tda[1]] + tail, dtype=object)
assert isinstance(expected[0], np.timedelta64)
tm.assert_index_equal(result, expected)
result = dti.where(mask, i2.asi8)
expected = Index([pd.NaT._value, pd.NaT._value] + tail, dtype=object)
assert isinstance(expected[0], int)
tm.assert_index_equal(result, expected)
td = pd.Timedelta(days=4)
result = dti.where(mask, td)
expected = Index([td, td] + tail, dtype=object)
assert expected[0] is td
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:147 | Complexity: Advanced | Last updated: 2026-06-02*