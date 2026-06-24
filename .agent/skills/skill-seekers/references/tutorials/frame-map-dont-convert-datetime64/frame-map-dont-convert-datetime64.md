# How To: Frame Map Dont Convert Datetime64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame map dont convert datetime64

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'x1': [datetime(1996, 1, 1)]})
```

**Verification:**
```python
assert result == 'M8[ns]'
```

### Step 2: Assign df = df.map(...)

```python
df = df.map(lambda x: x + BDay())
```

### Step 3: Assign df = df.map(...)

```python
df = df.map(lambda x: x + BDay())
```

### Step 4: Assign result = value

```python
result = df.x1.dtype
```

**Verification:**
```python
assert result == 'M8[ns]'
```


## Complete Example

```python
# Workflow
df = DataFrame({'x1': [datetime(1996, 1, 1)]})
df = df.map(lambda x: x + BDay())
df = df.map(lambda x: x + BDay())
result = df.x1.dtype
assert result == 'M8[ns]'
```

## Next Steps


---

*Source: test_map.py:162 | Complexity: Intermediate | Last updated: 2026-06-02*