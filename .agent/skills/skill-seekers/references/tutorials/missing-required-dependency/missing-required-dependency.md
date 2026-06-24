# How To: Missing Required Dependency

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test missing required dependency

## Prerequisites

**Required Modules:**
- `array`
- `subprocess`
- `sys`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.util.version`
- `sklearn`
- `dask.array`
- `xarray`


## Step-by-Step Guide

### Step 1: Assign pyexe = sys.executable.replace(...)

```python
pyexe = sys.executable.replace('\\', '/')
```

**Verification:**
```python
assert name in output
```

### Step 2: Assign call = value

```python
call = [pyexe, '-c', 'import pandas;print(pandas.__file__)']
```

### Step 3: Assign output = subprocess.check_output.decode(...)

```python
output = subprocess.check_output(call).decode()
```

### Step 4: Assign call = value

```python
call = [pyexe, '-sSE', '-c', 'import pandas']
```

### Step 5: Assign msg = value

```python
msg = f"Command '\\['{pyexe}', '-sSE', '-c', 'import pandas'\\]' returned non-zero exit status 1."
```

### Step 6: Assign output = exc.value.stdout.decode(...)

```python
output = exc.value.stdout.decode()
```

### Step 7: Call pytest.skip()

```python
pytest.skip('pandas installed as site package')
```

### Step 8: Call subprocess.check_output()

```python
subprocess.check_output(call, stderr=subprocess.STDOUT)
```

**Verification:**
```python
assert name in output
```


## Complete Example

```python
# Workflow
pyexe = sys.executable.replace('\\', '/')
call = [pyexe, '-c', 'import pandas;print(pandas.__file__)']
output = subprocess.check_output(call).decode()
if 'site-packages' in output:
    pytest.skip('pandas installed as site package')
call = [pyexe, '-sSE', '-c', 'import pandas']
msg = f"Command '\\['{pyexe}', '-sSE', '-c', 'import pandas'\\]' returned non-zero exit status 1."
with pytest.raises(subprocess.CalledProcessError, match=msg) as exc:
    subprocess.check_output(call, stderr=subprocess.STDOUT)
output = exc.value.stdout.decode()
for name in ['numpy', 'pytz', 'dateutil']:
    assert name in output
```

## Next Steps


---

*Source: test_downstream.py:191 | Complexity: Advanced | Last updated: 2026-06-02*