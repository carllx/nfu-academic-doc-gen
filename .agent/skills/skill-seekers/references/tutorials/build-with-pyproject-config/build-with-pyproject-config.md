# How To: Build With Pyproject Config

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test build with pyproject config

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `importlib`
- `os`
- `re`
- `shutil`
- `signal`
- `sys`
- `tarfile`
- `warnings`
- `concurrent`
- `pathlib`
- `typing`
- `zipfile`
- `pytest`
- `jaraco`
- `packaging.requirements`
- `setuptools.warnings`
- `textwrap`

**Setup Required:**
```python
# Fixtures: tmpdir, setup_script
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = {'pyproject.toml': DALS('\n                [build-system]\n                requires = ["setuptools", "wheel"]\n                build-backend = "setuptools.build_meta"\n\n                [project]\n                name = "foo"\n                license = {text = "MIT"}\n                description = "This is a Python package"\n                dynamic = ["version", "readme"]\n                classifiers = [\n                    "Development Status :: 5 - Production/Stable",\n                    "Intended Audience :: Developers"\n                ]\n                urls = {Homepage = "http://github.com"}\n                dependencies = [\n                    "appdirs",\n                ]\n\n                [project.optional-dependencies]\n                all = [\n                    "tomli>=1",\n                    "pyscaffold>=4,<5",\n                    \'importlib; python_version == "2.6"\',\n                ]\n\n                [project.scripts]\n                foo = "foo.cli:main"\n\n                [tool.setuptools]\n                zip-safe = false\n                package-dir = {"" = "src"}\n                packages = {find = {where = ["src"]}}\n                license-files = ["LICENSE*"]\n\n                [tool.setuptools.dynamic]\n                version = {attr = "foo.__version__"}\n                readme = {file = "README.rst"}\n\n                [tool.distutils.sdist]\n                formats = "gztar"\n                '), 'MANIFEST.in': DALS('\n                global-include *.py *.txt\n                global-exclude *.py[cod]\n                '), 'README.rst': 'This is a ``README``', 'LICENSE.txt': '---- placeholder MIT license ----', 'src': {'foo': {'__init__.py': "__version__ = '0.1'", '__init__.pyi': '__version__: str', 'cli.py': "def main(): print('hello world')", 'data.txt': "def main(): print('hello world')", 'py.typed': ''}}}
```

**Verification:**
```python
assert sdist_contents - {'foo-0.1/setup.py'} == {'foo-0.1', 'foo-0.1/LICENSE.txt', 'foo-0.1/MANIFEST.in', 'foo-0.1/PKG-INFO', 'foo-0.1/README.rst', 'foo-0.1/pyproject.toml', 'foo-0.1/setup.cfg', 'foo-0.1/src', 'foo-0.1/src/foo', 'foo-0.1/src/foo/__init__.py', 'foo-0.1/src/foo/__init__.pyi', 'foo-0.1/src/foo/cli.py', 'foo-0.1/src/foo/data.txt', 'foo-0.1/src/foo/py.typed', 'foo-0.1/src/foo.egg-info', 'foo-0.1/src/foo.egg-info/PKG-INFO', 'foo-0.1/src/foo.egg-info/SOURCES.txt', 'foo-0.1/src/foo.egg-info/dependency_links.txt', 'foo-0.1/src/foo.egg-info/entry_points.txt', 'foo-0.1/src/foo.egg-info/requires.txt', 'foo-0.1/src/foo.egg-info/top_level.txt', 'foo-0.1/src/foo.egg-info/not-zip-safe'}
```

### Step 2: Assign build_backend = self.get_build_backend(...)

```python
build_backend = self.get_build_backend()
```

**Verification:**
```python
assert wheel_contents == {'foo/__init__.py', 'foo/__init__.pyi', 'foo/cli.py', 'foo/data.txt', 'foo/py.typed', 'foo-0.1.dist-info/licenses/LICENSE.txt', 'foo-0.1.dist-info/METADATA', 'foo-0.1.dist-info/WHEEL', 'foo-0.1.dist-info/entry_points.txt', 'foo-0.1.dist-info/top_level.txt', 'foo-0.1.dist-info/RECORD'}
```

### Step 3: Assign unknown = setup_script

```python
files['setup.py'] = setup_script
```

**Verification:**
```python
assert license == '---- placeholder MIT license ----'
```

### Step 4: Call path.build()

```python
path.build(files)
```

**Verification:**
```python
assert line in metadata, (line, metadata)
```

### Step 5: Assign msgs = value

```python
msgs = ["'tool.setuptools.license-files' is deprecated in favor of 'project.license-files'", '`project.license` as a TOML table is deprecated']
```

**Verification:**
```python
assert metadata.strip().endswith('This is a ``README``')
```

### Step 6: Assign sdist_contents = set(...)

```python
sdist_contents = set(tar.getnames())
```

**Verification:**
```python
assert epoints.strip() == '[console_scripts]\nfoo = foo.cli:main'
```

### Step 7: Assign wheel_contents = set(...)

```python
wheel_contents = set(zipfile.namelist())
```

### Step 8: Assign metadata = str(...)

```python
metadata = str(zipfile.read('foo-0.1.dist-info/METADATA'), 'utf-8')
```

### Step 9: Assign license = str(...)

```python
license = str(zipfile.read('foo-0.1.dist-info/licenses/LICENSE.txt'), 'utf-8')
```

### Step 10: Assign epoints = str(...)

```python
epoints = str(zipfile.read('foo-0.1.dist-info/entry_points.txt'), 'utf-8')
```

**Verification:**
```python
assert line in metadata, (line, metadata)
```

### Step 11: Assign sdist_path = build_backend.build_sdist(...)

```python
sdist_path = build_backend.build_sdist('temp')
```

### Step 12: Assign wheel_file = build_backend.build_wheel(...)

```python
wheel_file = build_backend.build_wheel('temp')
```

### Step 13: Call warnings.filterwarnings()

```python
warnings.filterwarnings('ignore', msg, SetuptoolsDeprecationWarning)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir, setup_script

# Workflow
files = {'pyproject.toml': DALS('\n                [build-system]\n                requires = ["setuptools", "wheel"]\n                build-backend = "setuptools.build_meta"\n\n                [project]\n                name = "foo"\n                license = {text = "MIT"}\n                description = "This is a Python package"\n                dynamic = ["version", "readme"]\n                classifiers = [\n                    "Development Status :: 5 - Production/Stable",\n                    "Intended Audience :: Developers"\n                ]\n                urls = {Homepage = "http://github.com"}\n                dependencies = [\n                    "appdirs",\n                ]\n\n                [project.optional-dependencies]\n                all = [\n                    "tomli>=1",\n                    "pyscaffold>=4,<5",\n                    \'importlib; python_version == "2.6"\',\n                ]\n\n                [project.scripts]\n                foo = "foo.cli:main"\n\n                [tool.setuptools]\n                zip-safe = false\n                package-dir = {"" = "src"}\n                packages = {find = {where = ["src"]}}\n                license-files = ["LICENSE*"]\n\n                [tool.setuptools.dynamic]\n                version = {attr = "foo.__version__"}\n                readme = {file = "README.rst"}\n\n                [tool.distutils.sdist]\n                formats = "gztar"\n                '), 'MANIFEST.in': DALS('\n                global-include *.py *.txt\n                global-exclude *.py[cod]\n                '), 'README.rst': 'This is a ``README``', 'LICENSE.txt': '---- placeholder MIT license ----', 'src': {'foo': {'__init__.py': "__version__ = '0.1'", '__init__.pyi': '__version__: str', 'cli.py': "def main(): print('hello world')", 'data.txt': "def main(): print('hello world')", 'py.typed': ''}}}
if setup_script:
    files['setup.py'] = setup_script
build_backend = self.get_build_backend()
with tmpdir.as_cwd():
    path.build(files)
    msgs = ["'tool.setuptools.license-files' is deprecated in favor of 'project.license-files'", '`project.license` as a TOML table is deprecated']
    with warnings.catch_warnings():
        for msg in msgs:
            warnings.filterwarnings('ignore', msg, SetuptoolsDeprecationWarning)
        sdist_path = build_backend.build_sdist('temp')
        wheel_file = build_backend.build_wheel('temp')
with tarfile.open(os.path.join(tmpdir, 'temp', sdist_path)) as tar:
    sdist_contents = set(tar.getnames())
with ZipFile(os.path.join(tmpdir, 'temp', wheel_file)) as zipfile:
    wheel_contents = set(zipfile.namelist())
    metadata = str(zipfile.read('foo-0.1.dist-info/METADATA'), 'utf-8')
    license = str(zipfile.read('foo-0.1.dist-info/licenses/LICENSE.txt'), 'utf-8')
    epoints = str(zipfile.read('foo-0.1.dist-info/entry_points.txt'), 'utf-8')
assert sdist_contents - {'foo-0.1/setup.py'} == {'foo-0.1', 'foo-0.1/LICENSE.txt', 'foo-0.1/MANIFEST.in', 'foo-0.1/PKG-INFO', 'foo-0.1/README.rst', 'foo-0.1/pyproject.toml', 'foo-0.1/setup.cfg', 'foo-0.1/src', 'foo-0.1/src/foo', 'foo-0.1/src/foo/__init__.py', 'foo-0.1/src/foo/__init__.pyi', 'foo-0.1/src/foo/cli.py', 'foo-0.1/src/foo/data.txt', 'foo-0.1/src/foo/py.typed', 'foo-0.1/src/foo.egg-info', 'foo-0.1/src/foo.egg-info/PKG-INFO', 'foo-0.1/src/foo.egg-info/SOURCES.txt', 'foo-0.1/src/foo.egg-info/dependency_links.txt', 'foo-0.1/src/foo.egg-info/entry_points.txt', 'foo-0.1/src/foo.egg-info/requires.txt', 'foo-0.1/src/foo.egg-info/top_level.txt', 'foo-0.1/src/foo.egg-info/not-zip-safe'}
assert wheel_contents == {'foo/__init__.py', 'foo/__init__.pyi', 'foo/cli.py', 'foo/data.txt', 'foo/py.typed', 'foo-0.1.dist-info/licenses/LICENSE.txt', 'foo-0.1.dist-info/METADATA', 'foo-0.1.dist-info/WHEEL', 'foo-0.1.dist-info/entry_points.txt', 'foo-0.1.dist-info/top_level.txt', 'foo-0.1.dist-info/RECORD'}
assert license == '---- placeholder MIT license ----'
for line in ('Summary: This is a Python package', 'License: MIT', 'License-File: LICENSE.txt', 'Classifier: Intended Audience :: Developers', 'Requires-Dist: appdirs', 'Requires-Dist: ' + str(Requirement('tomli>=1 ; extra == "all"')), 'Requires-Dist: ' + str(Requirement('importlib; python_version=="2.6" and extra =="all"'))):
    assert line in metadata, (line, metadata)
assert metadata.strip().endswith('This is a ``README``')
assert epoints.strip() == '[console_scripts]\nfoo = foo.cli:main'
```

## Next Steps


---

*Source: test_build_meta.py:320 | Complexity: Advanced | Last updated: 2026-06-02*