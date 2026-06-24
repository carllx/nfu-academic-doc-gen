# How To: Dispatcher

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Testing the utilities of the CPU dispatcher

## Prerequisites

**Required Modules:**
- `numpy._core`
- `numpy._core._multiarray_umath`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: '\n    Testing the utilities of the CPU dispatcher\n    '

```python
'\n    Testing the utilities of the CPU dispatcher\n    '
```

**Verification:**
```python
assert_equal(test['func'], 'func' + highest_sfx)
```

### Step 2: Assign targets = value

```python
targets = ('X86_V2', 'X86_V3', 'VSX', 'VSX2', 'VSX3', 'NEON', 'ASIMD', 'ASIMDHP', 'VX', 'VXE', 'LSX', 'RVV')
```

**Verification:**
```python
assert_equal(test['var'], 'var' + highest_sfx)
```

### Step 3: Assign highest_sfx = ''

```python
highest_sfx = ''
```

**Verification:**
```python
assert_equal(test['func_xb'], 'func' + highest_sfx)
```

### Step 4: Assign all_sfx = value

```python
all_sfx = []
```

**Verification:**
```python
assert_equal(test['var_xb'], 'var' + highest_sfx)
```

### Step 5: Assign test = _umath_tests.test_dispatch(...)

```python
test = _umath_tests.test_dispatch()
```

**Verification:**
```python
assert_equal(test['func_xb'], 'nobase')
```

### Step 6: Call assert_equal()

```python
assert_equal(test['func'], 'func' + highest_sfx)
```

**Verification:**
```python
assert_equal(test['var_xb'], 'nobase')
```

### Step 7: Call assert_equal()

```python
assert_equal(test['var'], 'var' + highest_sfx)
```

**Verification:**
```python
assert_equal(test['all'], all_sfx)
```

### Step 8: Call all_sfx.append()

```python
all_sfx.append('func')
```

### Step 9: Call assert_equal()

```python
assert_equal(test['all'], all_sfx)
```

### Step 10: Call all_sfx.append()

```python
all_sfx.append('func' + '_' + feature)
```

### Step 11: Call assert_equal()

```python
assert_equal(test['func_xb'], 'func' + highest_sfx)
```

### Step 12: Call assert_equal()

```python
assert_equal(test['var_xb'], 'var' + highest_sfx)
```

### Step 13: Call assert_equal()

```python
assert_equal(test['func_xb'], 'nobase')
```

### Step 14: Call assert_equal()

```python
assert_equal(test['var_xb'], 'nobase')
```

### Step 15: Assign highest_sfx = value

```python
highest_sfx = '_' + feature
```


## Complete Example

```python
# Workflow
'\n    Testing the utilities of the CPU dispatcher\n    '
targets = ('X86_V2', 'X86_V3', 'VSX', 'VSX2', 'VSX3', 'NEON', 'ASIMD', 'ASIMDHP', 'VX', 'VXE', 'LSX', 'RVV')
highest_sfx = ''
all_sfx = []
for feature in reversed(targets):
    if feature in __cpu_baseline__:
        continue
    if feature not in __cpu_dispatch__ or not __cpu_features__[feature]:
        continue
    if not highest_sfx:
        highest_sfx = '_' + feature
    all_sfx.append('func' + '_' + feature)
test = _umath_tests.test_dispatch()
assert_equal(test['func'], 'func' + highest_sfx)
assert_equal(test['var'], 'var' + highest_sfx)
if highest_sfx:
    assert_equal(test['func_xb'], 'func' + highest_sfx)
    assert_equal(test['var_xb'], 'var' + highest_sfx)
else:
    assert_equal(test['func_xb'], 'nobase')
    assert_equal(test['var_xb'], 'nobase')
all_sfx.append('func')
assert_equal(test['all'], all_sfx)
```

## Next Steps


---

*Source: test_cpu_dispatcher.py:10 | Complexity: Advanced | Last updated: 2026-06-02*