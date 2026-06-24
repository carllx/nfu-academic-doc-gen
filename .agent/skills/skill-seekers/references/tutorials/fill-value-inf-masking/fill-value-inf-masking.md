# How To: Fill Value Inf Masking

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fill value inf masking

## Prerequisites

**Required Modules:**
- `__future__`
- `collections`
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.tests.arithmetic.common`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': [0, 1, 2], 'B': [1.1, None, 1.1]})
```

### Step 2: Assign other = pd.DataFrame(...)

```python
other = pd.DataFrame({'A': [1.1, 1.2, 1.3]}, index=[0, 2, 3])
```

### Step 3: Assign result = df.rfloordiv(...)

```python
result = df.rfloordiv(other, fill_value=1)
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'A': [np.inf, 1.0, 0.0, 1.0], 'B': [0.0, np.nan, 0.0, np.nan]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'A': [0, 1, 2], 'B': [1.1, None, 1.1]})
other = pd.DataFrame({'A': [1.1, 1.2, 1.3]}, index=[0, 2, 3])
result = df.rfloordiv(other, fill_value=1)
expected = pd.DataFrame({'A': [np.inf, 1.0, 0.0, 1.0], 'B': [0.0, np.nan, 0.0, np.nan]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numeric.py:1467 | Complexity: Intermediate | Last updated: 2026-06-02*