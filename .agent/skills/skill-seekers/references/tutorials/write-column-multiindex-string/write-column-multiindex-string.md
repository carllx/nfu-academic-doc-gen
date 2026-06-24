# How To: Write Column Multiindex String

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write column multiindex string

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
# Fixtures: pa
```

## Step-by-Step Guide

### Step 1: Assign engine = pa

```python
engine = pa
```

### Step 2: Assign arrays = value

```python
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
```

### Step 3: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(np.random.default_rng(2).standard_normal((8, 8)), columns=arrays)
```

### Step 4: Assign df.columns.names = value

```python
df.columns.names = ['ColLevel1', 'ColLevel2']
```

### Step 5: Call check_round_trip()

```python
check_round_trip(df, engine)
```


## Complete Example

```python
# Setup
# Fixtures: pa

# Workflow
engine = pa
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
df = pd.DataFrame(np.random.default_rng(2).standard_normal((8, 8)), columns=arrays)
df.columns.names = ['ColLevel1', 'ColLevel2']
check_round_trip(df, engine)
```

## Next Steps


---

*Source: test_parquet.py:574 | Complexity: Intermediate | Last updated: 2026-06-02*