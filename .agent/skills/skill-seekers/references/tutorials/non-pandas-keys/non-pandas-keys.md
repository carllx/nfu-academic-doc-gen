# How To: Non Pandas Keys

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non pandas keys

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

### Step 1: Assign path = value

```python
path = tmp_path / setup_path
```

**Verification:**
```python
assert len(store.keys(include='native')) == 3
```

### Step 2: Assign value1 = tables.Float32Col(...)

```python
value1 = tables.Float32Col()
```

**Verification:**
```python
assert set(store.keys(include='native')) == expected
```

### Step 3: Assign value2 = tables.Float32Col(...)

```python
value2 = tables.Float32Col()
```

**Verification:**
```python
assert set(store.keys(include='pandas')) == set()
```

### Step 4: Assign value3 = tables.Float32Col(...)

```python
value3 = tables.Float32Col()
```

**Verification:**
```python
assert len(df.columns) == 1
```

### Step 5: Assign group = h5file.create_group(...)

```python
group = h5file.create_group('/', 'group')
```

### Step 6: Call h5file.create_table()

```python
h5file.create_table(group, 'table1', Table1, 'Table 1')
```

### Step 7: Call h5file.create_table()

```python
h5file.create_table(group, 'table2', Table2, 'Table 2')
```

### Step 8: Call h5file.create_table()

```python
h5file.create_table(group, 'table3', Table3, 'Table 3')
```

**Verification:**
```python
assert len(store.keys(include='native')) == 3
```

### Step 9: Assign expected = value

```python
expected = {'/group/table1', '/group/table2', '/group/table3'}
```

**Verification:**
```python
assert set(store.keys(include='native')) == expected
```

### Step 10: Assign df = store.get(...)

```python
df = store.get(name)
```

**Verification:**
```python
assert len(df.columns) == 1
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
class Table1(tables.IsDescription):
    value1 = tables.Float32Col()

class Table2(tables.IsDescription):
    value2 = tables.Float32Col()

class Table3(tables.IsDescription):
    value3 = tables.Float32Col()
path = tmp_path / setup_path
with tables.open_file(path, mode='w') as h5file:
    group = h5file.create_group('/', 'group')
    h5file.create_table(group, 'table1', Table1, 'Table 1')
    h5file.create_table(group, 'table2', Table2, 'Table 2')
    h5file.create_table(group, 'table3', Table3, 'Table 3')
with HDFStore(path) as store:
    assert len(store.keys(include='native')) == 3
    expected = {'/group/table1', '/group/table2', '/group/table3'}
    assert set(store.keys(include='native')) == expected
    assert set(store.keys(include='pandas')) == set()
    for name in expected:
        df = store.get(name)
        assert len(df.columns) == 1
```

## Next Steps


---

*Source: test_keys.py:39 | Complexity: Advanced | Last updated: 2026-06-02*