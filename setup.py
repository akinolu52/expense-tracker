from setuptools import setup

setup(
    name='expense-tracker',
    version='0.1',
    py_modules=['expense_tracker_cli'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'expense-tracker = expense_tracker_cli:main',
        ],
    },
)
