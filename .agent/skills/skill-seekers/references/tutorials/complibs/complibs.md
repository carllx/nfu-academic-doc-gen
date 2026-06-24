# How To: Complibs

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test complibs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.io`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: tmp_path, lvl, lib, request
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((30, 4)), columns=list('ABCD'), index=np.arange(30).astype(np.str_))
```

**Verification:**
```python
assert node.filters.complevel == lvl
```

### Step 2: Assign tmpfile = value

```python
tmpfile = tmp_path / f'{lvl}_{lib}.h5'
```

**Verification:**
```python
assert node.filters.complib is None
```

### Step 3: Assign gname = value

```python
gname = f'{lvl}_{lib}'
```

**Verification:**
```python
assert node.filters.complib == lib
```

### Step 4: Call df.to_hdf()

```python
df.to_hdf(tmpfile, key=gname, complib=lib, complevel=lvl)
```

### Step 5: Assign result = read_hdf(...)

```python
result = read_hdf(tmpfile, gname)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 7: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason=f'Fails for {lib} on Linux and PY > 3.11'))
```

### Step 8: Call pytest.skip()

```python
pytest.skip('lzo not available')
```

### Step 9: Call pytest.skip()

```python
pytest.skip('bzip2 not available')
```

**Verification:**
```python
assert node.filters.complevel == lvl
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, lvl, lib, request

# Workflow
if PY311 and is_platform_linux() and (lib == 'blosc2') and (lvl != 0):
    request.applymarker(pytest.mark.xfail(reason=f'Fails for {lib} on Linux and PY > 3.11'))
df = DataFrame(np.ones((30, 4)), columns=list('ABCD'), index=np.arange(30).astype(np.str_))
if not tables.which_lib_version('lzo'):
    pytest.skip('lzo not available')
if not tables.which_lib_version('bzip2'):
    pytest.skip('bzip2 not available')
tmpfile = tmp_path / f'{lvl}_{lib}.h5'
gname = f'{lvl}_{lib}'
df.to_hdf(tmpfile, key=gname, complib=lib, complevel=lvl)
result = read_hdf(tmpfile, gname)
tm.assert_frame_equal(result, df)
with tables.open_file(tmpfile, mode='r') as h5table:
    for node in h5table.walk_nodes(where='/' + gname, classname='Leaf'):
        assert node.filters.complevel == lvl
        if lvl == 0:
            assert node.filters.complib is None
        else:
            assert node.filters.complib == lib
```

## Next Steps


---

*Source: test_file_handling.py:287 | Complexity: Advanced | Last updated: 2026-06-02*