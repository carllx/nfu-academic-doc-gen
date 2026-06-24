# How To: Missing Meta

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test missing meta

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
# Fixtures: missing_metadata
```

## Step-by-Step Guide

### Step 1: Assign result = json_normalize(...)

```python
result = json_normalize(data=missing_metadata, record_path='addresses', meta='name', errors='ignore')
```

### Step 2: Assign ex_data = value

```python
ex_data = [[9562, 'Morris St.', 'Massillon', 'OH', 44646, 'Alice'], [8449, 'Spring St.', 'Elizabethton', 'TN', 37643, np.nan]]
```

### Step 3: Assign columns = value

```python
columns = ['number', 'street', 'city', 'state', 'zip', 'name']
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(ex_data, columns=columns)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: missing_metadata

# Workflow
result = json_normalize(data=missing_metadata, record_path='addresses', meta='name', errors='ignore')
ex_data = [[9562, 'Morris St.', 'Massillon', 'OH', 44646, 'Alice'], [8449, 'Spring St.', 'Elizabethton', 'TN', 37643, np.nan]]
columns = ['number', 'street', 'city', 'state', 'zip', 'name']
expected = DataFrame(ex_data, columns=columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_normalize.py:637 | Complexity: Intermediate | Last updated: 2026-06-02*