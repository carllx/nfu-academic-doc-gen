# How To: Recarray Fromfile

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test recarray fromfile

## Prerequisites

**Required Modules:**
- `collections.abc`
- `pickle`
- `textwrap`
- `io`
- `os`
- `pathlib`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign data_dir = path.join(...)

```python
data_dir = path.join(path.dirname(__file__), 'data')
```

**Verification:**
```python
assert_equal(r1, r2)
```

### Step 2: Assign filename = path.join(...)

```python
filename = path.join(data_dir, 'recarray_from_file.fits')
```

**Verification:**
```python
assert_equal(r2, r3)
```

### Step 3: Assign fd = open(...)

```python
fd = open(filename, 'rb')
```

### Step 4: Call fd.seek()

```python
fd.seek(2880 * 2)
```

### Step 5: Assign r1 = np.rec.fromfile(...)

```python
r1 = np.rec.fromfile(fd, formats='f8,i4,S5', shape=3, byteorder='big')
```

### Step 6: Call fd.seek()

```python
fd.seek(2880 * 2)
```

### Step 7: Assign r2 = np.rec.array(...)

```python
r2 = np.rec.array(fd, formats='f8,i4,S5', shape=3, byteorder='big')
```

### Step 8: Call fd.seek()

```python
fd.seek(2880 * 2)
```

### Step 9: Assign bytes_array = BytesIO(...)

```python
bytes_array = BytesIO()
```

### Step 10: Call bytes_array.write()

```python
bytes_array.write(fd.read())
```

### Step 11: Call bytes_array.seek()

```python
bytes_array.seek(0)
```

### Step 12: Assign r3 = np.rec.fromfile(...)

```python
r3 = np.rec.fromfile(bytes_array, formats='f8,i4,S5', shape=3, byteorder='big')
```

### Step 13: Call fd.close()

```python
fd.close()
```

### Step 14: Call assert_equal()

```python
assert_equal(r1, r2)
```

### Step 15: Call assert_equal()

```python
assert_equal(r2, r3)
```


## Complete Example

```python
# Workflow
data_dir = path.join(path.dirname(__file__), 'data')
filename = path.join(data_dir, 'recarray_from_file.fits')
fd = open(filename, 'rb')
fd.seek(2880 * 2)
r1 = np.rec.fromfile(fd, formats='f8,i4,S5', shape=3, byteorder='big')
fd.seek(2880 * 2)
r2 = np.rec.array(fd, formats='f8,i4,S5', shape=3, byteorder='big')
fd.seek(2880 * 2)
bytes_array = BytesIO()
bytes_array.write(fd.read())
bytes_array.seek(0)
r3 = np.rec.fromfile(bytes_array, formats='f8,i4,S5', shape=3, byteorder='big')
fd.close()
assert_equal(r1, r2)
assert_equal(r2, r3)
```

## Next Steps


---

*Source: test_records.py:92 | Complexity: Advanced | Last updated: 2026-06-02*