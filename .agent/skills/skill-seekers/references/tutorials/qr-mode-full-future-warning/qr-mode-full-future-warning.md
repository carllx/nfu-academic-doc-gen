# How To: Qr Mode Full Future Warning

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check mode='full' FutureWarning.

In numpy 1.8 the mode options 'full' and 'economic' in linalg.qr were
deprecated. The release date will probably be sometime in the summer
of 2013.

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`


## Step-by-Step Guide

### Step 1: "Check mode='full' FutureWarning.\n\n    In numpy 1.8 the mode options 'full' and 'economic' in linalg.qr were\n    deprecated. The release date will probably be sometime in the summer\n    of 2013.\n\n    "

```python
"Check mode='full' FutureWarning.\n\n    In numpy 1.8 the mode options 'full' and 'economic' in linalg.qr were\n    deprecated. The release date will probably be sometime in the summer\n    of 2013.\n\n    "
```

### Step 2: Assign a = np.eye(...)

```python
a = np.eye(2)
```

### Step 3: Call pytest.warns()

```python
pytest.warns(DeprecationWarning, np.linalg.qr, a, mode='full')
```

### Step 4: Call pytest.warns()

```python
pytest.warns(DeprecationWarning, np.linalg.qr, a, mode='f')
```

### Step 5: Call pytest.warns()

```python
pytest.warns(DeprecationWarning, np.linalg.qr, a, mode='economic')
```

### Step 6: Call pytest.warns()

```python
pytest.warns(DeprecationWarning, np.linalg.qr, a, mode='e')
```


## Complete Example

```python
# Workflow
"Check mode='full' FutureWarning.\n\n    In numpy 1.8 the mode options 'full' and 'economic' in linalg.qr were\n    deprecated. The release date will probably be sometime in the summer\n    of 2013.\n\n    "
a = np.eye(2)
pytest.warns(DeprecationWarning, np.linalg.qr, a, mode='full')
pytest.warns(DeprecationWarning, np.linalg.qr, a, mode='f')
pytest.warns(DeprecationWarning, np.linalg.qr, a, mode='economic')
pytest.warns(DeprecationWarning, np.linalg.qr, a, mode='e')
```

## Next Steps


---

*Source: test_deprecations.py:9 | Complexity: Intermediate | Last updated: 2026-06-02*