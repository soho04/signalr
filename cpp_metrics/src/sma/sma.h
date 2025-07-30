#ifndef SMA_H
#define SMA_H

#include <vector>
#include <deque>

class SMA {
public:
    SMA(int period);
    void init(const std::vector<double>& initial_data);
    double addDataPoint(double value);
    double getValue() const;

private:
    int period_;
    double sum_;
    std::deque<double> window_;
    double sma_;
};

#endif