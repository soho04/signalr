// #include <pybind11/pybind11.h>
// namespace py = pybind11;

#include <deque>
#include <vector>
#include "sma.h"

SMA::SMA(int period) : period_(period), sum_(0.0), sma_(0.0) {}

void SMA::init(const std::vector<double> & initial_data) {

    window_.clear();
    sum_ = 0.0;
    sma_ = 0.0;

    for (double val : initial_data){
        window_.push_back(val);
        sum_ += val;
    }

    while (window_.size() < period_) {
        sum_ -= window_.front();
        window_.pop_front();
    }

    sma_ = sum_ / period_;
}

double SMA::addDataPoint(double value) {
    double lastDay = window_.front();
    window_.pop_front();
    window_.push_back(value);

    sma_ = (sum_ - lastDay + value) / period_;

    sum_ = sum_ - lastDay + value;
        
    return sma_;
}

double SMA::getValue() const {
    return sma_;
}

// PYBIND11_MODULE(indicators, module_itself) {
//     py::class_<SMA>(module_itself, "SMA")
//         .def(py::init<int>(), py::arg("period"))
//         .def("init", &SMA::init, py::arg("initial_data"), 
//             "Initialize the SMA with a vector of initial data points.")
//         .def("addDataPoint", &SMA::addDataPoint, py::arg("value"),
//             "Add a new data point to the SMA and delta-calculate the new value.")
//         .def("getValue", &SMA::getValue, "Get current SMA value.");
// }