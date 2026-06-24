# How To: Interp Various

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interp various

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

### Step 3: Assign df = df.set_index(...)

```python
df = df.set_index('C')
```

### Step 4: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 5: Assign result = df.interpolate(...)

```python
result = df.interpolate(method='polynomial', order=1)
```

### Step 6: Assign unknown = 2.66666667

```python
expected.loc[3, 'A'] = 2.66666667
```

### Step 7: Assign unknown = 5.76923076

```python
expected.loc[13, 'A'] = 5.76923076
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = df.interpolate(...)

```python
result = df.interpolate(method='cubic')
```

### Step 10: Assign unknown = 2.81547781

```python
expected.loc[3, 'A'] = 2.81547781
```

### Step 11: Assign unknown = 5.52964175

```python
expected.loc[13, 'A'] = 5.52964175
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign result = df.interpolate(...)

```python
result = df.interpolate(method='nearest')
```

### Step 14: Assign unknown = 2

```python
expected.loc[3, 'A'] = 2
```

### Step 15: Assign unknown = 5

```python
expected.loc[13, 'A'] = 5
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_dtype=False)
```

### Step 17: Assign result = df.interpolate(...)

```python
result = df.interpolate(method='quadratic')
```

### Step 18: Assign unknown = 2.82150771

```python
expected.loc[3, 'A'] = 2.82150771
```

### Step 19: Assign unknown = 6.12648668

```python
expected.loc[13, 'A'] = 6.12648668
```

### Step 20: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 21: Assign result = df.interpolate(...)

```python
result = df.interpolate(method='slinear')
```

### Step 22: Assign unknown = 2.66666667

```python
expected.loc[3, 'A'] = 2.66666667
```

### Step 23: Assign unknown = 5.76923077

```python
expected.loc[13, 'A'] = 5.76923077
```

### Step 24: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 25: Assign result = df.interpolate(...)

```python
result = df.interpolate(method='zero')
```

### Step 26: Assign unknown = 2.0

```python
expected.loc[3, 'A'] = 2.0
```

### Step 27: Assign unknown = 5

```python
expected.loc[13, 'A'] = 5
```

### Step 28: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_dtype=False)
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
df = DataFrame({'A': [1, 2, np.nan, 4, 5, np.nan, 7], 'C': [1, 2, 3, 5, 8, 13, 21]})
df = df.set_index('C')
expected = df.copy()
result = df.interpolate(method='polynomial', order=1)
expected.loc[3, 'A'] = 2.66666667
expected.loc[13, 'A'] = 5.76923076
tm.assert_frame_equal(result, expected)
result = df.interpolate(method='cubic')
expected.loc[3, 'A'] = 2.81547781
expected.loc[13, 'A'] = 5.52964175
tm.assert_frame_equal(result, expected)
result = df.interpolate(method='nearest')
expected.loc[3, 'A'] = 2
expected.loc[13, 'A'] = 5
tm.assert_frame_equal(result, expected, check_dtype=False)
result = df.interpolate(method='quadratic')
expected.loc[3, 'A'] = 2.82150771
expected.loc[13, 'A'] = 6.12648668
tm.assert_frame_equal(result, expected)
result = df.interpolate(method='slinear')
expected.loc[3, 'A'] = 2.66666667
expected.loc[13, 'A'] = 5.76923077
tm.assert_frame_equal(result, expected)
result = df.interpolate(method='zero')
expected.loc[3, 'A'] = 2.0
expected.loc[13, 'A'] = 5
tm.assert_frame_equal(result, expected, check_dtype=False)
```

## Next Steps


---

*Source: test_interpolate.py:220 | Complexity: Advanced | Last updated: 2026-06-02*