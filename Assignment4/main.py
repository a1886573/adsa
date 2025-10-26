#Assignment 4  implementation of graph algorithms
#a1886573 Aidan Matkovic Last edited 26/10/25 11:06 PM
#Was best decided to implement a Kruskal MST alg with union find sorting structure
def city_cost(cost):
    #finds the build cost for each city, A - Z is representing by 0-25 and then a-z is 26-51 (hence + 26 in line 9)
    if 'A' <= cost <= 'Z':
        return ord(cost) - ord('A')
    else:
        return ord(cost) - ord('a') + 26

def solve(country, build, destroy):
    #initialising variables
    edges = []
    N_cities = len(country)
    parent = [i for i in range(0,N_cities)]
    rank = [0]*N_cities
    MST_cost = 0
    MST = set()
    
    #find(x) function, slide 15, for each edge we find the parent
    def find(x):
        if parent[x] != x:  
            parent[x] = find(parent[x])
        return parent[x]
    
    #union function, slide 17, done via rank based
    def union(x,y):
        #roots x and y
        R_x = find(x)
        R_y = find(y)
        
        #if two roots are already in the same set, they dont have to be added again 
        if R_x == R_y:
            return False
        #if the x is the shorter root then, make y the parent to keep the height at a minimum
        if rank[R_x] < rank[R_y]:
            parent[R_x] = R_y
        #same logic applied here, if now y is smaller make x the parent
        elif rank[R_x] > rank[R_y]:
            parent[R_y] = R_x
        else:
            #and if they have the same height, just chose x to be the parent
            parent[R_y] = R_x
            #increment the combined height by 1
            rank[R_x] += 1

        return True
    
    #need to now loop through each existing roads between cities i and j
    for i in range(N_cities):
        for j in range(i+1,N_cities):
            #if country[i][j] == 1 then there exists a road
            if country[i][j] == '1':
                #to minimise cost within the Kruskal alg, a negative cost is appended so that the roads with cheaper destroy costs are preferred
                #Kruskal's method prefers cheaper to destroy roads
                edges.append((-city_cost(destroy[i][j]),i,j, True))
            else:
                #if the road does not exist then the cost to build it is added to the list 
                edges.append((city_cost(build[i][j]), i, j , False))
            
    
    # sorting the edges list from smallest to largest weight, lambda x: x[0] takes the first element of each as the key so can sort by that
    edges.sort(key = lambda x: x[0])
    

    #now interpreting the edges list
    for w ,u, v, existing in edges:
        if union(u,v):
            #adding the path (connecting edges) between u and v into the MST set 
            MST.add((u,v))
            MST.add((v,u))
            
            if existing:
                #if the road exists then added cost => 0
                MST_cost += 0
            else:
                #if not then has to be built, hence add the cost w
                MST_cost += w

    for i in range(N_cities):
        for j in range(i+1, N_cities):
            #the roads that were not chosen in the MST set will then have to be destroyed 
            if country[i][j] == '1' and (i,j) not in MST:
                # the cost of their destruction is then added to the overall MST cost 
                MST_cost += city_cost(destroy[i][j])

    return MST_cost


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



   




    



