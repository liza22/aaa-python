import random
from typing import Callable
from pizza import Pizza


def log(tmpl: str) -> Callable:
    """
    Декоратор для логирования времени выполнения функции.
    Принимает шаблон лога.
    """
    def decorator(function: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            exec_time = random.randint(1, 10)
            if tmpl:
                print(tmpl.format(exec_time))
            else:
                print(f"{function.__name__} - {exec_time}с!")
            return result
        return wrapper
    return decorator


@log('')
def bake(pizza: Pizza):
    """Готовит пиццу"""
    print(f"Приготовлена {pizza.__class__.__name__} "
          f"размера {pizza.size.value}")


@log('\U0001F697 Доставили за {}с!')
def delivery(pizza: Pizza):
    """Доставляет пиццу"""
    print(f"Доставка пиццы {pizza.__class__.__name__}")


@log('\U0001F3E0 Забрали за {}с!')
def pickup(pizza: Pizza):
    """Самовывоз"""
    print(f"Пицца {pizza.__class__.__name__} готова к самовывозу")
