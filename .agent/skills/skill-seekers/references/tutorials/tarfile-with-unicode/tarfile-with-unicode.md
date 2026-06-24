# How To: Tarfile With Unicode

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Create a tarfile containing only a file whose name is
a zero byte file called testimäge.png.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `tarfile`
- `pytest`
- `setuptools`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: '\n    Create a tarfile containing only a file whose name is\n    a zero byte file called testimäge.png.\n    '

```python
'\n    Create a tarfile containing only a file whose name is\n    a zero byte file called testimäge.png.\n    '
```

### Step 2: Assign tarobj = io.BytesIO(...)

```python
tarobj = io.BytesIO()
```

### Step 3: Assign target = value

```python
target = tmpdir / 'unicode-pkg-1.0.tar.gz'
```

### Step 4: Assign data = b''

```python
data = b''
```

### Step 5: Assign filename = 'testimäge.png'

```python
filename = 'testimäge.png'
```

### Step 6: Assign t = tarfile.TarInfo(...)

```python
t = tarfile.TarInfo(filename)
```

### Step 7: Assign t.size = len(...)

```python
t.size = len(data)
```

### Step 8: Call tgz.addfile()

```python
tgz.addfile(t, io.BytesIO(data))
```

### Step 9: Call tf.write()

```python
tf.write(tarobj.getvalue())
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
'\n    Create a tarfile containing only a file whose name is\n    a zero byte file called testimäge.png.\n    '
tarobj = io.BytesIO()
with tarfile.open(fileobj=tarobj, mode='w:gz') as tgz:
    data = b''
    filename = 'testimäge.png'
    t = tarfile.TarInfo(filename)
    t.size = len(data)
    tgz.addfile(t, io.BytesIO(data))
target = tmpdir / 'unicode-pkg-1.0.tar.gz'
with open(str(target), mode='wb') as tf:
    tf.write(tarobj.getvalue())
return str(target)
```

## Next Steps


---

*Source: test_archive_util.py:10 | Complexity: Advanced | Last updated: 2026-06-02*