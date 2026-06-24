# How To: Check Subprocess Call Timeout

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check subprocess call timeout

## Prerequisites

**Required Modules:**
- `re`
- `sys`
- `joblib.testing`


## Step-by-Step Guide

### Step 1: Assign code_timing_out = unknown.join(...)

```python
code_timing_out = '\n'.join(['import time', 'import sys', 'print("before sleep on stdout")', 'sys.stdout.flush()', 'sys.stderr.write("before sleep on stderr")', 'sys.stderr.flush()', 'time.sleep(10)', 'print("process should have be killed before")', 'sys.stdout.flush()'])
```

### Step 2: Assign pattern = re.compile(...)

```python
pattern = re.compile('Non-zero return code:.+Stdout:\nbefore sleep on stdout\\s+Stderr:\nbefore sleep on stderr', re.DOTALL)
```

### Step 3: Call excinfo.match()

```python
excinfo.match(pattern)
```

### Step 4: Call check_subprocess_call()

```python
check_subprocess_call([sys.executable, '-c', code_timing_out], timeout=1)
```


## Complete Example

```python
# Workflow
code_timing_out = '\n'.join(['import time', 'import sys', 'print("before sleep on stdout")', 'sys.stdout.flush()', 'sys.stderr.write("before sleep on stderr")', 'sys.stderr.flush()', 'time.sleep(10)', 'print("process should have be killed before")', 'sys.stdout.flush()'])
pattern = re.compile('Non-zero return code:.+Stdout:\nbefore sleep on stdout\\s+Stderr:\nbefore sleep on stderr', re.DOTALL)
with raises(ValueError) as excinfo:
    check_subprocess_call([sys.executable, '-c', code_timing_out], timeout=1)
excinfo.match(pattern)
```

## Next Steps


---

*Source: test_testing.py:61 | Complexity: Intermediate | Last updated: 2026-06-02*