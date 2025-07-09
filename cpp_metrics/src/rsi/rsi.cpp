#include "RSI.h"
#include <cstddef>
#include <iostream>
#include <cmath>

RSI::RSI(int period)
    : period_(period), gain_(0.0), loss_(0.0), avgGain_(0.0), avgLoss_(0.0), rsi_(0.0) {}

void RSI::init(const std::vector<double>& initial_data) {
    
    window_.push_back(initial_data[0]);

    for (size_t i = 1; i < initial_data.size(); ++i) {
        if (initial_data[i] > initial_data[i-1]) {
            gain_ += (initial_data[i] - initial_data[i-1]);
            window_.push_back(initial_data[i]);
        } else {
            loss_ += std::abs((initial_data[i] - initial_data[i-1]));
            window_.push_back(initial_data[i]);
        }
    }

    std::cout << "Total Loss: " << loss_ << std::endl;

    avgGain_ = gain_ / period_;
    avgLoss_ = loss_ / period_;

    rsi_ = 100 - (100 / (1 + (avgGain_ / avgLoss_)));
}

double RSI::addDataPoint(double value) {

    double delta = value - window_.back();
    double gain = 0.0;
    double loss = 0.0;

    window_.pop_front();
    window_.push_back(value);
   
    if (delta > 0) {
        gain = delta;
    } else {
        loss = -delta;
    }

    avgGain_ = ((avgGain_ * (period_ - 1)) + gain) / period_;
    avgLoss_ = ((avgLoss_ * (period_ - 1)) + loss) / period_;

    if (avgLoss_ == 0) {
        rsi_ = 100.0;
    } else {
        rsi_ = 100.0 - (100.0 / (1.0 + (avgGain_ / avgLoss_)));
    }

    return rsi_;
}

double RSI::getRSI() const {
    return rsi_;
}
