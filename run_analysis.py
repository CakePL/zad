from iris_analysis import calculate
from iris_analysis.io.load import load
from iris_analysis.io.save import save
import sys


if __name__ == '__main__':
    data = load(sys.argv[1])
    result = [{key: f(data[key]) for key in data} for f in (calculate.mean, calculate.median, calculate.std)]
    #following rows represents mean, madian and std respectively
    save(sys.argv[2], result)