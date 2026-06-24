# How To: With Options

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Specifying Python Command-line Options
--------------------------------------

You can specify a single argument on the '#!' line.  This can be used
to specify Python options like -O, to run in optimized mode or -i
to start the interactive interpreter.  You can combine multiple
options as usual. For example, to run in optimized mode and
enter the interpreter after running the script, you could use -Oi:

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pathlib`
- `platform`
- `subprocess`
- `sys`
- `textwrap`
- `pytest`
- `setuptools._importlib`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: "\n        Specifying Python Command-line Options\n        --------------------------------------\n\n        You can specify a single argument on the '#!' line.  This can be used\n        to specify Python options like -O, to run in optimized mode or -i\n        to start the interactive interpreter.  You can combine multiple\n        options as usual. For example, to run in optimized mode and\n        enter the interpreter after running the script, you could use -Oi:\n        "

```python
"\n        Specifying Python Command-line Options\n        --------------------------------------\n\n        You can specify a single argument on the '#!' line.  This can be used\n        to specify Python options like -O, to run in optimized mode or -i\n        to start the interactive interpreter.  You can combine multiple\n        options as usual. For example, to run in optimized mode and\n        enter the interpreter after running the script, you could use -Oi:\n        "
```

**Verification:**
```python
assert actual == expected
```

### Step 2: Call self.create_script()

```python
self.create_script(tmpdir)
```

### Step 3: Assign tmpl = textwrap.dedent.lstrip(...)

```python
tmpl = textwrap.dedent("\n            #!%(python_exe)s  -Oi\n            import sys\n            input = repr(sys.stdin.read())\n            print(sys.argv[0][-14:])\n            print(sys.argv[1:])\n            print(input)\n            if __debug__:\n                print('non-optimized')\n            sys.ps1 = '---'\n            ").lstrip()
```

### Step 4: Assign cmd = value

```python
cmd = [str(tmpdir / 'foo.exe')]
```

### Step 5: Assign proc = subprocess.Popen(...)

```python
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
```

### Step 6: Assign unknown = proc.communicate(...)

```python
stdout, _stderr = proc.communicate()
```

### Step 7: Assign actual = stdout.replace(...)

```python
actual = stdout.replace('\r\n', '\n')
```

### Step 8: Assign expected = textwrap.dedent.lstrip(...)

```python
expected = textwrap.dedent("\n            \\foo-script.py\n            []\n            ''\n            ---\n            ").lstrip()
```

**Verification:**
```python
assert actual == expected
```

### Step 9: Call f.write()

```python
f.write(self.prep_script(tmpl))
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
"\n        Specifying Python Command-line Options\n        --------------------------------------\n\n        You can specify a single argument on the '#!' line.  This can be used\n        to specify Python options like -O, to run in optimized mode or -i\n        to start the interactive interpreter.  You can combine multiple\n        options as usual. For example, to run in optimized mode and\n        enter the interpreter after running the script, you could use -Oi:\n        "
self.create_script(tmpdir)
tmpl = textwrap.dedent("\n            #!%(python_exe)s  -Oi\n            import sys\n            input = repr(sys.stdin.read())\n            print(sys.argv[0][-14:])\n            print(sys.argv[1:])\n            print(input)\n            if __debug__:\n                print('non-optimized')\n            sys.ps1 = '---'\n            ").lstrip()
with (tmpdir / 'foo-script.py').open('w') as f:
    f.write(self.prep_script(tmpl))
cmd = [str(tmpdir / 'foo.exe')]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
stdout, _stderr = proc.communicate()
actual = stdout.replace('\r\n', '\n')
expected = textwrap.dedent("\n            \\foo-script.py\n            []\n            ''\n            ---\n            ").lstrip()
assert actual == expected
```

## Next Steps


---

*Source: test_windows_wrappers.py:167 | Complexity: Advanced | Last updated: 2026-06-02*