# How To: Update Modify View

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test update modify view

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['1', np.nan], 'B': ['100', np.nan]})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': ['a', 'x'], 'B': ['100', '200']})
```

### Step 3: Assign df2_orig = df2.copy(...)

```python
df2_orig = df2.copy()
```

### Step 4: Assign result_view = value

```python
result_view = df2[:]
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': ['1', 'x'], 'B': ['100', '200']})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, expected)
```

### Step 7: Call df2.update()

```python
df2.update(df)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_view, df2_orig)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_view, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write, using_infer_string

# Workflow
df = DataFrame({'A': ['1', np.nan], 'B': ['100', np.nan]})
df2 = DataFrame({'A': ['a', 'x'], 'B': ['100', '200']})
df2_orig = df2.copy()
result_view = df2[:]
with tm.assert_cow_warning(warn_copy_on_write):
    df2.update(df)
expected = DataFrame({'A': ['1', 'x'], 'B': ['100', '200']})
tm.assert_frame_equal(df2, expected)
if using_copy_on_write or using_infer_string:
    tm.assert_frame_equal(result_view, df2_orig)
else:
    tm.assert_frame_equal(result_view, expected)
```

## Next Steps


---

*Source: test_update.py:178 | Complexity: Advanced | Last updated: 2026-06-02*