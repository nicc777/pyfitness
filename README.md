# pyFitness

Here are some classes I use in calculating stuff while I train/exercise.

Very early development.

## Quickstart

Here is a quick example for calculating time per distance unit

    Python 3.5.1 (default, Dec  7 2015, 21:59:10) 
    [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.1.76)] on darwin
    >>> from pyfitness.time_processing import TimeOverDistance
    >>> t = TimeOverDistance(0,41,8)
    >>> t.calc_min_per_distance(distance=7.5)
    000:05:29.07 per Km
