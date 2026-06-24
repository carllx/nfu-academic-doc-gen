# How To: Rmtree Readonly

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Verify onerr works as expected

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `stat`
- `sys`
- `unittest.mock`
- `setuptools`

**Setup Required:**
```python
# Fixtures: monkeypatch, tmp_path
```

## Step-by-Step Guide

### Step 1: 'Verify onerr works as expected'

```python
'Verify onerr works as expected'
```

**Verification:**
```python
assert chmod_fn.call_count == expected_count
```

### Step 2: Assign tmp_dir = value

```python
tmp_dir = tmp_path / 'with_readonly'
```

**Verification:**
```python
assert not tmp_dir.is_dir()
```

### Step 3: Call tmp_dir.mkdir()

```python
tmp_dir.mkdir()
```

### Step 4: Assign some_file = tmp_dir.joinpath(...)

```python
some_file = tmp_dir.joinpath('file.txt')
```

### Step 5: Call some_file.touch()

```python
some_file.touch()
```

### Step 6: Call some_file.chmod()

```python
some_file.chmod(stat.S_IREAD)
```

### Step 7: Assign expected_count = value

```python
expected_count = 1 if sys.platform.startswith('win') else 0
```

### Step 8: Assign chmod_fn = Mock(...)

```python
chmod_fn = Mock(wraps=_shutil.attempt_chmod_verbose)
```

### Step 9: Call monkeypatch.setattr()

```python
monkeypatch.setattr(_shutil, 'attempt_chmod_verbose', chmod_fn)
```

### Step 10: Call _shutil.rmtree()

```python
_shutil.rmtree(tmp_dir)
```

**Verification:**
```python
assert chmod_fn.call_count == expected_count
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch, tmp_path

# Workflow
'Verify onerr works as expected'
tmp_dir = tmp_path / 'with_readonly'
tmp_dir.mkdir()
some_file = tmp_dir.joinpath('file.txt')
some_file.touch()
some_file.chmod(stat.S_IREAD)
expected_count = 1 if sys.platform.startswith('win') else 0
chmod_fn = Mock(wraps=_shutil.attempt_chmod_verbose)
monkeypatch.setattr(_shutil, 'attempt_chmod_verbose', chmod_fn)
_shutil.rmtree(tmp_dir)
assert chmod_fn.call_count == expected_count
assert not tmp_dir.is_dir()
```

## Next Steps


---

*Source: test_shutil_wrapper.py:8 | Complexity: Advanced | Last updated: 2026-06-02*