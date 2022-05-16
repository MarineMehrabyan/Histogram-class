import random
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt, pow

class Histogram:

    def __init__(self, name, nbins, xlow, xup):
        self.name=name
        self.bins=nbins
        self.xlow=xlow
        self.xup=xup
        self.hist=np.zeros(self.bins)

    def get_bin_center(self, x):
        return self.xlow+(x-1)*self.get_bin_width()+self.get_bin_width()/2

    def draw_graph(self, fname: str)->None:
        bins=np.zeros(self.bins)
        widths = np.zeros(self.bins)
        for ii in range(self.bins):
            bins[ii] = self.get_bin_center(ii)
            widths[ii] = self.get_bin_width()
        plt.bar(bins, self.hist, widths)
        plt.title(self.name)
        plt.savefig(fname)

    def get_bin_width(self):
        return (self.xup-self.xlow)/self.bins


    def get_bin(self,x):
        n = int(np.ceil(self.get_bin_width()))
        mmin=self.xlow
        mmax=mmin+n
        level=1
        while(mmin<=self.xup):
            if x>=mmin and x<mmax:
                return level
            mmin = mmax
            mmax += n
            level += 1
        return None


    def fill(self, x):
       level=0
       n = int(np.ceil(self.get_bin_width()))

       for i in range(self.xlow, self.xup+1, n):
           if i==0:
               if x>=i and x<=i+n:
                   self.hist[level]+=1
           elif x>i and x<=i+n:
                self.hist[level]+=1

           level=level+1

    def get_integral(self):
        return (self.xup - self.xlow) * self.get_mean()

    def get_mean(self):
        return self.hist.sum()/self.bins

    def get_mod(self):
        return max(set(self.hist), key = list(self.hist).count)

    def get_bin_content(self, i):
        return self.hist[i]

    def get_minimum(self):
        return min(self.hist)

    def get_maximum_bin(self):
        max=0
        n = int(np.ceil(self.get_bin_width()))
        for i in range(n+1):
            if self.hist[i]>max:
                max=self.hist[i]
                maxindex=i
        return maxindex+1

    def assign(self, hist2):
        if(self.bins==hist2.bins):
            for i in range(0, len(hist2.hist)):
                self.hist[i]=hist2.hist[i]
        else:
            print("The sizes are not the same!")

    def get_std(self):
        sum=0
        mean=self.get_mean()
        for i in self.hist:
            sum=sum+pow((i-mean),2)
        res=1/self.bins * sum
        return sqrt(res)

    def printhist(self):
        print(self.hist)





h1=Histogram("my1_histo", 6,0,30)
h2=Histogram("my2_histo",10,-25,25)
a=[]
for i in range(50):
    a.append(random.randint(0,30))
a.sort()
for i in range(len(a)):
    h1.fill(a[i])

b=[]
for i in range(50):
    b.append(random.randint(-25,25))
b.sort()
for i in range(len(b)):
    h2.fill(b[i])
h1.printhist()
h2.printhist()
h1.assign(h2)
h1.printhist()
print("get standart deviation -> ",h1.get_std())
h2.draw_graph("my1_histo")
print("bin width ->  ", h1.get_bin_width(), '\n')
print("bin -> ", h1.get_bin(16))
print("integral ->  " , h1.get_integral())
print("mean ->  ", h1.get_mean())
print("mode -> ", h1.get_mod())
print("bin  content ->", h1.get_bin_content(4))
print("get minimum ->", h1.get_minimum())
print("get maximum bin ->", h1.get_maximum_bin())

