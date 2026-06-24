# How To: To Records Timeseries

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to records timeseries

## Prerequisites

**Required Modules:**
- `collections`
- `email`
- `email.parser`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = date_range(...)

```python
index = date_range('1/1/2000', periods=10)
```

**Verification:**
```python
assert result['index'].dtype == 'M8[ns]'
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 3)), index=index, columns=['a', 'b', 'c'])
```

### Step 3: Assign result = df.to_records(...)

```python
result = df.to_records()
```

**Verification:**
```python
assert result['index'].dtype == 'M8[ns]'
```

### Step 4: Assign result = df.to_records(...)

```python
result = df.to_records(index=False)
```


## Complete Example

```python
# Workflow
index = date_range('1/1/2000', periods=10)
df = DataFrame(np.random.default_rng(2).standard_normal((10, 3)), index=index, columns=['a', 'b', 'c'])
result = df.to_records()
assert result['index'].dtype == 'M8[ns]'
result = df.to_records(index=False)
```

## Next Steps


---

*Source: test_to_records.py:20 | Complexity: Intermediate | Last updated: 2026-06-02*