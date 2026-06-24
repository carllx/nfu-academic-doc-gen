# How To: Version

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test version

## Prerequisites

**Required Modules:**
- `__future__`
- `__future__`
- `sys`
- `os`
- `unittest`
- `greenlet`


## Step-by-Step Guide

### Step 1: Assign invoke_setup = value

```python
invoke_setup = '%s %s --version' % (sys.executable, setup_py)
```

### Step 2: Call self.assertEqual()

```python
self.assertEqual(sversion, greenlet.__version__)
```

### Step 3: Assign tried = value

```python
tried = []
```

### Step 4: Assign here = os.path.abspath(...)

```python
here = os.path.abspath(os.path.dirname(__file__))
```

### Step 5: Assign setup_py = find_dominating_file(...)

```python
setup_py = find_dominating_file('setup.py')
```

### Step 6: Assign sversion = f.read.strip(...)

```python
sversion = f.read().strip()
```

### Step 7: Assign up = value

```python
up = ['..'] * i
```

### Step 8: Assign path = value

```python
path = [here] + up + [name]
```

### Step 9: Assign fname = os.path.join(...)

```python
fname = os.path.join(*path)
```

### Step 10: Assign fname = os.path.abspath(...)

```python
fname = os.path.abspath(fname)
```

### Step 11: Call tried.append()

```python
tried.append(fname)
```

### Step 12: Call self.skipTest()

```python
self.skipTest('Unable to find setup.py; must be out of tree. ' + str(e))
```


## Complete Example

```python
# Workflow
def find_dominating_file(name):
    if os.path.exists(name):
        return name
    tried = []
    here = os.path.abspath(os.path.dirname(__file__))
    for i in range(10):
        up = ['..'] * i
        path = [here] + up + [name]
        fname = os.path.join(*path)
        fname = os.path.abspath(fname)
        tried.append(fname)
        if os.path.exists(fname):
            return fname
    raise AssertionError('Could not find file ' + name + '; checked ' + str(tried))
try:
    setup_py = find_dominating_file('setup.py')
except AssertionError as e:
    self.skipTest('Unable to find setup.py; must be out of tree. ' + str(e))
invoke_setup = '%s %s --version' % (sys.executable, setup_py)
with os.popen(invoke_setup) as f:
    sversion = f.read().strip()
self.assertEqual(sversion, greenlet.__version__)
```

## Next Steps


---

*Source: test_version.py:14 | Complexity: Advanced | Last updated: 2026-06-02*