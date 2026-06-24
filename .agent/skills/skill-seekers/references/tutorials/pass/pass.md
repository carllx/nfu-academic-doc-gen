# How To: Pass

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pass

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

### Step 1: Assign output_mypy = OUTPUT_MYPY

```python
output_mypy = OUTPUT_MYPY
```

### Step 2: Assign relpath = os.path.relpath(...)

```python
relpath = os.path.relpath(path)
```

### Step 3: Assign messages = value

```python
messages = []
```

### Step 4: Assign unknown = _strip_filename(...)

```python
lineno, content = _strip_filename(message)
```

### Step 5: Assign content = content.removeprefix.lstrip(...)

```python
content = content.removeprefix('error:').lstrip()
```

### Step 6: Call messages.append()

```python
messages.append(f'{relpath}:{lineno} - {content}')
```

### Step 7: Call pytest.fail()

```python
pytest.fail('\n'.join(messages), pytrace=False)
```


## Complete Example

```python
# Setup
# Fixtures: path

# Workflow
output_mypy = OUTPUT_MYPY
if path not in output_mypy:
    return
relpath = os.path.relpath(path)
messages = []
for message in output_mypy[path]:
    lineno, content = _strip_filename(message)
    content = content.removeprefix('error:').lstrip()
    messages.append(f'{relpath}:{lineno} - {content}')
if messages:
    pytest.fail('\n'.join(messages), pytrace=False)
```

## Next Steps


---

*Source: test_typing.py:142 | Complexity: Intermediate | Last updated: 2026-06-02*