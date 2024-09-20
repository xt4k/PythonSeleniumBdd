import allure
from fixtures.environment import generate_environment_file

# def before_all(context):
#     allure.environment('Browser', 'Chrome')

def after_all(context):
    generate_environment_file()
    allure.generate_report()