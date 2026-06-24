# How To: Due Date Enforcement

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test due date enforcement

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `inspect`
- `pytest`
- `setuptools.warnings`

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Call monkeypatch.setenv()

```python
monkeypatch.setenv('SETUPTOOLS_ENFORCE_DEPRECATION', 'true')
```

**Verification:**
```python
assert str(exc_info.value) == cleandoc(expected)
```

### Step 2: Assign expected = '\n    Summary\n    !!\n\n            ********************************************************************************\n            Lorem ipsum\n\n            This deprecation is overdue, please update your project and remove deprecated\n            calls to avoid build errors in the future.\n\n            See https://setuptools.pypa.io/en/latest/some_page.html for details.\n            ********************************************************************************\n\n    !!\n    '

```python
expected = '\n    Summary\n    !!\n\n            ********************************************************************************\n            Lorem ipsum\n\n            This deprecation is overdue, please update your project and remove deprecated\n            calls to avoid build errors in the future.\n\n            See https://setuptools.pypa.io/en/latest/some_page.html for details.\n            ********************************************************************************\n\n    !!\n    '
```

**Verification:**
```python
assert str(exc_info.value) == cleandoc(expected)
```

### Step 3: Assign _SUMMARY = 'Summary'

```python
_SUMMARY = 'Summary'
```

### Step 4: Assign _DETAILS = 'Lorem ipsum'

```python
_DETAILS = 'Lorem ipsum'
```

### Step 5: Assign _DUE_DATE = value

```python
_DUE_DATE = (2000, 11, 22)
```

### Step 6: Assign _SEE_DOCS = 'some_page.html'

```python
_SEE_DOCS = 'some_page.html'
```

### Step 7: Call _MyDeprecation.emit()

```python
_MyDeprecation.emit()
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
class _MyDeprecation(SetuptoolsDeprecationWarning):
    _SUMMARY = 'Summary'
    _DETAILS = 'Lorem ipsum'
    _DUE_DATE = (2000, 11, 22)
    _SEE_DOCS = 'some_page.html'
monkeypatch.setenv('SETUPTOOLS_ENFORCE_DEPRECATION', 'true')
with pytest.raises(SetuptoolsDeprecationWarning) as exc_info:
    _MyDeprecation.emit()
expected = '\n    Summary\n    !!\n\n            ********************************************************************************\n            Lorem ipsum\n\n            This deprecation is overdue, please update your project and remove deprecated\n            calls to avoid build errors in the future.\n\n            See https://setuptools.pypa.io/en/latest/some_page.html for details.\n            ********************************************************************************\n\n    !!\n    '
assert str(exc_info.value) == cleandoc(expected)
```

## Next Steps


---

*Source: test_warnings.py:76 | Complexity: Intermediate | Last updated: 2026-06-02*