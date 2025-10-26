#Assignment 4  implementation of graph algorithms
#a1886573 Aidan Matkovic
#Was best decided to implement a Kruskal MST alg with union find sorting structure
def city_cost(cost):
    #finds the build cost for each city, A - Z is representing by 0-25 and then a-z is 26-51 (hence + 26 in line 9)
    if 'A' <= cost <= 'Z':
        return ord(cost) - ord('A')
    else:
        return ord(cost) - ord('a') + 26

def solve(country, build, destroy):
    edges = []
    destroy_cost = 0
    N_cities = len(country)
    parent = [i for i in range(0,N_cities)]
    rank = [0]*N_cities
    MST_cost = 0
    count = 0

    def find(x):
        if parent[x] != x:  
            parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        R_x = find(x)
        R_y = find(y)

        if R_x == R_y:
            return False
        if rank[R_x] < rank[R_y]:
            parent[R_x] = R_y
        elif rank[R_x] > rank[R_y]:
            parent[R_y] = R_x
        else:
            parent[R_y] = R_x
            rank[R_x] += 1

        return True

    for i in range(N_cities):
        for j in range(i+1,N_cities):
            if country[i][j] == '1':
                destroy_cost += city_cost(destroy[i][j])
                edges.append((city_cost(destroy[i][j]), i, j))
            else:
                edges.append((city_cost(build[i][j]), i, j))
    
    # sorting the edges array from smallest to largest weight, lambda x: x[0] takes the first element of each as the key so can sort by that
    edges.sort(key = lambda x: x[0])
    
    for (w,u,v) in edges:
        if union(u,v):
            MST_cost += w
            count += 1
            if count == N_cities-1:
                break

    return destroy_cost + MST_cost


#main function to process the inputs
def main():
    #firstly need to split up the command line and disect each inputs country, build and destory
    commandLine = input().lstrip()
    country_input, build_input, destroy_input = commandLine.split()
    #allocate these parts accordingly:
    country = country_input.split(",")
    build = build_input.split(",")
    destroy = destroy_input.split(",")
    
    #call solve and print the results
    print(solve(country, build, destroy))

#call main
if __name__ == "__main__":
    main()



   




    



