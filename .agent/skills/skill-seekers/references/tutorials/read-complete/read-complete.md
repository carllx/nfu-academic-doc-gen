# How To: Read Complete

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read complete

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: pytables_hdf5_file
```

## Step-by-Step Guide

### Step 1: Assign unknown = pytables_hdf5_file

```python
path, objname, df = pytables_hdf5_file
```

### Step 2: Assign result = pd.read_hdf(...)

```python
result = pd.read_hdf(path, key=objname)
```

### Step 3: Assign expected = df

```python
expected = df
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_index_type=True)
```


## Complete Example

```python
# Setup
# Fixtures: pytables_hdf5_file

# Workflow
path, objname, df = pytables_hdf5_file
result = pd.read_hdf(path, key=objname)
expected = df
tm.assert_frame_equal(result, expected, check_index_type=True)
```

## Next Steps


---

*Source: test_compat.py:50 | Complexity: Intermediate | Last updated: 2026-06-02*