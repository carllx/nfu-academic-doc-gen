# How To: Setitem Cache Updating Slices

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem cache updating slices

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [600, 600, 600]}, index=date_range('5/7/2014', '5/9/2014'))
```

### Step 2: Assign out = DataFrame(...)

```python
out = DataFrame({'A': [0, 0, 0]}, index=date_range('5/7/2014', '5/9/2014'))
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'C': ['A', 'A', 'A'], 'D': [100, 200, 300]})
```

### Step 4: Assign six = Timestamp(...)

```python
six = Timestamp('5/7/2014')
```

### Step 5: Assign eix = Timestamp(...)

```python
eix = Timestamp('5/9/2014')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(out, expected)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(out['A'], expected['A'])
```

### Step 8: Assign out = DataFrame(...)

```python
out = DataFrame({'A': [0, 0, 0]}, index=date_range('5/7/2014', '5/9/2014'))
```

### Step 9: Assign out_original = out.copy(...)

```python
out_original = out.copy()
```

### Step 10: Assign out = DataFrame(...)

```python
out = DataFrame({'A': [0, 0, 0]}, index=date_range('5/7/2014', '5/9/2014'))
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(out, expected)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(out['A'], expected['A'])
```

### Step 13: Assign unknown = value

```python
out.loc[six:eix, row['C']] = out.loc[six:eix, row['C']] + row['D']
```

### Step 14: Assign v = value

```python
v = out[row['C']][six:eix] + row['D']
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(out, expected)
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(out['A'], expected['A'])
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(out, out_original)
```

### Step 18: Call tm.assert_series_equal()

```python
tm.assert_series_equal(out['A'], out_original['A'])
```

### Step 19: Assign unknown = v

```python
out[row['C']][six:eix] = v
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
expected = DataFrame({'A': [600, 600, 600]}, index=date_range('5/7/2014', '5/9/2014'))
out = DataFrame({'A': [0, 0, 0]}, index=date_range('5/7/2014', '5/9/2014'))
df = DataFrame({'C': ['A', 'A', 'A'], 'D': [100, 200, 300]})
six = Timestamp('5/7/2014')
eix = Timestamp('5/9/2014')
for ix, row in df.iterrows():
    out.loc[six:eix, row['C']] = out.loc[six:eix, row['C']] + row['D']
tm.assert_frame_equal(out, expected)
tm.assert_series_equal(out['A'], expected['A'])
out = DataFrame({'A': [0, 0, 0]}, index=date_range('5/7/2014', '5/9/2014'))
out_original = out.copy()
for ix, row in df.iterrows():
    v = out[row['C']][six:eix] + row['D']
    with tm.raises_chained_assignment_error(ix == 0 or warn_copy_on_write or using_copy_on_write):
        out[row['C']][six:eix] = v
if not using_copy_on_write:
    tm.assert_frame_equal(out, expected)
    tm.assert_series_equal(out['A'], expected['A'])
else:
    tm.assert_frame_equal(out, out_original)
    tm.assert_series_equal(out['A'], out_original['A'])
out = DataFrame({'A': [0, 0, 0]}, index=date_range('5/7/2014', '5/9/2014'))
for ix, row in df.iterrows():
    out.loc[six:eix, row['C']] += row['D']
tm.assert_frame_equal(out, expected)
tm.assert_series_equal(out['A'], expected['A'])
```

## Next Steps


---

*Source: test_chaining_and_caching.py:75 | Complexity: Advanced | Last updated: 2026-06-02*