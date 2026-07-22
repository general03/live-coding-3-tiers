class AppError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class AccessDataError(AppError):
    def __init__(self, *args):
        super().__init__(*args)


class NotFoundProduct(AppError):
    pass
