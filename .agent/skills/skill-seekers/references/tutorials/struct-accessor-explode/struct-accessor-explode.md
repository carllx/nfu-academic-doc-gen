# How To: Struct Accessor Explode

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test struct accessor explode

## Prerequisites

**Required Modules:**
- `re`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index([-100, 42, 123])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([{'painted': 1, 'snapping': {'sea': 'green'}}, {'painted': 2, 'snapping': {'sea': 'leatherback'}}, {'painted': 3, 'snapping': {'sea': 'hawksbill'}}], dtype=ArrowDtype(pa.struct([('painted', pa.int64()), ('snapping', pa.struct([('sea', pa.string())]))])), index=index)
```

### Step 3: Assign actual = ser.struct.explode(...)

```python
actual = ser.struct.explode()
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'painted': Series([1, 2, 3], index=index, dtype=ArrowDtype(pa.int64())), 'snapping': Series([{'sea': 'green'}, {'sea': 'leatherback'}, {'sea': 'hawksbill'}], index=index, dtype=ArrowDtype(pa.struct([('sea', pa.string())])))})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```


## Complete Example

```python
# Workflow
index = Index([-100, 42, 123])
ser = Series([{'painted': 1, 'snapping': {'sea': 'green'}}, {'painted': 2, 'snapping': {'sea': 'leatherback'}}, {'painted': 3, 'snapping': {'sea': 'hawksbill'}}], dtype=ArrowDtype(pa.struct([('painted', pa.int64()), ('snapping', pa.struct([('sea', pa.string())]))])), index=index)
actual = ser.struct.explode()
expected = DataFrame({'painted': Series([1, 2, 3], index=index, dtype=ArrowDtype(pa.int64())), 'snapping': Series([{'sea': 'green'}, {'sea': 'leatherback'}, {'sea': 'hawksbill'}], index=index, dtype=ArrowDtype(pa.struct([('sea', pa.string())])))})
tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_struct_accessor.py:109 | Complexity: Intermediate | Last updated: 2026-06-02*