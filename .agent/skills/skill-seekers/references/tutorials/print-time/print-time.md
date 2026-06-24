# How To: Print Time

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test print time

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `joblib.logger`

**Setup Required:**
```python
# Fixtures: tmpdir, capsys
```

## Step-by-Step Guide

### Step 1: Assign logfile = value

```python
logfile = tmpdir.join('test.log').strpath
```

### Step 2: Assign print_time = PrintTime(...)

```python
print_time = PrintTime(logfile=logfile)
```

### Step 3: Call print_time()

```python
print_time('Foo')
```

### Step 4: Assign print_time = PrintTime(...)

```python
print_time = PrintTime(logfile=logfile)
```

### Step 5: Call print_time()

```python
print_time('Foo')
```

### Step 6: Assign print_time = PrintTime(...)

```python
print_time = PrintTime(logfile=logfile)
```

### Step 7: Call print_time()

```python
print_time('Foo')
```

### Step 8: Assign unknown = capsys.readouterr(...)

```python
out_printed_text, err_printed_text = capsys.readouterr()
```

### Step 9: Assign match = value

```python
match = 'Foo: 0\\..s, 0\\..min\\nFoo: 0\\..s, 0..min\\nFoo: ' + '.\\..s, 0..min\\n'
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir, capsys

# Workflow
logfile = tmpdir.join('test.log').strpath
print_time = PrintTime(logfile=logfile)
print_time('Foo')
print_time = PrintTime(logfile=logfile)
print_time('Foo')
print_time = PrintTime(logfile=logfile)
print_time('Foo')
out_printed_text, err_printed_text = capsys.readouterr()
match = 'Foo: 0\\..s, 0\\..min\\nFoo: 0\\..s, 0..min\\nFoo: ' + '.\\..s, 0..min\\n'
if not re.match(match, err_printed_text):
    raise AssertionError('Excepted %s, got %s' % (match, err_printed_text))
```

## Next Steps


---

*Source: test_logger.py:13 | Complexity: Advanced | Last updated: 2026-06-02*