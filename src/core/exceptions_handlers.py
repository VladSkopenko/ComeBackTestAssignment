from fastapi import FastAPI
from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse

from src.core.exceptions import AddRecordError
from src.core.exceptions import AlreadyActivated
from src.core.exceptions import AlreadyDeactivated
from src.core.exceptions import AlreadyExists
from src.core.exceptions import BadRequest
from src.core.exceptions import CredentialsLicenseError
from src.core.exceptions import EmailNotConfirmed
from src.core.exceptions import ErrorConnectingDb
from src.core.exceptions import InvalidCredentials
from src.core.exceptions import InvalidEmail
from src.core.exceptions import InvalidLogin
from src.core.exceptions import InvalidPassword
from src.core.exceptions import InvalidRefreshToken
from src.core.exceptions import InvalidResetToken
from src.core.exceptions import InvalidToken
from src.core.exceptions import NotFound
from src.core.exceptions import PermissionDenied
from src.core.exceptions import PermissionsError
from src.core.exceptions import UserNotActive
from src.core.exceptions import VerificationError


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(NotFound)
    async def not_found_exception_handler(request: Request, exc: NotFound):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)}
        )

    @app.exception_handler(AlreadyExists)
    async def already_exists_exception_handler(request: Request, exc: AlreadyExists):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)}
        )

    @app.exception_handler(AlreadyActivated)
    async def already_activated_exception_handler(
        request: Request, exc: AlreadyActivated
    ):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)}
        )

    @app.exception_handler(AlreadyDeactivated)
    async def already_deactivated_exception_handler(
        request: Request, exc: AlreadyDeactivated
    ):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)}
        )

    @app.exception_handler(PermissionsError)
    async def permissions_error_exception_handler(
        request: Request, exc: PermissionsError
    ):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN, content={"detail": str(exc)}
        )

    @app.exception_handler(InvalidCredentials)
    async def invalid_credentials_exception_handler(
        request: Request, exc: InvalidCredentials
    ):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(exc.message)},
        )

    @app.exception_handler(PermissionDenied)
    async def permission_denied_exception_handler(
        request: Request, exc: PermissionDenied
    ):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"detail": str(exc.message)},
        )

    @app.exception_handler(BadRequest)
    async def bad_request_exception_handler(request: Request, exc: BadRequest):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc.message)},
        )

    @app.exception_handler(AddRecordError)
    async def add_record_handler(request: Request, exc: AddRecordError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc.message)}
        )

    @app.exception_handler(InvalidToken)
    async def invalid_token_exception_handler(request: Request, exc: InvalidToken):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": str(exc)}
        )

    @app.exception_handler(InvalidEmail)
    async def invalid_email_exception_handler(request: Request, exc: InvalidEmail):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": str(exc)}
        )

    @app.exception_handler(InvalidLogin)
    async def invalid_login_exception_handler(request: Request, exc: InvalidLogin):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": str(exc)}
        )

    @app.exception_handler(UserNotActive)
    async def user_not_active_exception_handler(request: Request, exc: UserNotActive):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN, content={"detail": str(exc)}
        )

    @app.exception_handler(EmailNotConfirmed)
    async def email_not_confirmed_exception_handler(
        request: Request, exc: EmailNotConfirmed
    ):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN, content={"detail": str(exc)}
        )

    @app.exception_handler(InvalidPassword)
    async def invalid_password_exception_handler(
        request: Request, exc: InvalidPassword
    ):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": str(exc)}
        )

    @app.exception_handler(VerificationError)
    async def verification_error_exception_handler(
        request: Request, exc: VerificationError
    ):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(exc)}
        )

    @app.exception_handler(CredentialsLicenseError)
    async def credentials_license_error_exception_handler(
        request: Request, exc: CredentialsLicenseError
    ):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN, content={"detail": str(exc)}
        )

    @app.exception_handler(InvalidRefreshToken)
    async def invalid_refresh_token_exception_handler(
        request: Request, exc: InvalidRefreshToken
    ):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": str(exc)}
        )

    @app.exception_handler(InvalidResetToken)
    async def invalid_reset_token_exception_handler(
        request: Request, exc: InvalidResetToken
    ):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": str(exc)}
        )

    @app.exception_handler(ErrorConnectingDb)
    async def error_connecting_db_exception_handler(
        request: Request, exc: ErrorConnectingDb
    ):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(exc)},
        )