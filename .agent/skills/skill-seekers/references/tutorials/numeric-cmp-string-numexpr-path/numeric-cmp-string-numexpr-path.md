# How To: Numeric Cmp String Numexpr Path

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test numeric cmp string numexpr path

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `collections`
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: box_with_array, monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign box = box_with_array

```python
box = box_with_array
```

### Step 2: Assign xbox = value

```python
xbox = box if box is not Index else np.ndarray
```

### Step 3: Assign obj = Series(...)

```python
obj = Series(np.random.default_rng(2).standard_normal(51))
```

### Step 4: Assign obj = tm.box_expected(...)

```python
obj = tm.box_expected(obj, box, transpose=False)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(np.zeros(51, dtype=bool))
```

### Step 6: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, xbox, transpose=False)
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result, ~expected)
```

### Step 9: Assign msg = 'Invalid comparison between dtype=float64 and str'

```python
msg = 'Invalid comparison between dtype=float64 and str'
```

### Step 10: Call m.setattr()

```python
m.setattr(expr, '_MIN_ELEMENTS', 50)
```

### Step 11: Assign result = value

```python
result = obj == 'a'
```

### Step 12: Call m.setattr()

```python
m.setattr(expr, '_MIN_ELEMENTS', 50)
```

### Step 13: Assign result = value

```python
result = obj != 'a'
```

### Step 14: obj < 'a'

```python
obj < 'a'
```


## Complete Example

```python
# Setup
# Fixtures: box_with_array, monkeypatch

# Workflow
box = box_with_array
xbox = box if box is not Index else np.ndarray
obj = Series(np.random.default_rng(2).standard_normal(51))
obj = tm.box_expected(obj, box, transpose=False)
with monkeypatch.context() as m:
    m.setattr(expr, '_MIN_ELEMENTS', 50)
    result = obj == 'a'
expected = Series(np.zeros(51, dtype=bool))
expected = tm.box_expected(expected, xbox, transpose=False)
tm.assert_equal(result, expected)
with monkeypatch.context() as m:
    m.setattr(expr, '_MIN_ELEMENTS', 50)
    result = obj != 'a'
tm.assert_equal(result, ~expected)
msg = 'Invalid comparison between dtype=float64 and str'
with pytest.raises(TypeError, match=msg):
    obj < 'a'
```

## Next Steps


---

*Source: test_numeric.py:143 | Complexity: Advanced | Last updated: 2026-06-02*