from setuptools import setup

setup(
    name="personal_paraphrase",
    version="1.0.0",
    py_modules=["paraphrase", "configEditor"],
    install_requires=["requests"],
    author="Robert (Bob) Greenwade",
    description="Persona-driven editorial rewriter for AI agents",
    license="MIT"
)
