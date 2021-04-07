class ESConnectionError(Exception):
    """Custom error exception that denotes a failure to establish
    a python ElasticSearch client handle, thus implying a connectivity
    problem to the ElasticSearch instance.
    """
    pass


class ESQueryError(Exception):
    """Custom error exception that denotes a failure when making a query call
    to ElasticSearch instance
    """
    pass
