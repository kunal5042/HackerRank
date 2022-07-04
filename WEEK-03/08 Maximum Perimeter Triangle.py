#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    largest_per = float('-inf')
    triangles = []
    
    # to find all possible triangles 
    for x in range(len(sticks)):
        for y in range(x+1, len(sticks)):
            for z in range(y+1, len(sticks)):
                # current possible triangle 
                triangle = [sticks[x], sticks[y], sticks[z]]
                triangle.sort(reverse=False)
                
                # if current three values does not satisfy conditions for a valid triangle 
                if triangle[2] >= triangle[0] + triangle[1]:
                    continue
                else:
                    # current perimeter
                    perimeter = sum(triangle)
                    
                    # if we found two such triangles whose perimeter is maximum
                    # add them to list of possible results
                    if perimeter == largest_per:
                        triangles.append(triangle)
                    
                    # if current perimeter is greater than largest perimeter found so far
                    # all the triangles in the possible results list are obsolete/useless, hence clear the triangles array
                    # and add the new triangle to the list
                    if perimeter > largest_per:
                        triangles.clear()
                        triangles.append(triangle)
                        largest_per = perimeter

    # if there are more than one
    if len(triangles) > 1:
        # start with the first one
        resultant_triangle = triangles[0]

        # compare it with remaining ones to find the best one
        for triangle in triangles[1:]:
            # if max of T1 > T2, result = T1
            if max(triangle) > max(resultant_triangle):
                resultant_triangle = triangle
              
            # if not, compare and find the max of min of both Ts
            elif max(triangle) == max(resultant_triangle):
                if min(triangle) > min(resultant_triangle):
                    resultant_triangle = triangle
                    
            else:
                continue
        
        return resultant_triangle
    else:
        # it could be a possiblity that we didn't find any such triangle
        # hence the len of resultant list will be zero
        # check that
        if len(triangles) != 0:
            # if it's not empty there is only one such triangle
            # return that
            return triangles[0]
        else:
            # if resultant list is empty, return -1
            return [-1]
    
# Kunal Wadhwa
