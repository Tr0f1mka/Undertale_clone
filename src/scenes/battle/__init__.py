# # В файле __init__.py директории
# import os
# import importlib

# __all__ = []

# # Автоматически импортируем все модули
# for filename in os.listdir(os.path.dirname(__file__)):
#     if filename.endswith('.py') and not filename.startswith('__'):
#         module_name = filename[:-3]
#         if not module_name.endswith("_stage"):
#             continue

#         module = importlib.import_module(f'.{module_name}', __package__)

#         # Добавляем все классы из модуля
#         for attr_name in dir(module):
#             if not attr_name.endswith("Stage"):
#                 continue

#             attr = getattr(module, attr_name)
#             if isinstance(attr, type):
#                 globals()[attr_name] = attr
#                 __all__.append(attr_name)

# # Затем можно импортировать так:
# # from my_directory import *
