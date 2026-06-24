# How To: Pytables Hdf5 File

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Use PyTables to create a simple HDF5 file.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: '\n    Use PyTables to create a simple HDF5 file.\n    '

```python
'\n    Use PyTables to create a simple HDF5 file.\n    '
```

### Step 2: Assign table_schema = value

```python
table_schema = {'c0': tables.Time64Col(pos=0), 'c1': tables.StringCol(5, pos=1), 'c2': tables.Int64Col(pos=2)}
```

### Step 3: Assign t0 = 1561105000.0

```python
t0 = 1561105000.0
```

### Step 4: Assign testsamples = value

```python
testsamples = [{'c0': t0, 'c1': 'aaaaa', 'c2': 1}, {'c0': t0 + 1, 'c1': 'bbbbb', 'c2': 2}, {'c0': t0 + 2, 'c1': 'ccccc', 'c2': 10 ** 5}, {'c0': t0 + 3, 'c1': 'ddddd', 'c2': 4294967295}]
```

### Step 5: Assign objname = 'pandas_test_timeseries'

```python
objname = 'pandas_test_timeseries'
```

### Step 6: Assign path = value

```python
path = tmp_path / 'written_with_pytables.h5'
```

### Step 7: yield (path, objname, pd.DataFrame(testsamples))

```python
yield (path, objname, pd.DataFrame(testsamples))
```

### Step 8: Assign t = f.create_table(...)

```python
t = f.create_table('/', name=objname, description=table_schema)
```

### Step 9: Call t.row.append()

```python
t.row.append()
```

### Step 10: Assign unknown = value

```python
t.row[key] = value
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'\n    Use PyTables to create a simple HDF5 file.\n    '
table_schema = {'c0': tables.Time64Col(pos=0), 'c1': tables.StringCol(5, pos=1), 'c2': tables.Int64Col(pos=2)}
t0 = 1561105000.0
testsamples = [{'c0': t0, 'c1': 'aaaaa', 'c2': 1}, {'c0': t0 + 1, 'c1': 'bbbbb', 'c2': 2}, {'c0': t0 + 2, 'c1': 'ccccc', 'c2': 10 ** 5}, {'c0': t0 + 3, 'c1': 'ddddd', 'c2': 4294967295}]
objname = 'pandas_test_timeseries'
path = tmp_path / 'written_with_pytables.h5'
with tables.open_file(path, mode='w') as f:
    t = f.create_table('/', name=objname, description=table_schema)
    for sample in testsamples:
        for key, value in sample.items():
            t.row[key] = value
        t.row.append()
yield (path, objname, pd.DataFrame(testsamples))
```

## Next Steps


---

*Source: test_compat.py:10 | Complexity: Advanced | Last updated: 2026-06-02*