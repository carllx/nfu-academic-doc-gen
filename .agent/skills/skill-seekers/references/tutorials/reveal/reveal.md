# How To: Reveal

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Validate that mypy correctly infers the return-types of
the expressions in `path`.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `importlib.util`
- `os`
- `re`
- `shutil`
- `textwrap`
- `collections`
- `typing`
- `pytest`
- `mypy`
- `collections.abc`
- `_pytest.mark.structures`

**Setup Required:**
```python
# Fixtures: path
```

## Step-by-Step Guide

### Step 1: 'Validate that mypy correctly infers the return-types of\n    the expressions in `path`.\n    '

```python
'Validate that mypy correctly infers the return-types of\n    the expressions in `path`.\n    '
```

### Step 2: Assign __tracebackhide__ = True

```python
__tracebackhide__ = True
```

### Step 3: Assign output_mypy = OUTPUT_MYPY

```python
output_mypy = OUTPUT_MYPY
```

### Step 4: Assign relpath = os.path.relpath(...)

```python
relpath = os.path.relpath(path)
```

### Step 5: Assign failures = value

```python
failures = []
```

### Step 6: Assign unknown = _strip_filename(...)

```python
lineno, error_msg = _strip_filename(error_line)
```

### Step 7: Assign error_msg = textwrap.indent(...)

```python
error_msg = textwrap.indent(error_msg, _FAIL_INDENT)
```

### Step 8: Assign reason = _FAIL_MSG_REVEAL.format(...)

```python
reason = _FAIL_MSG_REVEAL.format(relpath, lineno, error_msg)
```

### Step 9: Call failures.append()

```python
failures.append(reason)
```

### Step 10: Assign reasons = _FAIL_SEP.join(...)

```python
reasons = _FAIL_SEP.join(failures)
```

### Step 11: Call pytest.fail()

```python
pytest.fail(reasons, pytrace=False)
```


## Complete Example

```python
# Setup
# Fixtures: path

# Workflow
'Validate that mypy correctly infers the return-types of\n    the expressions in `path`.\n    '
__tracebackhide__ = True
output_mypy = OUTPUT_MYPY
if path not in output_mypy:
    return
relpath = os.path.relpath(path)
failures = []
for error_line in output_mypy[path]:
    lineno, error_msg = _strip_filename(error_line)
    error_msg = textwrap.indent(error_msg, _FAIL_INDENT)
    reason = _FAIL_MSG_REVEAL.format(relpath, lineno, error_msg)
    failures.append(reason)
if failures:
    reasons = _FAIL_SEP.join(failures)
    pytest.fail(reasons, pytrace=False)
```

## Next Steps


---

*Source: test_typing.py:165 | Complexity: Advanced | Last updated: 2026-06-02*