# How To: Orc Reader Empty

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test orc reader empty

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pyarrow`

**Setup Required:**
```python
# Fixtures: dirpath, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign columns = value

```python
columns = ['boolean1', 'byte1', 'short1', 'int1', 'long1', 'float1', 'double1', 'bytes1', 'string1']
```

### Step 2: Assign dtypes = value

```python
dtypes = ['bool', 'int8', 'int16', 'int32', 'int64', 'float32', 'float64', 'object', 'str' if using_infer_string else 'object']
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(index=pd.RangeIndex(0))
```

### Step 4: Assign expected.columns = expected.columns.astype(...)

```python
expected.columns = expected.columns.astype('str')
```

### Step 5: Assign inputfile = os.path.join(...)

```python
inputfile = os.path.join(dirpath, 'TestOrcFile.emptyFile.orc')
```

### Step 6: Assign got = read_orc(...)

```python
got = read_orc(inputfile, columns=columns)
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(expected, got)
```

### Step 8: Assign unknown = pd.Series(...)

```python
expected[colname] = pd.Series(dtype=dtype)
```


## Complete Example

```python
# Setup
# Fixtures: dirpath, using_infer_string

# Workflow
columns = ['boolean1', 'byte1', 'short1', 'int1', 'long1', 'float1', 'double1', 'bytes1', 'string1']
dtypes = ['bool', 'int8', 'int16', 'int32', 'int64', 'float32', 'float64', 'object', 'str' if using_infer_string else 'object']
expected = pd.DataFrame(index=pd.RangeIndex(0))
for colname, dtype in zip(columns, dtypes):
    expected[colname] = pd.Series(dtype=dtype)
expected.columns = expected.columns.astype('str')
inputfile = os.path.join(dirpath, 'TestOrcFile.emptyFile.orc')
got = read_orc(inputfile, columns=columns)
tm.assert_equal(expected, got)
```

## Next Steps


---

*Source: test_orc.py:45 | Complexity: Advanced | Last updated: 2026-06-02*