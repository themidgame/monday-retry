import time


class RetryExhaustedException(Exception):
    """Base class for other exceptions"""
    pass


def retry_api_request(action):
    def inner(self, query, timeout=30, retry_count=2, delay=0, error=None):
        # We raise an exception if the retry has been exhausted
        if retry_count <= 0:
            raise RetryExhaustedException(error)
        else:
            time.sleep(delay)
            value = action(self, query, timeout, retry_count)
            if 'errors' in value:
                return inner(self=self, query=query, timeout=timeout, retry_count=retry_count - 1, delay=value['delay'],
                             error=value['errors'])
            else:
                return value

    return inner
