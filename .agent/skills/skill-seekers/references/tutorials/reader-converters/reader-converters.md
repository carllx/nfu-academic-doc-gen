# How To: Reader Converters

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reader converters

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

### Step 1: Assign basename = 'test_converters'

```python
basename = 'test_converters'
```

### Step 2: Assign expected = DataFrame.from_dict(...)

```python
expected = DataFrame.from_dict({'IntCol': [1, 2, -3, -1000, 0], 'FloatCol': [12.5, np.nan, 18.3, 19.2, 5e-09], 'BoolCol': ['Found', 'Found', 'Found', 'Not found', 'Found'], 'StrCol': ['1', np.nan, '3', '4', '5']})
```

### Step 3: Assign converters = value

```python
converters = {'IntCol': lambda x: int(x) if x != '' else -1000, 'FloatCol': lambda x: 10 * x if x else np.nan, 2: lambda x: 'Found' if x != '' else 'Not found', 3: lambda x: str(x) if x else ''}
```

### Step 4: Assign actual = pd.read_excel(...)

```python
actual = pd.read_excel(basename + read_ext, sheet_name='Sheet1', converters=converters)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```


## Complete Example

```python
# Setup
# Fixtures: read_ext

# Workflow
basename = 'test_converters'
expected = DataFrame.from_dict({'IntCol': [1, 2, -3, -1000, 0], 'FloatCol': [12.5, np.nan, 18.3, 19.2, 5e-09], 'BoolCol': ['Found', 'Found', 'Found', 'Not found', 'Found'], 'StrCol': ['1', np.nan, '3', '4', '5']})
converters = {'IntCol': lambda x: int(x) if x != '' else -1000, 'FloatCol': lambda x: 10 * x if x else np.nan, 2: lambda x: 'Found' if x != '' else 'Not found', 3: lambda x: str(x) if x else ''}
actual = pd.read_excel(basename + read_ext, sheet_name='Sheet1', converters=converters)
tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_readers.py:503 | Complexity: Intermediate | Last updated: 2026-06-02*