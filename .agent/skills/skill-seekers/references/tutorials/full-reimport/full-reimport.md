# How To: Full Reimport

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test full reimport

## Prerequisites

**Required Modules:**
- `pickle`
- `subprocess`
- `sys`
- `textwrap`
- `importlib`
- `pytest`
- `numpy.exceptions`
- `numpy.testing`
- `numpy`
- `numpy._globals`
- `numpy`


## Step-by-Step Guide

### Step 1: Assign code = textwrap.dedent(...)

```python
code = textwrap.dedent('\n        import sys\n        import numpy as np\n\n        for k in [k for k in sys.modules if k.startswith(\'numpy\')]:\n            del sys.modules[k]\n\n        try:\n            import numpy as np\n        except ImportError as err:\n            if str(err) != "cannot load module more than once per process":\n                raise SystemExit(f"Unexpected ImportError: {err}")\n        else:\n            raise SystemExit("DID NOT RAISE ImportError")\n        ')
```

**Verification:**
```python
assert p.returncode == 0, p.stdout
```

### Step 2: Assign p = subprocess.run(...)

```python
p = subprocess.run((sys.executable, '-c', code), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8', check=False)
```

**Verification:**
```python
assert p.returncode == 0, p.stdout
```


## Complete Example

```python
# Workflow
code = textwrap.dedent('\n        import sys\n        import numpy as np\n\n        for k in [k for k in sys.modules if k.startswith(\'numpy\')]:\n            del sys.modules[k]\n\n        try:\n            import numpy as np\n        except ImportError as err:\n            if str(err) != "cannot load module more than once per process":\n                raise SystemExit(f"Unexpected ImportError: {err}")\n        else:\n            raise SystemExit("DID NOT RAISE ImportError")\n        ')
p = subprocess.run((sys.executable, '-c', code), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8', check=False)
assert p.returncode == 0, p.stdout
```

## Next Steps


---

*Source: test_reloading.py:45 | Complexity: Beginner | Last updated: 2026-06-02*