import codecs


class Range:
    def __init__(self, agefrom, ageto):
        self.agefrom = agefrom
        self.ageto = ageto

    def getFrom(self):
        return self.agefrom

    def getTo(self):
        return self.ageto

    def suitable(self):
        global o
        res = []
        for h in o:
            if self.agefrom <= h[1] <= self.ageto:
                res.append(str(h[0] + ' (' + str(h[1]) + ')'))
        return res

    def out(self):
        if self.ageto == 123:
            return str(self.agefrom) + '+'
        elif self.ageto == self.agefrom:
            return str(self.agefrom)
        else:
            return str(self.agefrom) + '-' + str(self.ageto)


def listOut(arr):
    global Fout
    res = ''
    for c in arr:
        res += str(c) + ', '
    Fout.write(res[:-2])


if __name__ == '__main__':

    n = [1, 2, 3, 70, 71, 120]  # задание границ

    Fout = codecs.open('output.txt', 'w', encoding='utf-8')
    with codecs.open('list_of_persons.txt', encoding='utf-8') as persons:
        personlist = list(set(persons.readline().split(', ')))
        o = []
        for one in personlist:
            if one != 'END':
                p = one.split()
                fio = " ".join(p[:-1])
                age = int(p[-1])
                o.append([fio, age])
        print(o)  # отладка

    s = [Range(0, n[0])]
    for i in range(0, len(n) - 1):
        s.append(Range(n[i] + 1, n[i + 1]))
    s.append(Range(n[-1]+1, 123))
    s = s[::-1]
    for c in s:
        print(c.out())  # отладка
    for k in range(len(s)):
        if len(s[k].suitable()) > 0:
            Fout.write((s[k]).out() + ': ')
            listOut(s[k].suitable())
            Fout.write('\n')
    Fout.close()
