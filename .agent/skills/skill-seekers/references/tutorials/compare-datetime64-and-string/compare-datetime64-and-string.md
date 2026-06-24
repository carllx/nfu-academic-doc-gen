# How To: Compare Datetime64 And String

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare datetime64 and string

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [{'a': '2015-07-01', 'b': '08335394550'}, {'a': '2015-07-02', 'b': '+49 (0) 0345 300033'}, {'a': '2015-07-03', 'b': '+49(0)2598 04457'}, {'a': '2015-07-04', 'b': '0741470003'}, {'a': '2015-07-05', 'b': '04181 83668'}]
```

### Step 2: Assign dtypes = value

```python
dtypes = {'a': 'datetime64[ns]', 'b': 'string'}
```

### Step 3: Assign df = pd.DataFrame.astype(...)

```python
df = pd.DataFrame(data=data).astype(dtypes)
```

### Step 4: Assign result_eq1 = unknown.eq(...)

```python
result_eq1 = df['a'].eq(df['b'])
```

### Step 5: Assign result_eq2 = value

```python
result_eq2 = df['a'] == df['b']
```

### Step 6: Assign result_neq = value

```python
result_neq = df['a'] != df['b']
```

### Step 7: Assign expected_eq = pd.Series(...)

```python
expected_eq = pd.Series([False] * 5)
```

### Step 8: Assign expected_neq = pd.Series(...)

```python
expected_neq = pd.Series([True] * 5)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_eq1, expected_eq)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_eq2, expected_eq)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_neq, expected_neq)
```


## Complete Example

```python
# Workflow
data = [{'a': '2015-07-01', 'b': '08335394550'}, {'a': '2015-07-02', 'b': '+49 (0) 0345 300033'}, {'a': '2015-07-03', 'b': '+49(0)2598 04457'}, {'a': '2015-07-04', 'b': '0741470003'}, {'a': '2015-07-05', 'b': '04181 83668'}]
dtypes = {'a': 'datetime64[ns]', 'b': 'string'}
df = pd.DataFrame(data=data).astype(dtypes)
result_eq1 = df['a'].eq(df['b'])
result_eq2 = df['a'] == df['b']
result_neq = df['a'] != df['b']
expected_eq = pd.Series([False] * 5)
expected_neq = pd.Series([True] * 5)
tm.assert_series_equal(result_eq1, expected_eq)
tm.assert_series_equal(result_eq2, expected_eq)
tm.assert_series_equal(result_neq, expected_neq)
```

## Next Steps


---

*Source: test_compare.py:119 | Complexity: Advanced | Last updated: 2026-06-02*