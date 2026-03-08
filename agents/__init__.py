"""Agents package for trip_agent.

Re-exports key symbols from the installed openai-agents SDK so that
sub-modules can do ``from agents import Agent, Runner, function_tool``
without naming-conflict issues with this local package.
"""

import importlib.util
import os
import sys

_this_dir = os.path.dirname(os.path.abspath(__file__))
_this_module = sys.modules[__name__]  # keep reference to our own module

# ── Locate the real openai-agents SDK in site-packages ────────────────────────
_sdk_dir: str | None = None
for _base in sys.path:
    _abs_base = os.path.abspath(_base) if _base else os.getcwd()
    _candidate = os.path.join(_abs_base, "agents")
    if (
        os.path.isdir(_candidate)
        and os.path.abspath(_candidate) != _this_dir
        and os.path.isfile(os.path.join(_candidate, "__init__.py"))
    ):
        _sdk_dir = _candidate
        break

if _sdk_dir is None:
    raise ImportError(
        "Cannot find the installed openai-agents package. "
        "Run: pip install openai-agents"
    )

# ── Load SDK as 'agents' so its internal absolute imports resolve correctly ───
# We temporarily swap *ourselves* out of sys.modules and put the real SDK
# module in our place.  After exec_module completes, we restore ourselves and
# pull the symbols we need.
_spec = importlib.util.spec_from_file_location(
    "agents",
    os.path.join(_sdk_dir, "__init__.py"),
    submodule_search_locations=[_sdk_dir],
)
assert _spec is not None and _spec.loader is not None
_sdk = importlib.util.module_from_spec(_spec)

# Swap: real SDK becomes 'agents' so its sub-imports (agents.xxx) work
sys.modules["agents"] = _sdk
try:
    _spec.loader.exec_module(_sdk)  # type: ignore[union-attr]
finally:
    # Restore our local package
    sys.modules["agents"] = _this_module

# ── Re-export key SDK symbols ─────────────────────────────────────────────────
Agent = _sdk.Agent
Runner = _sdk.Runner
function_tool = _sdk.function_tool

__all__ = ["Agent", "Runner", "function_tool"]


