# How To: Check Subprocess Call Non Zero Return Code

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check subprocess call non zero return code

## Prerequisites

**Required Modules:**
- `re`
- `sys`
- `joblib.testing`


## Step-by-Step Guide

### Step 1: Assign code_with_non_zero_exit = unknown.join(...)

```python
code_with_non_zero_exit = '\n'.join(['import sys', 'print("writing on stdout")', 'sys.stderr.write("writing on stderr")', 'sys.exit(123)'])
```

### Step 2: Assign pattern = re.compile(...)

```python
pattern = re.compile('Non-zero return code: 123.+Stdout:\nwriting on stdout.+Stderr:\nwriting on stderr', re.DOTALL)
```

### Step 3: Call excinfo.match()

```python
excinfo.match(pattern)
```

### Step 4: Call check_subprocess_call()

```python
check_subprocess_call([sys.executable, '-c', code_with_non_zero_exit])
```


## Complete Example

```python
# Workflow
code_with_non_zero_exit = '\n'.join(['import sys', 'print("writing on stdout")', 'sys.stderr.write("writing on stderr")', 'sys.exit(123)'])
pattern = re.compile('Non-zero return code: 123.+Stdout:\nwriting on stdout.+Stderr:\nwriting on stderr', re.DOTALL)
with raises(ValueError) as excinfo:
    check_subprocess_call([sys.executable, '-c', code_with_non_zero_exit])
excinfo.match(pattern)
```

## Next Steps


---

*Source: test_testing.py:39 | Complexity: Intermediate | Last updated: 2026-06-02*