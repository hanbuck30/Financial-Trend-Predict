# financial data predict

num_generations: 유전 알고리즘이 반복하는 세대(파생)의 총 수를 지정합니다.

num_parents_mating: 새로운 세대를 생성하기 위해 교배하는 솔루션(부모)의 수를 지정합니다.

fitness_func: 현재 모집단에서 각 솔루션의 적합도 값을 계산하는 사용자 정의 함수입니다. 이 적합도 함수는 문제에 따라 달라지며, 유전 알고리즘이 모집단의 솔루션을 어떻게 점수 매기는지 이해하는 데 도움을 줍니다.

sol_per_pop: 모집단의 솔루션 수를 지정합니다. 각 솔루션은 문제의 가능한 해답을 대표합니다.

num_genes: 각 솔루션에서의 유전자 수를 지정합니다. 각 유전자는 솔루션의 특정 부분을 대표합니다.

init_range_low와 init_range_high: 초기 모집단에서 유전자에 할당되는 무작위 값의 하한과 상한을 각각 지정합니다.

parent_selection_type: 교배하게 될 부모를 선택하는 방법을 지정합니다. 여러 가지 유형이 있으며, "rank", "random", "roulette", "tournament", "steady_state" 등이 있습니다.

keep_parents: 다음 세대에서 유지될 부모의 수를 지정합니다.

crossover_type: 교차(교배) 작업에 사용되는 방법을 지정합니다. "single_point", "two_points", "uniform" 등 여러 가지 유형이 있습니다.

mutation_type: 돌연변이 작업에 사용되는 방법을 지정합니다. "random", "swap", "scramble", "inversion" 등이 있습니다.

mutation_percent_genes: 돌연변이가 일어날 유전자의 비율을 지정합니다. 이 비율은 개별 솔루션의 유전자가 아닌 모집단의 총 유전자 수에서 계산됩니다.

## Optimizer
Gnetic Algorithm optimizer(GA)
Particle Swarm Optimizer(PSO)
