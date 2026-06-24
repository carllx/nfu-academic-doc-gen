# How To: Get Level Values Box Datetime64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get level values box datetime64

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign dates = date_range(...)

```python
dates = date_range('1/1/2000', periods=4)
```

**Verification:**
```python
assert isinstance(index.get_level_values(0)[0], Timestamp)
```

### Step 2: Assign levels = value

```python
levels = [dates, [0, 1]]
```

### Step 3: Assign codes = value

```python
codes = [[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]]
```

### Step 4: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=levels, codes=codes)
```

**Verification:**
```python
assert isinstance(index.get_level_values(0)[0], Timestamp)
```


## Complete Example

```python
# Workflow
dates = date_range('1/1/2000', periods=4)
levels = [dates, [0, 1]]
codes = [[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]]
index = MultiIndex(levels=levels, codes=codes)
assert isinstance(index.get_level_values(0)[0], Timestamp)
```

## Next Steps


---

*Source: test_get_level_values.py:15 | Complexity: Intermediate | Last updated: 2026-06-02*