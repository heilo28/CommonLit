import os
import glob


class Path:
    def __init__(self):
        self.PJT='CommonLit'
        self.root_path = self._root_path(self.PJT)
        self.train_path = self._train_path()
        self.valid_path = self._valid_path()

    def _root_path(self, root_dir):
        current_dir = os.getcwd()
        current_dir_sep = current_dir.split(os.sep)

        for idx, dir_name in enumerate(current_dir_sep):
            if root_dir == dir_name: break

        return os.sep.join(current_dir_sep[:idx + 1])

        return current_dir
    def _config_path(self):
        return os.path.join(self.root_path,'config/config.yml')
    def _data_path(self):
        return os.path.join(self.root_path, 'dataset')
    def _train_path(self):
        return os.path.join(self.root_path, 'data/summaries_train.csv')
    def _valid_path(self):
        return os.path.join(self.root_path, 'data/summaries_valid.csv')

if __name__ =="__main__":
    test = Path()