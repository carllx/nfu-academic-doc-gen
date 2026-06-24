# How To: Aggregate Item By Item

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test aggregate item by item

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`

**Setup Required:**
```python
# Fixtures: df
```

## Step-by-Step Guide

### Step 1: Assign grouped = df.groupby(...)

```python
grouped = df.groupby('A')
```

**Verification:**
```python
assert isinstance(result, DataFrame)
```

### Step 2: Assign aggfun_0 = value

```python
aggfun_0 = lambda ser: ser.size
```

**Verification:**
```python
assert len(result) == 0
```

### Step 3: Assign result = grouped.agg(...)

```python
result = grouped.agg(aggfun_0)
```

### Step 4: Assign foosum = unknown.sum(...)

```python
foosum = (df.A == 'foo').sum()
```

### Step 5: Assign barsum = unknown.sum(...)

```python
barsum = (df.A == 'bar').sum()
```

### Step 6: Assign K = len(...)

```python
K = len(result.columns)
```

### Step 7: Assign exp = Series(...)

```python
exp = Series(np.array([foosum] * K), index=list('BCD'), name='foo')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result.xs('foo'), exp)
```

### Step 9: Assign exp = Series(...)

```python
exp = Series(np.array([barsum] * K), index=list('BCD'), name='bar')
```

### Step 10: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result.xs('bar'), exp)
```

### Step 11: Assign result = DataFrame.groupby.agg(...)

```python
result = DataFrame().groupby(df.A).agg(aggfun_1)
```

**Verification:**
```python
assert isinstance(result, DataFrame)
```


## Complete Example

```python
# Setup
# Fixtures: df

# Workflow
grouped = df.groupby('A')
aggfun_0 = lambda ser: ser.size
result = grouped.agg(aggfun_0)
foosum = (df.A == 'foo').sum()
barsum = (df.A == 'bar').sum()
K = len(result.columns)
exp = Series(np.array([foosum] * K), index=list('BCD'), name='foo')
tm.assert_series_equal(result.xs('foo'), exp)
exp = Series(np.array([barsum] * K), index=list('BCD'), name='bar')
tm.assert_almost_equal(result.xs('bar'), exp)

def aggfun_1(ser):
    return ser.size
result = DataFrame().groupby(df.A).agg(aggfun_1)
assert isinstance(result, DataFrame)
assert len(result) == 0
```

## Next Steps


---

*Source: test_aggregate.py:312 | Complexity: Advanced | Last updated: 2026-06-02*