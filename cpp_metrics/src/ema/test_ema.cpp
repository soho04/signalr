#include <iostream>
#include <vector>
#include "EMA.h"

int main () {
    EMA ema(4, 3);

    std::vector<double> initial_data = {10, 11, 12, 13};

    ema.init(initial_data);

    std::cout << "Initial EMA value: " << ema.getEMA();

    ema.addDataPoint(14);

}
