# How To: Test1 Basic

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test1 basic

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.sas.sasreader`

**Setup Required:**
```python
# Fixtures: file01
```

## Step-by-Step Guide

### Step 1: Assign data_csv = pd.read_csv(...)

```python
data_csv = pd.read_csv(file01.replace('.xpt', '.csv'))
```

**Verification:**
```python
assert data.shape[0] == num_rows
```

### Step 2: Call numeric_as_float()

```python
numeric_as_float(data_csv)
```

**Verification:**
```python
assert m == num_rows
```

### Step 3: Assign data = read_sas(...)

```python
data = read_sas(file01, format='xport')
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(data, data_csv)
```

### Step 5: Assign num_rows = value

```python
num_rows = data.shape[0]
```

**Verification:**
```python
assert data.shape[0] == num_rows
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(data, data_csv.iloc[0:10, :])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(data, data_csv.iloc[0:10, :])
```

### Step 8: Assign m = 0

```python
m = 0
```

**Verification:**
```python
assert m == num_rows
```

### Step 9: Assign data = read_sas(...)

```python
data = read_sas(file01)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(data, data_csv)
```

### Step 11: Assign data = reader.read(...)

```python
data = reader.read(num_rows + 100)
```

### Step 12: Assign data = reader.read(...)

```python
data = reader.read(10)
```

### Step 13: Assign data = reader.get_chunk(...)

```python
data = reader.get_chunk()
```


## Complete Example

```python
# Setup
# Fixtures: file01

# Workflow
data_csv = pd.read_csv(file01.replace('.xpt', '.csv'))
numeric_as_float(data_csv)
data = read_sas(file01, format='xport')
tm.assert_frame_equal(data, data_csv)
num_rows = data.shape[0]
with read_sas(file01, format='xport', iterator=True) as reader:
    data = reader.read(num_rows + 100)
assert data.shape[0] == num_rows
with read_sas(file01, format='xport', iterator=True) as reader:
    data = reader.read(10)
tm.assert_frame_equal(data, data_csv.iloc[0:10, :])
with read_sas(file01, format='xport', chunksize=10) as reader:
    data = reader.get_chunk()
tm.assert_frame_equal(data, data_csv.iloc[0:10, :])
m = 0
with read_sas(file01, format='xport', chunksize=100) as reader:
    for x in reader:
        m += x.shape[0]
assert m == num_rows
data = read_sas(file01)
tm.assert_frame_equal(data, data_csv)
```

## Next Steps


---

*Source: test_xport.py:43 | Complexity: Advanced | Last updated: 2026-06-02*