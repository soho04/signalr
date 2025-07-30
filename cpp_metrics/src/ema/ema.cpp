#include <deque>
#include <vector>
#include <cstddef>
#include <iostream>
#include <cmath>
#include "ema.h"

EMA::EMA(int period, int smaPeriod) : period_(period), smaPeriod_(smaPeriod), sum_(0.0), alpha_(0.0), ema_(0.0) {}

void EMA::init(const std::vector<double> & initial_data) {

    alpha_ = 2.0 / (period_ + 1);
    
    for (size_t i = 0; i < smaPeriod_; ++i) {
        sum_ += initial_data[i];
    }

    ema_ = sum_ / smaPeriod_;

    sum_ = 0.0;

    for (size_t i = smaPeriod_; i < initial_data.size(); ++i) {
        ema_ = (alpha_ * initial_data[i]) + ((1 - alpha_) * ema_);
    }

}

double EMA::addDataPoint(double value) {

    ema_ = (alpha_ * value) + ((1 - alpha_) * ema_);

    return ema_;
}

double EMA::getEMA() const {
    return ema_;
}
