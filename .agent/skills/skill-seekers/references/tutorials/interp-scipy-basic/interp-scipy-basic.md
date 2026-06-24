# How To: Interp Scipy Basic

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interp scipy basic

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign s = Series(...)

```python
s = Series([1, 3, np.nan, 12, np.nan, 25])
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([1.0, 3.0, 7.5, 12.0, 18.5, 25.0])
```

### Step 4: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='slinear')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign msg = "The 'downcast' keyword in Series.interpolate is deprecated"

```python
msg = "The 'downcast' keyword in Series.interpolate is deprecated"
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([1, 3, 3, 12, 12, 25])
```

### Step 9: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='nearest')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected.astype('float'))
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign expected = Series(...)

```python
expected = Series([1, 3, 3, 12, 12, 25])
```

### Step 13: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='zero')
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected.astype('float'))
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 16: Assign expected = Series(...)

```python
expected = Series([1, 3.0, 6.823529, 12.0, 18.058824, 25.0])
```

### Step 17: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='quadratic')
```

### Step 18: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 19: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 20: Assign expected = Series(...)

```python
expected = Series([1.0, 3.0, 6.8, 12.0, 18.2, 25.0])
```

### Step 21: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='cubic')
```

### Step 22: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 23: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='slinear', downcast='infer')
```

### Step 24: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='nearest', downcast='infer')
```

### Step 25: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='zero', downcast='infer')
```

### Step 26: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='quadratic', downcast='infer')
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
s = Series([1, 3, np.nan, 12, np.nan, 25])
expected = Series([1.0, 3.0, 7.5, 12.0, 18.5, 25.0])
result = s.interpolate(method='slinear')
tm.assert_series_equal(result, expected)
msg = "The 'downcast' keyword in Series.interpolate is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = s.interpolate(method='slinear', downcast='infer')
tm.assert_series_equal(result, expected)
expected = Series([1, 3, 3, 12, 12, 25])
result = s.interpolate(method='nearest')
tm.assert_series_equal(result, expected.astype('float'))
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = s.interpolate(method='nearest', downcast='infer')
tm.assert_series_equal(result, expected)
expected = Series([1, 3, 3, 12, 12, 25])
result = s.interpolate(method='zero')
tm.assert_series_equal(result, expected.astype('float'))
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = s.interpolate(method='zero', downcast='infer')
tm.assert_series_equal(result, expected)
expected = Series([1, 3.0, 6.823529, 12.0, 18.058824, 25.0])
result = s.interpolate(method='quadratic')
tm.assert_series_equal(result, expected)
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = s.interpolate(method='quadratic', downcast='infer')
tm.assert_series_equal(result, expected)
expected = Series([1.0, 3.0, 6.8, 12.0, 18.2, 25.0])
result = s.interpolate(method='cubic')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_interpolate.py:285 | Complexity: Advanced | Last updated: 2026-06-02*