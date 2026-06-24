# How To: From Records Bad Index Column

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from records bad index column

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
df = DataFrame(np.random.default_rng(2).standard_normal((10, 3)), columns=['A', 'B', 'C'])
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df1.index, Index(df.C))
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df1.index, Index(df.C))
```

### Step 4: Assign msg = unknown.join(...)

```python
msg = '|'.join(["'None of \\[2\\] are in the columns'"])
```

### Step 5: Assign df1 = DataFrame.from_records(...)

```python
df1 = DataFrame.from_records(df, index=['C'])
```

### Step 6: Assign df1 = DataFrame.from_records(...)

```python
df1 = DataFrame.from_records(df, index='C')
```

### Step 7: Call DataFrame.from_records()

```python
DataFrame.from_records(df, index=[2])
```

### Step 8: Call DataFrame.from_records()

```python
DataFrame.from_records(df, index=2)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 3)), columns=['A', 'B', 'C'])
with tm.assert_produces_warning(FutureWarning):
    df1 = DataFrame.from_records(df, index=['C'])
tm.assert_index_equal(df1.index, Index(df.C))
with tm.assert_produces_warning(FutureWarning):
    df1 = DataFrame.from_records(df, index='C')
tm.assert_index_equal(df1.index, Index(df.C))
msg = '|'.join(["'None of \\[2\\] are in the columns'"])
with pytest.raises(KeyError, match=msg):
    with tm.assert_produces_warning(FutureWarning):
        DataFrame.from_records(df, index=[2])
with pytest.raises(KeyError, match=msg):
    with tm.assert_produces_warning(FutureWarning):
        DataFrame.from_records(df, index=2)
```

## Next Steps


---

*Source: test_from_records.py:206 | Complexity: Advanced | Last updated: 2026-06-02*