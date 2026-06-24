# How To: Indexer Constructor Arg

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indexer constructor arg

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

### Step 1: Assign use_expanding = value

```python
use_expanding = [True, False, True, False, True]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'values': range(5)})
```

### Step 3: Assign indexer = CustomIndexer(...)

```python
indexer = CustomIndexer(window_size=1, use_expanding=use_expanding)
```

### Step 4: Assign result = df.rolling.sum(...)

```python
result = df.rolling(indexer).sum()
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'values': [0.0, 1.0, 3.0, 3.0, 10.0]})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign start = np.empty(...)

```python
start = np.empty(num_values, dtype=np.int64)
```

### Step 8: Assign end = np.empty(...)

```python
end = np.empty(num_values, dtype=np.int64)
```

### Step 9: Assign unknown = 0

```python
start[i] = 0
```

### Step 10: Assign unknown = value

```python
end[i] = i + 1
```

### Step 11: Assign unknown = i

```python
start[i] = i
```

### Step 12: Assign unknown = value

```python
end[i] = i + self.window_size
```


## Complete Example

```python
# Workflow
use_expanding = [True, False, True, False, True]
df = DataFrame({'values': range(5)})

class CustomIndexer(BaseIndexer):

    def get_window_bounds(self, num_values, min_periods, center, closed, step):
        start = np.empty(num_values, dtype=np.int64)
        end = np.empty(num_values, dtype=np.int64)
        for i in range(num_values):
            if self.use_expanding[i]:
                start[i] = 0
                end[i] = i + 1
            else:
                start[i] = i
                end[i] = i + self.window_size
        return (start, end)
indexer = CustomIndexer(window_size=1, use_expanding=use_expanding)
result = df.rolling(indexer).sum()
expected = DataFrame({'values': [0.0, 1.0, 3.0, 3.0, 10.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_base_indexer.py:43 | Complexity: Advanced | Last updated: 2026-06-02*