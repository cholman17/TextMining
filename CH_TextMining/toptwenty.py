from string import punctuation, whitespace
import numpy as np
import pylab as plts
import matplotlib.pyplot as plt

Elmo = 'elmo_tweets.txt'
Oscar = 'oscargrouch_tweets.txt'
Cookie = 'cookiemonster_tweets.txt'
sesames = ["Elmo", "Oscar", "Cookie"]

sesame = [Elmo, Oscar, Cookie]
filterlist = ['the','of','an', 'a', 'this','with', 'or', 'in', 'that','for', 'is', 'are', 'and', 'dis', '\xe2\x80\xa6', '\xe2\x80\x98em']


def words(monster):
    list_ = []
    flag = False
    signal = "\n"
    op = open(monster, 'r')
    for line in op:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    op.close()
    return list_


def clean(word):
     result = ''
     for char in word:
         if (char in whitespace) or (char in punctuation):
             pass
         else:
             result += char.lower()
     return result

def histogram(data):
     hist = {}
     for word in data:
         if word == '':
             pass
         else:
             hist[word] = hist.get(word, 0) + 1
     return hist

def main():
    for monster in sesame:
        data = [clean(word) for word in words(monster)]
        print "Stats for %s:" % monster
        hist = histogram(data)
        top20 = []
        topw = []
        topv = []
        for key in hist:
            if key.lower() not in filterlist:
                top20.append([hist[key], key])
        top20.sort(reverse=True)
        for i in range(0, 20):
            topw.append(top20[i][1])
            topv.append(top20[i][0])
        for i in range(0, 20):
            print "  %s) %s %s" % (i + 1, top20[i][1], top20[i][0])

        print "\n"

        print '+++++++++++++++++++++++++++'
        print 'MAKING HISTOGRAM'

        x = 0

        pos = np.arange(len(topw))
        LABELS = topw
        width = 1.0     # gives histogram aspect to the bar diagram
        ax = plt.axes()
        ax.set_xticks(pos + (width / 2))
        ax.set_xticklabels(LABELS)
        plt.bar(pos,topv, width, color='r')
        plt.xlabel('Word Index')
        plt.ylabel('Frequency')
        plt.title('Frequency Chart for %s' % monster)
        fig = plt.gcf()
        plt.show()
        fig.savefig('wordfreq_%.5s.png' % monster)

        print 'FINISHED ALL GRAPHS'
main()
