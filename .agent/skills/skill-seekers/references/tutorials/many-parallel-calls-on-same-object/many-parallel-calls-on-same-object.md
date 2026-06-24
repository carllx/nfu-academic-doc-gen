# How To: Many Parallel Calls On Same Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test many parallel calls on same object

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
# Fixtures: backend
```

## Step-by-Step Guide

### Step 1: Assign cmd = unknown.format(...)

```python
cmd = "if 1:\n        import os\n        import time\n\n        import numpy as np\n\n        from joblib import Parallel, delayed\n        from testutils import return_slice_of_data\n\n        data = np.ones(100)\n\n        if __name__ == '__main__':\n            for i in range(5):\n                slice_of_data = Parallel(\n                    n_jobs=2, max_nbytes=1, backend='{b}')(\n                        delayed(return_slice_of_data)(data, 0, 20)\n                        for _ in range(10)\n                    )\n    ".format(b=backend)
```

**Verification:**
```python
assert p.returncode == 0, err.decode()
```

### Step 2: Assign env = os.environ.copy(...)

```python
env = os.environ.copy()
```

**Verification:**
```python
assert out == b'', out.decode()
```

### Step 3: Assign unknown = os.path.dirname(...)

```python
env['PYTHONPATH'] = os.path.dirname(__file__)
```

**Verification:**
```python
assert b'resource_tracker' not in err
```

### Step 4: Assign p = subprocess.Popen(...)

```python
p = subprocess.Popen([sys.executable, '-c', cmd], stderr=subprocess.PIPE, stdout=subprocess.PIPE, env=env)
```

### Step 5: Call p.wait()

```python
p.wait()
```

### Step 6: Assign unknown = p.communicate(...)

```python
out, err = p.communicate()
```

**Verification:**
```python
assert p.returncode == 0, err.decode()
```


## Complete Example

```python
# Setup
# Fixtures: backend

# Workflow
cmd = "if 1:\n        import os\n        import time\n\n        import numpy as np\n\n        from joblib import Parallel, delayed\n        from testutils import return_slice_of_data\n\n        data = np.ones(100)\n\n        if __name__ == '__main__':\n            for i in range(5):\n                slice_of_data = Parallel(\n                    n_jobs=2, max_nbytes=1, backend='{b}')(\n                        delayed(return_slice_of_data)(data, 0, 20)\n                        for _ in range(10)\n                    )\n    ".format(b=backend)
env = os.environ.copy()
env['PYTHONPATH'] = os.path.dirname(__file__)
p = subprocess.Popen([sys.executable, '-c', cmd], stderr=subprocess.PIPE, stdout=subprocess.PIPE, env=env)
p.wait()
out, err = p.communicate()
assert p.returncode == 0, err.decode()
assert out == b'', out.decode()
assert b'resource_tracker' not in err
```

## Next Steps


---

*Source: test_memmapping.py:628 | Complexity: Intermediate | Last updated: 2026-06-02*