#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  
#include "sma.h"
#include "rsi.h"
#include "ema.h"

namespace py = pybind11;

PYBIND11_MODULE(indicator, m) {
    py::class_<SMA>(m, "SMA")
        .def(py::init<int>(), py::arg("period"))
        .def("init", &SMA::init, py::arg("initial_data"))
        .def("addDataPoint", &SMA::addDataPoint, py::arg("value"))
        .def("getValue", &SMA::getValue);

    // Bind RSI
    py::class_<RSI>(m, "RSI")
        .def(py::init<int>(), py::arg("period"))
        .def("init", &RSI::init, py::arg("initial_data"))
        .def("addDataPoint", &RSI::addDataPoint, py::arg("value"))
        .def("getRSI", &RSI::getRSI);

    // Bind EMA
    py::class_<EMA>(m, "EMA")
        .def(py::init<int, int>(), py::arg("period"), py::arg("smaPeriod"))
        .def("init", &EMA::init, py::arg("initial_data"))
        .def("addDataPoint", &EMA::addDataPoint, py::arg("value"))
        .def("getEMA", &EMA::getEMA);
}