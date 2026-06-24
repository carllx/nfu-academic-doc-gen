# How To: Where Dt64 2D

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where dt64 2d

## Prerequisites

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=6)
```

### Step 2: Assign dta = dti._data.reshape(...)

```python
dta = dti._data.reshape(3, 2)
```

### Step 3: Assign other = value

```python
other = dta - dta[0, 0]
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(dta, columns=['A', 'B'])
```

### Step 5: Assign mask = np.asarray.copy(...)

```python
mask = np.asarray(df.isna()).copy()
```

### Step 6: Assign unknown = True

```python
mask[:, 1] = True
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': other[:, 0], 'B': dta[:, 1]})
```

### Step 8: Assign unknown = True

```python
mask[1, 0] = True
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': np.array([other[0, 0], dta[1, 0], other[2, 0]], dtype=object), 'B': dta[:, 1]})
```

### Step 10: Assign unknown = True

```python
mask[:] = True
```

### Step 11: Assign expected = df

```python
expected = df
```

### Step 12: Call _check_where_equivalences()

```python
_check_where_equivalences(df, mask, other, expected)
```

### Step 13: Call _check_where_equivalences()

```python
_check_where_equivalences(df, mask, other, expected)
```

### Step 14: Call _check_where_equivalences()

```python
_check_where_equivalences(df, mask, other, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=6)
dta = dti._data.reshape(3, 2)
other = dta - dta[0, 0]
df = DataFrame(dta, columns=['A', 'B'])
mask = np.asarray(df.isna()).copy()
mask[:, 1] = True
expected = DataFrame({'A': other[:, 0], 'B': dta[:, 1]})
with tm.assert_produces_warning(FutureWarning, match='Setting an item of incompatible dtype'):
    _check_where_equivalences(df, mask, other, expected)
mask[1, 0] = True
expected = DataFrame({'A': np.array([other[0, 0], dta[1, 0], other[2, 0]], dtype=object), 'B': dta[:, 1]})
with tm.assert_produces_warning(FutureWarning, match='Setting an item of incompatible dtype'):
    _check_where_equivalences(df, mask, other, expected)
mask[:] = True
expected = df
_check_where_equivalences(df, mask, other, expected)
```

## Next Steps


---

*Source: test_where.py:1040 | Complexity: Advanced | Last updated: 2026-06-02*