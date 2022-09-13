# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
import inspect


def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass

def print_name_and_args(func):
    func_name_original = func.__name__
    func_name = func.__name__.split('_')
    func_args = inspect.getfullargspec(func).args
    print("Original name function: ", func_name_original)
    print('Name function: ', *func_name)
    print('Names arguments: ', end=' ')
    if not len(func_args):
        print('no arguments\n')
    else:
        print(*func_args, '\n', sep=' ')


print_name_and_args(open_browser)
print_name_and_args(go_to_companyname_homepage)
print_name_and_args(find_registration_button_on_login_page)