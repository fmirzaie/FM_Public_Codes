import pandas as pd
import numpy as np
arrays = [["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],["one", "two", "one", "two", "one", "two", "one", "two"]]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
s = pd.Series(np.random.randn(8), index=index)

############
iterables = [["bar", "baz", "foo", "qux"], ["one", "two"]]
pd.MultiIndex.from_product(iterables, names=["first", "second"])

####
df = pd.DataFrame([["bar", "one"], ["bar", "two"], ["foo", "one"], ["foo", "two"]], columns=["first", "second"])
pd.MultiIndex.from_frame(df)

#####
arrays = [["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],["one", "two", "one", "two", "one", "two", "one", "two"]]
s = pd.Series(np.random.randn(8), index=arrays)
df = pd.DataFrame(np.random.randn(8, 4), index=arrays)
df.index.names
#
df = pd.DataFrame(np.random.randn(3, 8), index=["A", "B", "C"], columns=index)
df["bar"]
df.to_csv("multiindex.csv")