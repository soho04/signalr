#include <iostream>
#include <vector>
#include "RSI.h"

int main () {
    RSI rsi(2);

    std::vector<double> initial_data = {44.15, 43.61, 52.00};

    rsi.init(initial_data);

    std::cout << "Initial RSI value: " << rsi.getRSI() << std::endl;

    rsi.addDataPoint(50);

    std::cout << "RSI value: " << rsi.getRSI() << std::endl;

}
