# How To: Missing Meta Multilevel Record Path Errors Ignore

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test missing meta multilevel record path errors ignore

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
result = json_normalize(data=missing_metadata, record_path=['previous_residences', 'cities'], meta='name', errors='ignore')
```

### Step 2: Assign ex_data = value

```python
ex_data = [['Foo York City', 'Alice'], ['Barmingham', np.nan]]
```

### Step 3: Assign columns = value

```python
columns = ['city_name', 'name']
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
result = json_normalize(data=missing_metadata, record_path=['previous_residences', 'cities'], meta='name', errors='ignore')
ex_data = [['Foo York City', 'Alice'], ['Barmingham', np.nan]]
columns = ['city_name', 'name']
expected = DataFrame(ex_data, columns=columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_normalize.py:695 | Complexity: Intermediate | Last updated: 2026-06-02*