# How To: Api All

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test api all

## Prerequisites

**Required Modules:**
- `__future__`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api`
- `pandas`

**Required Fixtures:**
- `api_client` fixture


## Step-by-Step Guide

### Step 1: Assign expected = value

```python
expected = set(self.public_lib + self.misc + self.modules + self.classes + self.funcs + self.funcs_option + self.funcs_read + self.funcs_json + self.funcs_to) - set(self.deprecated_classes)
```

**Verification:**
```python
assert not extraneous
```

### Step 2: Assign actual = set(...)

```python
actual = set(pd.__all__)
```

**Verification:**
```python
assert not missing
```

### Step 3: Assign extraneous = value

```python
extraneous = actual - expected
```

**Verification:**
```python
assert not extraneous
```

### Step 4: Assign missing = value

```python
missing = expected - actual
```

**Verification:**
```python
assert not missing
```


## Complete Example

```python
# Workflow
expected = set(self.public_lib + self.misc + self.modules + self.classes + self.funcs + self.funcs_option + self.funcs_read + self.funcs_json + self.funcs_to) - set(self.deprecated_classes)
actual = set(pd.__all__)
extraneous = actual - expected
assert not extraneous
missing = expected - actual
assert not missing
```

## Next Steps


---

*Source: test_api.py:215 | Complexity: Intermediate | Last updated: 2026-06-02*