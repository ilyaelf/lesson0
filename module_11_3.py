import inspect

class Object():
    a = 10
    b = "11"
    def action(self):
        print("some action")
    def ab(self):
        print(f"{self.a}и{self.b}")

def introspection_info(obj):
    result = {}
    result['имя объекта'] = obj.__name__
    result['тип объекта'] = type(obj)
    m_list = []
    for attr_name in dir(obj):
        n = getattr(obj,attr_name)
        if inspect.isfunction(n):
            m_list.append(attr_name)
    result['методы'] = m_list
    atr_list = []
    for attr_name in dir(obj):
        n = getattr(obj,attr_name)
        if not (attr_name.startswith('_') or inspect.isfunction(n)):
            atr_list.append([attr_name,type(n)])
    result['атрибуты'] = atr_list
    result['модуль'] = obj.__module__
    return (result)


class_info = introspection_info(Object)
print(class_info)