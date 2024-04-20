# X = 10000
# for i in range(X):
#     for j in range(X):
#         k = i* j 
#     print(f"{i+1} / {X}", end='\r')

#------------------------------------------------------------
# from progress.bar import Bar
# X = 10000
# with Bar('Processing', max=X, fill="hi", suffix="%(percent).1f%% - %(eta)ds" ) as bar:
#     for i in range(X):
#         for j in range(X):
#             k = i* j 
#         bar.next()
#------------------------------------------------------------
# from tqdm.rich import tqdm  # or import trange()
# X = 10000
# for i in tqdm(range(X)):  # range >>> trange()
#     for j in range(X):
#         k = i* j 
#------------------------------------------------------------
# from tqdm.rich import trange  # or import trange()
# X = 10000
# for i in trange(X):  # range >>> trange()
#     for j in range(X):
#         k = i* j 
#------------------------------------------------------------
from tqdm.tk import tqdm  # or import trange()
X = 10000
for i in tqdm(range(X)):  # range >>> trange()
    for j in range(X):
        k = i* j 



# https://www.youtube.com/watch?v=giGxdaG4at4
        