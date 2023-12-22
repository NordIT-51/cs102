class User:
    def __init__(self, films_list: str):
        self.films = list(set(films_list.strip().split(',')))


def compare(main_user, target_user):
    arr = []  # не совпадающие
    n = 0  # кол-во совпавших
    for film_num in target_user.films:
        if film_num in main_user.films:
            n += 1
        else:
            arr.append(film_num)
    if n * 2 >= len(main_user.films):
        return arr, (n / len(main_user.films))
    else:
        return None, 0


if __name__ == '__main__':
    user = User(input())
    films = dict()
    recommend = dict()
    for i in open("films.txt", encoding="utf-8").readlines():
        film = i.rstrip().split(',')
        films[film[0]] = film[1]
        recommend[film[0]] = 0
    users = [User(s) for s in open('views_history.txt').readlines()]
    for t_user in users:
        rec = compare(user, t_user)
        if rec[0] is not None:
            for num in rec[0]:
                recommend[num] += rec[1]
    id = 0
    mx = 0
    for k, v in recommend.items():
        if v > mx:
            mx = v
            id = k
    print(films[id])
