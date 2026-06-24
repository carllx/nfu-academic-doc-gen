# How To: Loc Getitem Multiindex Tuple Level

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc getitem multiindex tuple level

## Prerequisites

**Required Modules:**
- `collections`
- `contextlib`
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.indexing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign lev1 = value

```python
lev1 = ['a', 'b', 'c']
```

**Verification:**
```python
assert result2 == 6
```

### Step 2: Assign lev2 = value

```python
lev2 = [(0, 1), (1, 0)]
```

### Step 3: Assign lev3 = value

```python
lev3 = [0, 1]
```

### Step 4: Assign cols = MultiIndex.from_product(...)

```python
cols = MultiIndex.from_product([lev1, lev2, lev3], names=['x', 'y', 'z'])
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(6, index=range(5), columns=cols)
```

### Step 6: Assign result = value

```python
result = df.loc[:, (lev1[0], lev2[0], lev3[0])]
```

### Step 7: Assign expected = value

```python
expected = df.iloc[:, :1]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign alt = df.xs(...)

```python
alt = df.xs((lev1[0], lev2[0], lev3[0]), level=[0, 1, 2], axis=1)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(alt, expected)
```

### Step 11: Assign ser = value

```python
ser = df.iloc[0]
```

### Step 12: Assign expected2 = value

```python
expected2 = ser.iloc[:1]
```

### Step 13: Assign alt2 = ser.xs(...)

```python
alt2 = ser.xs((lev1[0], lev2[0], lev3[0]), level=[0, 1, 2], axis=0)
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(alt2, expected2)
```

### Step 15: Assign result2 = value

```python
result2 = ser.loc[lev1[0], lev2[0], lev3[0]]
```

**Verification:**
```python
assert result2 == 6
```


## Complete Example

```python
# Workflow
lev1 = ['a', 'b', 'c']
lev2 = [(0, 1), (1, 0)]
lev3 = [0, 1]
cols = MultiIndex.from_product([lev1, lev2, lev3], names=['x', 'y', 'z'])
df = DataFrame(6, index=range(5), columns=cols)
result = df.loc[:, (lev1[0], lev2[0], lev3[0])]
expected = df.iloc[:, :1]
tm.assert_frame_equal(result, expected)
alt = df.xs((lev1[0], lev2[0], lev3[0]), level=[0, 1, 2], axis=1)
tm.assert_frame_equal(alt, expected)
ser = df.iloc[0]
expected2 = ser.iloc[:1]
alt2 = ser.xs((lev1[0], lev2[0], lev3[0]), level=[0, 1, 2], axis=0)
tm.assert_series_equal(alt2, expected2)
result2 = ser.loc[lev1[0], lev2[0], lev3[0]]
assert result2 == 6
```

## Next Steps


---

*Source: test_loc.py:3008 | Complexity: Advanced | Last updated: 2026-06-02*