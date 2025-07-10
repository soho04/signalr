import sys
import os

# Compute absolute path to cpp_metrics/src
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cpp_metrics', 'src'))

# Add it to sys.path if not already
if module_path not in sys.path:
    sys.path.insert(0, module_path)

# Now import
from indicator import SMA, EMA, RSI

# Example usage
sma = SMA(3)
sma.init([1, 2, 3])
sma.addDataPoint(4)
print("SMA value:", sma.getValue())

ema = EMA(3, 1)
ema.init([1, 2, 3])
print("EMA value:", ema.getEMA())
