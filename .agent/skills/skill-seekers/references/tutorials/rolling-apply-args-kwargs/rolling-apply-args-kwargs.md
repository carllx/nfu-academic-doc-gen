# How To: Rolling Apply Args Kwargs

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rolling apply args kwargs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: args_kwargs
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'gr': [1, 1], 'a': [1, 2]})
```

### Step 2: Assign idx = Index(...)

```python
idx = Index(['gr', 'a'])
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[11.0, 11.0], [11.0, 12.0]], columns=idx)
```

### Step 4: Assign result = df.rolling.apply(...)

```python
result = df.rolling(1).apply(numpysum, args=args_kwargs[0], kwargs=args_kwargs[1])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign midx = MultiIndex.from_tuples(...)

```python
midx = MultiIndex.from_tuples([(1, 0), (1, 1)], names=['gr', None])
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([11.0, 12.0], index=midx, name='a')
```

### Step 8: Assign gb_rolling = unknown.rolling(...)

```python
gb_rolling = df.groupby('gr')['a'].rolling(1)
```

### Step 9: Assign result = gb_rolling.apply(...)

```python
result = gb_rolling.apply(numpysum, args=args_kwargs[0], kwargs=args_kwargs[1])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: args_kwargs

# Workflow
def numpysum(x, par):
    return np.sum(x + par)
df = DataFrame({'gr': [1, 1], 'a': [1, 2]})
idx = Index(['gr', 'a'])
expected = DataFrame([[11.0, 11.0], [11.0, 12.0]], columns=idx)
result = df.rolling(1).apply(numpysum, args=args_kwargs[0], kwargs=args_kwargs[1])
tm.assert_frame_equal(result, expected)
midx = MultiIndex.from_tuples([(1, 0), (1, 1)], names=['gr', None])
expected = Series([11.0, 12.0], index=midx, name='a')
gb_rolling = df.groupby('gr')['a'].rolling(1)
result = gb_rolling.apply(numpysum, args=args_kwargs[0], kwargs=args_kwargs[1])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_apply.py:163 | Complexity: Advanced | Last updated: 2026-06-02*