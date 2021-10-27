import random
random.random()

def throw_dice():
        return random.randint(1,6)

def throw_until_double():
        d1 = throw_dice()
        d2 = throw_dice()
        count = 0
        while d1 != d2:
                print(f'fail d1:{d1} d2:{d2}')
                d1 = throw_dice()
                d2 = throw_dice()
                count += 1
        return count

def results_avg(res_list):
        return sum(res_list)/len(res_list)

def main():
        results = []

        for num in range(0,100):
                results.append(throw_until_double())
        print(f'it took {sum(results) }tries to get 100 doubles')


main()
