import yaml
from util.path_util import Path

class Config():
    def __init__(self):
        self.config = self._load_config()
        self.model_name = self.config['model']
    def _load_config(self):
        config_path = Path()._config_path()
        with open(config_path) as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
        return self.config

    def _set_model_name(self, model_name):
        self.config['model'] = model_name


if __name__ =="__main__":
    test = Config().model_name