from typing import Annotated

from fastapi import Depends

from api.services.app_services import AppServices
from api.services.get_services import get_services

ServicesDependency = Annotated[AppServices, Depends(get_services)]
