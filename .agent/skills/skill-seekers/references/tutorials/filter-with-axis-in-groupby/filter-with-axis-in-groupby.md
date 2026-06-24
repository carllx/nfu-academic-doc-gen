# How To: Filter With Axis In Groupby

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filter with axis in groupby

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = pd.MultiIndex.from_product(...)

```python
index = pd.MultiIndex.from_product([range(10), [0, 1]])
```

### Step 2: Assign data = DataFrame(...)

```python
data = DataFrame(np.arange(100).reshape(-1, 20), columns=index, dtype='int64')
```

### Step 3: Assign msg = 'DataFrame.groupby with axis=1'

```python
msg = 'DataFrame.groupby with axis=1'
```

### Step 4: Assign result = gb.filter(...)

```python
result = gb.filter(lambda x: x.iloc[0, 0] > 10)
```

### Step 5: Assign expected = value

```python
expected = data.iloc[:, 12:20]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign gb = data.groupby(...)

```python
gb = data.groupby(level=0, axis=1)
```


## Complete Example

```python
# Workflow
index = pd.MultiIndex.from_product([range(10), [0, 1]])
data = DataFrame(np.arange(100).reshape(-1, 20), columns=index, dtype='int64')
msg = 'DataFrame.groupby with axis=1'
with tm.assert_produces_warning(FutureWarning, match=msg):
    gb = data.groupby(level=0, axis=1)
result = gb.filter(lambda x: x.iloc[0, 0] > 10)
expected = data.iloc[:, 12:20]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_filters.py:124 | Complexity: Intermediate | Last updated: 2026-06-02*