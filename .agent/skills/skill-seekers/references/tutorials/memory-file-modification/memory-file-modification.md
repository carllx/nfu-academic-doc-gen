# How To: Memory File Modification

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test memory file modification

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `gc`
- `logging`
- `os`
- `os.path`
- `pickle`
- `shutil`
- `sys`
- `textwrap`
- `time`
- `pathlib`
- `pytest`
- `joblib._store_backends`
- `joblib.hashing`
- `joblib.memory`
- `joblib.parallel`
- `joblib.test.common`
- `joblib.testing`
- `functools`
- `tmp_joblib_`
- `tmp_joblib_`
- `datetime`
- `time`

**Setup Required:**
```python
# Fixtures: capsys, tmpdir, monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign dir_name = value

```python
dir_name = tmpdir.mkdir('tmp_import').strpath
```

**Verification:**
```python
assert out == '1\n2\nReloading\nx=1\n'
```

### Step 2: Assign filename = os.path.join(...)

```python
filename = os.path.join(dir_name, 'tmp_joblib_.py')
```

### Step 3: Assign content = 'def f(x):\n    print(x)\n    return x\n'

```python
content = 'def f(x):\n    print(x)\n    return x\n'
```

### Step 4: Call monkeypatch.syspath_prepend()

```python
monkeypatch.syspath_prepend(dir_name)
```

### Step 5: Assign memory = Memory(...)

```python
memory = Memory(location=tmpdir.strpath, verbose=0)
```

### Step 6: Assign f = memory.cache(...)

```python
f = memory.cache(tmp.f)
```

### Step 7: Call f()

```python
f(1)
```

### Step 8: Call f()

```python
f(2)
```

### Step 9: Call f()

```python
f(1)
```

### Step 10: Call f()

```python
f(1)
```

### Step 11: Call f()

```python
f(1)
```

### Step 12: Call shutil.rmtree()

```python
shutil.rmtree(dir_name)
```

### Step 13: Call os.mkdir()

```python
os.mkdir(dir_name)
```

### Step 14: Assign content = 'def f(x):\n    print("x=%s" % x)\n    return x\n'

```python
content = 'def f(x):\n    print("x=%s" % x)\n    return x\n'
```

### Step 15: Call f()

```python
f(1)
```

### Step 16: Call f()

```python
f(1)
```

### Step 17: Call sys.stdout.write()

```python
sys.stdout.write('Reloading\n')
```

### Step 18: Call sys.modules.pop()

```python
sys.modules.pop('tmp_joblib_')
```

### Step 19: Assign f = memory.cache(...)

```python
f = memory.cache(tmp.f)
```

### Step 20: Call f()

```python
f(1)
```

### Step 21: Call f()

```python
f(1)
```

### Step 22: Assign unknown = capsys.readouterr(...)

```python
out, err = capsys.readouterr()
```

**Verification:**
```python
assert out == '1\n2\nReloading\nx=1\n'
```

### Step 23: Call module_file.write()

```python
module_file.write(content)
```

### Step 24: Call module_file.write()

```python
module_file.write('\n\n' + content)
```

### Step 25: Call module_file.write()

```python
module_file.write(content)
```


## Complete Example

```python
# Setup
# Fixtures: capsys, tmpdir, monkeypatch

# Workflow
dir_name = tmpdir.mkdir('tmp_import').strpath
filename = os.path.join(dir_name, 'tmp_joblib_.py')
content = 'def f(x):\n    print(x)\n    return x\n'
with open(filename, 'w') as module_file:
    module_file.write(content)
monkeypatch.syspath_prepend(dir_name)
import tmp_joblib_ as tmp
memory = Memory(location=tmpdir.strpath, verbose=0)
f = memory.cache(tmp.f)
f(1)
f(2)
f(1)
with open(filename, 'w') as module_file:
    module_file.write('\n\n' + content)
f(1)
f(1)
shutil.rmtree(dir_name)
os.mkdir(dir_name)
content = 'def f(x):\n    print("x=%s" % x)\n    return x\n'
with open(filename, 'w') as module_file:
    module_file.write(content)
f(1)
f(1)
sys.stdout.write('Reloading\n')
sys.modules.pop('tmp_joblib_')
import tmp_joblib_ as tmp
f = memory.cache(tmp.f)
f(1)
f(1)
out, err = capsys.readouterr()
assert out == '1\n2\nReloading\nx=1\n'
```

## Next Steps


---

*Source: test_memory.py:741 | Complexity: Advanced | Last updated: 2026-06-02*