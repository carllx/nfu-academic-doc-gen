# How To: Symlink

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Ensure that symlink for the foo.exe is working correctly.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pathlib`
- `platform`
- `subprocess`
- `sys`
- `textwrap`
- `pytest`
- `setuptools._importlib`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: '\n        Ensure that symlink for the foo.exe is working correctly.\n        '

```python
'\n        Ensure that symlink for the foo.exe is working correctly.\n        '
```

**Verification:**
```python
assert actual == expected
```

### Step 2: Assign script_dir = value

```python
script_dir = tmpdir / 'script_dir'
```

### Step 3: Call script_dir.mkdir()

```python
script_dir.mkdir()
```

### Step 4: Call self.create_script()

```python
self.create_script(script_dir)
```

### Step 5: Assign symlink = pathlib.Path(...)

```python
symlink = pathlib.Path(tmpdir / 'foo.exe')
```

### Step 6: Call symlink.symlink_to()

```python
symlink.symlink_to(script_dir / 'foo.exe')
```

### Step 7: Assign cmd = value

```python
cmd = [str(tmpdir / 'foo.exe'), 'arg1', 'arg 2', 'arg "2\\"', 'arg 4\\', 'arg5 a\\\\b']
```

### Step 8: Assign proc = subprocess.Popen(...)

```python
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True, encoding='utf-8')
```

### Step 9: Assign unknown = proc.communicate(...)

```python
stdout, _stderr = proc.communicate('hello\nworld\n')
```

### Step 10: Assign actual = stdout.replace(...)

```python
actual = stdout.replace('\r\n', '\n')
```

### Step 11: Assign expected = textwrap.dedent.lstrip(...)

```python
expected = textwrap.dedent('\n            \\foo-script.py\n            [\'arg1\', \'arg 2\', \'arg "2\\\\"\', \'arg 4\\\\\', \'arg5 a\\\\\\\\b\']\n            \'hello\\nworld\\n\'\n            non-optimized\n            ').lstrip()
```

**Verification:**
```python
assert actual == expected
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
'\n        Ensure that symlink for the foo.exe is working correctly.\n        '
script_dir = tmpdir / 'script_dir'
script_dir.mkdir()
self.create_script(script_dir)
symlink = pathlib.Path(tmpdir / 'foo.exe')
symlink.symlink_to(script_dir / 'foo.exe')
cmd = [str(tmpdir / 'foo.exe'), 'arg1', 'arg 2', 'arg "2\\"', 'arg 4\\', 'arg5 a\\\\b']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True, encoding='utf-8')
stdout, _stderr = proc.communicate('hello\nworld\n')
actual = stdout.replace('\r\n', '\n')
expected = textwrap.dedent('\n            \\foo-script.py\n            [\'arg1\', \'arg 2\', \'arg "2\\\\"\', \'arg 4\\\\\', \'arg5 a\\\\\\\\b\']\n            \'hello\\nworld\\n\'\n            non-optimized\n            ').lstrip()
assert actual == expected
```

## Next Steps


---

*Source: test_windows_wrappers.py:130 | Complexity: Advanced | Last updated: 2026-06-02*