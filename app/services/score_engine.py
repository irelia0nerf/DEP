"""Compatibility layer re-exporting ``src`` scoring utilities."""

from src.services.score_engine import calculate, load_weights

__all__ = ["calculate", "load_weights"]
