# How To: Multiindex With Columns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex with columns

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

### Step 2: Assign dates = pd.date_range(...)

```python
dates = pd.date_range('01-Jan-2018', '01-Dec-2018', freq='MS')
```

### Step 3: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(np.random.default_rng(2).standard_normal((2 * len(dates), 3)), columns=list('ABC'))
```

### Step 4: Assign index1 = pd.MultiIndex.from_product(...)

```python
index1 = pd.MultiIndex.from_product([['Level1', 'Level2'], dates], names=['level', 'date'])
```

### Step 5: Assign index2 = index1.copy(...)

```python
index2 = index1.copy(names=None)
```

### Step 6: Assign df.index = index

```python
df.index = index
```

### Step 7: Call check_round_trip()

```python
check_round_trip(df, engine)
```

### Step 8: Call check_round_trip()

```python
check_round_trip(df, engine, read_kwargs={'columns': ['A', 'B']}, expected=df[['A', 'B']])
```


## Complete Example

```python
# Setup
# Fixtures: pa

# Workflow
engine = pa
dates = pd.date_range('01-Jan-2018', '01-Dec-2018', freq='MS')
df = pd.DataFrame(np.random.default_rng(2).standard_normal((2 * len(dates), 3)), columns=list('ABC'))
index1 = pd.MultiIndex.from_product([['Level1', 'Level2'], dates], names=['level', 'date'])
index2 = index1.copy(names=None)
for index in [index1, index2]:
    df.index = index
    check_round_trip(df, engine)
    check_round_trip(df, engine, read_kwargs={'columns': ['A', 'B']}, expected=df[['A', 'B']])
```

## Next Steps


---

*Source: test_parquet.py:492 | Complexity: Advanced | Last updated: 2026-06-02*