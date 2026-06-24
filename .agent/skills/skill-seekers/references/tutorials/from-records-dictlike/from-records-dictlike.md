# How To: From Records Dictlike

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from records dictlike

## Prerequisites

**Required Modules:**
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pytz`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': np.array(np.random.default_rng(2).standard_normal(6), dtype=np.float64), 'A1': np.array(np.random.default_rng(2).standard_normal(6), dtype=np.float64), 'B': np.array(np.arange(6), dtype=np.int64), 'C': ['foo'] * 6, 'D': np.array([True, False] * 3, dtype=bool), 'E': np.array(np.random.default_rng(2).standard_normal(6), dtype=np.float32), 'E1': np.array(np.random.default_rng(2).standard_normal(6), dtype=np.float32), 'F': np.array(np.arange(6), dtype=np.int32)})
```

### Step 2: Assign blocks = df._to_dict_of_blocks(...)

```python
blocks = df._to_dict_of_blocks()
```

### Step 3: Assign columns = value

```python
columns = []
```

### Step 4: Assign asdict = dict(...)

```python
asdict = dict(df.items())
```

### Step 5: Assign asdict2 = value

```python
asdict2 = {x: y.values for x, y in df.items()}
```

### Step 6: Assign results = value

```python
results = []
```

### Step 7: Call results.append()

```python
results.append(DataFrame.from_records(asdict).reindex(columns=df.columns))
```

### Step 8: Call results.append()

```python
results.append(DataFrame.from_records(asdict, columns=columns).reindex(columns=df.columns))
```

### Step 9: Call results.append()

```python
results.append(DataFrame.from_records(asdict2, columns=columns).reindex(columns=df.columns))
```

### Step 10: Call columns.extend()

```python
columns.extend(b.columns)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(r, df)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': np.array(np.random.default_rng(2).standard_normal(6), dtype=np.float64), 'A1': np.array(np.random.default_rng(2).standard_normal(6), dtype=np.float64), 'B': np.array(np.arange(6), dtype=np.int64), 'C': ['foo'] * 6, 'D': np.array([True, False] * 3, dtype=bool), 'E': np.array(np.random.default_rng(2).standard_normal(6), dtype=np.float32), 'E1': np.array(np.random.default_rng(2).standard_normal(6), dtype=np.float32), 'F': np.array(np.arange(6), dtype=np.int32)})
blocks = df._to_dict_of_blocks()
columns = []
for b in blocks.values():
    columns.extend(b.columns)
asdict = dict(df.items())
asdict2 = {x: y.values for x, y in df.items()}
results = []
results.append(DataFrame.from_records(asdict).reindex(columns=df.columns))
results.append(DataFrame.from_records(asdict, columns=columns).reindex(columns=df.columns))
results.append(DataFrame.from_records(asdict2, columns=columns).reindex(columns=df.columns))
for r in results:
    tm.assert_frame_equal(r, df)
```

## Next Steps


---

*Source: test_from_records.py:150 | Complexity: Advanced | Last updated: 2026-06-02*