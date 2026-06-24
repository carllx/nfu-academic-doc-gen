# How To: Reset Index Level

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset index level

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
```

### Step 2: Assign result = Series.reset_index(...)

```python
result = Series(range(4)).reset_index([], drop=True)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(range(4))
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign s = value

```python
s = df.set_index(['A', 'B'])['C']
```

### Step 6: Assign result = s.reset_index(...)

```python
result = s.reset_index(level=levels[0])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df.set_index('B'))
```

### Step 8: Assign result = s.reset_index(...)

```python
result = s.reset_index(level=levels[:1])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df.set_index('B'))
```

### Step 10: Assign result = s.reset_index(...)

```python
result = s.reset_index(level=levels)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 12: Assign result = df.set_index.reset_index(...)

```python
result = df.set_index(['A', 'B']).reset_index(level=levels, drop=True)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df[['C']])
```

### Step 14: Assign s = value

```python
s = df.set_index('A')['B']
```

### Step 15: Assign result = s.reset_index(...)

```python
result = s.reset_index(level=levels[0])
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df[['A', 'B']])
```

### Step 17: Assign result = s.reset_index(...)

```python
result = s.reset_index(level=levels[:1])
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df[['A', 'B']])
```

### Step 19: Assign result = s.reset_index(...)

```python
result = s.reset_index(level=levels[0], drop=True)
```

### Step 20: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, df['B'])
```

### Step 21: Call s.reset_index()

```python
s.reset_index(level=['A', 'E'])
```

### Step 22: Call s.reset_index()

```python
s.reset_index(level=[0, 1, 2])
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
for levels in (['A', 'B'], [0, 1]):
    s = df.set_index(['A', 'B'])['C']
    result = s.reset_index(level=levels[0])
    tm.assert_frame_equal(result, df.set_index('B'))
    result = s.reset_index(level=levels[:1])
    tm.assert_frame_equal(result, df.set_index('B'))
    result = s.reset_index(level=levels)
    tm.assert_frame_equal(result, df)
    result = df.set_index(['A', 'B']).reset_index(level=levels, drop=True)
    tm.assert_frame_equal(result, df[['C']])
    with pytest.raises(KeyError, match='Level E '):
        s.reset_index(level=['A', 'E'])
    s = df.set_index('A')['B']
    result = s.reset_index(level=levels[0])
    tm.assert_frame_equal(result, df[['A', 'B']])
    result = s.reset_index(level=levels[:1])
    tm.assert_frame_equal(result, df[['A', 'B']])
    result = s.reset_index(level=levels[0], drop=True)
    tm.assert_series_equal(result, df['B'])
    with pytest.raises(IndexError, match='Too many levels'):
        s.reset_index(level=[0, 1, 2])
result = Series(range(4)).reset_index([], drop=True)
expected = Series(range(4))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reset_index.py:77 | Complexity: Advanced | Last updated: 2026-06-02*