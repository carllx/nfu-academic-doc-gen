# How To: Resample Group Keys

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample group keys

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': 1, 'B': 2}, index=date_range('2000', periods=10))
```

### Step 2: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 3: Assign g = df.resample(...)

```python
g = df.resample('5D', group_keys=False)
```

### Step 4: Assign result = g.apply(...)

```python
result = g.apply(lambda x: x)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign g = df.resample(...)

```python
g = df.resample('5D')
```

### Step 7: Assign result = g.apply(...)

```python
result = g.apply(lambda x: x)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign expected.index = pd.MultiIndex.from_arrays(...)

```python
expected.index = pd.MultiIndex.from_arrays([pd.to_datetime(['2000-01-01', '2000-01-06']).as_unit('ns').repeat(5), expected.index])
```

### Step 10: Assign g = df.resample(...)

```python
g = df.resample('5D', group_keys=True)
```

### Step 11: Assign result = g.apply(...)

```python
result = g.apply(lambda x: x)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': 1, 'B': 2}, index=date_range('2000', periods=10))
expected = df.copy()
g = df.resample('5D', group_keys=False)
result = g.apply(lambda x: x)
tm.assert_frame_equal(result, expected)
g = df.resample('5D')
result = g.apply(lambda x: x)
tm.assert_frame_equal(result, expected)
expected.index = pd.MultiIndex.from_arrays([pd.to_datetime(['2000-01-01', '2000-01-06']).as_unit('ns').repeat(5), expected.index])
g = df.resample('5D', group_keys=True)
result = g.apply(lambda x: x)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_resample_api.py:103 | Complexity: Advanced | Last updated: 2026-06-02*