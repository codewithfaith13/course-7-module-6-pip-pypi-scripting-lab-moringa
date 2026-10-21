"""generate_log.py - Root-level entry point so `import generate_log` works.

The real implementation lives in lib/generate_log.py.
"""
from lib.generate_log import generate_log

__all__ = ["generate_log"]

if __name__ == "__main__":
    generate_log(["User logged in", "User updated profile", "Report exported"])
