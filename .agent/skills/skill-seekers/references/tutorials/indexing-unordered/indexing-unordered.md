# How To: Indexing Unordered

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indexing unordered

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range(start='2011-01-01', end='2011-01-15')
```

**Verification:**
```python
assert expected == result
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).random(len(rng)), index=rng)
```

### Step 3: Assign ts2 = pd.concat(...)

```python
ts2 = pd.concat([ts[0:4], ts[-4:], ts[4:-4]])
```

### Step 4: Assign result = unknown.sort_index(...)

```python
result = ts2['2011'].sort_index()
```

### Step 5: Assign expected = value

```python
expected = ts['2011']
```

### Step 6: Assign expected.index = expected.index._with_freq(...)

```python
expected.index = expected.index._with_freq(None)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign expected = value

```python
expected = ts[t]
```

### Step 9: Assign result = value

```python
result = ts2[t]
```

**Verification:**
```python
assert expected == result
```

### Step 10: Assign result = unknown.copy(...)

```python
result = ts2[slobj].copy()
```

### Step 11: Assign result = result.sort_index(...)

```python
result = result.sort_index()
```

### Step 12: Assign expected = value

```python
expected = ts[slobj]
```

### Step 13: Assign expected.index = expected.index._with_freq(...)

```python
expected.index = expected.index._with_freq(None)
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 15: Call compare()

```python
compare(key)
```


## Complete Example

```python
# Workflow
rng = date_range(start='2011-01-01', end='2011-01-15')
ts = Series(np.random.default_rng(2).random(len(rng)), index=rng)
ts2 = pd.concat([ts[0:4], ts[-4:], ts[4:-4]])
for t in ts.index:
    expected = ts[t]
    result = ts2[t]
    assert expected == result

def compare(slobj):
    result = ts2[slobj].copy()
    result = result.sort_index()
    expected = ts[slobj]
    expected.index = expected.index._with_freq(None)
    tm.assert_series_equal(result, expected)
for key in [slice('2011-01-01', '2011-01-15'), slice('2010-12-30', '2011-01-15'), slice('2011-01-01', '2011-01-16'), slice('2011-01-01', '2011-01-6'), slice('2011-01-06', '2011-01-8'), slice('2011-01-06', '2011-01-12')]:
    with pytest.raises(KeyError, match='Value based partial slicing on non-monotonic'):
        compare(key)
result = ts2['2011'].sort_index()
expected = ts['2011']
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime.py:372 | Complexity: Advanced | Last updated: 2026-06-02*