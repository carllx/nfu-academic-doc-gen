# How To: Corrwith Mixed Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test corrwith mixed dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: numeric_only
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 4, 3, 2], 'b': [4, 6, 7, 3], 'c': ['a', 'b', 'c', 'd']})
```

### Step 2: Assign s = Series(...)

```python
s = Series([0, 6, 7, 3])
```

### Step 3: Assign result = df.corrwith(...)

```python
result = df.corrwith(s, numeric_only=numeric_only)
```

### Step 4: Assign corrs = value

```python
corrs = [df['a'].corr(s), df['b'].corr(s)]
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(data=corrs, index=['a', 'b'])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Call df.corrwith()

```python
df.corrwith(s, numeric_only=numeric_only)
```


## Complete Example

```python
# Setup
# Fixtures: numeric_only

# Workflow
df = DataFrame({'a': [1, 4, 3, 2], 'b': [4, 6, 7, 3], 'c': ['a', 'b', 'c', 'd']})
s = Series([0, 6, 7, 3])
if numeric_only:
    result = df.corrwith(s, numeric_only=numeric_only)
    corrs = [df['a'].corr(s), df['b'].corr(s)]
    expected = Series(data=corrs, index=['a', 'b'])
    tm.assert_series_equal(result, expected)
else:
    with pytest.raises(ValueError, match='could not convert string to float'):
        df.corrwith(s, numeric_only=numeric_only)
```

## Next Steps


---

*Source: test_cov_corr.py:374 | Complexity: Intermediate | Last updated: 2026-06-02*