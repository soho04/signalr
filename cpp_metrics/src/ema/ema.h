#ifndef EMA_H
#define EMA_H

#include <vector>
#include <deque>

class EMA {
public:
    EMA(int period, int smaPeriod);
    void init(const std::vector<double>& initial_data);
    double addDataPoint(double value);
    double getEMA() const;

private:
    int period_;
    double smaPeriod_;
    double alpha_;
    std::deque<double> window_;
    double ema_;
    double sum_;
};

#endif
