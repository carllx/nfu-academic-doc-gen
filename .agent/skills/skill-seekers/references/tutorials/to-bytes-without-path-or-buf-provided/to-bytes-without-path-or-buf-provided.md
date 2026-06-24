# How To: To Bytes Without Path Or Buf Provided

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to bytes without path or buf provided

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
- `pandas._config`
- `pandas._config.config`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `pandas.io.parquet`
- `pyarrow`
- `fastparquet`
- `pyarrow.dataset`
- `pandas.compat._optional`
- `pyarrow`
- `pyarrow`
- `pyarrow`
- `pyarrow`
- `pyarrow`
- `pyarrow.parquet`
- `fastparquet`
- `fastparquet`
- `fastparquet`
- `fastparquet`
- `fastparquet`
- `pytz`

**Setup Required:**
```python
# Fixtures: pa, df_full
```

## Step-by-Step Guide

### Step 1: Assign buf_bytes = df_full.to_parquet(...)

```python
buf_bytes = df_full.to_parquet(engine=pa)
```

**Verification:**
```python
assert isinstance(buf_bytes, bytes)
```

### Step 2: Assign buf_stream = BytesIO(...)

```python
buf_stream = BytesIO(buf_bytes)
```

### Step 3: Assign res = read_parquet(...)

```python
res = read_parquet(buf_stream)
```

### Step 4: Assign expected = df_full.copy(...)

```python
expected = df_full.copy()
```

### Step 5: Assign unknown = None

```python
expected.loc[1, 'string_with_nan'] = None
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```


## Complete Example

```python
# Setup
# Fixtures: pa, df_full

# Workflow
buf_bytes = df_full.to_parquet(engine=pa)
assert isinstance(buf_bytes, bytes)
buf_stream = BytesIO(buf_bytes)
res = read_parquet(buf_stream)
expected = df_full.copy()
expected.loc[1, 'string_with_nan'] = None
tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_parquet.py:740 | Complexity: Intermediate | Last updated: 2026-06-02*