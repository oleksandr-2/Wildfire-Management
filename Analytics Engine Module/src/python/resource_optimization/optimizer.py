import pulp

class ResourceAllocator:
    def __init__(self, num_resources, resource_costs, resource_constraints):
        """
        Initializes the ResourceAllocator with given parameters.
        
        :param num_resources: Number of resources to allocate.
        :param resource_costs: List of costs for each resource.
        :param resource_constraints: List of constraints for resource allocation.
        """
        self.num_resources = num_resources
        self.resource_costs = resource_costs
        self.resource_constraints = resource_constraints
        self.problem = pulp.LpProblem("Resource_Allocation_Problem", pulp.LpMinimize)
        self.variables = self._create_variables()
    
    def _create_variables(self):
        """
        Creates a list of binary decision variables.
        
        :return: Dictionary of binary decision variables.
        """
        variables = {
            f"x{i}": pulp.LpVariable(f"x{i}", cat=pulp.LpBinary)
            for i in range(self.num_resources)
        }
        return variables
    
    def set_constraints(self):
        """
        Sets up constraints for the optimization problem.
        """
        for i, constraint in enumerate(self.resource_constraints):
            self.problem += pulp.lpSum([self.variables[f"x{j}"] for j in range(self.num_resources)]) <= constraint
    
    def set_objective(self):
        """
        Sets up the objective function for the optimization problem.
        """
        self.problem += pulp.lpSum([self.resource_costs[i] * self.variables[f"x{i}"] for i in range(self.num_resources)])
    
    def solve(self):
        """
        Solves the optimization problem and returns the result.
        
        :return: Dictionary of resource allocation decisions.
        """
        self.set_constraints()
        self.set_objective()
        self.problem.solve()
        return {v.name: v.varValue for v in self.variables.values()}
    
# Example usage
if __name__ == "__main__":
    # Number of resources
    num_resources = 5
    
    # Cost of each resource
    resource_costs = [10, 20, 30, 40, 50]
    
    # Constraints (e.g., budget limits)
    resource_constraints = [2, 2, 2, 2, 2]
    
    allocator = ResourceAllocator(num_resources, resource_costs, resource_constraints)
    solution = allocator.solve()
    
    print("Resource Allocation Solution:")
    for resource, allocation in solution.items():
        print(f"{resource}: {allocation}")
