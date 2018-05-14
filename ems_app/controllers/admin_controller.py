import pyramid_handlers
from ems_app.controllers.base_controller import BaseController
from ems_app.viewmodels.newemployeeviewmodel import NewEmployeeViewModel
from ems_app.services.emps_service import EmpsService


class AdminController(BaseController):
    # GET /admin/new_employee
    @pyramid_handlers.action(renderer='templates/admin/new_employee.pt',
                             request_method='GET',
                             name='new_employee')
    def new_employee_get(self):
        vm = NewEmployeeViewModel()
        return vm.to_dict()

    # POST /admin/new_employee
    @pyramid_handlers.action(renderer='templates/admin/new_employee.pt',
                             request_method='POST',
                             name='new_employee')
    def new_employee_post(self):
        vm = NewEmployeeViewModel()
        vm.from_dict(self.request.POST)

        # might want to add this ;)
        # if not vm.validate():
        #     return vm.to_dict()

        # Insert employee
        new_employee = EmpsService.create_employee(vm.first_name,vm.last_name, vm.birth_date,vm.gender,  vm.salary, vm.emp_image, vm.dept_name)
        # log new employee
        print("Created a new employee with id {}".format(new_employee.id))

        # redirect
        self.redirect('/emps')
