# How To: Named Lists

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test named lists

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

### Step 1: Assign options = value

```python
options = ['one', 'two', 'three']
```

### Step 2: Call self.assertEqual()

```python
self.assertEqual(regex.match('333\\L<bar>444', '333one444', bar=options).group(), '333one444')
```

### Step 3: Call self.assertEqual()

```python
self.assertEqual(regex.match('(?i)333\\L<bar>444', '333TWO444', bar=options).group(), '333TWO444')
```

### Step 4: Call self.assertEqual()

```python
self.assertEqual(regex.match('333\\L<bar>444', '333four444', bar=options), None)
```

### Step 5: Assign options = value

```python
options = [b'one', b'two', b'three']
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(regex.match(b'333\\L<bar>444', b'333one444', bar=options).group(), b'333one444')
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(regex.match(b'(?i)333\\L<bar>444', b'333TWO444', bar=options).group(), b'333TWO444')
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(regex.match(b'333\\L<bar>444', b'333four444', bar=options), None)
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(repr(type(regex.compile('3\\L<bar>4\\L<bar>+5', bar=['one', 'two', 'three']))), self.PATTERN_CLASS)
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(regex.findall('^\\L<options>', 'solid QWERT', options=set(['good', 'brilliant', '+s\\ol[i}d'])), [])
```

### Step 11: Call self.assertEqual()

```python
self.assertEqual(regex.findall('^\\L<options>', '+solid QWERT', options=set(['good', 'brilliant', '+solid'])), ['+solid'])
```

### Step 12: Assign options = value

```python
options = ['STRASSE']
```

### Step 13: Call self.assertEqual()

```python
self.assertEqual(regex.match('(?fi)\\L<words>', 'straße', words=options).span(), (0, 6))
```

### Step 14: Assign options = value

```python
options = ['STRASSE', 'stress']
```

### Step 15: Call self.assertEqual()

```python
self.assertEqual(regex.match('(?fi)\\L<words>', 'straße', words=options).span(), (0, 6))
```

### Step 16: Assign options = value

```python
options = ['straße']
```

### Step 17: Call self.assertEqual()

```python
self.assertEqual(regex.match('(?fi)\\L<words>', 'STRASSE', words=options).span(), (0, 7))
```

### Step 18: Assign options = value

```python
options = ['kit']
```

### Step 19: Call self.assertEqual()

```python
self.assertEqual(regex.search('(?i)\\L<words>', 'SKITS', words=options).span(), (1, 4))
```

### Step 20: Call self.assertEqual()

```python
self.assertEqual(regex.search('(?i)\\L<words>', 'SKİTS', words=options).span(), (1, 4))
```

### Step 21: Call self.assertEqual()

```python
self.assertEqual(regex.search('(?fi)\\b(\\w+) +\\1\\b', ' straße STRASSE ').span(), (1, 15))
```

### Step 22: Call self.assertEqual()

```python
self.assertEqual(regex.search('(?fi)\\b(\\w+) +\\1\\b', ' STRASSE straße ').span(), (1, 15))
```

### Step 23: Call self.assertEqual()

```python
self.assertEqual(regex.search('^\\L<options>$', '', options=[]).span(), (0, 0))
```


## Complete Example

```python
# Workflow
options = ['one', 'two', 'three']
self.assertEqual(regex.match('333\\L<bar>444', '333one444', bar=options).group(), '333one444')
self.assertEqual(regex.match('(?i)333\\L<bar>444', '333TWO444', bar=options).group(), '333TWO444')
self.assertEqual(regex.match('333\\L<bar>444', '333four444', bar=options), None)
options = [b'one', b'two', b'three']
self.assertEqual(regex.match(b'333\\L<bar>444', b'333one444', bar=options).group(), b'333one444')
self.assertEqual(regex.match(b'(?i)333\\L<bar>444', b'333TWO444', bar=options).group(), b'333TWO444')
self.assertEqual(regex.match(b'333\\L<bar>444', b'333four444', bar=options), None)
self.assertEqual(repr(type(regex.compile('3\\L<bar>4\\L<bar>+5', bar=['one', 'two', 'three']))), self.PATTERN_CLASS)
self.assertEqual(regex.findall('^\\L<options>', 'solid QWERT', options=set(['good', 'brilliant', '+s\\ol[i}d'])), [])
self.assertEqual(regex.findall('^\\L<options>', '+solid QWERT', options=set(['good', 'brilliant', '+solid'])), ['+solid'])
options = ['STRASSE']
self.assertEqual(regex.match('(?fi)\\L<words>', 'straße', words=options).span(), (0, 6))
options = ['STRASSE', 'stress']
self.assertEqual(regex.match('(?fi)\\L<words>', 'straße', words=options).span(), (0, 6))
options = ['straße']
self.assertEqual(regex.match('(?fi)\\L<words>', 'STRASSE', words=options).span(), (0, 7))
options = ['kit']
self.assertEqual(regex.search('(?i)\\L<words>', 'SKITS', words=options).span(), (1, 4))
self.assertEqual(regex.search('(?i)\\L<words>', 'SKİTS', words=options).span(), (1, 4))
self.assertEqual(regex.search('(?fi)\\b(\\w+) +\\1\\b', ' straße STRASSE ').span(), (1, 15))
self.assertEqual(regex.search('(?fi)\\b(\\w+) +\\1\\b', ' STRASSE straße ').span(), (1, 15))
self.assertEqual(regex.search('^\\L<options>$', '', options=[]).span(), (0, 0))
```

## Next Steps


---

*Source: test_regex.py:2558 | Complexity: Advanced | Last updated: 2026-06-02*