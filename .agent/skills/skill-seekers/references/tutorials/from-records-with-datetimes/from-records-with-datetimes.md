# How To: From Records With Datetimes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from records with datetimes

## Prerequisites

**Required Modules:**
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pytz`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame({'EXPIRY': [datetime(2005, 3, 1, 0, 0), None]})
```

### Step 2: Assign arrdata = value

```python
arrdata = [np.array([datetime(2005, 3, 1, 0, 0), None])]
```

### Step 3: Assign dtypes = value

```python
dtypes = [('EXPIRY', '<M8[ns]')]
```

### Step 4: Assign recarray = np.rec.fromarrays(...)

```python
recarray = np.rec.fromarrays(arrdata, dtype=dtypes)
```

### Step 5: Assign result = DataFrame.from_records(...)

```python
result = DataFrame.from_records(recarray)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign arrdata = value

```python
arrdata = [np.array([datetime(2005, 3, 1, 0, 0), None])]
```

### Step 8: Assign dtypes = value

```python
dtypes = [('EXPIRY', '<M8[m]')]
```

### Step 9: Assign recarray = np.rec.fromarrays(...)

```python
recarray = np.rec.fromarrays(arrdata, dtype=dtypes)
```

### Step 10: Assign result = DataFrame.from_records(...)

```python
result = DataFrame.from_records(recarray)
```

### Step 11: Assign unknown = unknown.astype(...)

```python
expected['EXPIRY'] = expected['EXPIRY'].astype('M8[s]')
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Call pytest.skip()

```python
pytest.skip('known failure of test on non-little endian')
```


## Complete Example

```python
# Workflow
if not is_platform_little_endian():
    pytest.skip('known failure of test on non-little endian')
expected = DataFrame({'EXPIRY': [datetime(2005, 3, 1, 0, 0), None]})
arrdata = [np.array([datetime(2005, 3, 1, 0, 0), None])]
dtypes = [('EXPIRY', '<M8[ns]')]
recarray = np.rec.fromarrays(arrdata, dtype=dtypes)
result = DataFrame.from_records(recarray)
tm.assert_frame_equal(result, expected)
arrdata = [np.array([datetime(2005, 3, 1, 0, 0), None])]
dtypes = [('EXPIRY', '<M8[m]')]
recarray = np.rec.fromarrays(arrdata, dtype=dtypes)
result = DataFrame.from_records(recarray)
expected['EXPIRY'] = expected['EXPIRY'].astype('M8[s]')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_from_records.py:34 | Complexity: Advanced | Last updated: 2026-06-02*