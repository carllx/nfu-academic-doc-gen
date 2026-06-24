# How To: Categorical Conversion

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical conversion

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.tests.io.pytables.common`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path
```

## Step-by-Step Guide

### Step 1: Assign obsids = value

```python
obsids = ['ESP_012345_6789', 'ESP_987654_3210']
```

### Step 2: Assign imgids = value

```python
imgids = ['APF00006np', 'APF0001imm']
```

### Step 3: Assign data = value

```python
data = [4.3, 9.8]
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'obsids': obsids, 'imgids': imgids, 'data': data})
```

### Step 5: Assign expected = value

```python
expected = df.iloc[[], :]
```

### Step 6: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 7: Call df.to_hdf()

```python
df.to_hdf(path, key='df', format='table', data_columns=True)
```

### Step 8: Assign result = read_hdf(...)

```python
result = read_hdf(path, 'df', where='obsids=B')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign df.obsids = df.obsids.astype(...)

```python
df.obsids = df.obsids.astype('category')
```

### Step 11: Assign df.imgids = df.imgids.astype(...)

```python
df.imgids = df.imgids.astype('category')
```

### Step 12: Assign expected = value

```python
expected = df.iloc[[], :]
```

### Step 13: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 14: Call df.to_hdf()

```python
df.to_hdf(path, key='df', format='table', data_columns=True)
```

### Step 15: Assign result = read_hdf(...)

```python
result = read_hdf(path, 'df', where='obsids=B')
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
obsids = ['ESP_012345_6789', 'ESP_987654_3210']
imgids = ['APF00006np', 'APF0001imm']
data = [4.3, 9.8]
df = DataFrame({'obsids': obsids, 'imgids': imgids, 'data': data})
expected = df.iloc[[], :]
path = tmp_path / setup_path
df.to_hdf(path, key='df', format='table', data_columns=True)
result = read_hdf(path, 'df', where='obsids=B')
tm.assert_frame_equal(result, expected)
df.obsids = df.obsids.astype('category')
df.imgids = df.imgids.astype('category')
expected = df.iloc[[], :]
path = tmp_path / setup_path
df.to_hdf(path, key='df', format='table', data_columns=True)
result = read_hdf(path, 'df', where='obsids=B')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:141 | Complexity: Advanced | Last updated: 2026-06-02*