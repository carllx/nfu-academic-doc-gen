# How To: Wheel Mode

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wheel mode

## Prerequisites

**Required Modules:**
- `__future__`
- `contextlib`
- `glob`
- `inspect`
- `os`
- `pathlib`
- `stat`
- `subprocess`
- `sys`
- `sysconfig`
- `zipfile`
- `typing`
- `pytest`
- `jaraco`
- `packaging.tags`
- `setuptools._importlib`
- `setuptools.wheel`
- `contexts`
- `textwrap`
- `distutils.sysconfig`
- `distutils.util`


## Step-by-Step Guide

### Step 1: Assign params = dict(...)

```python
params = dict(id='script', file_defs={'script.py': DALS("\n                #/usr/bin/python\n                print('hello world!')\n                "), 'script.sh': DALS("\n                #/bin/sh\n                echo 'hello world!'\n                ")}, setup_kwargs=dict(scripts=['script.py', 'script.sh']), install_tree=flatten_tree({'foo-1.0-py{py_version}.egg': {'EGG-INFO': ['PKG-INFO', 'RECORD', 'WHEEL', 'top_level.txt', {'scripts': ['script.py', 'script.sh']}]}}))
```

**Verification:**
```python
assert script_sh.exists()
```

### Step 2: Assign project_name = params.get(...)

```python
project_name = params.get('name', 'foo')
```

**Verification:**
```python
assert oct(stat.S_IMODE(script_sh.stat().st_mode)) == '0o777'
```

### Step 3: Assign version = params.get(...)

```python
version = params.get('version', '1.0')
```

### Step 4: Assign install_tree = params.get(...)

```python
install_tree = params.get('install_tree')
```

### Step 5: Assign file_defs = params.get(...)

```python
file_defs = params.get('file_defs', {})
```

### Step 6: Assign setup_kwargs = params.get(...)

```python
setup_kwargs = params.get('setup_kwargs', {})
```

### Step 7: Assign file_defs = value

```python
file_defs = {'setup.py': (DALS('\n                # -*- coding: utf-8 -*-\n                from setuptools import setup\n                import setuptools\n                setup(**%r)\n                ') % kwargs).encode('utf-8')}
```

### Step 8: Call _check_wheel_install()

```python
_check_wheel_install(filename, install_dir, install_tree, project_name, version, None)
```

### Step 9: Assign w = Wheel(...)

```python
w = Wheel(filename)
```

### Step 10: Assign base = value

```python
base = pathlib.Path(install_dir) / w.egg_name()
```

### Step 11: Assign script_sh = value

```python
script_sh = base / 'EGG-INFO' / 'scripts' / 'script.sh'
```

**Verification:**
```python
assert script_sh.exists()
```

### Step 12: Call file_defs.update()

```python
file_defs.update(extra_file_defs)
```

### Step 13: Call path.build()

```python
path.build(file_defs, source_dir)
```

### Step 14: Assign runsh = value

```python
runsh = pathlib.Path(source_dir) / 'script.sh'
```

### Step 15: Call os.chmod()

```python
os.chmod(runsh, 511)
```

### Step 16: Call subprocess.check_call()

```python
subprocess.check_call((sys.executable, 'setup.py', '-q', 'bdist_wheel'), cwd=source_dir)
```

### Step 17: yield glob.glob(os.path.join(source_dir, 'dist', '*.whl'))[0]

```python
yield glob.glob(os.path.join(source_dir, 'dist', '*.whl'))[0]
```

**Verification:**
```python
assert oct(stat.S_IMODE(script_sh.stat().st_mode)) == '0o777'
```


## Complete Example

```python
# Workflow
@contextlib.contextmanager
def build_wheel(extra_file_defs=None, **kwargs):
    file_defs = {'setup.py': (DALS('\n                # -*- coding: utf-8 -*-\n                from setuptools import setup\n                import setuptools\n                setup(**%r)\n                ') % kwargs).encode('utf-8')}
    if extra_file_defs:
        file_defs.update(extra_file_defs)
    with tempdir() as source_dir:
        path.build(file_defs, source_dir)
        runsh = pathlib.Path(source_dir) / 'script.sh'
        os.chmod(runsh, 511)
        subprocess.check_call((sys.executable, 'setup.py', '-q', 'bdist_wheel'), cwd=source_dir)
        yield glob.glob(os.path.join(source_dir, 'dist', '*.whl'))[0]
params = dict(id='script', file_defs={'script.py': DALS("\n                #/usr/bin/python\n                print('hello world!')\n                "), 'script.sh': DALS("\n                #/bin/sh\n                echo 'hello world!'\n                ")}, setup_kwargs=dict(scripts=['script.py', 'script.sh']), install_tree=flatten_tree({'foo-1.0-py{py_version}.egg': {'EGG-INFO': ['PKG-INFO', 'RECORD', 'WHEEL', 'top_level.txt', {'scripts': ['script.py', 'script.sh']}]}}))
project_name = params.get('name', 'foo')
version = params.get('version', '1.0')
install_tree = params.get('install_tree')
file_defs = params.get('file_defs', {})
setup_kwargs = params.get('setup_kwargs', {})
with build_wheel(name=project_name, version=version, install_requires=[], extras_require={}, extra_file_defs=file_defs, **setup_kwargs) as filename, tempdir() as install_dir:
    _check_wheel_install(filename, install_dir, install_tree, project_name, version, None)
    w = Wheel(filename)
    base = pathlib.Path(install_dir) / w.egg_name()
    script_sh = base / 'EGG-INFO' / 'scripts' / 'script.sh'
    assert script_sh.exists()
    if sys.platform != 'win32':
        assert oct(stat.S_IMODE(script_sh.stat().st_mode)) == '0o777'
```

## Next Steps


---

*Source: test_wheel.py:605 | Complexity: Advanced | Last updated: 2026-06-02*