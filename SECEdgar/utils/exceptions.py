class EDGARQueryError(Exception):
    """
    This error is thrown when a query receives a response that is not a 200 response.
    """

    def __str__(self):
        return "An error occured while making the query."


class EDGARFieldError(Exception):
    """
    This error is thrown when an invalid field is given to an endpoint.
    """

    def __init__(self, endpoint, field):
        self.endpoint = endpoint
        self.field = field

    def __str__(self):
        return "Field {field} not found in endpoint {endpoint}".format(
            field=self.field, endpoint=self.endpoint
        )


class CIKError(Exception):
    """
    This error is thrown when an invalid CIK is given.
    """

    def __init__(self, cik):
        self.cik = cik

    def __str__(self):
        return "CIK {cik} is not valid. Must be str or int with 10 digits.".format(cik=self.cik)


class FilingTypeError(Exception):
    """This error is thrown when an invalid filing type is given. """

    def __str__(self):
        return "The filing type given is not valid."
