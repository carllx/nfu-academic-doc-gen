# How To: Cython Group Mean Wrong Min Count

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cython group mean wrong min count

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.groupby`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign actual = np.zeros(...)

```python
actual = np.zeros(shape=(1, 1), dtype='float64')
```

### Step 2: Assign counts = np.zeros(...)

```python
counts = np.zeros(1, dtype='int64')
```

### Step 3: Assign data = value

```python
data = np.zeros(1, dtype='float64')[:, None]
```

### Step 4: Assign labels = np.zeros(...)

```python
labels = np.zeros(1, dtype=np.intp)
```

### Step 5: Call group_mean()

```python
group_mean(actual, counts, data, labels, is_datetimelike=True, min_count=0)
```


## Complete Example

```python
# Workflow
actual = np.zeros(shape=(1, 1), dtype='float64')
counts = np.zeros(1, dtype='int64')
data = np.zeros(1, dtype='float64')[:, None]
labels = np.zeros(1, dtype=np.intp)
with pytest.raises(AssertionError, match='min_count'):
    group_mean(actual, counts, data, labels, is_datetimelike=True, min_count=0)
```

## Next Steps


---

*Source: test_libgroupby.py:258 | Complexity: Intermediate | Last updated: 2026-06-02*