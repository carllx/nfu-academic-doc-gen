# How To: Turkic

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test turkic

## Prerequisites

**Required Modules:**
- `weakref`
- `copy`
- `pickle`
- `regex`
- `string`
- `sys`
- `unittest`
- `array`


## Step-by-Step Guide

### Step 1: Assign pairs = 'I=i;I=ı;i=İ'

```python
pairs = 'I=i;I=ı;i=İ'
```

### Step 2: Assign all_chars = set(...)

```python
all_chars = set()
```

### Step 3: Assign matching = set(...)

```python
matching = set()
```

### Step 4: Assign unknown = pair.split(...)

```python
ch1, ch2 = pair.split('=')
```

### Step 5: Call all_chars.update()

```python
all_chars.update((ch1, ch2))
```

### Step 6: Call matching.add()

```python
matching.add((ch1, ch1))
```

### Step 7: Call matching.add()

```python
matching.add((ch1, ch2))
```

### Step 8: Call matching.add()

```python
matching.add((ch2, ch1))
```

### Step 9: Call matching.add()

```python
matching.add((ch2, ch2))
```

### Step 10: Assign m = regex.match(...)

```python
m = regex.match('(?i)\\A' + ch1 + '\\Z', ch2)
```

### Step 11: Call self.fail()

```python
self.fail('{} matching {}'.format(ascii(ch1), ascii(ch2)))
```

### Step 12: Call self.fail()

```python
self.fail('{} not matching {}'.format(ascii(ch1), ascii(ch2)))
```


## Complete Example

```python
# Workflow
pairs = 'I=i;I=ı;i=İ'
all_chars = set()
matching = set()
for pair in pairs.split(';'):
    ch1, ch2 = pair.split('=')
    all_chars.update((ch1, ch2))
    matching.add((ch1, ch1))
    matching.add((ch1, ch2))
    matching.add((ch2, ch1))
    matching.add((ch2, ch2))
for ch1 in all_chars:
    for ch2 in all_chars:
        m = regex.match('(?i)\\A' + ch1 + '\\Z', ch2)
        if m:
            if (ch1, ch2) not in matching:
                self.fail('{} matching {}'.format(ascii(ch1), ascii(ch2)))
        elif (ch1, ch2) in matching:
            self.fail('{} not matching {}'.format(ascii(ch1), ascii(ch2)))
```

## Next Steps


---

*Source: test_regex.py:2532 | Complexity: Advanced | Last updated: 2026-06-02*