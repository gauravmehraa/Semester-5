import java.util.*;
public class BFS {

  public static void bfs(Map<Integer, List<Integer>> graph, int start){
    Set<Integer> visited = new HashSet<>();
    Queue<Integer> queue = new LinkedList<>();

    visited.add(start);
    queue.add(start);

    while(!queue.isEmpty()){
      int current = queue.poll();
      System.out.print(current + " ");
      for(int neighbor: graph.get(current)){
        if(!visited.contains(neighbor)){
          visited.add(neighbor);
          queue.add(neighbor);
        }
      }
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
    System.out.println("Breadth First Search: ");
    bfs(graph, start);

    sc.close();
  }
}