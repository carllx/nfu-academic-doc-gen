# How To: Agg Period Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg period index

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.printing`
- `pandas.tests.extension.decimal.array`


## Step-by-Step Guide

### Step 1: Assign prng = period_range(...)

```python
prng = period_range('2012-1-1', freq='M', periods=3)
```

**Verification:**
```python
assert isinstance(rs.index, PeriodIndex)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((3, 2)), index=prng)
```

### Step 3: Assign rs = df.groupby.sum(...)

```python
rs = df.groupby(level=0).sum()
```

**Verification:**
```python
assert isinstance(rs.index, PeriodIndex)
```

### Step 4: Assign index = period_range(...)

```python
index = period_range(start='1999-01', periods=5, freq='M')
```

### Step 5: Assign s1 = Series(...)

```python
s1 = Series(np.random.default_rng(2).random(len(index)), index=index)
```

### Step 6: Assign s2 = Series(...)

```python
s2 = Series(np.random.default_rng(2).random(len(index)), index=index)
```

### Step 7: Assign df = DataFrame.from_dict(...)

```python
df = DataFrame.from_dict({'s1': s1, 's2': s2})
```

### Step 8: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(df.index.month)
```

### Step 9: Call list()

```python
list(grouped)
```


## Complete Example

```python
# Workflow
prng = period_range('2012-1-1', freq='M', periods=3)
df = DataFrame(np.random.default_rng(2).standard_normal((3, 2)), index=prng)
rs = df.groupby(level=0).sum()
assert isinstance(rs.index, PeriodIndex)
index = period_range(start='1999-01', periods=5, freq='M')
s1 = Series(np.random.default_rng(2).random(len(index)), index=index)
s2 = Series(np.random.default_rng(2).random(len(index)), index=index)
df = DataFrame.from_dict({'s1': s1, 's2': s2})
grouped = df.groupby(df.index.month)
list(grouped)
```

## Next Steps


---

*Source: test_other.py:88 | Complexity: Advanced | Last updated: 2026-06-02*