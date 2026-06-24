# How To: C Unit Test

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Run C unit tests in a subprocess.

## Prerequisites

**Required Modules:**
- `__future__`
- `os`
- `subprocess`
- `sys`
- `tempfile`
- `unittest`


## Step-by-Step Guide

### Step 1: 'Run C unit tests in a subprocess.'

```python
'Run C unit tests in a subprocess.'
```

### Step 2: Assign env = os.environ.copy(...)

```python
env = os.environ.copy()
```

### Step 3: Assign unknown = unknown.join(...)

```python
env['CPPFLAGS'] = ' '.join(cppflags)
```

### Step 4: Assign status = subprocess.check_call(...)

```python
status = subprocess.check_call([sys.executable, 'setup.py', 'build_ext', f'--build-lib={tmpdir}', f'--build-temp={tmpdir}', '--run-capi-tests'], env=env, cwd=os.path.join(base_dir, 'mypyc', 'lib-rt'))
```

### Step 5: Assign env = os.environ.copy(...)

```python
env = os.environ.copy()
```

### Step 6: Assign status = subprocess.call(...)

```python
status = subprocess.call([sys.executable, '-c', 'import sys, test_capi; sys.exit(test_capi.run_tests())'], env=env, cwd=tmpdir)
```

### Step 7: Assign unknown = 'yes'

```python
env['GTEST_COLOR'] = 'yes'
```


## Complete Example

```python
# Workflow
'Run C unit tests in a subprocess.'
cppflags: list[str] = []
env = os.environ.copy()
if sys.platform == 'darwin':
    cppflags += ['-O0', '-mmacosx-version-min=10.10', '-stdlib=libc++']
elif sys.platform == 'linux':
    cppflags += ['-O0']
env['CPPFLAGS'] = ' '.join(cppflags)
with tempfile.TemporaryDirectory() as tmpdir:
    status = subprocess.check_call([sys.executable, 'setup.py', 'build_ext', f'--build-lib={tmpdir}', f'--build-temp={tmpdir}', '--run-capi-tests'], env=env, cwd=os.path.join(base_dir, 'mypyc', 'lib-rt'))
    env = os.environ.copy()
    if 'GTEST_COLOR' not in os.environ:
        env['GTEST_COLOR'] = 'yes'
    status = subprocess.call([sys.executable, '-c', 'import sys, test_capi; sys.exit(test_capi.run_tests())'], env=env, cwd=tmpdir)
    if status != 0:
        raise AssertionError('make test: C unit test failure')
```

## Next Steps


---

*Source: test_external.py:18 | Complexity: Intermediate | Last updated: 2026-06-02*