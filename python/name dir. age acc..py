import operator

def person_lister(f):
    def inner(people):
        # taking in 'd' dict. to sort
        d = {}
        for i in people:
            key, value = (i[0], i[1], i[3]), int(i[2])
            d[key] = value

        # creating sorted dict. 'upd'
        sortedv = sorted(d.values())
        upd = {}
        l = []

        # creating final l list with age sorted fname,lname,gender
        for j in range(len(sortedv)):
            for k in list(d.keys()):
                if (d[k] == sortedv[j]):
                    p = (list(k))
                    p.insert(2, 0)
                    l.append(f(p))
                    del d[k]
        return l

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')