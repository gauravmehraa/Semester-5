import java.util.*;

class Node {
    char name;
    int f, g;

    Node(char name, int f, int g) {
      this.name = name;
      this.f = f;
      this.g = g;
    }
}

class Edge {
    char destination;
    int cost;

    Edge(char destination, int cost) {
      this.destination = destination;
      this.cost = cost;
    }
}

public class AStar {

  public static List<Character> aStar(Map<Character, List<Edge>> graph, Character start, Map<Character, Integer> heuristic) {
    PriorityQueue<Node> fringe = new PriorityQueue<>(Comparator.comparingInt(n -> n.f));
    List<Character> path = new ArrayList<>();
    int distance = 0;

    fringe.add(new Node(start, heuristic.get(start), 0));
    while (!fringe.isEmpty()) {
      Node current = fringe.poll();
      char currentNode = current.name;
      int travelled = current.g;
      path.add(currentNode);
      distance += travelled;
      if (currentNode == 'B') break;
        for(Edge neighborEdge: graph.get(currentNode)){
          char neighbor = neighborEdge.destination;
          int gn = neighborEdge.cost;
          if(!path.contains(neighbor)) {
            int f = heuristic.get(neighbor) + gn + distance;
            fringe.add(new Node(neighbor, f, gn));
          }
        }
      }
    return path;
  }

  public static void add(Map<Character, List<Edge>> graph, char u, char v, int cost){
    if(!graph.containsKey(u)) graph.put(u, new ArrayList<>());
    graph.get(u).add(new Edge(v, cost));
    if(!graph.containsKey(v)) graph.put(v, new ArrayList<>());
    graph.get(v).add(new Edge(u, cost));
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    Map<Character, List<Edge>> graph = new HashMap<>();
    add(graph, 'A', 'Z', 75);
    add(graph, 'A', 'T', 118);
    add(graph, 'A', 'S', 140);
    add(graph, 'Z', 'O', 71);
    add(graph, 'O', 'S', 151);
    add(graph, 'T', 'L', 111);
    add(graph, 'L', 'M', 70);
    add(graph, 'M', 'D', 75);
    add(graph, 'D', 'C', 120);
    add(graph, 'S', 'R', 80);
    add(graph, 'S', 'F', 99);
    add(graph, 'R', 'C', 146);
    add(graph, 'C', 'P', 138);
    add(graph, 'R', 'P', 97);
    add(graph, 'F', 'B', 211);
    add(graph, 'P', 'B', 101);
    add(graph, 'B', 'G', 90);
    add(graph, 'B', 'U', 85);
    add(graph, 'U', 'H', 98);
    add(graph, 'H', 'E', 86);
    add(graph, 'U', 'V', 142);
    add(graph, 'V', 'I', 92);
    add(graph, 'I', 'N', 87);

    Map<Character, Integer> heuristic = new HashMap<>();
    heuristic.put('A', 366);
    heuristic.put('B', 0);
    heuristic.put('C', 160);
    heuristic.put('D', 242);
    heuristic.put('E', 161);
    heuristic.put('F', 178);
    heuristic.put('G', 77);
    heuristic.put('H', 151);
    heuristic.put('I', 226);
    heuristic.put('L', 244);
    heuristic.put('M', 241);
    heuristic.put('N', 234);
    heuristic.put('O', 380);
    heuristic.put('P', 98);
    heuristic.put('R', 193);
    heuristic.put('S', 253);
    heuristic.put('T', 329);
    heuristic.put('U', 80);
    heuristic.put('V', 199);
    heuristic.put('Z', 374);

    System.out.print("Enter start node: ");
    char start = sc.nextLine().charAt(0);
    List<Character> path = aStar(graph, start, heuristic);
    if(!path.isEmpty()) System.out.println(path);
    else System.out.println("No path found");
    sc.close();
    }
}

