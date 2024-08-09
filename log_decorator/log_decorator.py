"""log_decorator module."""
import logging
from functools import wraps


def log_call(func):
    """Generate a log of func."""

    @wraps(func)
    def fn(*args, **kwargs):
        pos_args = ", ".join(repr(x) for x in args)
        kw_args = ", ".join(f"{x}={repr(y)}" for x, y in kwargs.items())
        log_msg = f"Calling: {func.__name__}({pos_args}, {kw_args})"
        logging.info(log_msg)
        return func(*args, **kwargs)

    return fn
