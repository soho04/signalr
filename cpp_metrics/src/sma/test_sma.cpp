#include <iostream>
#include <vector>
#include "SMA.h"

int main() {
    SMA sma(3);

    std::vector<double> initial_data = {1.0, 2.0, 3.0};
    sma.init(initial_data);

    std::cout << "Initial SMA value: " << sma.getValue() << std::endl;

    sma.addDataPoint(4.0);
    std::cout << "SMA after adding 4.0: " << sma.getValue() << std::endl;

    sma.addDataPoint(5.0);
    std::cout << "SMA after adding 5.0: " << sma.getValue() << std::endl;

    return 0;
}