#ifndef RSI_H
#define RSI_H

#include <vector>
#include <deque>

class RSI {
public:
    RSI(int period);
    void init(const std::vector<double>& initial_data);
    double addDataPoint(double value);
    double getRSI() const;

private:
    int period_;
    double gain_;
    double loss_;
    double avgGain_;
    double avgLoss_;
    std::deque<double> window_;
    double rsi_;
};

#endif // RSI_H
