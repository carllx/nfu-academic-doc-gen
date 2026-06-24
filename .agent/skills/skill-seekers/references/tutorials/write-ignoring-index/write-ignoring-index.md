# How To: Write Ignoring Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write ignoring index

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
# Fixtures: engine
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['q', 'r', 's']})
```

### Step 2: Assign write_kwargs = value

```python
write_kwargs = {'compression': None, 'index': False}
```

### Step 3: Assign expected = df.reset_index(...)

```python
expected = df.reset_index(drop=True)
```

### Step 4: Call check_round_trip()

```python
check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)
```

### Step 5: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['q', 'r', 's']}, index=['zyx', 'wvu', 'tsr'])
```

### Step 6: Call check_round_trip()

```python
check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)
```

### Step 7: Assign arrays = value

```python
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
```

### Step 8: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'one': list(range(8)), 'two': [-i for i in range(8)]}, index=arrays)
```

### Step 9: Assign expected = df.reset_index(...)

```python
expected = df.reset_index(drop=True)
```

### Step 10: Call check_round_trip()

```python
check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)
```


## Complete Example

```python
# Setup
# Fixtures: engine

# Workflow
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['q', 'r', 's']})
write_kwargs = {'compression': None, 'index': False}
expected = df.reset_index(drop=True)
check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['q', 'r', 's']}, index=['zyx', 'wvu', 'tsr'])
check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
df = pd.DataFrame({'one': list(range(8)), 'two': [-i for i in range(8)]}, index=arrays)
expected = df.reset_index(drop=True)
check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)
```

## Next Steps


---

*Source: test_parquet.py:511 | Complexity: Advanced | Last updated: 2026-06-02*