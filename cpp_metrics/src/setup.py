from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext
import os

this_dir = os.path.abspath(os.path.dirname(__file__))

ext_modules = [
    Pybind11Extension(
        name="indicator",
        sources=[
            os.path.join(this_dir, "bindings.cpp"),
            os.path.join(this_dir, "ema", "ema.cpp"),
            os.path.join(this_dir, "sma", "sma.cpp"),
            os.path.join(this_dir, "rsi", "rsi.cpp"),
        ],
        include_dirs=[
            os.path.join(this_dir, "ema"),
            os.path.join(this_dir, "sma"),
            os.path.join(this_dir, "rsi"),
        ],
        cxx_std=17
    )
]

setup(
    name="indicator",
    version="0.1",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
