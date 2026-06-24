# How To: Non Categorical Value Label Convert Categoricals Error

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non categorical value label convert categoricals error

## Prerequisites

**Required Modules:**
- `bz2`
- `datetime`
- `datetime`
- `gzip`
- `io`
- `os`
- `struct`
- `tarfile`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.frame`
- `pandas.io.parsers`
- `pandas.io.stata`


## Step-by-Step Guide

### Step 1: Assign value_labels = value

```python
value_labels = {'repeated_labels': {10: 'Ten', 20: 'More than ten', 40: 'More than ten'}}
```

**Verification:**
```python
assert reader_value_labels == value_labels
```

### Step 2: Assign data = DataFrame(...)

```python
data = DataFrame({'repeated_labels': [10, 10, 20, 20, 40, 40]})
```

### Step 3: Call data.to_stata()

```python
data.to_stata(path, value_labels=value_labels)
```

**Verification:**
```python
assert reader_value_labels == value_labels
```

### Step 4: Assign col = 'repeated_labels'

```python
col = 'repeated_labels'
```

### Step 5: Assign repeats = value

```python
repeats = '-' * 80 + '\n' + '\n'.join(['More than ten'])
```

### Step 6: Assign msg = value

```python
msg = f'\nValue labels for column {col} are not unique. These cannot be converted to\npandas categoricals.\n\nEither read the file with `convert_categoricals` set to False or use the\nlow level interface in `StataReader` to separately read the values and the\nvalue_labels.\n\nThe repeated labels are:\n{repeats}\n'
```

### Step 7: Assign reader_value_labels = reader.value_labels(...)

```python
reader_value_labels = reader.value_labels()
```

### Step 8: Call read_stata()

```python
read_stata(path, convert_categoricals=True)
```


## Complete Example

```python
# Workflow
value_labels = {'repeated_labels': {10: 'Ten', 20: 'More than ten', 40: 'More than ten'}}
data = DataFrame({'repeated_labels': [10, 10, 20, 20, 40, 40]})
with tm.ensure_clean() as path:
    data.to_stata(path, value_labels=value_labels)
    with StataReader(path, convert_categoricals=False) as reader:
        reader_value_labels = reader.value_labels()
    assert reader_value_labels == value_labels
    col = 'repeated_labels'
    repeats = '-' * 80 + '\n' + '\n'.join(['More than ten'])
    msg = f'\nValue labels for column {col} are not unique. These cannot be converted to\npandas categoricals.\n\nEither read the file with `convert_categoricals` set to False or use the\nlow level interface in `StataReader` to separately read the values and the\nvalue_labels.\n\nThe repeated labels are:\n{repeats}\n'
    with pytest.raises(ValueError, match=msg):
        read_stata(path, convert_categoricals=True)
```

## Next Steps


---

*Source: test_stata.py:2303 | Complexity: Advanced | Last updated: 2026-06-02*