# How To: Raise On Drop Duplicate Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test raise on drop duplicate index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: actual
```

## Step-by-Step Guide

### Step 1: Assign level = value

```python
level = 0 if isinstance(actual.index, MultiIndex) else None
```

### Step 2: Assign msg = re.escape(...)

```python
msg = re.escape('"[\'c\'] not found in axis"')
```

### Step 3: Assign expected_no_err = actual.drop(...)

```python
expected_no_err = actual.drop('c', axis=0, level=level, errors='ignore')
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected_no_err, actual)
```

### Step 5: Assign expected_no_err = actual.T.drop(...)

```python
expected_no_err = actual.T.drop('c', axis=1, level=level, errors='ignore')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected_no_err.T, actual)
```

### Step 7: Call actual.drop()

```python
actual.drop('c', level=level, axis=0)
```

### Step 8: Call actual.T.drop()

```python
actual.T.drop('c', level=level, axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: actual

# Workflow
level = 0 if isinstance(actual.index, MultiIndex) else None
msg = re.escape('"[\'c\'] not found in axis"')
with pytest.raises(KeyError, match=msg):
    actual.drop('c', level=level, axis=0)
with pytest.raises(KeyError, match=msg):
    actual.T.drop('c', level=level, axis=1)
expected_no_err = actual.drop('c', axis=0, level=level, errors='ignore')
tm.assert_frame_equal(expected_no_err, actual)
expected_no_err = actual.T.drop('c', axis=1, level=level, errors='ignore')
tm.assert_frame_equal(expected_no_err.T, actual)
```

## Next Steps


---

*Source: test_drop.py:246 | Complexity: Advanced | Last updated: 2026-06-02*