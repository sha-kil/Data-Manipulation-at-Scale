import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    #value = record[1]
    #words = value.split()
    #for w in words:
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      #total += v
        if v[0] == "order":
            for j in list_of_values:
                if j[0] != "order":
                    val = v + j
                    mr.emit(val)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
