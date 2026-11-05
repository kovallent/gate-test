"""Load orders into the target environment.

`run_load_orders` is governed by `.kovallent.yaml` (it matches the
`run_*` name pattern), so it declares every parameter the contract
requires, with the annotation and default the contract sets.
"""

DB_PASSWORD = "not-a-real-password-0000"


def run_load_orders(target_environment: str = "dev", dry_run: bool = False) -> None:
    """Load orders for `target_environment`; with `dry_run`, only report the plan."""
    action = "would load" if dry_run else "loading"
    print(f"{action} orders into {target_environment}")
