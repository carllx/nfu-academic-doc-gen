# How To: Rfc822 Escape

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: We want to ensure a multi-line header parses correctly.

For interoperability, the escaped value should also "round-trip" over
`email.generator.Generator.flatten` and `email.message_from_*`
(see pypa/setuptools#4033).

The main issue is that internally `email.policy.EmailPolicy` uses
`splitlines` which will split on some control chars. If all the new lines
are not prefixed with spaces, the parser will interrupt reading
the current header and produce an incomplete value, while
incorrectly interpreting the rest of the headers as part of the payload.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `email`
- `email.generator`
- `email.policy`
- `io`
- `os`
- `pathlib`
- `sys`
- `sysconfig`
- `unittest.mock`
- `copy`
- `distutils`
- `distutils.errors`
- `distutils.util`
- `pytest`
- `pwd`

**Setup Required:**
```python
# Fixtures: given, wanted
```

## Step-by-Step Guide

### Step 1: '\n        We want to ensure a multi-line header parses correctly.\n\n        For interoperability, the escaped value should also "round-trip" over\n        `email.generator.Generator.flatten` and `email.message_from_*`\n        (see pypa/setuptools#4033).\n\n        The main issue is that internally `email.policy.EmailPolicy` uses\n        `splitlines` which will split on some control chars. If all the new lines\n        are not prefixed with spaces, the parser will interrupt reading\n        the current header and produce an incomplete value, while\n        incorrectly interpreting the rest of the headers as part of the payload.\n        '

```python
'\n        We want to ensure a multi-line header parses correctly.\n\n        For interoperability, the escaped value should also "round-trip" over\n        `email.generator.Generator.flatten` and `email.message_from_*`\n        (see pypa/setuptools#4033).\n\n        The main issue is that internally `email.policy.EmailPolicy` uses\n        `splitlines` which will split on some control chars. If all the new lines\n        are not prefixed with spaces, the parser will interrupt reading\n        the current header and produce an incomplete value, while\n        incorrectly interpreting the rest of the headers as part of the payload.\n        '
```

**Verification:**
```python
assert msg.get_payload() == 'payload\n'
```

### Step 2: Assign res = rfc822_escape(...)

```python
res = rfc822_escape(given)
```

**Verification:**
```python
assert msg['other-header'] == '42'
```

### Step 3: Assign policy = email.policy.EmailPolicy(...)

```python
policy = email.policy.EmailPolicy(utf8=True, mangle_from_=False, max_line_length=0)
```

**Verification:**
```python
assert set(msg['header'].splitlines()) == set(res.splitlines())
```

### Step 4: Assign raw = value

```python
raw = f'header: {res}\nother-header: 42\n\npayload\n'
```

**Verification:**
```python
assert res == wanted
```

### Step 5: Assign orig = email.message_from_string(...)

```python
orig = email.message_from_string(raw)
```

### Step 6: Call email.generator.Generator.flatten()

```python
email.generator.Generator(buffer, policy=policy).flatten(orig)
```

### Step 7: Call buffer.seek()

```python
buffer.seek(0)
```

### Step 8: Assign regen = email.message_from_file(...)

```python
regen = email.message_from_file(buffer)
```

**Verification:**
```python
assert msg.get_payload() == 'payload\n'
```


## Complete Example

```python
# Setup
# Fixtures: given, wanted

# Workflow
'\n        We want to ensure a multi-line header parses correctly.\n\n        For interoperability, the escaped value should also "round-trip" over\n        `email.generator.Generator.flatten` and `email.message_from_*`\n        (see pypa/setuptools#4033).\n\n        The main issue is that internally `email.policy.EmailPolicy` uses\n        `splitlines` which will split on some control chars. If all the new lines\n        are not prefixed with spaces, the parser will interrupt reading\n        the current header and produce an incomplete value, while\n        incorrectly interpreting the rest of the headers as part of the payload.\n        '
res = rfc822_escape(given)
policy = email.policy.EmailPolicy(utf8=True, mangle_from_=False, max_line_length=0)
with io.StringIO() as buffer:
    raw = f'header: {res}\nother-header: 42\n\npayload\n'
    orig = email.message_from_string(raw)
    email.generator.Generator(buffer, policy=policy).flatten(orig)
    buffer.seek(0)
    regen = email.message_from_file(buffer)
for msg in (orig, regen):
    assert msg.get_payload() == 'payload\n'
    assert msg['other-header'] == '42'
    assert set(msg['header'].splitlines()) == set(res.splitlines())
assert res == wanted
```

## Next Steps


---

*Source: test_util.py:192 | Complexity: Advanced | Last updated: 2026-06-02*