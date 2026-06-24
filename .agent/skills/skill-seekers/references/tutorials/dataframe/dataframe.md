# How To: Dataframe

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dataframe

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: data
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
NCOLS, NROWS = (10, 20)
```

**Verification:**
```python
assert df2.num_columns() == NCOLS
```

### Step 2: Assign data = value

```python
data = {f'col{int((i - NCOLS / 2) % NCOLS + 1)}': [data() for _ in range(NROWS)] for i in range(NCOLS)}
```

**Verification:**
```python
assert df2.num_rows() == NROWS
```

### Step 3: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(data)
```

**Verification:**
```python
assert list(df2.column_names()) == list(data.keys())
```

### Step 4: Assign df2 = df.__dataframe__(...)

```python
df2 = df.__dataframe__()
```

**Verification:**
```python
assert isinstance(result.attrs['_INTERCHANGE_PROTOCOL_BUFFERS'], list)
```

### Step 5: Assign indices = value

```python
indices = (0, 2)
```

**Verification:**
```python
assert isinstance(expected.attrs['_INTERCHANGE_PROTOCOL_BUFFERS'], list)
```

### Step 6: Assign names = tuple(...)

```python
names = tuple((list(data.keys())[idx] for idx in indices))
```

### Step 7: Assign result = from_dataframe(...)

```python
result = from_dataframe(df2.select_columns(indices))
```

### Step 8: Assign expected = from_dataframe(...)

```python
expected = from_dataframe(df2.select_columns_by_name(names))
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert isinstance(result.attrs['_INTERCHANGE_PROTOCOL_BUFFERS'], list)
```


## Complete Example

```python
# Setup
# Fixtures: data

# Workflow
NCOLS, NROWS = (10, 20)
data = {f'col{int((i - NCOLS / 2) % NCOLS + 1)}': [data() for _ in range(NROWS)] for i in range(NCOLS)}
df = pd.DataFrame(data)
df2 = df.__dataframe__()
assert df2.num_columns() == NCOLS
assert df2.num_rows() == NROWS
assert list(df2.column_names()) == list(data.keys())
indices = (0, 2)
names = tuple((list(data.keys())[idx] for idx in indices))
result = from_dataframe(df2.select_columns(indices))
expected = from_dataframe(df2.select_columns_by_name(names))
tm.assert_frame_equal(result, expected)
assert isinstance(result.attrs['_INTERCHANGE_PROTOCOL_BUFFERS'], list)
assert isinstance(expected.attrs['_INTERCHANGE_PROTOCOL_BUFFERS'], list)
```

## Next Steps


---

*Source: test_impl.py:150 | Complexity: Advanced | Last updated: 2026-06-02*