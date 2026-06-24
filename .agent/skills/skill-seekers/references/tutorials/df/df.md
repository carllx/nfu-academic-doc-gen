# How To: Df

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: df

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dr = date_range(...)

```python
dr = date_range('2016-01-01', '2016-01-03', freq='12h')
```

### Step 2: Assign abc = value

```python
abc = ['a', 'b', 'c']
```

### Step 3: Assign mi = MultiIndex.from_product(...)

```python
mi = MultiIndex.from_product([dr, abc])
```

### Step 4: Assign frame = DataFrame(...)

```python
frame = DataFrame({'c1': range(15)}, index=mi)
```


## Complete Example

```python
# Workflow
dr = date_range('2016-01-01', '2016-01-03', freq='12h')
abc = ['a', 'b', 'c']
mi = MultiIndex.from_product([dr, abc])
frame = DataFrame({'c1': range(15)}, index=mi)
return frame
```

## Next Steps


---

*Source: test_partial_indexing.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*