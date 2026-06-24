# How To: Runtime Feature Selection

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Ensure that when selecting `NPY_ENABLE_CPU_FEATURES`, only the
features exactly specified are dispatched.

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

### Step 1: '\n        Ensure that when selecting `NPY_ENABLE_CPU_FEATURES`, only the\n        features exactly specified are dispatched.\n        '

```python
'\n        Ensure that when selecting `NPY_ENABLE_CPU_FEATURES`, only the\n        features exactly specified are dispatched.\n        '
```

**Verification:**
```python
assert set(enabled_features) == {feature}
```

### Step 2: Assign out = self._run(...)

```python
out = self._run()
```

**Verification:**
```python
assert set(enabled_features) == set(non_baseline_features)
```

### Step 3: Assign non_baseline_features = _text_to_list(...)

```python
non_baseline_features = _text_to_list(out.stdout)
```

### Step 4: Assign feature = value

```python
feature = non_baseline_features[0]
```

### Step 5: Assign unknown = feature

```python
self.env['NPY_ENABLE_CPU_FEATURES'] = feature
```

### Step 6: Assign out = self._run(...)

```python
out = self._run()
```

### Step 7: Assign enabled_features = _text_to_list(...)

```python
enabled_features = _text_to_list(out.stdout)
```

**Verification:**
```python
assert set(enabled_features) == {feature}
```

### Step 8: Assign unknown = unknown.join(...)

```python
self.env['NPY_ENABLE_CPU_FEATURES'] = ','.join(non_baseline_features)
```

### Step 9: Assign out = self._run(...)

```python
out = self._run()
```

### Step 10: Assign enabled_features = _text_to_list(...)

```python
enabled_features = _text_to_list(out.stdout)
```

**Verification:**
```python
assert set(enabled_features) == set(non_baseline_features)
```

### Step 11: Call pytest.skip()

```python
pytest.skip('No dispatchable features outside of baseline detected.')
```

### Step 12: Call pytest.skip()

```python
pytest.skip('Only one non-baseline feature detected.')
```


## Complete Example

```python
# Workflow
'\n        Ensure that when selecting `NPY_ENABLE_CPU_FEATURES`, only the\n        features exactly specified are dispatched.\n        '
out = self._run()
non_baseline_features = _text_to_list(out.stdout)
if non_baseline_features is None:
    pytest.skip('No dispatchable features outside of baseline detected.')
feature = non_baseline_features[0]
self.env['NPY_ENABLE_CPU_FEATURES'] = feature
out = self._run()
enabled_features = _text_to_list(out.stdout)
assert set(enabled_features) == {feature}
if len(non_baseline_features) < 2:
    pytest.skip('Only one non-baseline feature detected.')
self.env['NPY_ENABLE_CPU_FEATURES'] = ','.join(non_baseline_features)
out = self._run()
enabled_features = _text_to_list(out.stdout)
assert set(enabled_features) == set(non_baseline_features)
```

## Next Steps


---

*Source: test_cpu_features.py:195 | Complexity: Advanced | Last updated: 2026-06-02*