# How To: Impossible Feature Disable

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: Test that a RuntimeError is thrown if an impossible feature-disabling
request is made. This includes disabling a baseline feature.

## Prerequisites

**Required Modules:**
- `os`
- `pathlib`
- `platform`
- `re`
- `subprocess`
- `sys`
- `pytest`
- `numpy._core._multiarray_umath`
- `textwrap`
- `subprocess`


## Step-by-Step Guide

### Step 1: '\n        Test that a RuntimeError is thrown if an impossible feature-disabling\n        request is made. This includes disabling a baseline feature.\n        '

```python
'\n        Test that a RuntimeError is thrown if an impossible feature-disabling\n        request is made. This includes disabling a baseline feature.\n        '
```

### Step 2: Assign bad_feature = value

```python
bad_feature = self.BASELINE_FEAT
```

### Step 3: Assign unknown = bad_feature

```python
self.env['NPY_DISABLE_CPU_FEATURES'] = bad_feature
```

### Step 4: Assign msg = value

```python
msg = f"You cannot disable CPU feature '{bad_feature}', since it is part of the baseline optimizations"
```

### Step 5: Assign err_type = 'RuntimeError'

```python
err_type = 'RuntimeError'
```

### Step 6: Call self._expect_error()

```python
self._expect_error(msg, err_type)
```

### Step 7: Call pytest.skip()

```python
pytest.skip('There are no unavailable features to test with')
```


## Complete Example

```python
# Workflow
'\n        Test that a RuntimeError is thrown if an impossible feature-disabling\n        request is made. This includes disabling a baseline feature.\n        '
if self.BASELINE_FEAT is None:
    pytest.skip('There are no unavailable features to test with')
bad_feature = self.BASELINE_FEAT
self.env['NPY_DISABLE_CPU_FEATURES'] = bad_feature
msg = f"You cannot disable CPU feature '{bad_feature}', since it is part of the baseline optimizations"
err_type = 'RuntimeError'
self._expect_error(msg, err_type)
```

## Next Steps


---

*Source: test_cpu_features.py:279 | Complexity: Intermediate | Last updated: 2026-06-02*