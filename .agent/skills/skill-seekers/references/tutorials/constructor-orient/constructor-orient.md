# How To: Constructor Orient

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor orient

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_string_frame
```

## Step-by-Step Guide

### Step 1: Assign data_dict = value

```python
data_dict = float_string_frame.T._series
```

### Step 2: Assign recons = DataFrame.from_dict(...)

```python
recons = DataFrame.from_dict(data_dict, orient='index')
```

### Step 3: Assign expected = float_string_frame.reindex(...)

```python
expected = float_string_frame.reindex(index=recons.index)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(recons, expected)
```

### Step 5: Assign a = value

```python
a = {'hi': [32, 3, 3], 'there': [3, 5, 3]}
```

### Step 6: Assign rs = DataFrame.from_dict(...)

```python
rs = DataFrame.from_dict(a, orient='index')
```

### Step 7: Assign xp = DataFrame.from_dict.T.reindex(...)

```python
xp = DataFrame.from_dict(a).T.reindex(list(a.keys()))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(rs, xp)
```


## Complete Example

```python
# Setup
# Fixtures: float_string_frame

# Workflow
data_dict = float_string_frame.T._series
recons = DataFrame.from_dict(data_dict, orient='index')
expected = float_string_frame.reindex(index=recons.index)
tm.assert_frame_equal(recons, expected)
a = {'hi': [32, 3, 3], 'there': [3, 5, 3]}
rs = DataFrame.from_dict(a, orient='index')
xp = DataFrame.from_dict(a).T.reindex(list(a.keys()))
tm.assert_frame_equal(rs, xp)
```

## Next Steps


---

*Source: test_from_dict.py:108 | Complexity: Advanced | Last updated: 2026-06-02*