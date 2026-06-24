# How To: Operators Combine

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test operators combine

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.core.computation.check`

**Setup Required:**
```python
# Fixtures: op, equiv_op, fv
```

## Step-by-Step Guide

### Step 1: Assign a = Series(...)

```python
a = Series([np.nan, 1.0, 2.0, 3.0, np.nan], index=np.arange(5))
```

### Step 2: Assign b = Series(...)

```python
b = Series([np.nan, 1, np.nan, 3, np.nan, 4.0], index=np.arange(6))
```

### Step 3: Assign result = op(...)

```python
result = op(a, b)
```

### Step 4: Assign exp = equiv_op(...)

```python
exp = equiv_op(a, b)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 6: Call _check_fill()

```python
_check_fill(op, equiv_op, a, b, fill_value=fv)
```

### Step 7: Call op()

```python
op(a, b, axis=0)
```

### Step 8: Assign exp_index = a.index.union(...)

```python
exp_index = a.index.union(b.index)
```

### Step 9: Assign a = a.reindex(...)

```python
a = a.reindex(exp_index)
```

### Step 10: Assign b = b.reindex(...)

```python
b = b.reindex(exp_index)
```

### Step 11: Assign amask = isna(...)

```python
amask = isna(a)
```

### Step 12: Assign bmask = isna(...)

```python
bmask = isna(b)
```

### Step 13: Assign exp_values = value

```python
exp_values = []
```

### Step 14: Assign result = meth(...)

```python
result = meth(a, b, fill_value=fill_value)
```

### Step 15: Assign expected = Series(...)

```python
expected = Series(exp_values, exp_index)
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 17: Call exp_values.append()

```python
exp_values.append(op(fill_value, b[i]))
```

### Step 18: Call exp_values.append()

```python
exp_values.append(np.nan)
```

### Step 19: Call exp_values.append()

```python
exp_values.append(op(a[i], fill_value))
```

### Step 20: Call exp_values.append()

```python
exp_values.append(op(a[i], b[i]))
```

### Step 21: Call exp_values.append()

```python
exp_values.append(np.nan)
```


## Complete Example

```python
# Setup
# Fixtures: op, equiv_op, fv

# Workflow
def _check_fill(meth, op, a, b, fill_value=0):
    exp_index = a.index.union(b.index)
    a = a.reindex(exp_index)
    b = b.reindex(exp_index)
    amask = isna(a)
    bmask = isna(b)
    exp_values = []
    for i in range(len(exp_index)):
        with np.errstate(all='ignore'):
            if amask[i]:
                if bmask[i]:
                    exp_values.append(np.nan)
                    continue
                exp_values.append(op(fill_value, b[i]))
            elif bmask[i]:
                if amask[i]:
                    exp_values.append(np.nan)
                    continue
                exp_values.append(op(a[i], fill_value))
            else:
                exp_values.append(op(a[i], b[i]))
    result = meth(a, b, fill_value=fill_value)
    expected = Series(exp_values, exp_index)
    tm.assert_series_equal(result, expected)
a = Series([np.nan, 1.0, 2.0, 3.0, np.nan], index=np.arange(5))
b = Series([np.nan, 1, np.nan, 3, np.nan, 4.0], index=np.arange(6))
result = op(a, b)
exp = equiv_op(a, b)
tm.assert_series_equal(result, exp)
_check_fill(op, equiv_op, a, b, fill_value=fv)
op(a, b, axis=0)
```

## Next Steps


---

*Source: test_arithmetic.py:120 | Complexity: Advanced | Last updated: 2026-06-02*