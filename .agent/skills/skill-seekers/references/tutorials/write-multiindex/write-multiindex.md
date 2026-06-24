# How To: Write Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write multiindex

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

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': [1, 2, 3]})
```

### Step 3: Assign index = pd.MultiIndex.from_tuples(...)

```python
index = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1)])
```

### Step 4: Assign df.index = index

```python
df.index = index
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
df = pd.DataFrame({'A': [1, 2, 3]})
index = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1)])
df.index = index
check_round_trip(df, engine)
```

## Next Steps


---

*Source: test_parquet.py:483 | Complexity: Intermediate | Last updated: 2026-06-02*