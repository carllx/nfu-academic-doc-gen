# How To: Get Handle Pyarrow Compat

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get handle pyarrow compat

## Prerequisites

**Required Modules:**
- `codecs`
- `errno`
- `functools`
- `io`
- `mmap`
- `os`
- `pathlib`
- `pickle`
- `tempfile`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `py.path`


## Step-by-Step Guide

### Step 1: Assign pa_csv = pytest.importorskip(...)

```python
pa_csv = pytest.importorskip('pyarrow.csv')
```

**Verification:**
```python
assert not s.closed
```

### Step 2: Assign data = 'a,b,c\n1,2,3\n©,®,®\nLook,a snake,🐍'

```python
data = 'a,b,c\n1,2,3\n©,®,®\nLook,a snake,🐍'
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': ['1', '©', 'Look'], 'b': ['2', '®', 'a snake'], 'c': ['3', '®', '🐍']})
```

### Step 4: Assign s = StringIO(...)

```python
s = StringIO(data)
```

### Step 5: Assign df = pa_csv.read_csv.to_pandas(...)

```python
df = pa_csv.read_csv(handles.handle).to_pandas()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

**Verification:**
```python
assert not s.closed
```

### Step 7: Assign expected = expected.astype(...)

```python
expected = expected.astype('object')
```


## Complete Example

```python
# Workflow
pa_csv = pytest.importorskip('pyarrow.csv')
data = 'a,b,c\n1,2,3\n©,®,®\nLook,a snake,🐍'
expected = pd.DataFrame({'a': ['1', '©', 'Look'], 'b': ['2', '®', 'a snake'], 'c': ['3', '®', '🐍']})
s = StringIO(data)
with icom.get_handle(s, 'rb', is_text=False) as handles:
    df = pa_csv.read_csv(handles.handle).to_pandas()
    if pa_version_under19p0:
        expected = expected.astype('object')
    tm.assert_frame_equal(df, expected)
    assert not s.closed
```

## Next Steps


---

*Source: test_common.py:156 | Complexity: Intermediate | Last updated: 2026-06-02*