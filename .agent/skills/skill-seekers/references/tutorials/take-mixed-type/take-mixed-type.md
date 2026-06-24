# How To: Take Mixed Type

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take mixed type

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_string_frame
```

## Step-by-Step Guide

### Step 1: Assign order = value

```python
order = [4, 1, 2, 0, 3]
```

### Step 2: Assign order = value

```python
order = [4, 1, -2]
```

### Step 3: Assign result = df.take(...)

```python
result = df.take(order, axis=0)
```

### Step 4: Assign expected = df.reindex(...)

```python
expected = df.reindex(df.index.take(order))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = df.take(...)

```python
result = df.take(order, axis=1)
```

### Step 7: Assign expected = value

```python
expected = df.loc[:, ['foo', 'B', 'C', 'A', 'D']]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = df.take(...)

```python
result = df.take(order, axis=0)
```

### Step 10: Assign expected = df.reindex(...)

```python
expected = df.reindex(df.index.take(order))
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign result = df.take(...)

```python
result = df.take(order, axis=1)
```

### Step 13: Assign expected = value

```python
expected = df.loc[:, ['foo', 'B', 'D']]
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: float_string_frame

# Workflow
order = [4, 1, 2, 0, 3]
for df in [float_string_frame]:
    result = df.take(order, axis=0)
    expected = df.reindex(df.index.take(order))
    tm.assert_frame_equal(result, expected)
    result = df.take(order, axis=1)
    expected = df.loc[:, ['foo', 'B', 'C', 'A', 'D']]
    tm.assert_frame_equal(result, expected)
order = [4, 1, -2]
for df in [float_string_frame]:
    result = df.take(order, axis=0)
    expected = df.reindex(df.index.take(order))
    tm.assert_frame_equal(result, expected)
    result = df.take(order, axis=1)
    expected = df.loc[:, ['foo', 'B', 'D']]
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_take.py:56 | Complexity: Advanced | Last updated: 2026-06-02*