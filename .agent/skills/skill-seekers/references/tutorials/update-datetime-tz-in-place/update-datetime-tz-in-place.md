# How To: Update Datetime Tz In Place

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test update datetime tz in place

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
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign result = DataFrame(...)

```python
result = DataFrame([pd.Timestamp('2019', tz='UTC')])
```

### Step 2: Assign orig = result.copy(...)

```python
orig = result.copy()
```

### Step 3: Assign view = value

```python
view = result[:]
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([pd.Timestamp('2019-01-02', tz='UTC')])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Call result.update()

```python
result.update(result + pd.Timedelta(days=1))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(view, expected)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(view, orig)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
result = DataFrame([pd.Timestamp('2019', tz='UTC')])
orig = result.copy()
view = result[:]
with tm.assert_produces_warning(FutureWarning if warn_copy_on_write else None, match='Setting a value'):
    result.update(result + pd.Timedelta(days=1))
expected = DataFrame([pd.Timestamp('2019-01-02', tz='UTC')])
tm.assert_frame_equal(result, expected)
if not using_copy_on_write:
    tm.assert_frame_equal(view, expected)
else:
    tm.assert_frame_equal(view, orig)
```

## Next Steps


---

*Source: test_update.py:145 | Complexity: Advanced | Last updated: 2026-06-02*