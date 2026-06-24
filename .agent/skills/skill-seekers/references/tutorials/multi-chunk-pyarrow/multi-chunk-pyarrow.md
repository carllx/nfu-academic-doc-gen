# How To: Multi Chunk Pyarrow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multi chunk pyarrow

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.core.interchange.column`
- `pandas.core.interchange.dataframe_protocol`
- `pandas.core.interchange.from_dataframe`
- `pandas.core.interchange.utils`
- `pyarrow.interchange`
- `pyarrow.compute`
- `pyarrow.interchange`
- `pyarrow.interchange`


## Step-by-Step Guide

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow', '11.0.0')
```

### Step 2: Assign n_legs = pa.chunked_array(...)

```python
n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
```

### Step 3: Assign names = value

```python
names = ['n_legs']
```

### Step 4: Assign table = pa.table(...)

```python
table = pa.table([n_legs], names=names)
```

### Step 5: Call pd.api.interchange.from_dataframe()

```python
pd.api.interchange.from_dataframe(table, allow_copy=False)
```


## Complete Example

```python
# Workflow
pa = pytest.importorskip('pyarrow', '11.0.0')
n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
names = ['n_legs']
table = pa.table([n_legs], names=names)
with pytest.raises(RuntimeError, match='Cannot do zero copy conversion into multi-column DataFrame block'):
    pd.api.interchange.from_dataframe(table, allow_copy=False)
```

## Next Steps


---

*Source: test_impl.py:294 | Complexity: Intermediate | Last updated: 2026-06-02*