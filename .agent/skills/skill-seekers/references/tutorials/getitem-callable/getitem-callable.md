# How To: Getitem Callable

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem callable

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign result = value

```python
result = float_frame[lambda x: 'A']
```

### Step 2: Assign expected = value

```python
expected = float_frame.loc[:, 'A']
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 4: Assign result = value

```python
result = float_frame[lambda x: ['A', 'B']]
```

### Step 5: Assign expected = value

```python
expected = float_frame.loc[:, ['A', 'B']]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, float_frame.loc[:, ['A', 'B']])
```

### Step 7: Assign df = value

```python
df = float_frame[:3]
```

### Step 8: Assign result = value

```python
result = df[lambda x: [True, False, True]]
```

### Step 9: Assign expected = value

```python
expected = float_frame.iloc[[0, 2], :]
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
result = float_frame[lambda x: 'A']
expected = float_frame.loc[:, 'A']
tm.assert_series_equal(result, expected)
result = float_frame[lambda x: ['A', 'B']]
expected = float_frame.loc[:, ['A', 'B']]
tm.assert_frame_equal(result, float_frame.loc[:, ['A', 'B']])
df = float_frame[:3]
result = df[lambda x: [True, False, True]]
expected = float_frame.iloc[[0, 2], :]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:218 | Complexity: Advanced | Last updated: 2026-06-02*