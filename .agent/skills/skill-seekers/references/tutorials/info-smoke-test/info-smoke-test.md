# How To: Info Smoke Test

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test info smoke test

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `re`
- `string`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: fixture_func_name, request
```

## Step-by-Step Guide

### Step 1: Assign frame = request.getfixturevalue(...)

```python
frame = request.getfixturevalue(fixture_func_name)
```

**Verification:**
```python
assert len(result) > 10
```

### Step 2: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 3: Call frame.info()

```python
frame.info(buf=buf)
```

### Step 4: Assign result = buf.getvalue.splitlines(...)

```python
result = buf.getvalue().splitlines()
```

**Verification:**
```python
assert len(result) > 10
```

### Step 5: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 6: Call frame.info()

```python
frame.info(buf=buf, verbose=False)
```


## Complete Example

```python
# Setup
# Fixtures: fixture_func_name, request

# Workflow
frame = request.getfixturevalue(fixture_func_name)
buf = StringIO()
frame.info(buf=buf)
result = buf.getvalue().splitlines()
assert len(result) > 10
buf = StringIO()
frame.info(buf=buf, verbose=False)
```

## Next Steps


---

*Source: test_info.py:83 | Complexity: Intermediate | Last updated: 2026-06-02*