# How To: Engine Used

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test engine used

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
# Fixtures: read_ext, engine, monkeypatch
```

## Step-by-Step Guide

### Step 1: Call monkeypatch.setattr()

```python
monkeypatch.setattr(pd.ExcelFile, 'parse', parser)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign expected_defaults = value

```python
expected_defaults = {'xlsx': 'openpyxl', 'xlsm': 'openpyxl', 'xlsb': 'pyxlsb', 'xls': 'xlrd', 'ods': 'odf'}
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = pd.read_excel(...)

```python
result = pd.read_excel(f)
```

### Step 4: Assign expected = engine

```python
expected = engine
```

### Step 5: Assign expected = value

```python
expected = expected_defaults[read_ext[1:]]
```


## Complete Example

```python
# Setup
# Fixtures: read_ext, engine, monkeypatch

# Workflow
def parser(self, *args, **kwargs):
    return self.engine
monkeypatch.setattr(pd.ExcelFile, 'parse', parser)
expected_defaults = {'xlsx': 'openpyxl', 'xlsm': 'openpyxl', 'xlsb': 'pyxlsb', 'xls': 'xlrd', 'ods': 'odf'}
with open('test1' + read_ext, 'rb') as f:
    result = pd.read_excel(f)
if engine is not None:
    expected = engine
else:
    expected = expected_defaults[read_ext[1:]]
assert result == expected
```

## Next Steps


---

*Source: test_readers.py:163 | Complexity: Intermediate | Last updated: 2026-06-02*