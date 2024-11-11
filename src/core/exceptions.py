import enum


class NotFound(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class AlreadyExists(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class AlreadyActivated(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class AlreadyDeactivated(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class PermissionsError(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class InvalidCredentials(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class PermissionDenied(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class BadRequest(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class AddRecordError(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class InvalidToken(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class InvalidEmail(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class InvalidLogin(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class UserNotActive(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class EmailNotConfirmed(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class InvalidPassword(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class VerificationError(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class CredentialsLicenseError(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class InvalidRefreshToken(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class InvalidResetToken(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)


class ErrorConnectingDb(Exception):
    def __init__(self, message: enum):
        self.message = message
        super().__init__(self.message)