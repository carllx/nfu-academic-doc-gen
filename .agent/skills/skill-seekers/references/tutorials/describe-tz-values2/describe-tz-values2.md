# How To: Describe Tz Values2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe tz values2

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tz = 'CET'

```python
tz = 'CET'
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series(range(5))
```

### Step 3: Assign start = Timestamp(...)

```python
start = Timestamp(2018, 1, 1)
```

### Step 4: Assign end = Timestamp(...)

```python
end = Timestamp(2018, 1, 5)
```

### Step 5: Assign s2 = Series(...)

```python
s2 = Series(date_range(start, end, tz=tz))
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame({'s1': s1, 's2': s2})
```

### Step 7: Assign s1_ = s1.describe(...)

```python
s1_ = s1.describe()
```

### Step 8: Assign s2_ = s2.describe(...)

```python
s2_ = s2.describe()
```

### Step 9: Assign idx = value

```python
idx = ['count', 'mean', 'min', '25%', '50%', '75%', 'max', 'std']
```

### Step 10: Assign expected = pd.concat.reindex(...)

```python
expected = pd.concat([s1_, s2_], axis=1, keys=['s1', 's2']).reindex(idx, copy=False)
```

### Step 11: Assign result = df.describe(...)

```python
result = df.describe(include='all')
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
tz = 'CET'
s1 = Series(range(5))
start = Timestamp(2018, 1, 1)
end = Timestamp(2018, 1, 5)
s2 = Series(date_range(start, end, tz=tz))
df = DataFrame({'s1': s1, 's2': s2})
s1_ = s1.describe()
s2_ = s2.describe()
idx = ['count', 'mean', 'min', '25%', '50%', '75%', 'max', 'std']
expected = pd.concat([s1_, s2_], axis=1, keys=['s1', 's2']).reindex(idx, copy=False)
result = df.describe(include='all')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:301 | Complexity: Advanced | Last updated: 2026-06-02*