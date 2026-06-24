# How To: Cython Agg Nullable Int

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cython agg nullable int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: op_name
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['A', 'B'] * 5, 'B': pd.array([1, 2, 3, 4, 5, 6, 7, 8, 9, pd.NA], dtype='Int64')})
```

### Step 2: Assign result = getattr(...)

```python
result = getattr(df.groupby('A')['B'], op_name)()
```

### Step 3: Assign df2 = df.assign(...)

```python
df2 = df.assign(B=df['B'].astype('float64'))
```

### Step 4: Assign expected = getattr(...)

```python
expected = getattr(df2.groupby('A')['B'], op_name)()
```

### Step 5: Assign expected = expected.convert_dtypes(...)

```python
expected = expected.convert_dtypes(convert_integer=convert_integer)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign convert_integer = False

```python
convert_integer = False
```

### Step 8: Assign convert_integer = True

```python
convert_integer = True
```


## Complete Example

```python
# Setup
# Fixtures: op_name

# Workflow
df = DataFrame({'A': ['A', 'B'] * 5, 'B': pd.array([1, 2, 3, 4, 5, 6, 7, 8, 9, pd.NA], dtype='Int64')})
result = getattr(df.groupby('A')['B'], op_name)()
df2 = df.assign(B=df['B'].astype('float64'))
expected = getattr(df2.groupby('A')['B'], op_name)()
if op_name in ('mean', 'median'):
    convert_integer = False
else:
    convert_integer = True
expected = expected.convert_dtypes(convert_integer=convert_integer)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_cython.py:335 | Complexity: Advanced | Last updated: 2026-06-02*