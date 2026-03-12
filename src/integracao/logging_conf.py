import logging
from pathlib import Path

def setup_logging(log_path: str | None = "sync_log.log") -> None:
    """Set up logging configuration.

    Args:
        log_pat (str | None): Path to the log file. Defaults to "sync_log.log".
    
    Handlers: FileHandler and StreamHandler.
    Format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    Level: DEBUG
    """
    handlers: list[logging.Handler] = [logging.StreamHandler()]
    if log_path:
        handlers.append(logging.FileHandler(Path(log_path)))
    
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        handlers = handlers
    )
    