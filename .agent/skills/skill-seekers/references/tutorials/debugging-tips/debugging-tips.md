# How To: Debugging Tips

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Make sure to display useful debugging tips to the user.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `os`
- `platform`
- `stat`
- `subprocess`
- `sys`
- `copy`
- `importlib`
- `importlib.machinery`
- `pathlib`
- `textwrap`
- `typing`
- `unittest.mock`
- `uuid`
- `jaraco.envs`
- `jaraco.path`
- `pytest`
- `path`
- `setuptools._importlib`
- `setuptools.command.editable_wheel`
- `setuptools.dist`
- `setuptools.extension`
- `setuptools.warnings`
- `distutils.core`
- `distutils.command.build_ext`

**Setup Required:**
```python
# Fixtures: tmpdir_cwd, monkeypatch
```

## Step-by-Step Guide

### Step 1: 'Make sure to display useful debugging tips to the user.'

```python
'Make sure to display useful debugging tips to the user.'
```

**Verification:**
```python
assert any(('debugging-tips' in note for note in ctx.value.__notes__))
```

### Step 2: Call jaraco.path.build()

```python
jaraco.path.build({'module.py': 'x = 42'})
```

### Step 3: Assign dist = Distribution(...)

```python
dist = Distribution()
```

### Step 4: Assign dist.script_name = 'setup.py'

```python
dist.script_name = 'setup.py'
```

### Step 5: Call dist.set_defaults()

```python
dist.set_defaults()
```

### Step 6: Assign cmd = editable_wheel(...)

```python
cmd = editable_wheel(dist)
```

### Step 7: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 8: Assign SimulatedErr = type(...)

```python
SimulatedErr = type('SimulatedErr', (Exception,), {})
```

### Step 9: Assign simulated_failure = Mock(...)

```python
simulated_failure = Mock(side_effect=SimulatedErr())
```

### Step 10: Call monkeypatch.setattr()

```python
monkeypatch.setattr(cmd, 'get_finalized_command', simulated_failure)
```

**Verification:**
```python
assert any(('debugging-tips' in note for note in ctx.value.__notes__))
```

### Step 11: Call cmd.run()

```python
cmd.run()
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, monkeypatch

# Workflow
'Make sure to display useful debugging tips to the user.'
jaraco.path.build({'module.py': 'x = 42'})
dist = Distribution()
dist.script_name = 'setup.py'
dist.set_defaults()
cmd = editable_wheel(dist)
cmd.ensure_finalized()
SimulatedErr = type('SimulatedErr', (Exception,), {})
simulated_failure = Mock(side_effect=SimulatedErr())
monkeypatch.setattr(cmd, 'get_finalized_command', simulated_failure)
with pytest.raises(SimulatedErr) as ctx:
    cmd.run()
assert any(('debugging-tips' in note for note in ctx.value.__notes__))
```

## Next Steps


---

*Source: test_editable_install.py:1191 | Complexity: Advanced | Last updated: 2026-06-02*