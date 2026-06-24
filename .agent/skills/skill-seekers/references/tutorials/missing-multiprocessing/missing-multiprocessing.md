# How To: Missing Multiprocessing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test that import joblib works even if _multiprocessing is missing.

pytest has already imported everything from joblib. The most reasonable way
to test importing joblib with modified environment is to invoke a separate
Python process. This also ensures that we don't break other tests by
importing a bad `_multiprocessing` module.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `subprocess`
- `sys`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: "\n    Test that import joblib works even if _multiprocessing is missing.\n\n    pytest has already imported everything from joblib. The most reasonable way\n    to test importing joblib with modified environment is to invoke a separate\n    Python process. This also ensures that we don't break other tests by\n    importing a bad `_multiprocessing` module.\n    "

```python
"\n    Test that import joblib works even if _multiprocessing is missing.\n\n    pytest has already imported everything from joblib. The most reasonable way\n    to test importing joblib with modified environment is to invoke a separate\n    Python process. This also ensures that we don't break other tests by\n    importing a bad `_multiprocessing` module.\n    "
```

### Step 2: Call unknown.write_text()

```python
(tmp_path / '_multiprocessing.py').write_text('raise ImportError("No _multiprocessing module!")')
```

### Step 3: Assign env = dict(...)

```python
env = dict(os.environ)
```

### Step 4: Assign unknown = unknown.join(...)

```python
env['PYTHONPATH'] = ':'.join([str(tmp_path)] + sys.path)
```

### Step 5: Call subprocess.check_call()

```python
subprocess.check_call([sys.executable, '-c', 'import joblib, math; joblib.Parallel(n_jobs=1)(joblib.delayed(math.sqrt)(i**2) for i in range(10))'], env=env)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
"\n    Test that import joblib works even if _multiprocessing is missing.\n\n    pytest has already imported everything from joblib. The most reasonable way\n    to test importing joblib with modified environment is to invoke a separate\n    Python process. This also ensures that we don't break other tests by\n    importing a bad `_multiprocessing` module.\n    "
(tmp_path / '_multiprocessing.py').write_text('raise ImportError("No _multiprocessing module!")')
env = dict(os.environ)
env['PYTHONPATH'] = ':'.join([str(tmp_path)] + sys.path)
subprocess.check_call([sys.executable, '-c', 'import joblib, math; joblib.Parallel(n_jobs=1)(joblib.delayed(math.sqrt)(i**2) for i in range(10))'], env=env)
```

## Next Steps


---

*Source: test_missing_multiprocessing.py:11 | Complexity: Intermediate | Last updated: 2026-06-02*