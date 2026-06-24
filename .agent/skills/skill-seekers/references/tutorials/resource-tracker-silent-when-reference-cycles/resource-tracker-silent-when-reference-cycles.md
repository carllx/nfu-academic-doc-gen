# How To: Resource Tracker Silent When Reference Cycles

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resource tracker silent when reference cycles

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
cmd = 'if 1:\n        import numpy as np\n        from joblib import Parallel, delayed\n\n\n        data = np.random.rand(int(2e6)).reshape((int(1e6), 2))\n\n        # Build a complex cyclic reference that is likely to delay garbage\n        # collection of the memmapped array in the worker processes.\n        first_list = current_list = [data]\n        for i in range(10):\n            current_list = [current_list]\n        first_list.append(current_list)\n\n        if __name__ == "__main__":\n            results = Parallel(n_jobs=2, backend="{b}")(\n                delayed(len)(current_list) for i in range(10))\n            assert results == [1] * 10\n    '.format(b=backend)
```

**Verification:**
```python
assert p.returncode == 0, out + '\n\n' + err
```

### Step 2: Assign p = subprocess.Popen(...)

```python
p = subprocess.Popen([sys.executable, '-c', cmd], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
```

**Verification:**
```python
assert 'resource_tracker' not in err, err
```

### Step 3: Call p.wait()

```python
p.wait()
```

### Step 4: Assign unknown = p.communicate(...)

```python
out, err = p.communicate()
```

### Step 5: Assign out = out.decode(...)

```python
out = out.decode()
```

### Step 6: Assign err = err.decode(...)

```python
err = err.decode()
```

**Verification:**
```python
assert p.returncode == 0, out + '\n\n' + err
```

### Step 7: Call pytest.xfail()

```python
pytest.xfail('The temporary folder cannot be deleted on Windows in the presence of a reference cycle')
```


## Complete Example

```python
# Setup
# Fixtures: backend

# Workflow
if backend == 'loky' and sys.platform.startswith('win'):
    pytest.xfail('The temporary folder cannot be deleted on Windows in the presence of a reference cycle')
cmd = 'if 1:\n        import numpy as np\n        from joblib import Parallel, delayed\n\n\n        data = np.random.rand(int(2e6)).reshape((int(1e6), 2))\n\n        # Build a complex cyclic reference that is likely to delay garbage\n        # collection of the memmapped array in the worker processes.\n        first_list = current_list = [data]\n        for i in range(10):\n            current_list = [current_list]\n        first_list.append(current_list)\n\n        if __name__ == "__main__":\n            results = Parallel(n_jobs=2, backend="{b}")(\n                delayed(len)(current_list) for i in range(10))\n            assert results == [1] * 10\n    '.format(b=backend)
p = subprocess.Popen([sys.executable, '-c', cmd], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
p.wait()
out, err = p.communicate()
out = out.decode()
err = err.decode()
assert p.returncode == 0, out + '\n\n' + err
assert 'resource_tracker' not in err, err
```

## Next Steps


---

*Source: test_memmapping.py:683 | Complexity: Intermediate | Last updated: 2026-06-02*