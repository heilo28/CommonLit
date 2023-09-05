import yaml
from path_util import Path

class Config():
    def __init__(self):
        self.config = self._load_config()
    def _load_config(self):
        config_path = Path()._config_path()
        with open(config_path) as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
        return self.config


if __name__ =="__main__":
    test = Config()