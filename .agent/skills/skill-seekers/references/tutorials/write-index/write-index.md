# How To: Write Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write index

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

### Step 1: Assign check_names = value

```python
check_names = engine != 'fastparquet'
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': [1, 2, 3]})
```

### Step 3: Call check_round_trip()

```python
check_round_trip(df, engine)
```

### Step 4: Assign indexes = value

```python
indexes = [[2, 3, 4], pd.date_range('20130101', periods=3), list('abc'), [1, 3, 4]]
```

### Step 5: Assign df.index = value

```python
df.index = [0, 1, 2]
```

### Step 6: Assign df.index.name = 'foo'

```python
df.index.name = 'foo'
```

### Step 7: Call check_round_trip()

```python
check_round_trip(df, engine)
```

### Step 8: Assign df.index = index

```python
df.index = index
```

### Step 9: Call check_round_trip()

```python
check_round_trip(df, engine, check_names=check_names)
```

### Step 10: Assign df.index = df.index._with_freq(...)

```python
df.index = df.index._with_freq(None)
```


## Complete Example

```python
# Setup
# Fixtures: engine

# Workflow
check_names = engine != 'fastparquet'
df = pd.DataFrame({'A': [1, 2, 3]})
check_round_trip(df, engine)
indexes = [[2, 3, 4], pd.date_range('20130101', periods=3), list('abc'), [1, 3, 4]]
for index in indexes:
    df.index = index
    if isinstance(index, pd.DatetimeIndex):
        df.index = df.index._with_freq(None)
    check_round_trip(df, engine, check_names=check_names)
df.index = [0, 1, 2]
df.index.name = 'foo'
check_round_trip(df, engine)
```

## Next Steps


---

*Source: test_parquet.py:459 | Complexity: Advanced | Last updated: 2026-06-02*