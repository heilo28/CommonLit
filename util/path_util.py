import os
import glob

def _root_path(root_dir):
    current_dir = os.getcwd()
    current_dir_sep = current_dir.split(os.sep)

    for idx, dir_name in enumerate(current_dir_sep):
        if root_dir == dir_name : break

    return os.sep.join(current_dir_sep[:idx + 1])

    return current_dir
class Path:
    def __init__(self):
        self.root_path = _root_path('CommonLit')
    def _config_path(self):
        return os.path.join(self.root_path,'./config/config.yml')
    def _data_path(self):
        return os.path.join(self.root_path, 'dataset')

