# How To: Len

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test len

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
```

**Verification:**
```python
assert len(grouped) == len(df)
```

### Step 2: Assign grouped = df.groupby(...)

```python
grouped = df.groupby([lambda x: x.year, lambda x: x.month, lambda x: x.day])
```

**Verification:**
```python
assert len(grouped) == expected
```

### Step 3: Assign grouped = df.groupby(...)

```python
grouped = df.groupby([lambda x: x.year, lambda x: x.month])
```

### Step 4: Assign expected = len(...)

```python
expected = len({(x.year, x.month) for x in df.index})
```

**Verification:**
```python
assert len(grouped) == expected
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
grouped = df.groupby([lambda x: x.year, lambda x: x.month, lambda x: x.day])
assert len(grouped) == len(df)
grouped = df.groupby([lambda x: x.year, lambda x: x.month])
expected = len({(x.year, x.month) for x in df.index})
assert len(grouped) == expected
```

## Next Steps


---

*Source: test_groupby.py:319 | Complexity: Intermediate | Last updated: 2026-06-02*