# Anti-Patterns — Before / After Examples

Concrete examples of the four failure modes across Python, TypeScript, and shell.

## 1. Silent assumptions

**Before** — picks one interpretation without asking:
```python
# User: "add pagination"
def list_users(page_size=10):          # assumes offset pagination
    return db.query(User).limit(page_size).all()
```

**After** — surfaces the choice:
```
Two interpretations: (a) offset/page pagination, (b) cursor-based.
Cursor is safer for large, changing datasets. Proceeding with cursor
unless you need page numbers.
```

## 2. Speculative abstraction

**Before** — a factory for a single implementation:
```typescript
interface PaymentProcessor { charge(a: number): Promise<void>; }
class StripeProcessor implements PaymentProcessor { /* ... */ }
class PaymentProcessorFactory {
  create(kind: string): PaymentProcessor { /* switch with one case */ }
}
```

**After** — the code that is actually needed:
```typescript
async function charge(amount: number): Promise<void> {
  return stripe.charges.create({ amount });
}
```

## 3. Unrequested features

**Before** — adds caching, retries, and config nobody asked for:
```python
def fetch(url, retries=3, cache=TtlCache(300), timeout=30, backoff=2.0):
    ...
```

**After** — does exactly the task:
```python
def fetch(url, timeout=30):
    return requests.get(url, timeout=timeout)
```

## 4. Drive-by refactor (diff noise)

**Before** — reformats and renames unrelated code:
```diff
- def calc(a,b):
+ def calculate(a: int, b: int) -> int:
+     """Compute the sum."""
-     return a+b
+     return a + b
```
in a commit whose stated goal was "fix login redirect".

**After** — only the requested change:
```diff
-     return redirect("/home")
+     return redirect(next_url or "/home")
```

## 5. Dead-code accumulation

**Before** — leaves scaffolding:
```typescript
const DEBUG = true;                    // added while exploring
function _oldParse(x) { /* unused */ } // superseded
export function parse(x) { /* real */ }
```

**After** — removes your own scaffolding:
```typescript
export function parse(x) { /* real */ }
```

## 6. Vague goal

**Before**
```
Plan: make the API more robust.
```

**After**
```
1. Add a test that a 500 from upstream returns 502 → verify: test fails today.
2. Map upstream errors to 502 → verify: test passes.
3. Add a timeout of 5s → verify: test with a slow mock passes.
```

## 7. Error handling for impossible cases

**Before**
```python
def area(r: float) -> float:
    if not isinstance(r, (int, float)):
        raise TypeError("r must be numeric")   # type system already enforces this
    if r < 0:
        raise ValueError("r must be >= 0")     # caller contract, not this function's job
    return 3.14159 * r * r
```

**After**
```python
def area(r: float) -> float:
    return 3.14159 * r * r
```

## 8. Shell: over-engineered one-liner

**Before**
```bash
if [ "$(echo "$1" | tr '[:upper:]' '[:lower:]')" = "yes" ]; then
  do_thing
fi
```

**After**
```bash
case "${1,,}" in
  yes) do_thing ;;
esac
```

## 9. Premature generalization (TypeScript)

**Before**
```typescript
type Result<T, E = Error, M = undefined> = { ok: true; value: T; meta: M }
  | { ok: false; error: E; meta: M };
```

**After**
```typescript
type Result<T> = { ok: true; value: T } | { ok: false; error: Error };
```

## 10. Comment churn

**Before** — rewrites every comment in the file while fixing one function.
**After** — updates only the comment on the function you changed, if it became inaccurate.

## Using these examples

- Point the reviewer at the specific pattern, not "code feels bloated".
- Prefer deleting the abstraction over documenting it.
- When in doubt, ask: *does this line trace to the request?*
