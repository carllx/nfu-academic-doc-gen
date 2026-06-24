# How To: Memory Usage Components Narrow Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test memory usage components narrow series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `sys`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign series = Series(...)

```python
series = Series(range(5), dtype=dtype, index=[f'i-{i}' for i in range(5)], name='a')
```

**Verification:**
```python
assert total_usage == non_index_usage + index_usage
```

### Step 2: Assign total_usage = series.memory_usage(...)

```python
total_usage = series.memory_usage(index=True)
```

### Step 3: Assign non_index_usage = series.memory_usage(...)

```python
non_index_usage = series.memory_usage(index=False)
```

### Step 4: Assign index_usage = series.index.memory_usage(...)

```python
index_usage = series.index.memory_usage()
```

**Verification:**
```python
assert total_usage == non_index_usage + index_usage
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
series = Series(range(5), dtype=dtype, index=[f'i-{i}' for i in range(5)], name='a')
total_usage = series.memory_usage(index=True)
non_index_usage = series.memory_usage(index=False)
index_usage = series.index.memory_usage()
assert total_usage == non_index_usage + index_usage
```

## Next Steps


---

*Source: test_misc.py:134 | Complexity: Intermediate | Last updated: 2026-06-02*