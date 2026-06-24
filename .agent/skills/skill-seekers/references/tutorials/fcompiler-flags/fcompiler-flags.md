# How To: Fcompiler Flags

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test fcompiler flags

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy.testing`
- `numpy.distutils.fcompiler`

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Call monkeypatch.setenv()

```python
monkeypatch.setenv('NPY_DISTUTILS_APPEND_FLAGS', '0')
```

**Verification:**
```python
assert_(new_flags == [new_flag])
```

### Step 2: Assign fc = numpy.distutils.fcompiler.new_fcompiler(...)

```python
fc = numpy.distutils.fcompiler.new_fcompiler(compiler='none')
```

**Verification:**
```python
assert_(new_flags == [new_flag])
```

### Step 3: Assign flag_vars = fc.flag_vars.clone(...)

```python
flag_vars = fc.flag_vars.clone(lambda *args, **kwargs: None)
```

**Verification:**
```python
assert_(new_flags == prev_flags + [new_flag])
```

### Step 4: Call monkeypatch.setenv()

```python
monkeypatch.setenv('NPY_DISTUTILS_APPEND_FLAGS', '1')
```

### Step 5: Assign new_flag = unknown.format(...)

```python
new_flag = '-dummy-{}-flag'.format(opt)
```

### Step 6: Assign prev_flags = getattr(...)

```python
prev_flags = getattr(flag_vars, opt)
```

### Step 7: Call monkeypatch.setenv()

```python
monkeypatch.setenv(envvar, new_flag)
```

### Step 8: Assign new_flags = getattr(...)

```python
new_flags = getattr(flag_vars, opt)
```

### Step 9: Call monkeypatch.delenv()

```python
monkeypatch.delenv(envvar)
```

### Step 10: Call assert_()

```python
assert_(new_flags == [new_flag])
```

### Step 11: Assign new_flag = unknown.format(...)

```python
new_flag = '-dummy-{}-flag'.format(opt)
```

### Step 12: Assign prev_flags = getattr(...)

```python
prev_flags = getattr(flag_vars, opt)
```

### Step 13: Call monkeypatch.setenv()

```python
monkeypatch.setenv(envvar, new_flag)
```

### Step 14: Assign new_flags = getattr(...)

```python
new_flags = getattr(flag_vars, opt)
```

### Step 15: Call monkeypatch.delenv()

```python
monkeypatch.delenv(envvar)
```

### Step 16: Call assert_()

```python
assert_(new_flags == [new_flag])
```

### Step 17: Call assert_()

```python
assert_(new_flags == prev_flags + [new_flag])
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
monkeypatch.setenv('NPY_DISTUTILS_APPEND_FLAGS', '0')
fc = numpy.distutils.fcompiler.new_fcompiler(compiler='none')
flag_vars = fc.flag_vars.clone(lambda *args, **kwargs: None)
for opt, envvar in customizable_flags:
    new_flag = '-dummy-{}-flag'.format(opt)
    prev_flags = getattr(flag_vars, opt)
    monkeypatch.setenv(envvar, new_flag)
    new_flags = getattr(flag_vars, opt)
    monkeypatch.delenv(envvar)
    assert_(new_flags == [new_flag])
monkeypatch.setenv('NPY_DISTUTILS_APPEND_FLAGS', '1')
for opt, envvar in customizable_flags:
    new_flag = '-dummy-{}-flag'.format(opt)
    prev_flags = getattr(flag_vars, opt)
    monkeypatch.setenv(envvar, new_flag)
    new_flags = getattr(flag_vars, opt)
    monkeypatch.delenv(envvar)
    if prev_flags is None:
        assert_(new_flags == [new_flag])
    else:
        assert_(new_flags == prev_flags + [new_flag])
```

## Next Steps


---

*Source: test_fcompiler.py:15 | Complexity: Advanced | Last updated: 2026-06-02*