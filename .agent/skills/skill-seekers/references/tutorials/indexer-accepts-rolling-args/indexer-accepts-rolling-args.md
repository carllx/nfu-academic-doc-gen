# How To: Indexer Accepts Rolling Args

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indexer accepts rolling args

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.indexers.objects`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'values': range(5)})
```

### Step 2: Assign indexer = CustomIndexer(...)

```python
indexer = CustomIndexer(window_size=1)
```

### Step 3: Assign result = df.rolling.sum(...)

```python
result = df.rolling(indexer, center=True, min_periods=1, closed='both', step=1).sum()
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'values': [0.0, 1.0, 10.0, 3.0, 4.0]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign start = np.empty(...)

```python
start = np.empty(num_values, dtype=np.int64)
```

### Step 7: Assign end = np.empty(...)

```python
end = np.empty(num_values, dtype=np.int64)
```

### Step 8: Assign unknown = 0

```python
start[i] = 0
```

### Step 9: Assign unknown = num_values

```python
end[i] = num_values
```

### Step 10: Assign unknown = i

```python
start[i] = i
```

### Step 11: Assign unknown = value

```python
end[i] = i + self.window_size
```


## Complete Example

```python
# Workflow
df = DataFrame({'values': range(5)})

class CustomIndexer(BaseIndexer):

    def get_window_bounds(self, num_values, min_periods, center, closed, step):
        start = np.empty(num_values, dtype=np.int64)
        end = np.empty(num_values, dtype=np.int64)
        for i in range(num_values):
            if center and min_periods == 1 and (closed == 'both') and (step == 1) and (i == 2):
                start[i] = 0
                end[i] = num_values
            else:
                start[i] = i
                end[i] = i + self.window_size
        return (start, end)
indexer = CustomIndexer(window_size=1)
result = df.rolling(indexer, center=True, min_periods=1, closed='both', step=1).sum()
expected = DataFrame({'values': [0.0, 1.0, 10.0, 3.0, 4.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_base_indexer.py:67 | Complexity: Advanced | Last updated: 2026-06-02*