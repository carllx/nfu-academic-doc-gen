# How To: Astype With Exclude String

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype with exclude string

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

### Step 1: Assign df = float_frame.copy(...)

```python
df = float_frame.copy()
```

### Step 2: Assign expected = float_frame.astype(...)

```python
expected = float_frame.astype(int)
```

### Step 3: Assign unknown = 'foo'

```python
df['string'] = 'foo'
```

### Step 4: Assign casted = df.astype(...)

```python
casted = df.astype(int, errors='ignore')
```

### Step 5: Assign unknown = 'foo'

```python
expected['string'] = 'foo'
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(casted, expected)
```

### Step 7: Assign df = float_frame.copy(...)

```python
df = float_frame.copy()
```

### Step 8: Assign expected = float_frame.astype(...)

```python
expected = float_frame.astype(np.int32)
```

### Step 9: Assign unknown = 'foo'

```python
df['string'] = 'foo'
```

### Step 10: Assign casted = df.astype(...)

```python
casted = df.astype(np.int32, errors='ignore')
```

### Step 11: Assign unknown = 'foo'

```python
expected['string'] = 'foo'
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(casted, expected)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
df = float_frame.copy()
expected = float_frame.astype(int)
df['string'] = 'foo'
casted = df.astype(int, errors='ignore')
expected['string'] = 'foo'
tm.assert_frame_equal(casted, expected)
df = float_frame.copy()
expected = float_frame.astype(np.int32)
df['string'] = 'foo'
casted = df.astype(np.int32, errors='ignore')
expected['string'] = 'foo'
tm.assert_frame_equal(casted, expected)
```

## Next Steps


---

*Source: test_astype.py:107 | Complexity: Advanced | Last updated: 2026-06-02*