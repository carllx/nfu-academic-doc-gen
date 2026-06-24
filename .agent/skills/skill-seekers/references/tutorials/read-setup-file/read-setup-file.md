# How To: Read Setup File

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read setup file

## Prerequisites

**Required Modules:**
- `os`
- `pathlib`
- `warnings`
- `distutils.extension`
- `pytest`
- `test.support.warnings_helper`


## Step-by-Step Guide

### Step 1: Assign setup = os.path.join(...)

```python
setup = os.path.join(os.path.dirname(__file__), 'Setup.sample')
```

**Verification:**
```python
assert names == wanted
```

### Step 2: Assign exts = read_setup_file(...)

```python
exts = read_setup_file(setup)
```

### Step 3: Assign names = value

```python
names = [ext.name for ext in exts]
```

### Step 4: Call names.sort()

```python
names.sort()
```

### Step 5: Assign wanted = value

```python
wanted = ['_arraysurfarray', '_camera', '_numericsndarray', '_numericsurfarray', 'base', 'bufferproxy', 'cdrom', 'color', 'constants', 'display', 'draw', 'event', 'fastevent', 'font', 'gfxdraw', 'image', 'imageext', 'joystick', 'key', 'mask', 'mixer', 'mixer_music', 'mouse', 'movie', 'overlay', 'pixelarray', 'pypm', 'rect', 'rwobject', 'scrap', 'surface', 'surflock', 'time', 'transform']
```

**Verification:**
```python
assert names == wanted
```


## Complete Example

```python
# Workflow
setup = os.path.join(os.path.dirname(__file__), 'Setup.sample')
exts = read_setup_file(setup)
names = [ext.name for ext in exts]
names.sort()
wanted = ['_arraysurfarray', '_camera', '_numericsndarray', '_numericsurfarray', 'base', 'bufferproxy', 'cdrom', 'color', 'constants', 'display', 'draw', 'event', 'fastevent', 'font', 'gfxdraw', 'image', 'imageext', 'joystick', 'key', 'mask', 'mixer', 'mixer_music', 'mouse', 'movie', 'overlay', 'pixelarray', 'pypm', 'rect', 'rwobject', 'scrap', 'surface', 'surflock', 'time', 'transform']
assert names == wanted
```

## Next Steps


---

*Source: test_extension.py:13 | Complexity: Intermediate | Last updated: 2026-06-02*