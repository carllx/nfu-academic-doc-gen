# How To: Reader Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reader dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `functools`
- `io`
- `os`
- `pathlib`
- `platform`
- `re`
- `urllib.error`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `s3fs`
- `py.path`
- `pyarrow`
- `pandas.arrays`
- `xlrd`
- `xlrd`
- `python_calamine`
- `python_calamine`

**Setup Required:**
```python
# Fixtures: read_ext
```

## Step-by-Step Guide

### Step 1: Assign basename = 'testdtype'

```python
basename = 'testdtype'
```

### Step 2: Assign actual = pd.read_excel(...)

```python
actual = pd.read_excel(basename + read_ext)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3, 4], 'b': [2.5, 3.5, 4.5, 5.5], 'c': [1, 2, 3, 4], 'd': [1.0, 2.0, np.nan, 4.0]})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```

### Step 5: Assign actual = pd.read_excel(...)

```python
actual = pd.read_excel(basename + read_ext, dtype={'a': 'float64', 'b': 'float32', 'c': str})
```

### Step 6: Assign unknown = unknown.astype(...)

```python
expected['a'] = expected['a'].astype('float64')
```

### Step 7: Assign unknown = unknown.astype(...)

```python
expected['b'] = expected['b'].astype('float32')
```

### Step 8: Assign unknown = Series(...)

```python
expected['c'] = Series(['001', '002', '003', '004'], dtype='str')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```

### Step 10: Assign msg = 'Unable to convert column d to type int64'

```python
msg = 'Unable to convert column d to type int64'
```

### Step 11: Call pd.read_excel()

```python
pd.read_excel(basename + read_ext, dtype={'d': 'int64'})
```


## Complete Example

```python
# Setup
# Fixtures: read_ext

# Workflow
basename = 'testdtype'
actual = pd.read_excel(basename + read_ext)
expected = DataFrame({'a': [1, 2, 3, 4], 'b': [2.5, 3.5, 4.5, 5.5], 'c': [1, 2, 3, 4], 'd': [1.0, 2.0, np.nan, 4.0]})
tm.assert_frame_equal(actual, expected)
actual = pd.read_excel(basename + read_ext, dtype={'a': 'float64', 'b': 'float32', 'c': str})
expected['a'] = expected['a'].astype('float64')
expected['b'] = expected['b'].astype('float32')
expected['c'] = Series(['001', '002', '003', '004'], dtype='str')
tm.assert_frame_equal(actual, expected)
msg = 'Unable to convert column d to type int64'
with pytest.raises(ValueError, match=msg):
    pd.read_excel(basename + read_ext, dtype={'d': 'int64'})
```

## Next Steps


---

*Source: test_readers.py:529 | Complexity: Advanced | Last updated: 2026-06-02*