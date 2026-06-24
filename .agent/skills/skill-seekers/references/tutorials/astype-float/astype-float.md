# How To: Astype Float

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype float

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign casted = float_frame.astype(...)

```python
casted = float_frame.astype(int)
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame(float_frame.values.astype(int), index=float_frame.index, columns=float_frame.columns)
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(casted, expected)
```

### Step 4: Assign casted = float_frame.astype(...)

```python
casted = float_frame.astype(np.int32)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(float_frame.values.astype(np.int32), index=float_frame.index, columns=float_frame.columns)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(casted, expected)
```

### Step 7: Assign unknown = '5'

```python
float_frame['foo'] = '5'
```

### Step 8: Assign casted = float_frame.astype(...)

```python
casted = float_frame.astype(int)
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame(float_frame.values.astype(int), index=float_frame.index, columns=float_frame.columns)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(casted, expected)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
casted = float_frame.astype(int)
expected = DataFrame(float_frame.values.astype(int), index=float_frame.index, columns=float_frame.columns)
tm.assert_frame_equal(casted, expected)
casted = float_frame.astype(np.int32)
expected = DataFrame(float_frame.values.astype(np.int32), index=float_frame.index, columns=float_frame.columns)
tm.assert_frame_equal(casted, expected)
float_frame['foo'] = '5'
casted = float_frame.astype(int)
expected = DataFrame(float_frame.values.astype(int), index=float_frame.index, columns=float_frame.columns)
tm.assert_frame_equal(casted, expected)
```

## Next Steps


---

*Source: test_astype.py:38 | Complexity: Advanced | Last updated: 2026-06-02*