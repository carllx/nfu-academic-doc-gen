# How To: Pyinstaller

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Compile and run pyinstaller-smoke.py using PyInstaller.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `subprocess`
- `pathlib`
- `pytest`

**Setup Required:**
```python
# Fixtures: mode, tmp_path
```

## Step-by-Step Guide

### Step 1: 'Compile and run pyinstaller-smoke.py using PyInstaller.'

```python
'Compile and run pyinstaller-smoke.py using PyInstaller.'
```

**Verification:**
```python
assert p.stdout.strip() == b'I made it!'
```

### Step 2: Assign pyinstaller_cli = value

```python
pyinstaller_cli = pytest.importorskip('PyInstaller.__main__').run
```

### Step 3: Assign source = Path.with_name.resolve(...)

```python
source = Path(__file__).with_name('pyinstaller-smoke.py').resolve()
```

### Step 4: Assign args = value

```python
args = ['--workpath', str(tmp_path / 'build'), '--distpath', str(tmp_path / 'dist'), '--specpath', str(tmp_path), mode, str(source)]
```

### Step 5: Call pyinstaller_cli()

```python
pyinstaller_cli(args)
```

### Step 6: Assign p = subprocess.run(...)

```python
p = subprocess.run([str(exe)], check=True, stdout=subprocess.PIPE)
```

**Verification:**
```python
assert p.stdout.strip() == b'I made it!'
```

### Step 7: Assign exe = value

```python
exe = tmp_path / 'dist' / source.stem
```

### Step 8: Assign exe = value

```python
exe = tmp_path / 'dist' / source.stem / source.stem
```


## Complete Example

```python
# Setup
# Fixtures: mode, tmp_path

# Workflow
'Compile and run pyinstaller-smoke.py using PyInstaller.'
pyinstaller_cli = pytest.importorskip('PyInstaller.__main__').run
source = Path(__file__).with_name('pyinstaller-smoke.py').resolve()
args = ['--workpath', str(tmp_path / 'build'), '--distpath', str(tmp_path / 'dist'), '--specpath', str(tmp_path), mode, str(source)]
pyinstaller_cli(args)
if mode == '--onefile':
    exe = tmp_path / 'dist' / source.stem
else:
    exe = tmp_path / 'dist' / source.stem / source.stem
p = subprocess.run([str(exe)], check=True, stdout=subprocess.PIPE)
assert p.stdout.strip() == b'I made it!'
```

## Next Steps


---

*Source: test_pyinstaller.py:13 | Complexity: Advanced | Last updated: 2026-06-02*