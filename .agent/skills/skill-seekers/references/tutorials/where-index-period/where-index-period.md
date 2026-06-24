# How To: Where Index Period

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where index period

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2016-01-01', periods=3, freq='QS')
```

### Step 2: Assign pi = dti.to_period(...)

```python
pi = dti.to_period('Q')
```

### Step 3: Assign cond = np.array(...)

```python
cond = np.array([False, True, False])
```

### Step 4: Assign value = value

```python
value = pi[-1] + pi.freq * 10
```

### Step 5: Assign expected = pd.PeriodIndex(...)

```python
expected = pd.PeriodIndex([value, pi[1], value])
```

### Step 6: Assign result = pi.where(...)

```python
result = pi.where(cond, value)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign other = np.asarray(...)

```python
other = np.asarray(pi + pi.freq * 10, dtype=object)
```

### Step 9: Assign result = pi.where(...)

```python
result = pi.where(cond, other)
```

### Step 10: Assign expected = pd.PeriodIndex(...)

```python
expected = pd.PeriodIndex([other[0], pi[1], other[2]])
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 12: Assign td = pd.Timedelta(...)

```python
td = pd.Timedelta(days=4)
```

### Step 13: Assign expected = pd.Index(...)

```python
expected = pd.Index([td, pi[1], td], dtype=object)
```

### Step 14: Assign result = pi.where(...)

```python
result = pi.where(cond, td)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 16: Assign per = pd.Period(...)

```python
per = pd.Period('2020-04-21', 'D')
```

### Step 17: Assign expected = pd.Index(...)

```python
expected = pd.Index([per, pi[1], per], dtype=object)
```

### Step 18: Assign result = pi.where(...)

```python
result = pi.where(cond, per)
```

### Step 19: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = pd.date_range('2016-01-01', periods=3, freq='QS')
pi = dti.to_period('Q')
cond = np.array([False, True, False])
value = pi[-1] + pi.freq * 10
expected = pd.PeriodIndex([value, pi[1], value])
result = pi.where(cond, value)
tm.assert_index_equal(result, expected)
other = np.asarray(pi + pi.freq * 10, dtype=object)
result = pi.where(cond, other)
expected = pd.PeriodIndex([other[0], pi[1], other[2]])
tm.assert_index_equal(result, expected)
td = pd.Timedelta(days=4)
expected = pd.Index([td, pi[1], td], dtype=object)
result = pi.where(cond, td)
tm.assert_index_equal(result, expected)
per = pd.Period('2020-04-21', 'D')
expected = pd.Index([per, pi[1], per], dtype=object)
result = pi.where(cond, per)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_coercion.py:517 | Complexity: Advanced | Last updated: 2026-06-02*