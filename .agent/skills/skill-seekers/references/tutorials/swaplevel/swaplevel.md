# How To: Swaplevel

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test swaplevel

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: multiindex_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign frame = multiindex_dataframe_random_data

```python
frame = multiindex_dataframe_random_data
```

**Verification:**
```python
assert not swapped.index.equals(frame.index)
```

### Step 2: Assign swapped = unknown.swaplevel(...)

```python
swapped = frame['A'].swaplevel()
```

**Verification:**
```python
assert back.index.equals(frame.index)
```

### Step 3: Assign swapped2 = unknown.swaplevel(...)

```python
swapped2 = frame['A'].swaplevel(0)
```

### Step 4: Assign swapped3 = unknown.swaplevel(...)

```python
swapped3 = frame['A'].swaplevel(0, 1)
```

### Step 5: Assign swapped4 = unknown.swaplevel(...)

```python
swapped4 = frame['A'].swaplevel('first', 'second')
```

**Verification:**
```python
assert not swapped.index.equals(frame.index)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(swapped, swapped2)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(swapped, swapped3)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(swapped, swapped4)
```

### Step 9: Assign back = swapped.swaplevel(...)

```python
back = swapped.swaplevel()
```

### Step 10: Assign back2 = swapped.swaplevel(...)

```python
back2 = swapped.swaplevel(0)
```

### Step 11: Assign back3 = swapped.swaplevel(...)

```python
back3 = swapped.swaplevel(0, 1)
```

### Step 12: Assign back4 = swapped.swaplevel(...)

```python
back4 = swapped.swaplevel('second', 'first')
```

**Verification:**
```python
assert back.index.equals(frame.index)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(back, back2)
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(back, back3)
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(back, back4)
```

### Step 16: Assign ft = value

```python
ft = frame.T
```

### Step 17: Assign swapped = ft.swaplevel(...)

```python
swapped = ft.swaplevel('first', 'second', axis=1)
```

### Step 18: Assign exp = value

```python
exp = frame.swaplevel('first', 'second').T
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(swapped, exp)
```

### Step 20: Assign msg = 'Can only swap levels on a hierarchical axis.'

```python
msg = 'Can only swap levels on a hierarchical axis.'
```

### Step 21: Call DataFrame.swaplevel()

```python
DataFrame(range(3)).swaplevel()
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_dataframe_random_data

# Workflow
frame = multiindex_dataframe_random_data
swapped = frame['A'].swaplevel()
swapped2 = frame['A'].swaplevel(0)
swapped3 = frame['A'].swaplevel(0, 1)
swapped4 = frame['A'].swaplevel('first', 'second')
assert not swapped.index.equals(frame.index)
tm.assert_series_equal(swapped, swapped2)
tm.assert_series_equal(swapped, swapped3)
tm.assert_series_equal(swapped, swapped4)
back = swapped.swaplevel()
back2 = swapped.swaplevel(0)
back3 = swapped.swaplevel(0, 1)
back4 = swapped.swaplevel('second', 'first')
assert back.index.equals(frame.index)
tm.assert_series_equal(back, back2)
tm.assert_series_equal(back, back3)
tm.assert_series_equal(back, back4)
ft = frame.T
swapped = ft.swaplevel('first', 'second', axis=1)
exp = frame.swaplevel('first', 'second').T
tm.assert_frame_equal(swapped, exp)
msg = 'Can only swap levels on a hierarchical axis.'
with pytest.raises(TypeError, match=msg):
    DataFrame(range(3)).swaplevel()
```

## Next Steps


---

*Source: test_swaplevel.py:8 | Complexity: Advanced | Last updated: 2026-06-02*