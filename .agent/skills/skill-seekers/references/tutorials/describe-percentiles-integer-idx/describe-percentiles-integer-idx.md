# How To: Describe Percentiles Integer Idx

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe percentiles integer idx

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [1]})
```

### Step 2: Assign pct = np.linspace(...)

```python
pct = np.linspace(0, 1, 10 + 1)
```

### Step 3: Assign result = df.describe(...)

```python
result = df.describe(percentiles=pct)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'x': [1.0, 1.0, np.nan, 1.0, *(1.0 for _ in pct), 1.0]}, index=['count', 'mean', 'std', 'min', '0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%', 'max'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'x': [1]})
pct = np.linspace(0, 1, 10 + 1)
result = df.describe(percentiles=pct)
expected = DataFrame({'x': [1.0, 1.0, np.nan, 1.0, *(1.0 for _ in pct), 1.0]}, index=['count', 'mean', 'std', 'min', '0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%', 'max'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:328 | Complexity: Intermediate | Last updated: 2026-06-02*