# How To: Impossible Feature Enable

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test that a RuntimeError is thrown if an impossible feature-enabling
request is made. This includes enabling a feature not supported by the
machine, or disabling a baseline optimization.

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

### Step 1: '\n        Test that a RuntimeError is thrown if an impossible feature-enabling\n        request is made. This includes enabling a feature not supported by the\n        machine, or disabling a baseline optimization.\n        '

```python
'\n        Test that a RuntimeError is thrown if an impossible feature-enabling\n        request is made. This includes enabling a feature not supported by the\n        machine, or disabling a baseline optimization.\n        '
```

### Step 2: Assign bad_feature = value

```python
bad_feature = self.UNAVAILABLE_FEAT
```

### Step 3: Assign unknown = bad_feature

```python
self.env['NPY_ENABLE_CPU_FEATURES'] = bad_feature
```

### Step 4: Assign msg = value

```python
msg = f'You cannot enable CPU features \\({bad_feature}\\), since they are not supported by your machine.'
```

### Step 5: Assign err_type = 'RuntimeError'

```python
err_type = 'RuntimeError'
```

### Step 6: Call self._expect_error()

```python
self._expect_error(msg, err_type)
```

### Step 7: Assign feats = value

```python
feats = f'{bad_feature}, Foobar'
```

### Step 8: Assign unknown = feats

```python
self.env['NPY_ENABLE_CPU_FEATURES'] = feats
```

### Step 9: Assign msg = value

```python
msg = f'You cannot enable CPU features \\({bad_feature}\\), since they are not supported by your machine.'
```

### Step 10: Call self._expect_error()

```python
self._expect_error(msg, err_type)
```

### Step 11: Call pytest.skip()

```python
pytest.skip('There are no unavailable features to test with')
```

### Step 12: Assign feats = value

```python
feats = f'{bad_feature}, {self.BASELINE_FEAT}'
```

### Step 13: Assign unknown = feats

```python
self.env['NPY_ENABLE_CPU_FEATURES'] = feats
```

### Step 14: Assign msg = value

```python
msg = f'You cannot enable CPU features \\({bad_feature}\\), since they are not supported by your machine.'
```

### Step 15: Call self._expect_error()

```python
self._expect_error(msg, err_type)
```


## Complete Example

```python
# Workflow
'\n        Test that a RuntimeError is thrown if an impossible feature-enabling\n        request is made. This includes enabling a feature not supported by the\n        machine, or disabling a baseline optimization.\n        '
if self.UNAVAILABLE_FEAT is None:
    pytest.skip('There are no unavailable features to test with')
bad_feature = self.UNAVAILABLE_FEAT
self.env['NPY_ENABLE_CPU_FEATURES'] = bad_feature
msg = f'You cannot enable CPU features \\({bad_feature}\\), since they are not supported by your machine.'
err_type = 'RuntimeError'
self._expect_error(msg, err_type)
feats = f'{bad_feature}, Foobar'
self.env['NPY_ENABLE_CPU_FEATURES'] = feats
msg = f'You cannot enable CPU features \\({bad_feature}\\), since they are not supported by your machine.'
self._expect_error(msg, err_type)
if self.BASELINE_FEAT is not None:
    feats = f'{bad_feature}, {self.BASELINE_FEAT}'
    self.env['NPY_ENABLE_CPU_FEATURES'] = feats
    msg = f'You cannot enable CPU features \\({bad_feature}\\), since they are not supported by your machine.'
    self._expect_error(msg, err_type)
```

## Next Steps


---

*Source: test_cpu_features.py:296 | Complexity: Advanced | Last updated: 2026-06-02*