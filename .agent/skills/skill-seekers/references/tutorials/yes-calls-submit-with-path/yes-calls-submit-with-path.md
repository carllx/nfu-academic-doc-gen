# How To: Yes Calls Submit With Path

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test yes calls submit with path

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `json`
- `pathlib`
- `unittest.mock`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.signal_collectors`
- `asyncio`
- `skill_seekers.cli.main`
- `skill_seekers.cli.main`
- `argparse`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.parsers`
- `argparse`
- `skill_seekers.cli.parsers.scan_parser`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign cfg = self._write_cfg(...)

```python
cfg = self._write_cfg(tmp_path, 'newlib')
```

**Verification:**
```python
assert submit.call_count == 1
```

### Step 2: Assign submit = self._async_mock(...)

```python
submit = self._async_mock(return_value={'ok': True, 'message': 'https://github.com/x/y/issues/1'})
```

**Verification:**
```python
assert args[0] == cfg
```

### Step 3: Assign prompt = self._async_mock(...)

```python
prompt = self._async_mock(return_value='y')
```

### Step 4: Assign find = self._async_mock(...)

```python
find = self._async_mock(return_value=None)
```

**Verification:**
```python
assert submit.call_count == 1
```

### Step 5: Assign unknown = value

```python
args, _ = submit.call_args
```

**Verification:**
```python
assert args[0] == cfg
```

### Step 6: Call self._run()

```python
self._run(maybe_publish([cfg], skip_prompt=False))
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
cfg = self._write_cfg(tmp_path, 'newlib')
submit = self._async_mock(return_value={'ok': True, 'message': 'https://github.com/x/y/issues/1'})
prompt = self._async_mock(return_value='y')
find = self._async_mock(return_value=None)
with patch.dict('os.environ', {'GITHUB_TOKEN': 'fake'}), patch('skill_seekers.cli.scan_command._submit_config', submit), patch('skill_seekers.cli.scan_command._prompt_async', prompt), patch('skill_seekers.cli.scan_command._find_existing_issue', find):
    self._run(maybe_publish([cfg], skip_prompt=False))
assert submit.call_count == 1
args, _ = submit.call_args
assert args[0] == cfg
```

## Next Steps


---

*Source: test_scan_command.py:733 | Complexity: Advanced | Last updated: 2026-06-02*