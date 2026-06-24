# How To: Interp Alt Scipy

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interp alt scipy

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, np.nan, 4, 5, np.nan, 7], 'C': [1, 2, 3, 5, 8, 13, 21]})
```

### Step 3: Assign result = df.interpolate(...)

```python
result = df.interpolate(method='barycentric')
```

### Step 4: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 5: Assign unknown = 3

```python
expected.loc[2, 'A'] = 3
```

### Step 6: Assign unknown = 6

```python
expected.loc[5, 'A'] = 6
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign msg = "The 'downcast' keyword in DataFrame.interpolate is deprecated"

```python
msg = "The 'downcast' keyword in DataFrame.interpolate is deprecated"
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected.astype(np.int64))
```

### Step 10: Assign result = df.interpolate(...)

```python
result = df.interpolate(method='krogh')
```

### Step 11: Assign expectedk = df.copy(...)

```python
expectedk = df.copy()
```

### Step 12: Assign unknown = value

```python
expectedk['A'] = expected['A']
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expectedk)
```

### Step 14: Assign result = df.interpolate(...)

```python
result = df.interpolate(method='pchip')
```

### Step 15: Assign unknown = 3

```python
expected.loc[2, 'A'] = 3
```

### Step 16: Assign unknown = 6.0

```python
expected.loc[5, 'A'] = 6.0
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 18: Assign result = df.interpolate(...)

```python
result = df.interpolate(method='barycentric', downcast='infer')
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
df = DataFrame({'A': [1, 2, np.nan, 4, 5, np.nan, 7], 'C': [1, 2, 3, 5, 8, 13, 21]})
result = df.interpolate(method='barycentric')
expected = df.copy()
expected.loc[2, 'A'] = 3
expected.loc[5, 'A'] = 6
tm.assert_frame_equal(result, expected)
msg = "The 'downcast' keyword in DataFrame.interpolate is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.interpolate(method='barycentric', downcast='infer')
tm.assert_frame_equal(result, expected.astype(np.int64))
result = df.interpolate(method='krogh')
expectedk = df.copy()
expectedk['A'] = expected['A']
tm.assert_frame_equal(result, expectedk)
result = df.interpolate(method='pchip')
expected.loc[2, 'A'] = 3
expected.loc[5, 'A'] = 6.0
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_interpolate.py:259 | Complexity: Advanced | Last updated: 2026-06-02*