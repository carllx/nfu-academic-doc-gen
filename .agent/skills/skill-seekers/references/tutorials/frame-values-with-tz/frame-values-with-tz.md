# How To: Frame Values With Tz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame values with tz

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tz = 'US/Central'

```python
tz = 'US/Central'
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': date_range('2000', periods=4, tz=tz)})
```

### Step 3: Assign result = value

```python
result = df.values
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([[Timestamp('2000-01-01', tz=tz)], [Timestamp('2000-01-02', tz=tz)], [Timestamp('2000-01-03', tz=tz)], [Timestamp('2000-01-04', tz=tz)]])
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign unknown = value

```python
df['B'] = df['A']
```

### Step 7: Assign result = value

```python
result = df.values
```

### Step 8: Assign expected = np.concatenate(...)

```python
expected = np.concatenate([expected, expected], axis=1)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 10: Assign est = 'US/Eastern'

```python
est = 'US/Eastern'
```

### Step 11: Assign unknown = unknown.dt.tz_convert(...)

```python
df['C'] = df['A'].dt.tz_convert(est)
```

### Step 12: Assign new = np.array(...)

```python
new = np.array([[Timestamp('2000-01-01T01:00:00', tz=est)], [Timestamp('2000-01-02T01:00:00', tz=est)], [Timestamp('2000-01-03T01:00:00', tz=est)], [Timestamp('2000-01-04T01:00:00', tz=est)]])
```

### Step 13: Assign expected = np.concatenate(...)

```python
expected = np.concatenate([expected, new], axis=1)
```

### Step 14: Assign result = value

```python
result = df.values
```

### Step 15: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
tz = 'US/Central'
df = DataFrame({'A': date_range('2000', periods=4, tz=tz)})
result = df.values
expected = np.array([[Timestamp('2000-01-01', tz=tz)], [Timestamp('2000-01-02', tz=tz)], [Timestamp('2000-01-03', tz=tz)], [Timestamp('2000-01-04', tz=tz)]])
tm.assert_numpy_array_equal(result, expected)
df['B'] = df['A']
result = df.values
expected = np.concatenate([expected, expected], axis=1)
tm.assert_numpy_array_equal(result, expected)
est = 'US/Eastern'
df['C'] = df['A'].dt.tz_convert(est)
new = np.array([[Timestamp('2000-01-01T01:00:00', tz=est)], [Timestamp('2000-01-02T01:00:00', tz=est)], [Timestamp('2000-01-03T01:00:00', tz=est)], [Timestamp('2000-01-04T01:00:00', tz=est)]])
expected = np.concatenate([expected, new], axis=1)
result = df.values
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_values.py:87 | Complexity: Advanced | Last updated: 2026-06-02*