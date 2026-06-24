# How To: Resource Tracker Retries When Permissionerror

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resource tracker retries when permissionerror

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `faulthandler`
- `gc`
- `itertools`
- `mmap`
- `os`
- `pickle`
- `platform`
- `subprocess`
- `sys`
- `threading`
- `time`
- `pytest`
- `joblib._memmapping_reducer`
- `joblib._memmapping_reducer`
- `joblib.backports`
- `joblib.executor`
- `joblib.parallel`
- `joblib.pool`
- `joblib.test.common`
- `joblib.testing`
- `joblib._memmapping_reducer`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign filename = value

```python
filename = tmpdir.join('test.mmap').strpath
```

**Verification:**
```python
assert p.returncode == 0, err.decode()
```

### Step 2: Assign cmd = unknown.format(...)

```python
cmd = 'if 1:\n    import os\n    import numpy as np\n    import time\n    from joblib.externals.loky.backend import resource_tracker\n    resource_tracker.VERBOSE = 1\n\n    # Start the resource tracker\n    resource_tracker.ensure_running()\n    time.sleep(1)\n\n    # Create a file containing numpy data\n    memmap = np.memmap(r"{filename}", dtype=np.float64, shape=10, mode=\'w+\')\n    memmap[:] = np.arange(10).astype(np.int8).data\n    memmap.flush()\n    assert os.path.exists(r"{filename}")\n    del memmap\n\n    # Create a np.memmap backed by this file\n    memmap = np.memmap(r"{filename}", dtype=np.float64, shape=10, mode=\'w+\')\n    resource_tracker.register(r"{filename}", "file")\n\n    # Ask the resource_tracker to delete the file backing the np.memmap , this\n    # should raise PermissionError that the resource_tracker will log.\n    resource_tracker.maybe_unlink(r"{filename}", "file")\n\n    # Wait for the resource_tracker to process the maybe_unlink before cleaning\n    # up the memmap\n    time.sleep(2)\n    '.format(filename=filename)
```

**Verification:**
```python
assert out == b''
```

### Step 3: Assign p = subprocess.Popen(...)

```python
p = subprocess.Popen([sys.executable, '-c', cmd], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
```

**Verification:**
```python
assert msg in err.decode()
```

### Step 4: Call p.wait()

```python
p.wait()
```

### Step 5: Assign unknown = p.communicate(...)

```python
out, err = p.communicate()
```

**Verification:**
```python
assert p.returncode == 0, err.decode()
```

### Step 6: Assign msg = unknown.format(...)

```python
msg = 'tried to unlink {}, got PermissionError'.format(filename)
```

**Verification:**
```python
assert msg in err.decode()
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
filename = tmpdir.join('test.mmap').strpath
cmd = 'if 1:\n    import os\n    import numpy as np\n    import time\n    from joblib.externals.loky.backend import resource_tracker\n    resource_tracker.VERBOSE = 1\n\n    # Start the resource tracker\n    resource_tracker.ensure_running()\n    time.sleep(1)\n\n    # Create a file containing numpy data\n    memmap = np.memmap(r"{filename}", dtype=np.float64, shape=10, mode=\'w+\')\n    memmap[:] = np.arange(10).astype(np.int8).data\n    memmap.flush()\n    assert os.path.exists(r"{filename}")\n    del memmap\n\n    # Create a np.memmap backed by this file\n    memmap = np.memmap(r"{filename}", dtype=np.float64, shape=10, mode=\'w+\')\n    resource_tracker.register(r"{filename}", "file")\n\n    # Ask the resource_tracker to delete the file backing the np.memmap , this\n    # should raise PermissionError that the resource_tracker will log.\n    resource_tracker.maybe_unlink(r"{filename}", "file")\n\n    # Wait for the resource_tracker to process the maybe_unlink before cleaning\n    # up the memmap\n    time.sleep(2)\n    '.format(filename=filename)
p = subprocess.Popen([sys.executable, '-c', cmd], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
p.wait()
out, err = p.communicate()
assert p.returncode == 0, err.decode()
assert out == b''
msg = 'tried to unlink {}, got PermissionError'.format(filename)
assert msg in err.decode()
```

## Next Steps


---

*Source: test_memmapping.py:170 | Complexity: Intermediate | Last updated: 2026-06-02*