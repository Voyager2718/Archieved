import copy

p1 = [10000 for i in range(80)]
p_real = [0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.145675, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.2035795918367347, 0.096, 0.096, 0.096, 0.096, 0.096, 0.096, 0.096, 0.096, 0.096, 0.096, 0.096, 0.096, 0.096, 0.096, 0.096]#16周岁以上至60周岁以下（不含60周岁）的劳动年龄人口91096万人，60周岁及以上人口2.22亿人
old_std = 65

def population_ratio(population):
    print('------------POPULATION RATIO------------')
    print((sum(population[0:20]),sum(population[20:old_std]),sum(population[old_std:80])))
    print('------------POPULATION RATIO------------\n')
    return (sum(population[0:20]),sum(population[20:old_std]),sum(population[old_std:80]))

def feed_ratio(pop_ratio):
    print('------------FEED RATIO------------')
    print((pop_ratio[0]+pop_ratio[2])/pop_ratio[1])
    print('------------FEED RATIO------------')
    return (pop_ratio[0]+pop_ratio[2])/pop_ratio[1]
    

def iter(population, years, birth_rate, birth_age):
    population = copy.deepcopy(population)
    max_fr = 0
    max_fr_year = 0
    min_fr = 999
    min_fr_year = 0
    feed_ratio_list = []
    population_list_0_20 = []
    population_list_20_60 = []
    population_list_60_80 = []
    population_list_all = []
    for i in range(years+1):
        print('------------------------------------------------------------------------------------------------\nYear:',i)
        print(population)
        fr = feed_ratio(population_ratio(population))
        print('------------------------------------------------------------------------------------------------\n')
        max_fr_year = [max_fr_year,i][fr>max_fr]
        max_fr = max(fr, max_fr)
        min_fr_year = [min_fr_year,i][fr<min_fr]
        min_fr = min(fr, min_fr)
        feed_ratio_list += [fr]
        population_list_0_20 += [sum(population[0:20])]
        population_list_20_60 += [sum(population[20:old_std])]
        population_list_60_80 += [sum(population[old_std:80])]
        population_list_all += [sum(population)]
        population = [population[birth_age]*(birth_rate(i)/2)] + population
        del population[len(population)-1]
        print()
    print('\n\n\n\n','\n------------MAX FEED RATIO------------')
    print('MAX FEED RATIO:',max_fr)
    print('MAX FEED RATIO YEAR:',max_fr_year)
    print('------------MAX FEED RATIO------------')
    print('\n------------MIN FEED RATIO------------')
    print('MIN FEED RATIO:',min_fr)
    print('MIN FEED RATIO YEAR:',min_fr_year)
    print('------------MIN FEED RATIO------------')
    print('\n\nYear simulated:',years, '\nAverage birth age:',birth_age)
    return (feed_ratio_list, population_list_0_20, population_list_20_60, population_list_60_80, population_list_all)

    
def export_csv(results, project):
    ratio = open(project+'_ratio.csv', 'w+')
    pop0 = open(project+'_pop0.csv', 'w+')
    pop1 = open(project+'_pop1.csv', 'w+')
    pop2 = open(project+'_pop2.csv', 'w+')
    all = open(project+'_all.csv', 'w+')
    for i in range(len(results[0])):
        ratio.write(str(i)+str(',')+str(results[0][i])+str('\n'))
        pop0.write(str(i)+str(',')+str(results[1][i])+str(',')+str(results[4][i])+str('\n'))
        pop1.write(str(i)+str(',')+str(results[2][i])+str(',')+str(results[4][i])+str('\n'))
        pop2.write(str(i)+str(',')+str(results[3][i])+str(',')+str(results[4][i])+str('\n'))
        all.write(str(i)+str(',')+str(results[0][i])+str(',')+str(results[1][i])+str(',')+str(results[2][i])+str(',')+str(results[3][i])+str(',')+str(results[4][i])+'\n')
    ratio.close()
    pop0.close()
    pop1.close()
    pop2.close()
    all.close()



# iter(p1,80,1,20)
# iter(p1,80,1,30)
# iter(p1,80,0.5,20)
# results = iter(p1,80,lambda x: 1,30) #模拟 80 年，生育率 1, 平均 30 岁生育
# results = iter(p1,80,lambda x: 1.05 if x < 20 else 1.5,30) #计划生育版（计划生育 20 年后恢复 1.5 生育率）
results = iter(p_real,80,lambda x: 1.6,30) #真实人口比例，模拟 80 年，生育率 1.6, 平均 30 岁生育
export_csv(results,'80y1br30aba') #输出结果


