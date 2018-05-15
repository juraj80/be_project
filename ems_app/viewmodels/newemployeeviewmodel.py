from ems_app.viewmodels.viewmodelbase import ViewModelBase


class NewEmployeeViewModel(ViewModelBase):
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.birth_date = None
        self.gender = None
        self.salary = None
        self.emp_image = None
        self.dept_name = None
        # self.tracks_text = None
        self.error = None

    def from_dict(self, data_dict):
        self.first_name = data_dict.get('first_name')
        self.last_name = data_dict.get('last_name')

        self.birth_date = data_dict.get('birth_date')
        self.gender = data_dict.get('gender')
        self.salary = float(data_dict.get('salary'))
        self.emp_image = data_dict.get('emp_image')
        self.dept_name = data_dict.get('dept_name')
   #     self.tracks_text = data_dict.get('tracks_text')

    # @property
    # def track_titles(self):
    #     return [
    #         t.strip()
    #         for t in self.tracks_text.split('\n')
    #         if t and t.strip()
    #     ]

