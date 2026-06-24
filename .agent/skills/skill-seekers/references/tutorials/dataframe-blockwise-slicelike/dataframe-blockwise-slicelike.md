# How To: Dataframe Blockwise Slicelike

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe blockwise slicelike

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `enum`
- `functools`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation`
- `pandas.tests.frame.common`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.integers(...)

```python
arr = np.random.default_rng(2).integers(0, 1000, (100, 10))
```

### Step 2: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(arr)
```

### Step 3: Assign df2 = df1.copy.astype(...)

```python
df2 = df1.copy().astype({1: 'float', 3: 'float', 7: 'float'})
```

### Step 4: Assign unknown = value

```python
df2.iloc[0, [1, 3, 7]] = np.nan
```

### Step 5: Assign df3 = df1.copy.astype(...)

```python
df3 = df1.copy().astype({5: 'float'})
```

### Step 6: Assign unknown = value

```python
df3.iloc[0, [5]] = np.nan
```

### Step 7: Assign df4 = df1.copy.astype(...)

```python
df4 = df1.copy().astype({2: 'float', 3: 'float', 4: 'float'})
```

### Step 8: Assign unknown = value

```python
df4.iloc[0, np.arange(2, 5)] = np.nan
```

### Step 9: Assign df5 = df1.copy.astype(...)

```python
df5 = df1.copy().astype({4: 'float', 5: 'float', 6: 'float'})
```

### Step 10: Assign unknown = value

```python
df5.iloc[0, np.arange(4, 7)] = np.nan
```

### Step 11: Assign res = value

```python
res = left + right
```

### Step 12: Assign expected = DataFrame(...)

```python
expected = DataFrame({i: left[i] + right[i] for i in left.columns})
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).integers(0, 1000, (100, 10))
df1 = DataFrame(arr)
df2 = df1.copy().astype({1: 'float', 3: 'float', 7: 'float'})
df2.iloc[0, [1, 3, 7]] = np.nan
df3 = df1.copy().astype({5: 'float'})
df3.iloc[0, [5]] = np.nan
df4 = df1.copy().astype({2: 'float', 3: 'float', 4: 'float'})
df4.iloc[0, np.arange(2, 5)] = np.nan
df5 = df1.copy().astype({4: 'float', 5: 'float', 6: 'float'})
df5.iloc[0, np.arange(4, 7)] = np.nan
for left, right in [(df1, df2), (df2, df3), (df4, df5)]:
    res = left + right
    expected = DataFrame({i: left[i] + right[i] for i in left.columns})
    tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:1957 | Complexity: Advanced | Last updated: 2026-06-02*