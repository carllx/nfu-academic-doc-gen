# How To: Engine Kwargs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test engine kwargs

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
# Fixtures: read_ext, engine
```

## Step-by-Step Guide

### Step 1: Assign expected_defaults = value

```python
expected_defaults = {'xlsx': {'foo': 'abcd'}, 'xlsm': {'foo': 123}, 'xlsb': {'foo': 'True'}, 'xls': {'foo': True}, 'ods': {'foo': 'abcd'}}
```

### Step 2: Assign msg = re.escape(...)

```python
msg = re.escape("open_workbook() got an unexpected keyword argument 'foo'")
```

### Step 3: Assign msg = re.escape(...)

```python
msg = re.escape("load() got an unexpected keyword argument 'foo'")
```

### Step 4: Assign msg = re.escape(...)

```python
msg = re.escape("load_workbook() got an unexpected keyword argument 'foo'")
```

### Step 5: Call pd.read_excel()

```python
pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0, engine_kwargs=expected_defaults[read_ext[1:]])
```


## Complete Example

```python
# Setup
# Fixtures: read_ext, engine

# Workflow
expected_defaults = {'xlsx': {'foo': 'abcd'}, 'xlsm': {'foo': 123}, 'xlsb': {'foo': 'True'}, 'xls': {'foo': True}, 'ods': {'foo': 'abcd'}}
if engine in {'xlrd', 'pyxlsb'}:
    msg = re.escape("open_workbook() got an unexpected keyword argument 'foo'")
elif engine == 'odf':
    msg = re.escape("load() got an unexpected keyword argument 'foo'")
else:
    msg = re.escape("load_workbook() got an unexpected keyword argument 'foo'")
if engine is not None:
    with pytest.raises(TypeError, match=msg):
        pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0, engine_kwargs=expected_defaults[read_ext[1:]])
```

## Next Steps


---

*Source: test_readers.py:187 | Complexity: Intermediate | Last updated: 2026-06-02*