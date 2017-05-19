import radical.utils as ru
from radical.entk.exceptions import *
from radical.entk import states


class Task(object):

    def __init__(self):

        self._uid       = ru.generate_id('radical.entk.task')
        self._name      = str()

        self._state     = states.NEW

        # Attributes necessary for execution
        self._pre_exec      = list()
        self._executable    = list()
        self._arguments     = list()
        self._post_exec     = list()
        self._cores  = 1

        # Data staging attributes
        self._upload_input_data     = list()
        self._copy_input_data       = list()
        self._link_input_data       = list()
        self._copy_output_data      = list()
        self._download_output_data  = list()


        ## The following help in updation
        # Stage this task belongs to
        self._parent_stage = None
        # Pipeline this task belongs to
        self._parent_pipeline = None


    # -----------------------------------------------
    # Getter functions
    # -----------------------------------------------

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name
    
    @property
    def state(self):
        return self._state
    
    @property
    def pre_exec(self):
        return self._pre_exec
    
    @property
    def executable(self):
        return self._executable
    
    @property
    def arguments(self):
        return self._arguments
    
    @property
    def post_exec(self):
        return self._post_exec

    @property
    def cores(self):
        return self._cores

    @property
    def upload_input_data(self):
        return self._upload_input_data
    
    @property
    def copy_input_data(self):
        return self._copy_input_data
    
    @property
    def link_input_data(self):
        return self._link_input_data
    
    @property
    def copy_output_data(self):
        return self._copy_output_data
    
    @property
    def download_output_data(self):
        return self._download_output_data

    @property
    def parent_stage(self):
        return self._parent_stage
    
    @property
    def parent_pipeline(self):
        return self._parent_pipeline    
    # -----------------------------------------------


    # -----------------------------------------------
    # Setter functions
    # -----------------------------------------------

    @name.setter
    def name(self, value):
        if isinstance(value,str):
            self._name = value
        else:
            raise TypeError(expected_type=str, actual_type=type(value))

    @state.setter
    def state(self, value):
        if isinstance(value,str):
            self._state = value
        else:
            raise TypeError(expected_type=str, actual_type=type(value))

    @pre_exec.setter
    def pre_exec(self, value):
        if isinstance(value, list):
            self._pre_exec = value
        else:
            raise TypeError(expected_type=list, actual_type=type(value))


    @executable.setter
    def executable(self, value):
        if isinstance(value, list):
            self._executable = value
        else:
            raise TypeError(expected_type=list, actual_type=type(value))

    @arguments.setter
    def arguments(self, value):
        if isinstance(value, list):
            self._arguments = value
        else:
            raise TypeError(expected_type=list, actual_type=type(value))


    @post_exec.setter
    def post_exec(self, value):
        if isinstance(value, list):
            self._post_exec = value
        else:
            raise TypeError(expected_type=list, actual_type=type(value))

    @cores.setter
    def cores(self, val):
        if isinstance(val, int):
            self._cores = val
        else:
            raise TypeError(expected_type=int, actual_type=type(val))


    @upload_input_data.setter
    def upload_input_data(self, value):
        if isinstance(value, list):
            self._upload_input_data = value
        else:
            raise TypeError(expected_type=list, actual_type=type(value))

    @copy_input_data.setter
    def copy_input_data(self, value):
        if isinstance(value, list):
            self._copy_input_data = value
        else:
            raise TypeError(expected_type=list, actual_type=type(value))

    @link_input_data.setter
    def link_input_data(self, value):
        if isinstance(value, list):
            self._link_input_data = value
        else:
            raise TypeError(expected_type=list, actual_type=type(value))

    @copy_output_data.setter
    def copy_output_data(self, value):
        if isinstance(value, list):
            self._copy_output_data = value
        else:
            raise TypeError(expected_type=list, actual_type=type(value))

    @download_output_data.setter
    def download_output_data(self, value):
        if isinstance(value, list):
            self._download_output_data = value
        else:
            raise TypeError(expected_type=list, actual_type=type(value))

    @parent_stage.setter
    def parent_stage(self, value):
        if isinstance(value,str):
            self._parent_stage = value
        else:
            raise TypeError(expected_type=str, actual_type=type(value))

    @parent_pipeline.setter
    def parent_pipeline(self, value):
        if isinstance(value,str):
            self._parent_pipeline = value
        else:
            raise TypeError(expected_type=str, actual_type=type(value))
    # -----------------------------------------------

    def replicate(self, original_task):

        self._uid       = ru.generate_id('radical.entk.task')
        self._name      = original_task.name

        self._state     = states.NEW

        # Attributes necessary for execution
        self._pre_exec      = original_task.pre_exec
        self._executable    = original_task.executable
        self._arguments     = original_task.arguments
        self._post_exec     = original_task.post_exec

        # Data staging attributes
        self._upload_input_data     = original_task.upload_input_data
        self._copy_input_data       = original_task.copy_input_data
        self._link_input_data       = original_task.link_input_data
        self._copy_output_data      = original_task.copy_output_data
        self._download_output_data  = original_task.download_output_data


        ## The following help in updation
        # Stage this task belongs to
        self._parent_stage = original_task.parent_stage
        # Pipeline this task belongs to
        self._parent_pipeline = original_task.parent_pipeline

        
    def to_dict(self):

        task_desc_as_dict = {
                                                'uid': self._uid,
                                                'name': self._name,
                                                'state': self._state,

                                                'pre_exec': self._pre_exec,
                                                'executable': self._executable,
                                                'arguments': self._arguments,
                                                'post_exec': self._post_exec,
                                                'cores': self._cores,

                                                'upload_input_data': self._upload_input_data,
                                                'copy_input_data': self._copy_input_data,
                                                'link_input_data': self._link_input_data,
                                                'copy_output_data': self._copy_output_data,
                                                'download_output_data': self._download_output_data,

                                                'parent_stage': self._parent_stage,
                                                'parent_pipeline': self._parent_pipeline,
                                        }

        return task_desc_as_dict
        