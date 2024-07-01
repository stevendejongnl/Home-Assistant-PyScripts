from enum import Enum


class DependencyType(Enum):
    REAL = 'real'
    FAKE = 'fake'


class DependencyInjection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DependencyInjection, cls).__new__(cls, *args, **kwargs)
            cls._instance.dependencies = {}
        return cls._instance

    def add_dependency(self, dependency_info: tuple):
        name, instance, dependency_type = dependency_info
        self.dependencies[name] = {'instance': instance, 'type': dependency_type.value}

    def get_dependency(self, cls):
        dependency = self.dependencies.get(cls.__name__)
        if dependency:
            return dependency['instance']
        return None


def add_dependency(dependency_type: DependencyType):
    def decorator(cls):
        dependency_injection = DependencyInjection()
        dependency_injection.add_dependency((cls.__name__, cls(), dependency_type))
        return cls
    return decorator
