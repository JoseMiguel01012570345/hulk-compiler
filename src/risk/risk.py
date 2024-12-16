import logging
import functools

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='hulk.log', filemode='w', format='%(asctime)s - %(message)s')

frame_logger = []

def log_state_on_error(func):
    """Decorator to log local variables when an error occurs."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Capture local variables using inspect
            frame = frame_logger[-1]  # Get the previous frame (the function's frame)
            local_vars = frame.f_locals  # Get local variables from that frame
            
            logging.error(f"An error occurred in {func.__name__}: {e}")
            logging.debug("Local variables at error:")
            for name, value in local_vars.items():
                logging.debug(f"{name} = {value}")
                
            raise  # Re-raise the exception after logging

    return wrapper