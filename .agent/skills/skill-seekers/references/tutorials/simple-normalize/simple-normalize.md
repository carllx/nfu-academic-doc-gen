# How To: Simple Normalize

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple normalize

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.json._normalize`

**Setup Required:**
```python
# Fixtures: state_data
```

## Step-by-Step Guide

### Step 1: Assign result = json_normalize(...)

```python
result = json_normalize(state_data[0], 'counties')
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame(state_data[0]['counties'])
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 4: Assign result = json_normalize(...)

```python
result = json_normalize(state_data, 'counties')
```

### Step 5: Assign expected = value

```python
expected = []
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = json_normalize(...)

```python
result = json_normalize(state_data, 'counties', meta='state')
```

### Step 9: Assign unknown = np.array.repeat(...)

```python
expected['state'] = np.array(['Florida', 'Ohio']).repeat([3, 2])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Call expected.extend()

```python
expected.extend(rec['counties'])
```


## Complete Example

```python
# Setup
# Fixtures: state_data

# Workflow
result = json_normalize(state_data[0], 'counties')
expected = DataFrame(state_data[0]['counties'])
tm.assert_frame_equal(result, expected)
result = json_normalize(state_data, 'counties')
expected = []
for rec in state_data:
    expected.extend(rec['counties'])
expected = DataFrame(expected)
tm.assert_frame_equal(result, expected)
result = json_normalize(state_data, 'counties', meta='state')
expected['state'] = np.array(['Florida', 'Ohio']).repeat([3, 2])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_normalize.py:154 | Complexity: Advanced | Last updated: 2026-06-02*