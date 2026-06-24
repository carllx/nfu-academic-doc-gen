# How To: Array Manager Depr Env Var

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test array manager depr env var

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `subprocess`
- `sys`
- `pytest`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas._testing`
- `pandas.core.internals`

**Setup Required:**
```python
# Fixtures: manager
```

## Step-by-Step Guide

### Step 1: Assign test_env = os.environ.copy(...)

```python
test_env = os.environ.copy()
```

**Verification:**
```python
assert msg in stderr_msg, stderr_msg
```

### Step 2: Assign unknown = manager

```python
test_env['PANDAS_DATA_MANAGER'] = manager
```

### Step 3: Assign response = subprocess.run(...)

```python
response = subprocess.run([sys.executable, '-c', 'import pandas'], capture_output=True, env=test_env, check=True)
```

### Step 4: Assign msg = 'FutureWarning: The env variable PANDAS_DATA_MANAGER is set'

```python
msg = 'FutureWarning: The env variable PANDAS_DATA_MANAGER is set'
```

### Step 5: Assign stderr_msg = response.stderr.decode(...)

```python
stderr_msg = response.stderr.decode('utf-8')
```

**Verification:**
```python
assert msg in stderr_msg, stderr_msg
```


## Complete Example

```python
# Setup
# Fixtures: manager

# Workflow
test_env = os.environ.copy()
test_env['PANDAS_DATA_MANAGER'] = manager
response = subprocess.run([sys.executable, '-c', 'import pandas'], capture_output=True, env=test_env, check=True)
msg = 'FutureWarning: The env variable PANDAS_DATA_MANAGER is set'
stderr_msg = response.stderr.decode('utf-8')
assert msg in stderr_msg, stderr_msg
```

## Next Steps


---

*Source: test_managers.py:91 | Complexity: Intermediate | Last updated: 2026-06-02*