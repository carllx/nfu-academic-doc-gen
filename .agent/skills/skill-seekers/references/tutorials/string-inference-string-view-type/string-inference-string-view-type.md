# How To: String Inference String View Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test string inference string view type

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas`
- `pandas._testing`
- `pandas.io.feather_format`
- `pyarrow`
- `pyarrow`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign path = value

```python
path = tmp_path / 'string_view.parquet'
```

### Step 2: Assign table = pa.table(...)

```python
table = pa.table({'a': pa.array([None, 'b', 'c'], pa.string_view())})
```

### Step 3: Call feather.write_feather()

```python
feather.write_feather(table, path)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = read_feather(...)

```python
result = read_feather(path)
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(data={'a': [None, 'b', 'c']}, dtype=pd.StringDtype(na_value=np.nan))
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
import pyarrow as pa
from pyarrow import feather
path = tmp_path / 'string_view.parquet'
table = pa.table({'a': pa.array([None, 'b', 'c'], pa.string_view())})
feather.write_feather(table, path)
with pd.option_context('future.infer_string', True):
    result = read_feather(path)
    expected = pd.DataFrame(data={'a': [None, 'b', 'c']}, dtype=pd.StringDtype(na_value=np.nan))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_feather.py:271 | Complexity: Intermediate | Last updated: 2026-06-02*