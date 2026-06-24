# How To: Info Memory Usage Bug On Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test info memory usage bug on multiindex

## Prerequisites

**Required Modules:**
- `io`
- `string`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign N = 100

```python
N = 100
```

**Verification:**
```python
assert s.values.nbytes == unstacked.values.nbytes
```

### Step 2: Assign M = len(...)

```python
M = len(ascii_uppercase)
```

**Verification:**
```python
assert s.memory_usage(deep=True) > unstacked.memory_usage(deep=True).sum()
```

### Step 3: Assign index = MultiIndex.from_product(...)

```python
index = MultiIndex.from_product([list(ascii_uppercase), date_range('20160101', periods=N)], names=['id', 'date'])
```

**Verification:**
```python
assert diff < 2000
```

### Step 4: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).standard_normal(N * M), index=index)
```

### Step 5: Assign unstacked = s.unstack(...)

```python
unstacked = s.unstack('id')
```

**Verification:**
```python
assert s.values.nbytes == unstacked.values.nbytes
```

### Step 6: Assign diff = value

```python
diff = unstacked.memory_usage(deep=True).sum() - s.memory_usage(deep=True)
```

**Verification:**
```python
assert diff < 2000
```


## Complete Example

```python
# Workflow
N = 100
M = len(ascii_uppercase)
index = MultiIndex.from_product([list(ascii_uppercase), date_range('20160101', periods=N)], names=['id', 'date'])
s = Series(np.random.default_rng(2).standard_normal(N * M), index=index)
unstacked = s.unstack('id')
assert s.values.nbytes == unstacked.values.nbytes
assert s.memory_usage(deep=True) > unstacked.memory_usage(deep=True).sum()
diff = unstacked.memory_usage(deep=True).sum() - s.memory_usage(deep=True)
assert diff < 2000
```

## Next Steps


---

*Source: test_info.py:175 | Complexity: Intermediate | Last updated: 2026-06-02*