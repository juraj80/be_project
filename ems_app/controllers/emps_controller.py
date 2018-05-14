import pyramid_handlers
from ems_app.controllers.base_controller import BaseController
from ems_app.services.emps_service import EmpsService


class EmpsController(BaseController):
    @pyramid_handlers.action(renderer='templates/employees/index.pt')
    def index(self):
        # data / service access
        all_emps = EmpsService.get_emps()

        # return the model
        return {'emps': all_emps}
