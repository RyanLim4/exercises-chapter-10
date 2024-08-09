"""log_decorator module."""
import logging
from functools import wraps


def log_call(func):
    """Generate a log of func."""

    @wraps(func)
    def fn(*args, **kwargs):
        pos_args = ", ".join(repr(x) for x in args)
        kw_args = ", ".join(f"{x}={repr(y)}" for x, y in kwargs.items())
        if pos_args:
            if kw_args:
                log_msg = f"Calling: {func.__name__}({pos_args}, {kw_args})"
            else:
                log_msg = f"Calling: {func.__name__}({pos_args})"
        elif kw_args:
            log_msg = f"Calling: {func.__name__}({kw_args})"
        else:
            log_msg = f"Calling: {func.__name__}()"
        logging.info(log_msg)
        return func(*args, **kwargs)

    return fn
