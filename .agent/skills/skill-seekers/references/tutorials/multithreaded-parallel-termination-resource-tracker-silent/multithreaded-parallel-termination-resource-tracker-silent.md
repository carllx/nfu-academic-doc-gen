# How To: Multithreaded Parallel Termination Resource Tracker Silent

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multithreaded parallel termination resource tracker silent

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign cmd = 'if 1:\n        import os\n        import numpy as np\n        from joblib import Parallel, delayed\n        from joblib.externals.loky.backend import resource_tracker\n        from concurrent.futures import ThreadPoolExecutor, wait\n\n        resource_tracker.VERBOSE = 0\n\n        array = np.arange(int(1e2))\n\n        temp_dirs_thread_1 = set()\n        temp_dirs_thread_2 = set()\n\n\n        def raise_error(array):\n            raise ValueError\n\n\n        def parallel_get_filename(array, temp_dirs):\n            with Parallel(backend="loky", n_jobs=2, max_nbytes=10) as p:\n                for i in range(10):\n                    [filename] = p(\n                        delayed(getattr)(array, "filename") for _ in range(1)\n                    )\n                    temp_dirs.add(os.path.dirname(filename))\n\n\n        def parallel_raise(array, temp_dirs):\n            with Parallel(backend="loky", n_jobs=2, max_nbytes=10) as p:\n                for i in range(10):\n                    [filename] = p(\n                        delayed(raise_error)(array) for _ in range(1)\n                    )\n                    temp_dirs.add(os.path.dirname(filename))\n\n\n        executor = ThreadPoolExecutor(max_workers=2)\n\n        # both function calls will use the same loky executor, but with a\n        # different Parallel object.\n        future_1 = executor.submit({f1}, array, temp_dirs_thread_1)\n        future_2 = executor.submit({f2}, array, temp_dirs_thread_2)\n\n        # Wait for both threads to terminate their backend\n        wait([future_1, future_2])\n\n        future_1.result()\n        future_2.result()\n    '

```python
cmd = 'if 1:\n        import os\n        import numpy as np\n        from joblib import Parallel, delayed\n        from joblib.externals.loky.backend import resource_tracker\n        from concurrent.futures import ThreadPoolExecutor, wait\n\n        resource_tracker.VERBOSE = 0\n\n        array = np.arange(int(1e2))\n\n        temp_dirs_thread_1 = set()\n        temp_dirs_thread_2 = set()\n\n\n        def raise_error(array):\n            raise ValueError\n\n\n        def parallel_get_filename(array, temp_dirs):\n            with Parallel(backend="loky", n_jobs=2, max_nbytes=10) as p:\n                for i in range(10):\n                    [filename] = p(\n                        delayed(getattr)(array, "filename") for _ in range(1)\n                    )\n                    temp_dirs.add(os.path.dirname(filename))\n\n\n        def parallel_raise(array, temp_dirs):\n            with Parallel(backend="loky", n_jobs=2, max_nbytes=10) as p:\n                for i in range(10):\n                    [filename] = p(\n                        delayed(raise_error)(array) for _ in range(1)\n                    )\n                    temp_dirs.add(os.path.dirname(filename))\n\n\n        executor = ThreadPoolExecutor(max_workers=2)\n\n        # both function calls will use the same loky executor, but with a\n        # different Parallel object.\n        future_1 = executor.submit({f1}, array, temp_dirs_thread_1)\n        future_2 = executor.submit({f2}, array, temp_dirs_thread_2)\n\n        # Wait for both threads to terminate their backend\n        wait([future_1, future_2])\n\n        future_1.result()\n        future_2.result()\n    '
```

**Verification:**
```python
assert p.returncode == returncode, err.decode()
```

### Step 2: Assign functions_and_returncodes = value

```python
functions_and_returncodes = [('parallel_get_filename', 'parallel_get_filename', 0), ('parallel_get_filename', 'parallel_raise', 1), ('parallel_raise', 'parallel_raise', 1)]
```

**Verification:**
```python
assert b'resource_tracker' not in err, err.decode()
```

### Step 3: Assign p = subprocess.Popen(...)

```python
p = subprocess.Popen([sys.executable, '-c', cmd.format(f1=f1, f2=f2)], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
```

### Step 4: Call p.wait()

```python
p.wait()
```

### Step 5: Assign unknown = p.communicate(...)

```python
_, err = p.communicate()
```

**Verification:**
```python
assert p.returncode == returncode, err.decode()
```


## Complete Example

```python
# Workflow
cmd = 'if 1:\n        import os\n        import numpy as np\n        from joblib import Parallel, delayed\n        from joblib.externals.loky.backend import resource_tracker\n        from concurrent.futures import ThreadPoolExecutor, wait\n\n        resource_tracker.VERBOSE = 0\n\n        array = np.arange(int(1e2))\n\n        temp_dirs_thread_1 = set()\n        temp_dirs_thread_2 = set()\n\n\n        def raise_error(array):\n            raise ValueError\n\n\n        def parallel_get_filename(array, temp_dirs):\n            with Parallel(backend="loky", n_jobs=2, max_nbytes=10) as p:\n                for i in range(10):\n                    [filename] = p(\n                        delayed(getattr)(array, "filename") for _ in range(1)\n                    )\n                    temp_dirs.add(os.path.dirname(filename))\n\n\n        def parallel_raise(array, temp_dirs):\n            with Parallel(backend="loky", n_jobs=2, max_nbytes=10) as p:\n                for i in range(10):\n                    [filename] = p(\n                        delayed(raise_error)(array) for _ in range(1)\n                    )\n                    temp_dirs.add(os.path.dirname(filename))\n\n\n        executor = ThreadPoolExecutor(max_workers=2)\n\n        # both function calls will use the same loky executor, but with a\n        # different Parallel object.\n        future_1 = executor.submit({f1}, array, temp_dirs_thread_1)\n        future_2 = executor.submit({f2}, array, temp_dirs_thread_2)\n\n        # Wait for both threads to terminate their backend\n        wait([future_1, future_2])\n\n        future_1.result()\n        future_2.result()\n    '
functions_and_returncodes = [('parallel_get_filename', 'parallel_get_filename', 0), ('parallel_get_filename', 'parallel_raise', 1), ('parallel_raise', 'parallel_raise', 1)]
for f1, f2, returncode in functions_and_returncodes:
    p = subprocess.Popen([sys.executable, '-c', cmd.format(f1=f1, f2=f2)], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait()
    _, err = p.communicate()
    assert p.returncode == returncode, err.decode()
    assert b'resource_tracker' not in err, err.decode()
```

## Next Steps


---

*Source: test_memmapping.py:552 | Complexity: Intermediate | Last updated: 2026-06-02*