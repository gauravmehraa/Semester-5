import java.io.*;
import java.net.*;

public class Client{
  public static void getUsers() throws Exception {
    StringBuilder result = new StringBuilder();
    URL url = new URL("http://localhost:3000");
    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
    conn.setRequestMethod("GET");
    try(BufferedReader reader = new BufferedReader(
      new InputStreamReader(conn.getInputStream()))) {
        for(String line; (line = reader.readLine()) != null; ) result.append(line);
    }
    System.out.println(result.toString());
 }

 public static void main(String[] args) throws Exception {
   getUsers();
 }
}