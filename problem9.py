## 9.Mutations
## https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return "".join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    i = int(i)
    result = mutate_string(s, i, c)
    print(result)
