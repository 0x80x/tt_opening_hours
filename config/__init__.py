import importlib

# Паттерн одиночки, что бы был только 1 экзепляр класса настроек
class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            config = importlib.import_module('config.conf')
            for key, value in config.__dict__.items():
                setattr(cls._instance, key, value)
        return cls._instance
    

settings = AppConfig()