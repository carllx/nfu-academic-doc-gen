# How To: Read Files

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test read files

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `sys`
- `pathlib`
- `pytest`
- `setuptools._static`
- `setuptools.config`
- `setuptools.discovery`
- `distutils.errors`

**Setup Required:**
```python
# Fixtures: tmp_path, monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign dir_ = value

```python
dir_ = tmp_path / 'dir_'
```

**Verification:**
```python
assert expand.read_files(list(files)) == 'a\nb\nc'
```

### Step 2: Call unknown.mkdir()

```python
(tmp_path / '_dir').mkdir(exist_ok=True)
```

**Verification:**
```python
assert expand.read_files(list(files), dir_) == 'a\nb\nc'
```

### Step 3: Call unknown.touch()

```python
(tmp_path / 'a.txt').touch()
```

### Step 4: Assign files = value

```python
files = {'a.txt': 'a', 'dir1/b.txt': 'b', 'dir1/dir2/c.txt': 'c'}
```

### Step 5: Call write_files()

```python
write_files(files, dir_)
```

### Step 6: Assign secrets = Path(...)

```python
secrets = Path(str(dir_) + 'secrets')
```

### Step 7: Call secrets.mkdir()

```python
secrets.mkdir(exist_ok=True)
```

### Step 8: Call write_files()

```python
write_files({'secrets.txt': 'secret keys'}, secrets)
```

**Verification:**
```python
assert expand.read_files(list(files), dir_) == 'a\nb\nc'
```

### Step 9: Call m.chdir()

```python
m.chdir(dir_)
```

**Verification:**
```python
assert expand.read_files(list(files)) == 'a\nb\nc'
```

### Step 10: Assign cannot_access_msg = "Cannot access '.*\\.\\..a\\.txt'"

```python
cannot_access_msg = "Cannot access '.*\\.\\..a\\.txt'"
```

### Step 11: Assign cannot_access_secrets_msg = "Cannot access '.*secrets\\.txt'"

```python
cannot_access_secrets_msg = "Cannot access '.*secrets\\.txt'"
```

### Step 12: Call expand.read_files()

```python
expand.read_files(['../a.txt'], dir_)
```

### Step 13: Call expand.read_files()

```python
expand.read_files(['../a.txt'])
```

### Step 14: Call expand.read_files()

```python
expand.read_files(['../dir_secrets/secrets.txt'])
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, monkeypatch

# Workflow
dir_ = tmp_path / 'dir_'
(tmp_path / '_dir').mkdir(exist_ok=True)
(tmp_path / 'a.txt').touch()
files = {'a.txt': 'a', 'dir1/b.txt': 'b', 'dir1/dir2/c.txt': 'c'}
write_files(files, dir_)
secrets = Path(str(dir_) + 'secrets')
secrets.mkdir(exist_ok=True)
write_files({'secrets.txt': 'secret keys'}, secrets)
with monkeypatch.context() as m:
    m.chdir(dir_)
    assert expand.read_files(list(files)) == 'a\nb\nc'
    cannot_access_msg = "Cannot access '.*\\.\\..a\\.txt'"
    with pytest.raises(DistutilsOptionError, match=cannot_access_msg):
        expand.read_files(['../a.txt'])
    cannot_access_secrets_msg = "Cannot access '.*secrets\\.txt'"
    with pytest.raises(DistutilsOptionError, match=cannot_access_secrets_msg):
        expand.read_files(['../dir_secrets/secrets.txt'])
assert expand.read_files(list(files), dir_) == 'a\nb\nc'
with pytest.raises(DistutilsOptionError, match=cannot_access_msg):
    expand.read_files(['../a.txt'], dir_)
```

## Next Steps


---

*Source: test_expand.py:40 | Complexity: Advanced | Last updated: 2026-06-02*