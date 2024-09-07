import java.util.*;
public class DFS {

  public static void dfs(Map<Integer, List<Integer>> graph, int start){
    Set<Integer> visited = new HashSet<>();
    helper(start, graph, visited);
  }

  public static void helper(int current, Map<Integer, List<Integer>> graph, Set<Integer> visited){
    visited.add(current);
    System.out.print(current + " ");
    for(int neighbor: graph.get(current)){
      if(!visited.contains(neighbor)) helper(neighbor, graph, visited);
    }
  }

  public static void add(Map<Integer, List<Integer>> graph, int u, int v){
    if(!graph.containsKey(u)) graph.put(u, new ArrayList<>());
    graph.get(u).add(v);
    if(!graph.containsKey(v)) graph.put(v, new ArrayList<>());
    graph.get(v).add(u);
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    Map<Integer, List<Integer>> graph = new HashMap<>();

    add(graph, 0, 1);
    add(graph, 0, 2);
    add(graph, 0, 3);
    add(graph, 1, 2);
    add(graph, 2, 4);

    System.out.print("Enter start node: ");
    int start = sc.nextInt();
    System.out.println("Depth First Search: ");
    dfs(graph, start);

    sc.close();
  }
}