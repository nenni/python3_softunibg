from .base_loader import Loader
import yaml


class YAMLLoader(Loader):

    def load(self):
        with open(self.filename) as f:
            input_data = yaml.load(f)
            # print(input_data, input_data.__class__)
            return input_data

